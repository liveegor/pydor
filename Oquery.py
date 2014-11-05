#!/usr/bin/python
# -*- coding: utf-8 -*-


import Stuff
import sys
import prettytable


# Russian support for client
import os
os.environ['NLS_LANG'] = 'Russian.AL32UTF8'


# Good module import
try:
    import cx_Oracle
except ImportError, info:
    print "Import Error:", info
    sys.exit()
if cx_Oracle.version < '3.0':
    print "Very old version of cx_Oracle :", cx_Oracle.version
    sys.exit()


# Query to execute
query = 'select break_numb from break'


# Connect to database
try:
    db = cx_Oracle.connect (Stuff.login, Stuff.password, Stuff.server + '/' + Stuff.SID)
    cursor = db.cursor()
    cursor.execute(query)
    pt = prettytable.from_db_cursor(cursor)
    print pt.get_string()

except cx_Oracle.Error, error:
    print str(error).decode('utf8')

