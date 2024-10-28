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




Start by pulling applications in a waiting status with a SIRA date within the last X days that hit specific SIRA rules, noting which rules were triggered.
Gather additional applicant information, including home phone, work phone, mobile phone numbers, employment history, income history, duration of stay at the address, task lists, local rule hits, total match score, operating system name, and fraud risk score.
Identify how many other applications used the same cookie before the current application to assess patterns and potential fraud risks.
Count instances of phone and email fraud based on applicant details and identify any fraudulent behavior.
Pull all quotation data from the last 90 days along with cookie information related to those applications and quotations, including associated email addresses and IP addresses.
Check which SIRA rules were hit for each application and compile that information for analysis.
Retrieve all applications marked as "mos" (most suspicious) from the past three years, noting the applicant's name and date of birth, and return applications from the last 445 days with prior applications marked as "mos."
List all accounts opened in the last three months, including their addresses, emails, and mobile numbers, and return applications from the last 445 days that share account details with accounts older than three months.
Fetch bureau data from Equifax, verifying any applications lacking bureau data against Equifax and adding tradeline data for summarization.
Create base rules, including a secondary rule for low-risk score accounts, and combine results from old and new data to refine the rules.
Identify cases with duplicate IDs but different rules applied.
Finalize the base rules and set up an email notification system for stakeholders when an automatic decision is made based on the established base rules.
Draft an email to the operations team to trigger automation for SIRA CNI cases, attaching the relevant cases for processing.
