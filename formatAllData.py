import json
import csv

'''
with open("pdf_text.json", "r") as inFile:
    pdfText = json.loads(inFile.read())
with open("/Users/mariannemartinez/devv/cs497/hw3-neural-models-marikmartinez/qa_pairs.tsv") as inFile1:
    questionToAnswer = 
with open("/Users/mariannemartinez/devv/cs497/hw3-neural-models-marikmartinez/qa_pairs.tsv", "r") as inFile1:
    # questionToAnswer = json.loads(inFile1.read())
    questionToAnswer = inFile1.read().split('\t')
'''


with open("/Users/mariannemartinez/devv/cs497/finalProjectNLP/train.json", "r") as inFile2:
    codeToLectureList = json.load(inFile2)

# with open("qa_pairs.tsv") as fin:
with open("/Users/mariannemartinez/devv/cs497/hw3-neural-models-marikmartinez/qa_pairs.tsv") as fin:
    qa_pairs = []
    for line in fin:
        j = json.loads(line)
        qa_pairs.append(j)

with open("code_lecture_pairs.tsv", "w") as outFile1:
    for pair in codeToLectureList:
        # print(pair[0])
        messages = [{'role': 'user', 'content': pair["question"]}, {'role': 'assistant', 'content': pair["answer"]}]
        print(json.dumps(messages), sep='\t', file=outFile1)

with open("combined_finetuning_data.tsv", "w") as outFile2:
    for pair in codeToLectureList:
        # print(pair[0])
        messages = [{'role': 'user', 'content': pair["question"]}, {'role': 'assistant', 'content': pair["answer"]}]
        print(json.dumps(messages), sep='\t', file=outFile2)

        # messages = [{'role': 'user', 'content': pair[0]["question"]}, {'role': 'assistant', 'content': pair[1]["answer"]}]
        # print(json.dumps(messages), sep='\t', file=outFile1)
            
    for pair in qa_pairs:
        messages = [{'role': 'user', 'content': pair[0]["content"]}, {'role': 'assistant', 'content': pair[1]["content"]}]
        # print(json.dump(pair), sep='\t', file=outFile2)
        print(json.dumps(messages), sep='\t', file=outFile2)
        # json.dump(pair, outFile2)

        
