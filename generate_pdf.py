from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super.__init__()
        self.add_font('DejaVu', '','fonts/DejaVuSans-Bold.ttf',uni=True)
        self.set_auto_page_break(auto=True, margin=15)

pdf = PDF()
pdf.set_font("DejaVu", size=12)
pdf.add_page()

#Adding Title Page

pdf.set_font("DejaVu", style="B", size=24)
pdf.cell(200,10, text = "Advanced Document Summarizer", ln=True, align="C")
pdf.set_font("DejaVu", size=12)
pdf.ln(10)
pdf.cell(200,10,txt="A Python-based application for efficient summarization.", ln=True, align="C")
pdf.ln(20)

#Adding Overview Section

pdf.set_font("DejaVu", style="B", size=16)
pdf.cell(0,10, txt="Overview", ln=True)
pdf.ln(10)
pdf.set_font("DejaVu", size=12)
overview_text = (
    "The Advanced Document Summarizer is a Python application that extracts"
    "key points or summaries from uploaded text and PDF documents."
    "and interactive GUI, support for multiple file formats, and AI-powered"
    "summarization using Natural Language Processing (NLP) techniques."
)

pdf.multi_cell(0,10, txt=overview_text)
pdf.output("DocumentSummarizer_Documentation.pdf")