import tkinter as tk
from tkinter import filedialog, ttk
from utils.summarizer_logic import summarize_text, read_pdf

class DocumentSummarizerApp:
    def __init__(self):
        self.result_text = None
        self.open_document = None
        self.progress = None
        self.root = tk.Tk()
        self.root.title("Advanced Document Summarizer")
        self.setup_gui()

    def setup_gui(self):
        ttk.Label(self.root, text="Document Summarizer").grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Open Document", command=self.open_document).grid(row=1, column=0, padx=10, pady = 10)
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.grid(row=2, column=0, padx= 10, pady=10)
        self.result_text = tk.Text(self.root, height=15, width=60)
        self.result_text.grid(row=3, column=0, padx=10, pady=10)

    def open_document(self):
        file_path = filedialog.askopenfile(filetypes=[("Text and PDF Files :", "*.txt" "*.pdf")])
        if file_path:
            self.progress.start(10)
            if file_path.endswith(".pdf"):
                text = read_pdf(file_path)
            else:
                with open(file_path,'r',encoding='utf-8') as file :
                    text = file.read()
            summary = summarize_text(text)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, summary)
            self.progress.stop()

    def run(self):
        self.root.mainloop()
