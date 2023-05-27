import PyPDF2
import os
import re


class PdfReader:
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path

    def read_pdf(self):
        pdf_content = []
        file_path = os.path.join(self.file_path, self.file_name)
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                for page_number in range(num_pages):
                    page_obj = pdf_reader.pages[page_number]
                    text = page_obj.extract_text()
                    text = self.remove_special_characters(text)
                    pdf_content.append(text)
            return pdf_content
        except Exception as e:
            print(e)
            return None

    def remove_special_characters(self, text):
        text = text.replace('\n', ' ')
        text = re.sub(r'[^\w\s]', '', text)

        return text


def process_pdf():
    current_dir = os.getcwd()
    files_dir = os.path.join(current_dir, 'documents')
    files_dir_content = os.listdir(files_dir)
    for file in files_dir_content:
        pdf_obj = PdfReader(file, files_dir)
        pdf_content = pdf_obj.read_pdf()
    return pdf_content
