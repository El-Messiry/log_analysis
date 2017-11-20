# Log Analysis

### Description:
This is Log Analysis project (#3) of Udacity Full Stack Webdevelopment .
Having large database it's required to fetch data effeciently from the Database `postgresql` and to benefit from the power of SQL queries and reduce Python code as much as possible 

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


1. First it connects to Database
2. Then it creates all the views of the queries needed
3. After all the Queries been added as view we embed them in functions
4. these functions return required information
5. Printing the Results 


**B) `db_helpers.py`**
Contains Class `my_database()` which inherits from the `psycopg2` to interact with any given database .

- The constructor takes only the database name which you'd like to connect to , in `log_analysis.py` 

	

- having `mydb` instance that is connected to `newsdata` database you can access all the functions inside.
- `connect_db() , close_db("db instance")` used for openning and closing connection to database 

- `db_read()` to fetch data from DB,`db_upc()` *Update,Post,Create* queries can be used by this function.

- `db_create_view()` to create view query to the Database 
- `db_fetch_view()`to fetch the created view 

### Useage :

1. First download and install the following :
	- download and install postgresql from [here](http://postgresguide.com/setup/install.html) 
	- download database , zipped file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 
	- unzipp the file `neswdata.sql` and copy it to your Database
	- this [link](https://www.postgresql.org/docs/8.1/static/backup.html) should help with copying the database
	
2. In **`log_analysis.py`** please specify your Database name
ex:
	
		# Please specify your Database name
		DB = "newsdata"
		mydb = my_database(DB)
		
3. after connecting to your Database , use your instance to create your desired queries 
		
		mydb.db_create_view("top_articles", top_articles_q)
		# create view in database 		
		
4. Creating view queries Easy up the process of fetching data
5. After you make your queries using functions from **`db_helpers`**
6. print your results

		print_report()
