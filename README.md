# DocumentSummarizer
For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

The Document Summarizer is a Python-based application that extracts summaries from uploaded text and PDF documents using Natural Language Processing (NLP) techniques. This project includes a basic GUI to interact with the application, upload documents, and view the summarized content.

---

## **Documentation for Basic Version of Document Summarizer**

### **1. Project Overview**

The **Document Summarizer** is a Python-based application that extracts summaries from uploaded text and PDF documents using **Natural Language Processing (NLP)** techniques. This project includes a basic GUI to interact with the application, upload documents, and view the summarized content.

---

### **2. Features**

- **Upload Support for PDF and Text Files**: Users can upload `.txt` and `.pdf` files.
- **Basic Text Summarization**: Summarization is done using **spaCy**'s pre-trained model, and the first few sentences of the document are displayed as a summary.
- **Simple GUI**: The project includes a basic GUI built using **Tkinter** for easy document selection and display of the summarized content.

---

### **3. File and Folder Structure**

Below is the structure of the project files and folders:

```
DocumentSummarizer/
├── data/                     
│   ├── sample_documents/     # Sample documents to test
├── gui/                      
│   ├── __init__.py           # Initializes the gui module
│   ├── summarizer_gui.py     # GUI for document summarization
├── utils/                    
│   ├── __init__.py           # Initializes the utils module
│   ├── summarizer_logic.py   # Logic for document summarization
├── main.py                   # Main entry point to launch the app
├── requirements.txt          # List of dependencies for the project
├── README.md                 # Project's readme file
├── LICENSE                   # License for the project
```

---

### **4. Installation Instructions**

Follow these steps to set up and run the **Document Summarizer** project locally on your machine.

#### **4.1 Prerequisites**

Ensure that the following software is installed on your system:

- **Python 3.x**: You can download Python from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package installer. It comes with Python by default, but make sure it's up to date by running `python -m pip install --upgrade pip`.

#### **4.2 Clone the Repository**

To clone the repository to your local machine, run the following command:

```bash
git clone https://github.com/your-thekartikeyamishra/DocumentSummarizer.git
```

#### **4.3 Install Dependencies**

Navigate into the project directory:

```bash
cd DocumentSummarizer
```

Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

Activate the virtual environment:
- On Windows:

    ```bash
    .venv\Scripts\activate
    ```

- On macOS/Linux:

    ```bash
    source .venv/bin/activate
    ```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

#### **4.4 Run the Application**

Once the dependencies are installed, run the application using the following command:

```bash
python main.py
```

This will launch the GUI where you can upload your text and PDF files and see the summarized output.

---

### **5. Project Usage**

1. **Launch the Application**: After running `main.py`, a Tkinter window will open.
2. **Upload Documents**: Click on the "Upload Documents" button and select `.txt` or `.pdf` files from your system.
3. **View Summaries**: The first few sentences of the uploaded document will be displayed as a summary in the text box below the "Upload Documents" button.

---

### **6. File Descriptions**

- **main.py**: This is the entry point for the application. It initializes the GUI and starts the event loop.
- **gui/summarizer_gui.py**: Contains the GUI logic for the document summarization. It provides a window where the user can interact with the system.
- **utils/summarizer_logic.py**: Contains functions for reading PDF and text files, and summarizing them using the spaCy model.
- **requirements.txt**: A file that lists the dependencies required to run the project, such as `spaCy`, `Tkinter`, and `PyPDF2`.

---



## Overview
The **Document Summarizer** is a Python application that extracts summaries from uploaded `.txt` and `.pdf` documents using **Natural Language Processing (NLP)** techniques. The application includes a simple **GUI** where users can upload documents and view their summaries.

## Features
- Upload support for `.txt` and `.pdf` files.
- Summarizes documents using **spaCy**.
- Simple and intuitive **GUI** powered by **Tkinter**.

## Folder Structure
```
DocumentSummarizer/
├── data/                     
│   ├── sample_documents/     # Sample documents to test
├── gui/                      
│   ├── __init__.py           # Initializes the gui module
│   ├── summarizer_gui.py     # GUI for document summarization
├── utils/                    
│   ├── __init__.py           # Initializes the utils module
│   ├── summarizer_logic.py   # Logic for document summarization
├── main.py                   # Main entry point to launch the app
├── requirements.txt          # List of dependencies for the project
├── README.md                 # Project's readme file
├── LICENSE                   # License for the project
```

## Installation Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/thekartikeyamishra/DocumentSummarizer.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd DocumentSummarizer
    ```

3. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

5. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the application**:
    ```bash
    python main.py
    ```

## Usage
- After running the application, a GUI window will appear.
- Click the "Upload Documents" button to select `.txt` or `.pdf` files.
- The summaries will be displayed in the text box below the button.

