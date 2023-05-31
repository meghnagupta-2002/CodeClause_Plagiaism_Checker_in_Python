import difflib
import tkinter as tk
from tkinter import filedialog
import PyPDF2
from docx import Document
# Create the GUI window
root = tk.Tk()
root.title("Plagiarism Checker")
root.geometry("300x300")

def check_plagiarism(text1, text2, threshold=0.9):
    difference = difflib.SequenceMatcher(None, text1, text2)
    similarity_score = difference.ratio()

    return similarity_score


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text


def extract_text_from_word(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def extract_text_from_code(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def browse_file(label):
    file_path = filedialog.askopenfilename()
    label.config(text=file_path)


def compare_files():
    file1 = file1_label.cget("text")
    file2 = file2_label.cget("text")

    if file1 and file2:
        text1, text2 = "", ""
        if file1.lower().endswith('.pdf'):
            text1 = extract_text_from_pdf(file1)
        elif file1.lower().endswith(('.doc', '.docx')):
            text1 = extract_text_from_word(file1)
        elif file1.lower().endswith(('.py', '.java', '.cpp', '.c', '.css', '.html', '.*')):
            text1 = extract_text_from_code(file1)
        else:
            with open(file1, 'r') as f1:
                text1 = f1.read()

        if file2.lower().endswith('.pdf'):
            text2 = extract_text_from_pdf(file2)
        elif file2.lower().endswith(('.doc', '.docx')):
            text2 = extract_text_from_word(file2)
        elif file2.lower().endswith(('.py', '.java', '.cpp', '.c', '.css', '.html', '.*')):
            text2 = extract_text_from_code(file2)
        else:
            with open(file2, 'r') as f2:
                text2 = f2.read()

        similarity_score = check_plagiarism(text1, text2)
        result.config(
            text="Plagiarism Percentage: {:.2%}".format(similarity_score))
    else:
        result.config(text="Please select both files.")

# Create button and configure the labels
file1_label = tk.Label(root, text="Select File 1:")
file1_label.pack(pady=10)
file1_button = tk.Button(root, text="Browse",
                        command=lambda: browse_file(file1_label))
file1_button.pack()

file2_label = tk.Label(root, text="Select File 2:")
file2_label.pack(pady=20)
file2_button = tk.Button(root, text="Browse",
                        command=lambda: browse_file(file2_label))
file2_button.pack()

compare = tk.Button(root, text="Compare", command=compare_files)
compare.pack(pady=30)

# Create and configure the result label
result = tk.Label(root, text="")
result.pack()

# Run the GUI main loop
root.mainloop()
