#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

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
    print "Very old version of cx_Oracle :",cx_Oracle.version
    sys.exit()


# Connect to database
try:
    db = cx_Oracle.connect('autopark', '0000', 'orclsrv/study')
except cx_Oracle.DatabaseError, error:
    print "Login  Error:", error
    exit(0)
print 'Oracle DB Version: ', db.version
print 'Encoding: ', db.encoding


# Execute SQL
cursor = db.cursor()
cursor.numbersAsStrings = True
try:
    # cursor.execute('SELECT * FROM NLS_DATABASE_PARAMETERS')
    cursor.execute('SELECT * FROM autopark.bus')
    result = cursor.fetchall()
    for row in result:
        for elem in row:
            print elem, '\t',
        print '' 
except cx_Oracle.DatabaseError, error:
    print 'Error: ', error


# Execute Procedure
try:
    number = 'а004вр'
    result = None
    result = cursor.callproc('PROCEDURE1', [number, result])
    print 'Bus with number', number, 'is', result[1]
    for elem in result:
        print elem
except cx_Oracle.DatabaseError, error:
    print 'Error: ', error


# Close connection
db.close()