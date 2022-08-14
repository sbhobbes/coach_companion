# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/14/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/1/2022

import sqlite3
from sqlite3 import Error

def InsertIntoTables(db_file, table, columns, values, valueType = None):

    conn = None

    try:
        conn = sqlite3.Connection(db_file)
        print('SQLite Version: ' + sqlite3.version)
        
        def ExecuteQuery(sql):
            c = conn.cursor()
            print(sql)

            c.execute(sql)

        if valueType == None:
            for i, value in enumerate(values):
                print(f'Inserting record {i} into {table}...')
                ExecuteQuery(f'''INSERT INTO {table} {columns} VALUES {value};''')
        else:
            print(f'Inserting record into {table}...')
            ExecuteQuery(f'''INSERT INTO {table} {columns} VALUES {values};''')
        
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            print('Finished inserting records.')
            conn.close()