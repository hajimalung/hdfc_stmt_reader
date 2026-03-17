# hdfc_stmt_reader

This Python project provides a script to extract and analyze transaction data from HDFC bank statement PDFs using the tabula library.

## Features

- Reads HDFC bank statement PDFs
- Searches for specific strings in transaction descriptions
- Calculates total amounts sent and received matching the search criteria
- Handles multiple tables in the PDF

## Prerequisites

- Python 3.x
- Java (required for tabula-py)

## Installation and Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   cd stmtreader
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python:

```
python stmt_reader_tabula.py
```

When prompted:

- Enter the HDFC statement PDF file name (e.g., `statement.pdf`). If no input is provided, it defaults to `orig_stmt.pdf`.
- Enter the search string to look for in the transaction descriptions (e.g., a name or keyword).

The script will:

- Extract tables from the PDF
- Search for the entered string in the transaction descriptions
- Calculate and display the total amounts sent and received for matching transactions
- If the search string contains "MD SALEEM", it will also display additional financial calculations

## Dependencies

- tabula-py: For PDF table extraction
- pandas: For data manipulation
- jpype1: Java-Python bridge for tabula-py
