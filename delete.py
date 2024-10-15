import re

# Define a function to extract 'ab' followed by any characters up to the first space
def extract_ab_before_space(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
        # Regular expression to find all occurrences of 'ab' followed by any characters up to the first space
        matches = re.findall(r'\bab\S*', content)
        
        return matches

# Path to your file
file_path = 'your_file.txt'

# Call the function and print the results
results = extract_ab_before_space(file_path)
print(results)
