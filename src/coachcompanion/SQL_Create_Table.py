# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/15/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 7/15/2022

import sqlite3
from sqlite3 import Error

def CreateTables(db_file, tables, columns):

    conn = None

    try:
        conn = sqlite3.Connection(db_file)
        print('SQLite Version: ' + sqlite3.version)
        
        def ExecuteQuery(sql):
            c = conn.cursor()

            c.execute(sql)

        for x in range(len(tables)):
            print(f'Creating "{tables[x]}" table...')
            ExecuteQuery(f'''CREATE TABLE IF NOT EXISTS {tables[x]} {columns[x]};''')
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()
            print('Finished creating tables.')