data _null_;
    today_num = weekday(today());
    today_name = put(today(), weekdate.);
    put "Today is day " today_num "of the week (" today_name ")";
run;
