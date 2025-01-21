def generate_object_construct_from_lines():
    print("Enter column names (line by line). Type 'END' to stop:")
    column_names = []
    while True:
        column = input()  # Read column name line by line
        if column.strip().upper() == "END":
            break
        column_names.append(column.strip())
    
    output = []
    for column in column_names:
        result = (
            f"OBJECT_CONSTRUCT(\n"
            f"    'fieldColumnName', '{column}',\n"
            f"    'fieldLabel', '',\n"
            f"    'fieldValue', A.{column},\n"
            f"    'fieldType', ''\n"
            f") AS {column}_Json"
        )
        output.append(result)
    return "\n,\n".join(output)


# Generate the SQL
sql_output = generate_object_construct_from_lines()
print("\nGenerated SQL:\n")
print(sql_output)
