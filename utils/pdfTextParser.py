import os
import pdfplumber
import json

def pdf_text_to_dict(pdf_dir, output_dict):
    """
    Extract text from all PDFs in a directory and store it in a dictionary.

    Args:
        pdf_dir (str): Directory containing PDFs.
        output_dict (dict): Dictionary to store extracted text.
    """

    for file_name in os.listdir(pdf_dir):
        if file_name.endswith(".pdf"):
            try:
                with pdfplumber.open(pdf_dir + os.sep + file_name) as pdf:
                    text = ''
                    for page in pdf.pages:
                        text += '\n'.join(page.extract_text().splitlines())
                    output_dict[file_name[:-4]] = text
            except Exception as e:
                print(f"Error extracting text from {file_name}: {e}")

# Usage example:
pdf_dir = 'data/lecturePdfs'
output_dict = {}
pdf_text_to_dict(pdf_dir, output_dict)

# Save the dictionary to a JSON file
json.dump(output_dict, open('pdf_text.json', 'w'))


