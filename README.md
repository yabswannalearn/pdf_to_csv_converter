# PDF to CSV Table Extractor

This command-line script extracts **tabular data** from a PDF file and converts it into a single, clean **CSV** file. It is designed to handle **large documents** where tables may span across multiple pages, consolidating all found data into one output file.

This tool is ideal for **data analysts, researchers**, and anyone needing to extract structured data from PDF reports for use in spreadsheets or data analysis software.

---

## 🛠 Prerequisites

Make sure the following software is installed:

- **Python 3.6+**  
  Download from [python.org](https://www.python.org/).  
  ✅ *Important:* During installation on Windows, check **"Add Python to PATH"*

- **Java Development Kit (JDK)**  
  Required by **tabula-py** for PDF processing.  
  Download from [Oracle Java](https://www.oracle.com/java/technologies/javase-downloads.html)

  🔧 After installation, make sure **Java is added to your system’s PATH**. (See Troubleshooting below.)

---

## 📦 Installation

1. **Save the Script**  
   Save `pdf_to_csv_converter.py` to a folder (e.g., `C:\pdf_converter\`)

2. **Open Terminal**  
   - Windows: Open Command Prompt / PowerShell / VS Code terminal  
   - macOS/Linux: Open Terminal

3. **Install Libraries**  
   Run this command:
   ```bash
   pip install tabula-py pandas jpype1
