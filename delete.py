The process retrieves data from the accounts, change_of_address, and card_events tables. <br>
It captures essential details such as customer names, mobile numbers, event dates, and indicators related to account status. <br>
Inner joins are performed between accounts and change_of_address to filter for active accounts with recent changes of address. <br>
A left join with the card_events table includes event data for card reissues and requests associated with each account. <br>
A subquery calculates the count of reissued cards per account, grouping results by account ID. <br>
A left join with the established_phone_numbers table identifies mobile numbers that are either non-established or do not start with '7'. <br>
The query checks whether the current day is Monday. If it is, it filters card event dates for the last three days; for other days, it filters for the previous day. <br>
Conditions check for rep_ind (Reputation Indicator) and proc_ind (Processing Indicator) being equal to 0, signaling accounts requiring further investigation. <br>
The final query constructs the output with necessary fields for analysis, including account status, mobile number status, and counts from the reissue subquery. <br>
The daily output is inserted into a designated repository table (e.g., repository_table) for monitoring and further investigation. <br>
