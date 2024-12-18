import os
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from transformers import BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# Define the model and LoRA configurations
MODEL_NAME = "Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2"
LORA_RANK = 8
LORA_ALPHA = 16
LORA_DROPOUT = 0.05

def main():
    # Load question-answer pairs dataset
    # Replace 'path/to/dataset' with your dataset path or Hugging Face dataset identifier
    dataset = load_dataset("json", data_files={"train": "train.json"})

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)

    quantization_config = BitsAndBytesConfig()
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, quantization_config=quantization_config, device_map="auto")


    # Prepare the model for LoRA training
    model = prepare_model_for_kbit_training(model)
    lora_config = LoraConfig(
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        target_modules=["q_proj", "v_proj"],  # Adjust based on model architecture
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)

    # Tokenization and data preparation
    def preprocess_function(examples):
        # Concatenate question and answer into a single string
        inputs = [f"Question: {q}\nAnswer: {a}" for q, a in zip(examples["question"], examples["answer"])]
        return tokenizer(inputs, max_length=512, truncation=True, padding="max_length")

    tokenized_datasets = dataset.map(preprocess_function, batched=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./lora-finetuned-llama",
        evaluation_strategy="steps",
        eval_steps=500,
        save_steps=1000,
        logging_steps=100,
        learning_rate=1e-4,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        save_total_limit=2,
        fp16=True,
        report_to="none",
        load_best_model_at_end=True,
    )

    # Define data collator
    def data_collator(features):
        labels = torch.tensor([f["input_ids"] for f in features], dtype=torch.long)
        attention_mask = torch.tensor([f["attention_mask"] for f in features], dtype=torch.long)
        return {"input_ids": labels, "attention_mask": attention_mask, "labels": labels}

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["eval"],
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    # Train the model
    trainer.train()

    # Save the final model and tokenizer
    model.save_pretrained("./lora-finetuned-llama")
    tokenizer.save_pretrained("./lora-finetuned-llama")

if __name__ == "__main__":
    main()

