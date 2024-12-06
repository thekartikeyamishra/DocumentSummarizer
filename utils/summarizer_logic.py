import  spacy
import pdfplumber

nlp = spacy.load("en_core_web_sm")

def summarize_text(text, max_sentences =3):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    if len(sentences) <= max_sentences:
        return  text
    summary = ".".join(sentences[:max_sentences])
    return summary+"..."

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
