# ======================================================
# dbutils.py
# ------------------------------------------------------
# Written by G.D. Walters
# 20 September, 2019
# ======================================================
# version 0.2
# ======================================================
import datetime
import time
import sqlite3
import codecs


# ======================================================
# Returns a the current data/time in Unix format
# ======================================================
def timestamp():
    tstamp = time.time()
    return tstamp


# ======================================================
# This function will take:
#     timestamp : Unix Timestame information from above or a preset variable
#     output format: integer - decides the output format of the data
#     debug: boolean - if set to True, will provide output of the parameters
# --------------------------------------------------------------------------
# This is useful for creating timestamps in SQLite field data.  SQLite
# does not provide an automatic timestamp fieldtype
# ======================================================
def from_timestamp(ts, whichformat=2, debug=False):
    if debug:
        print(f'   DEBUG: Timestamp:{ts} - Which: {whichformat}')
    if whichformat == 1:
        tf = '%Y-%m-%d %H:%M:%S'
    elif whichformat == 2:
        tf = '%m/%d/%Y %H:%M:%S'
    elif whichformat == 3:
        tf = '%d.%m.%Y %H:%M:%S'
    elif whichformat == 4:
        tf = '%d.%m.%y %H:%M:%S'
    elif whichformat == 5:
        tf = '%d/%m/%Y %H:%M:%S'
    elif whichformat == 6:
        tf = '%A, %d. %B %Y %I:%M%p'
    elif whichformat == 7:
        tf = '%x'
    elif whichformat == 8:
        tf = '%X'
    humantime = datetime.datetime.fromtimestamp(ts).strftime(tf)
    return humantime


# ======================================================
# This function prints a list of all table names in the database
# ======================================================
def getSQLiteTables(databasename):
    sql = "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite%'"
    # global connection, cursor
    connection = sqlite3.Connection(databasename)
    cursor = connection.cursor()
    recset = list(cursor.execute(sql))
    if len(recset) > 0:
        for r in recset:
            print(r)


# ======================================================
# This function queries a database and provides a list of
# all tables in the database and returns the names of each
# table and the schema for that table
# ======================================================
def getSQLiteAllTableInfo(databasename):
    sql = "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite%'"
    # global connection, cursor
    connection = sqlite3.Connection(databasename)
    cursor = connection.cursor()
    recset = list(cursor.execute(sql))
    if len(recset) > 0:
        for r in recset:
            sql = f"PRAGMA table_info({r[0]})"
            newrecs = list(cursor.execute(sql))
            if len(newrecs):
                print(f'Table name: {r[0]}')
                for n in newrecs:
                    print(n)
            print('-'*30)


# ======================================================
# This function queries the database and gets schema information
# and the number of records in that table.
# ======================================================
def getSQLiteTableInfo(databasename, tablename):
    # global connection, cursor
    connection = sqlite3.Connection(databasename)
    cursor = connection.cursor()
    print(
        f'Data from getSQLiteTableInfo - Databasename: {databasename} TableName: {tablename}')
    sql = f"PRAGMA table_info({tablename})"
    newrecs = list(cursor.execute(sql))
    if len(newrecs):
        # print(f'Table name: {tablename}')
        for n in newrecs:
            print(n)
    sql = f"SELECT * from {tablename}"
    recset = list(cursor.execute(sql))
    print(f'Number of records: {len(recset)}')
    print('-'*30)


def quote(s):
    # ======================================================
    # Creates a valid SQL quoted string
    # ======================================================
    pos = s.find("'", 0, len(s))
    if pos != -1:
        # print(f"POS={pos}")
        s = s.replace("'", "''")
    s = "'" + s + "'"
    # print(s)
    return s


def enc(strng):
    return codecs.encode(strng, 'rot_13')


# ======================================================
# If this file is used as an imported module, the code below
# will not run.  However, only if the file is run direct from the
# command line, it will provide a demonstration of each function.
# ---------------------------------
# This section also provides an example how how to use each function
# ======================================================
if __name__ == '__main__':
    timstmp = timestamp()
    print(f'Raw Timestamp (Unix time): {timstmp}')
    print(f'Style 1: {from_timestamp(timstmp, 1)}')
    print(f'Style 2: {from_timestamp(timstmp, 2)}')
    print(f'Style 3: {from_timestamp(timstmp, 3)}')
    print(f'Style 4: {from_timestamp(timstmp, 4)}')
    print(f'Style 5: {from_timestamp(timstmp, 5)}')
    print(f'Style 6 (locale default): {from_timestamp(timstmp, 6)}')
    print(f'Style 7: {from_timestamp(timstmp, 7)}')
    print(f'Style 8: {from_timestamp(timstmp, 8)}')
    print(f'No Style Passed: {from_timestamp(timstmp)}')
    print('~'*30)
    print('Function getSQLiteTables')
    getSQLiteTables('assets.db')
    print('~'*30)
    print('Function getSQLiteAllTableInfo')
    getSQLiteAllTableInfo('assets.db')
    print('~'*30)
    print('Function getSQLiteTableInfo')
    getSQLiteTableInfo('assets.db', 'names')
    getSQLiteTableInfo('assets.db', 'pwds')
    getSQLiteTableInfo('assets.db', 'seclevels')
    getSQLiteTableInfo('assets.db', 'links1')
