# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/15/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 7/27/2022

import sqlite3
import pandas as pd
from pandas.io.sql import DatabaseError
from sqlite3 import Error
from coachcompanion.SQL_Insert import *
from coachcompanion.SQL_Create_Table import *

def ExtractData(db_file, tables, columns = None, conditions = None):
    """Create a connection to a SQLite database."""

    conn = None

    try:
        conn = sqlite3.Connection(db_file)
        print('SQLite Version: ' + sqlite3.version)

        def ExecuteQuery(sql):

            try:
                print(sql)
                df = pd.read_sql_query(sql, conn)
                return df

            except DatabaseError as e:
                print(e)
                return None

        print(f'Querying "{tables}" table...')

        if conditions and columns:
            data = ExecuteQuery(f'''SELECT {columns} FROM {tables} WHERE {conditions};''')
        elif conditions and not columns:
            data = ExecuteQuery(f'''SELECT * FROM {tables} WHERE {conditions};''')
        elif columns and not conditions:
            data = ExecuteQuery(f'''SELECT {columns} FROM {tables};''')

        return data

    except Error as e:
        print(e)
        
        return None
        
    finally:
        if conn:
            conn.close()

# def GetTeams(db_file):

#     conn = None

#     try:
#         conn = sqlite3.Connection(db_file)
#         print('SQLite Version: ' + sqlite3.version)

#         print(f'Querying "Teams" table...')

#         sql = '''SELECT
#                     TEAM_ID
#                  FROM
#                     TEAMS
#                  WHERE
#                     ACTIVE_FLAG = 1;'''
        
#         c = conn.cursor()
#         c.execute(sql)

#         rows = c.fetchall()

#         dataList = []
#         for row in rows:
#             dataList.append(row)
        
#         if len(dataList) > 0:
#             return dataList
#         else:
#             return None

#     except Error as e:
#         print(e)

#         return None

#     finally:
#         if conn:
#             conn.close()