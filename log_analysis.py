#!/usr/bin/env python3

'''
Created on Nov 16, 2017

@author: messiry
'''

from db_helpers import my_database


# please specify your Database name
DB = "newsdata"
mydb = my_database(DB)

# ----------------------------------------------------------#
# Creating DB views
# ----------------------------------------------------------#


# ---------------- Top Articles Views ----------------------#

top_log_articles_q = \
    """
        SELECT path,count(*) as num FROM log
        GROUP BY path ORDER BY num DESC;
    """
# Creating View in DB
mydb.db_create_view("top3_log_articles", top_log_articles_q)


top_articles_q = \
    """
        SELECT log.path,log.num,a.title,a.author FROM
        (SELECT * FROM top_log_articles) AS log ,articles AS a
        WHERE log.path LIKE '%' ||a.slug || '%' ;
    """
# Creating View in DB
mydb.db_create_view("top_articles", top_articles_q)


# ---------------- Top Authors Views -----------------------#

top_author_q = \
    """
        SELECT top.title,top.num AS view_num ,a.name
        FROM (SELECT * FROM top_articles) AS top, authors AS a
        WHERE top.author=a.id;
    """
# Creating View in DB
mydb.db_create_view("top_articles_authors", top_author_q)


# ---------------- FAIL % Views ----------------------------#

error_q = \
    """
        SELECT time::DATE,count(*) AS total
        FROM log WHERE status !='200 OK'
        GROUP BY time::DATE
        ORDER BY time::DATE DESC;
    """
# must create view with name "err"
# Creating View in DB
mydb.db_create_view("err", error_q)


success_q = \
    """
        SELECT time::DATE,count(*) AS total
        FROM log
        GROUP BY time::DATE
        ORDER BY time::DATE DESC;
    """
# must create view with name "suc"
# Creating View in DB
mydb.db_create_view("suc", success_q)


suc_err = \
    """
        SELECT err_t.time::DATE AS time , err_t.total AS err_total ,
        suc_t.total AS success_total ,
        ROUND(100*(CAST(err_t.total AS decimal)/ suc_t.total ),1) AS percent
        FROM (SELECT * FROM err) AS err_t,(SELECT * FROM suc) AS suc_t
        WHERE  err_t.time::DATE = suc_t.time::DATE
        ORDER BY percent DESC ;
    """
# must create view with name "status_analysis"
# Creating View in DB
mydb.db_create_view("status_analysis", suc_err)


# ----------------------------------------------------------#
# Top 3 articles
# ----------------------------------------------------------#

def get_top_articles(condition_q=0):
    # Fetching View from DB
    return mydb.db_fetch_view(view_name="top_articles",
                              condition_q=condition_q)


# ----------------------------------------------------------#
# Most read authors
# ----------------------------------------------------------#


def get_top_authors(condition_q=0):
    # Fetching View from DB
    return mydb.db_fetch_view(view_name="top_articles_authors",
                              condition_q=condition_q)


# ----------------------------------------------------------#
# Calculating percentage of plus 1% fail status code
# ----------------------------------------------------------#

def get_fail_percentage(condition_q):
    # Fetching View from DB
    return mydb.db_fetch_view(view_name="status_analysis",
                              condition_q=condition_q)

# ----------------------------------------------------------#
# Printing Results
# ----------------------------------------------------------#

print("Top Articles & Authors :\n")

# Top authors also fetches the article title & view number
# Printing top articles and authors
for article in get_top_authors(condition_q="LIMIT 3"):
    print("Article :'" + article[0] + "'\n" +
          "By      : " + str(article[1]) + "\n" +
          "Views   : " + str(article[2]) + "\n" +
          "----------------------------------------------\n")

print("Fail Percentage : \n")
# printing Fail percentage
for item in get_fail_percentage("WHERE percent > 1"):
    print("Date: "+str(item[0]))
    print("Total status code 404: " + str(item[1]))
    print("Total Responses      : " + str(item[2]))
    print("Percentage of Failure: " + str(item[3])+" %")

if __name__ == "__main__":
    pass
