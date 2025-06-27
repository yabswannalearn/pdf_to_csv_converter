# pdf_to_csv_converter.py
import tabula
import pandas as pd
import sys
import os

def convert_pdf_to_csv(pdf_path, csv_path):
    """
    Extracts tables from all pages of a PDF file and saves them into a single CSV file.

    This function is designed to handle PDFs containing large tables that may span
    multiple pages. It reads the tables from each page and concatenates them
    into one comprehensive CSV.

    Args:
        pdf_path (str): The full path to the input PDF file.
        csv_path (str): The full path where the output CSV file will be saved.
    """
    print(f"Starting conversion for '{pdf_path}'...")

    # --- Input Validation ---
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' was not found.")
        print("Please check the file path and try again.")
        return
    
    if not pdf_path.lower().endswith('.pdf'):
        print(f"Error: The specified input file '{pdf_path}' is not a PDF.")
        return

    try:
        # --- PDF Table Extraction ---
        # The 'read_pdf' function from the 'tabula' library reads tables from a PDF.
        # 'pages="all"' tells it to process every page in the document.
        # 'lattice=True' is an option that helps with tables that have clear grid lines.
        # If your table doesn't have visible lines, you might try 'stream=True' instead.
        # This returns a list of DataFrames, where each DataFrame represents a table found.
        print("Extracting tables from the PDF. This may take a while for large files...")
        list_of_dataframes = tabula.read_pdf(pdf_path, pages='all', lattice=True)

        if not list_of_dataframes:
            print("Warning: No tables were found in the PDF.")
            print("This can happen if the PDF contains scanned images of tables instead of text,")
            print("or if the table structure is very complex. You could try using 'stream=True'.")
            return

        # --- Data Consolidation ---
        # We concatenate all the extracted DataFrames from the list into a single DataFrame.
        # This is crucial for tables that span multiple pages.
        print(f"Found {len(list_of_dataframes)} tables across all pages. Combining them...")
        combined_df = pd.concat(list_of_dataframes, ignore_index=True)

        # --- CSV File Generation ---
        # The 'to_csv' method from the pandas library saves the DataFrame to a CSV file.
        # 'index=False' prevents pandas from writing the DataFrame index as a column in the CSV.
        combined_df.to_csv(csv_path, index=False)

        print("-" * 50)
        print("✅ Conversion Successful!")
        print(f"Data has been saved to: '{csv_path}'")
        print(f"Total rows processed: {len(combined_df)}")
        print("-" * 50)

    except Exception as e:
        print(f"An error occurred during the conversion process: {e}")
        print("Please ensure you have Java installed and that the PDF is not password-protected or corrupted.")

if __name__ == '__main__':
    # This block allows the script to be run from the command line.
    # To run it, you would type:
    # python pdf_to_csv_converter.py "path/to/your/file.pdf" "path/to/your/output.csv"

    if len(sys.argv) != 3:
        print("Usage: python pdf_to_csv_converter.py <input_pdf_path> <output_csv_path>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_csv = sys.argv[2]
    
    convert_pdf_to_csv(input_pdf, output_csv)
