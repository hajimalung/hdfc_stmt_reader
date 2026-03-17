import tabula
import pandas as pd

hdfc_statement = input("Enter a hdfc statement file name (only .pdf): ")
if not hdfc_statement:
    hdfc_statement = "orig_stmt.pdf"
user_input = input("Enter a string: ")
print(f"searching for '{user_input}' in the statement({hdfc_statement})...")  # Debug print to check user input

dfs = tabula.read_pdf(hdfc_statement, pages='all', multiple_tables=True)

count = 0  # Add counter
totalSentTo = 0
totalReceivedFrom = 0
print(f"Total dataframes extracted: {len(dfs)}")  # Debug print to check number of dataframes
for dfIndex, df in enumerate(dfs):  # Print only the first table for demonstration
    for index, row in df.iterrows():
        row_dict = row.to_list()  # Convert the row to a list
        if user_input in str(row_dict[1]):
            if not pd.isna(row_dict[4]):
                totalSentTo += float(str(row_dict[4]).replace(',', ''))
            if not pd.isna(row_dict[5]):
                totalReceivedFrom += float(str(row_dict[5]).replace(',', ''))
            # print(f" {row_dict} found in dataframe {dfIndex}")
            count += 1

print(f"Total matches found: {count}")  # Display count
print(f"Total amount sent: {totalSentTo}")  # Display total amount
print(f" - Total amount received: {totalReceivedFrom}")  # Display total amount
