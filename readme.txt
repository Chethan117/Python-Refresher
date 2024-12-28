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



<ol>
  <li><b>Gather Data:</b> We start by looking at the case data stored in a system. This data includes details like when each case happened, which queue it was in, and its category.</li>
  <li><b>Organize and Filter:</b> We then filter this data to focus only on cases that occurred in the last three months, starting from the first day of the current month. We organize the data by the date and time the case occurred, which queue it was in, and the type of queue.</li>
  <li><b>Count the Cases:</b> After organizing the data, we count how many cases fall into each combination of date, time, queue name, and category.</li>
  <li><b>Push the Data to Snowflake:</b> Once the data is organized and counted, we push it into Snowflake, which is a cloud-based data storage system. Snowflake helps us store this data in an organized way so we can easily access it for analysis.</li>
  <li><b>Visualize in Tableau:</b> After the data is stored in Snowflake, we use Tableau (a tool for creating visual reports) to turn this data into interactive charts and tables. This makes it easy to see patterns, trends, and insights at a glance.</li>
</ol>

<p>By doing this, we create a report that not only organizes and counts the cases but also allows stakeholders to easily explore and understand the data visually in Tableau. This helps with decision-making and better understanding of how cases are being handled over time.</p>

