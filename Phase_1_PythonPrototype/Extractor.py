import pymupdf as  fitz

def extract_text(path):
    doc = fitz.open(path)
    text = "".join([page.get_text() for page in doc])
    return text

path = r"C:\Users\Akhona\IdeaProjects\Ukzn_Smart_Timetable\Phase_1_PythonPrototype\Comp102 timetable.pdf"
print(extract_text(path))
