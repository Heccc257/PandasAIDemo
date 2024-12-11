基础功能，支持添加一个目录下的所有表，也可以单独添加单个表。
支持进行chat，以及输出history
```
(myapp) append csvs
append csvs/area_by_country.csv successfully!
append csvs/people.csv successfully!
append csvs/revenue_by_country.csv successfully!
(myapp) chat
Please enter a question:
Which are the top 5 countries by sales?
[Response]: The top 5 countries by sales are: China, United States, Japan, Germany, United Kingdom
(myapp) chat
Please enter a question:
Which three countries have the highest income-to-area ratio
[Response]: The three countries with the highest income-to-area ratio are: Italy, Germany, Japan
(myapp) get_history
histories:{ {question:Which are the top 5 countries by sales?, response:The top 5 countries by sales are: China, United States, Japan, Germany, United Kingdom}, {question:Which three countries have the highest income-to-area ratio, response:The three countries with the highest income-to-area ratio are: Italy, Germany, Japan},  }
(myapp) chat_with_history
Please enter a question and we will answer it with chat history:
list the income-to-area ratio of the highest three countries
[Response]:    country    area  income_to_area_ratio  income-to-area ratio
3    Italy  301336              0.013606              0.009624
2  Germany  357022              0.008123              0.008123
7    Japan  377972              0.006879              0.006085
```

支持删除表格，删除后不能正确地回答 `who earns the most`
```
(myapp) append csvs
append csvs/area_by_country.csv successfully!
append csvs/people.csv successfully!
append csvs/revenue_by_country.csv successfully!
(myapp) chat
Please enter a question:
who earns the most
[Response]: The person who earns the most is Frank.
(myapp) delete csvs/people.csv
delete csvs/people.csv successfully!
(myapp) chat
Please enter a question:
who earns the most
[Response]: The country that earns the most is China.
```

还支持进行表连接，并且将结果导出到`export.csv`中
```
(PandasAIDemo) append csvs
append csvs/people.csv successfully!
append csvs/area_by_country.csv successfully!
append csvs/revenue_by_country.csv successfully!
(PandasAIDemo) export
Please enter a cmd to export a new table:
Joining the people table with the country
[Response]:       name  age        country  salary     area  revenue
0    Alice   25  United States    5000  9833520     5000
1      Bob   30  United States    6000  9833520     5000
2  Charlie   35  United States    4500  9833520     5000
3    David   40         Canada    2600  9984670     2500
4    Emily   45          China   90000  9596961     7000
5    Frank   50          Japan  100000   377972     4500
6    Grace   35        Germany    4200   357022     4100
7    Henry   30        Germany    4000   357022     4100
8      Ivy   35          Spain    2700   505992     2100
9     Jack   40          Spain    2100   505992     2100
Exported to export.csv successfully
```