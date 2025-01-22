def generate_object_and_array_construct():
    print("Enter column names (line by line). Type 'END' to stop:")
    column_names = []
    while True:
        column = input()  # Read column name line by line
        if column.strip().upper() == "END":
            break
        column_names.append(column.strip())
    
    # Generate OBJECT_CONSTRUCT for each column
    object_constructs = []
    json_names = []
    for column in column_names:
        object_construct = (
            f"OBJECT_CONSTRUCT(\n"
            f"    'fieldColumnName', '{column}',\n"
            f"    'fieldLabel', '',\n"
            f"    'fieldValue', A.{column},\n"
            f"    'fieldType', ''\n"
            f") AS {column}_Json"
        )
        object_constructs.append(object_construct)
        json_names.append(f"{column}_Json")
    
    # Generate ARRAY_CONSTRUCT with all JSON names
    array_construct = f"ARRAY_CONSTRUCT({', '.join(json_names)}) AS All_Json_Values"

    # Generate the comma-separated list of column names
    column_names_list = ", ".join(column_names)
    
    # Combine OBJECT_CONSTRUCT, ARRAY_CONSTRUCT, and the list of column names
    final_output = (
        "\n".join(object_constructs) + "\n,\n" +
        array_construct + "\n\n" +
        f"-- Column names in list format:\n{column_names_list}"
    )
    return final_output


# Generate the SQL
sql_output = generate_object_and_array_construct()
print("\nGenerated SQL:\n")
print(sql_output)
