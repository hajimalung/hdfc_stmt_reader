import tabula
import pandas as pd

hdfc_statement = input("Enter a hdfc statement file name (only .pdf): ")
user_input = input("Enter a string: ")
print(f"searching for '{user_input}' in the statement...")  # Debug print to check user input

dfs = tabula.read_pdf(hdfc_statement, pages='all', multiple_tables=True)

count = 1  # Add counter
totalSentTo = 0
totalReceivedFrom = 0
bikeCost = 165000
plotWithdrawl = 1900000
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
if "MD SALEEM" in user_input:
    print(f" - Total plot withdrawal: {plotWithdrawl}")  # Display total plot withdrawal
    print(f" - Total bike cost: {bikeCost}")  # Display total bike cost
    print(f"final effective amount sent till 2020 JAN : {totalSentTo - totalReceivedFrom - plotWithdrawl}")  # Display final effective amount

