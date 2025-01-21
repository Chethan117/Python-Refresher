def generate_object_construct(column_names):
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


# Example input
columns = ["Column1", "Column2", "Column3"]

# Generate the SQL
sql_output = generate_object_construct(columns)
print(sql_output)
