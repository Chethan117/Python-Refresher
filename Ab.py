data utf8_data;
  set original_data;
  utf8_column = unicodec(original_column, 'utf-8');
run;


data cleaned_data;
  set original_data;
  cleaned_column = prxchange('s/[^\x20-\x7E]/ /', -1, original_column);
run;




/* Step 1: Set the encoding option */
options encoding=utf-8;

/* Step 2: Cleanse the data */
data clean_data;
    set original_data;

    /* Replace invalid characters (example: replace '?' with space) */
    column_a_cleaned = tranwrd(column_a, '?', ' ');

    /* Remove non-printable characters using regular expressions */
    column_a_cleaned = prxchange('s/[^[:print:]]//o', -1, column_a);
run;

/* Step 3: Load clean data into Snowflake */
proc sql;
    /* Connect to Snowflake */
    connect to odbc (dsn="your_dsn_name" uid="your_username" pwd="your_password");

    /* Load cleansed data into Snowflake */
    execute (
        COPY INTO your_snowflake_schema.your_snowflake_table
        FROM (SELECT column_a_cleaned FROM your_saslib.clean_data)
        FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' ESCAPE = '\\')
    ) by odbc;
    
    /* Disconnect from Snowflake */
    disconnect from odbc;
quit;
