import re

# Sample SQL content


# Define the regular expression pattern
pattern = r"(?:FROM|JOIN)\s+(\w+)\.(\w+)"


with open("your_sql_file.sql", "r") as file:
    sql_content = file.read()

matches = re.findall(pattern, sql_content)

for match in matches:
    dbname, tablename = match
    print(f"|{dbname}|{tablename}|")
