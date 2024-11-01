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


CASE 
        WHEN UPPER(t2.column_name) LIKE 'POLICY RULL%' 
             AND POSITION('RR' IN UPPER(t2.column_name)) > 0 
        THEN UPPER(SUBSTRING(
                t2.column_name, 
                POSITION('RR' IN UPPER(t2.column_name)), 
                4
            ))

