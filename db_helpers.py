#!/usr/bin/env python3
'''
Created on Nov 16, 2017

@author: messiry
'''

import psycopg2

# the following inheritance is gladly From StackOverFlow
# without it , it would pass an error ( 3 args given )


class my_database(psycopg2.extensions.connection):
    '''
        Class my database
        used to facilitate Database interactions

        I/P : Database name (string)

    '''
    def __init__(self, dbname):
        '''Class builder '''
        self.dbname = dbname

    def connect_db(self):
        """ Opening Database connection """

        db = psycopg2.connect(database=self.dbname)
        cursor = db.cursor()
        return cursor, db

    def close_db(self, db):
        """
            close connection
            takes Database instance
        """
        db.close()
        return

    def db_read(self, query=0, condition=0):
        """
            Read data from Database
            case 1: no condition , passing direct query
            case 2: passing condition
        """
        c, db = self.connect_db()
        if not c or not db:
            print("ERROR: Couldn't connect to DB")
            return   # Error msg should be raised.

        if not condition:
            c.execute(query)
        else:
            c.execute(query, condition)
        result = c.fetchall()

        self.close_db(db)
        return result

    def db_upc(self, query=0):
        """
            Update - Post - Create Queries
            Takes Direct queries only
        """
        if not query:
            print("ERROR: Query Required")
            return

        c, db = self.connect_db()
        if not c or not db:
            print("ERROR: Couldn't connect to DB")
            return   # Error msg should be raised.

        c.execute(query)
        db.commit()

        self.close_db(db)
        return

    def db_create_view(self, view_name, query):
        """
            Creating View in Database Query
            Takes View_name , Query
            Update the View Table
            with view and corresponding query
        """
        c, db = self.connect_db()
        if not c or not db:
            print("ERROR: Couldn't connect to DB")
            return   # Error msg should be raised.
        view_query = ("CREATE OR REPLACE VIEW " + view_name + " AS "+query)

        c.execute(view_query)
        db.commit()

        self.close_db(db)
        return

    def db_fetch_view(self, view_name=0, condition_q=0):
        """
            Fetch the View Query
            Takes View name , Condition
            Case 1: DEFAULT it Fetch all if no Query given
            case 2: Giving Condition Query
            case2 it parses the condition with view
            NOTE : DO NOT PASS " ; " IN YOUR QUERY
        """

        if condition_q:
            query = "SELECT * FROM " + view_name + " " + condition_q + " ;"
        else:
            query = "SELECT * FROM " + view_name+" ;"
        return self.db_read(query)

