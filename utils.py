import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


def analyze_resume(text):
    feedback = []

    if "Python" in text:
        feedback.append("Good: Python skill detected")
    else:
        feedback.append("Add Python skill if applicable")

    if "project" in text.lower():
        feedback.append("Projects section found")
    else:
        feedback.append("Add a projects section")

    if len(text) < 500:
        feedback.append("Resume seems too short")
    else:
        feedback.append("Resume length looks good")

    return feedback