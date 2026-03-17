from pypdf import PdfReader

reader = PdfReader('orig_stmt.pdf')

print(f"Total pages: {len(reader.pages)}")

first_page = reader.pages[1]
print(f"Text from the first page:\n{first_page.extract_text()}")
# pageContent = first_page.extract_text()
# lines = pageContent.splitlines()

# for i, line in enumerate(lines, start=1):
#     print(f"{i}: {line}") if "MD SALEEM-NETBANK" in line else None