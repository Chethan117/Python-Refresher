<h3>Background</h3>
<p><b>Goal:</b> Provide a clear summary of daily fraud losses in Tableau to help identify trends and issues related to transaction declines.</p>

<hr>

<h3>Intent</h3>
<p><b>What:</b> Summarize daily fraud losses for visualization in Tableau.</p>

<hr>

<h3>Methodology</h3>
<ol>
  <li><b>Daily Declines:</b> Identify daily declined transactions by grouping data by date and reason, counting unique accounts, and summing declines.</li>
  <li><b>Genuine Declines:</b> Find non-fraudulent declined transactions using the same process as fraud-related declines.</li>
  <li><b>Total Transactions:</b> Calculate total transactions processed daily over the past 13 months.</li>
  <li><b>Genuine Transactions:</b> Determine daily non-fraudulent transactions over the past 13 months.</li>
  <li><b>Decline Rates:</b> Compare declined transactions to total transactions to measure daily decline rates.</li>
  <li><b>Genuine Decline Rates:</b> Compare genuine declines to total genuine transactions for daily rates.</li>
 <li><b>Decline Rates in Basis Points:</b> Combine the daily fraud-related decline rates and genuine decline rates to provide a clear picture of overall trends.</li>
  <li><b>Decline Volumes:</b> Summarize the daily volumes of declined transactions for all reasons (both fraud-related and genuine) and prepare the data for visualization. The data is then saved in Snowflake to make it available in Tableau for analysis.</li>
</ol>

<hr>

<h3>Non-Execution Impact</h3>
<p>(To be detailed based on requirements)</p>
