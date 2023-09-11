import os
import pdfplumber
import fitz

PDF_FILE_PATH = "../pdf/{파일명}.pdf"
TXT_FILE_PATH = "../txt/outputs.txt"

INPUT_DIR = "../pdf/학습 데이터"


def text_to_txt_file(text, file_name):
    with open(file_name, "a", encoding='UTF-8') as f:
        f.write(text)


def pdf_to_text_by_pdfplumber():
    with pdfplumber.open(PDF_FILE_PATH) as pdf:
        pages = pdf.pages
        for page in pages:
            text = page.extract_text()
            text_to_txt_file(text, TXT_FILE_PATH)


def pdf_to_text_by_pymupdf():
    pdf_file = fitz.open(PDF_FILE_PATH)
    text = ""
    for page_num in range(len(pdf_file)):
        page = pdf_file.load_page(page_num)
        text += page.get_text("text")
    text_to_txt_file(text, TXT_FILE_PATH)


def pdf_to_text_by_pdfplumber2(pdf_path, txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages
        text = ""
        for page in pages:
            text += page.extract_text()
        text_to_txt_file(text, txt_path)


def pdf_to_text_by_pymupdf2(pdf_path, txt_path):
    pdf_file = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(pdf_file)):
        page = pdf_file.load_page(page_num)
        text += page.get_text("text")
    text_to_txt_file(text, txt_path)


# pdf_to_text_by_pymupdf2()

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".pdf"):
        pdf_file_path = os.path.join(INPUT_DIR, filename)
        pdf_to_text_by_pymupdf2(pdf_file_path, TXT_FILE_PATH)