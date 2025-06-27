PDF to CSV Table Extractor
This command-line script extracts tabular data from a PDF file and converts it into a single, clean CSV file. It is designed to handle large documents where tables may span across multiple pages, consolidating all found data into one output file.

This tool is ideal for data analysts, researchers, and anyone needing to extract structured data from PDF reports for use in spreadsheets or data analysis software.

Prerequisites
Before you can run this script, you must have the following software installed on your system:

Python 3.6+: The script is written in Python. If you don't have it, download it from python.org.

Important: During installation on Windows, ensure you check the box that says "Add Python to PATH".

Java Development Kit (JDK): The underlying library, tabula-py, requires a Java runtime to process PDFs.

You can download the latest version of Java from the official Java website.

After installation, you must ensure Java is added to your system's PATH variable to be accessible from the command line (see the Troubleshooting section for instructions).

Installation
Once the prerequisites are met, you need to install the necessary Python libraries.

Save the Script: Save the pdf_to_csv_converter.py script to a directory on your computer (e.g., C:\pdf_converter\).

Open a Terminal:

Windows: Open Command Prompt, PowerShell, or the VS Code terminal.

macOS/Linux: Open Terminal.

Install Libraries: Run the following command to install tabula-py, pandas, and jpype1. jpype1 is highly recommended for better performance.

pip install tabula-py pandas jpype1

How to Use
This script is run from your terminal.

Navigate to the Script Directory: In your terminal, change to the directory where you saved the script.

cd C:\pdf_converter

Prepare Your Paths: Identify the full path to your input PDF and decide on a full path for your output CSV file.

Pro Tip: Enclose your paths in double quotes (" ") to avoid issues with spaces in file or folder names.

Run the Command: Use the following format to execute the script:

python pdf_to_csv_converter.py "PATH_TO_YOUR_INPUT.pdf" "PATH_TO_YOUR_OUTPUT.csv"

Example:

python pdf_to_csv_converter.py "C:\Users\reina\Downloads\deped masterlist.pdf" "C:\Users\reina\Downloads\deped_masterlist_converted.csv"

Wait for Completion: The script will print its progress. For very large files, this process can take several minutes. Once complete, it will show a "Conversion Successful!" message, and your CSV file will be ready at the specified location.

Troubleshooting
Error: 'java' command is not found...
This is the most common issue. It means Python cannot find your Java installation.

Solution: You need to add Java's bin directory to your system's PATH environment variable.

Find your Java bin folder: It's typically located at a path like C:\Program Files\Java\jdk-17.0.2\bin. Copy this path.

Edit System Variables:

Press the Windows key, type env, and select "Edit the system environment variables".

Click the "Environment Variables..." button.

In the "System variables" section, find and select the Path variable, then click "Edit...".

Click "New" and paste the Java bin path you copied.

Click OK on all windows to save.

Restart your Terminal/VS Code: You must restart your command prompt or code editor for the changes to take effect.

Warning: No tables were found in the PDF
Check PDF Type: This script works best on digitally generated PDFs where text is selectable. It will not work on scanned PDFs (images of text).

Try stream mode: If your table does not have clear grid lines, open the .py script and change lattice=True to stream=True.
