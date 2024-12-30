<ol>
  <li><b>Collect Authorization Data:</b> Gather data about authorizations (dates, fraud status, amounts) for the last 3 months. Filter out irrelevant transactions.</li>
  <li><b>Clean Old Data:</b> Remove outdated records (older than 13 months) and duplicates from the past 3 months in the <code>allauthorizationrep</code> table.</li>
  <li><b>Add New Data:</b> Insert the latest processed authorization data into the cleaned table.</li>
  <li><b>Summarize Total Transactions:</b> Calculate total transactions and amounts for non-fraudulent cases from the last 13 months.</li>
  <li><b>Collect Declined Transactions:</b> Gather details about declined transactions (dates, decision makers, fraud status) for the last 3 months. Focus on specific decision types like disputes or reissues.</li>
  <li><b>Combine and Summarize Data:</b> Create summaries for Total Declines, Genuine Declines (non-fraudulent), and Approved Fraud (fraudulent but approved). Merge this data with total transactions for context.</li>
  <li><b>Update Final Table:</b> Delete old data from the final Snowflake table. Insert the new summarized data into the table.</li>
</ol>
