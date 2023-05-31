# Plagiarism Checker
This is a simple plagiarism checker application built using Python and the tkinter library for the graphical user interface (GUI). The application allows you to compare the similarity between two text files, PDF files, or code files to check for potential plagiarism.


## Features
- Select File 1: Click on the "Browse" button next to "Select File 1" to choose the first file for comparison.
- Select File 2: Click on the "Browse" button next to "Select File 2" to choose the second file for comparison.
- Compare: Click on the "Compare" button to initiate the comparison process.
- Plagiarism Percentage: The application calculates the similarity between the two files and displays the plagiarism percentage as the result.
- Supported File Types: The application supports text files (e.g., .txt), PDF files, and code files (e.g., .py, .java, .cpp, .c, .css, .html, etc.).


## Requirements
- Python 3.x
- tkinter library (usually included with Python)
- PyPDF2 library (install with `pip install PyPDF2`)
- python-docx library (install with `pip install python-docx`)


## How to Use
1. Run the script using Python: `python plagiarism_checker.py`.
2. The plagiarism checker window will open.
3. Click on the "Browse" button next to "Select File 1" to choose the first file for comparison.
4. Click on the "Browse" button next to "Select File 2" to choose the second file for comparison.
5. Click on the "Compare" button to initiate the comparison process.
6. The application will extract the text from the selected files based on their file types (text, PDF, or code).
7. The similarity between the two texts will be calculated using the SequenceMatcher from the difflib library.
8. The plagiarism percentage will be displayed as the result.
9. To compare other files, repeat steps 3-8.
10. Close the application window to exit.

Note: The plagiarism checker may not provide 100% accurate results and is intended as a basic tool for initial plagiarism detection. The similarity score is based on text matching algorithms and does not consider context or meaning. It is always recommended to perform thorough checks and analysis for accurate plagiarism detection.

Feel free to modify and enhance the code according to your requirements. Enjoy checking for potential plagiarism!
