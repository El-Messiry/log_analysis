# Log Analysis

### Description:
This is Log Analysis project (#3) of Udacity Full Stack Webdevelopment .
Given 3 question to answer using SQL Queries :

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time? 
- On which days did more than 1% of requests lead to errors? 


### Contents:
- **log_analysis.py:**
Python Code to fetch the required information to answer the 3 questions above
- **db_helpers.py:**
Contains all the helping functions regarding interacting with `newsdata` Database with in the Postgresql .


### Walk Through:
**A)`log_analysis.py`** 
1- Deletes all the Views used in queries from DB
2- Deletes Table Views then Creates it again
>1 & 2 are just measures to gurantee program should run again and again with out errors like: ( relation already exists , table already exists etc....)

3- SQL Query to Fetch most read articles & creates view of it in DB
4- Based on step 3 , it Fetches the Authors name of each article 
5- Aggregating the total error `404 NOT FOUND`,`200 OK` and grouping by Date and storing it in a view .
6-By using the 2 views above we Create a new table with percantage of Failure .
7-Printing the Results of the 3 Questions .


**B) `db_helpers.py`**
Contains Class `my_database()` which inherits from the `psycopg2` to interact with any given database .

- The constructor takes only the database name which you'd like to connect to , in `log_analysis.py` ex:

		DB = "newsdata"
		mydb = my_database(DB) 
	

- having `mydb` instance that is connected to `newsdata` database you can access all the functions inside.
- `connect_db() , close_db("db instance")` used for openning and closing connection to database 

- `db_read()` to fetch data from DB,`db_upc()` *Update,Post,Create* queries can be used by this function.

- `db_create_view()` to create view query to the Database 
- `db_fetch_view()`to fetch the created view 
