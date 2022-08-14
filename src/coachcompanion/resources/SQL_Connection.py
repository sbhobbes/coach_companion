# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/11/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 7/11/2022

import sqlite3
from sqlite3 import Error

def CreateConnection(db_file):
    """Create a connection to a SQLite database."""

    conn = None

    try:
        conn = sqlite3.Connection(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def GenerateSystemDefaultLookups(db_file):

    conn = None

    try:
        conn = sqlite3.Connection(db_file)
        print(sqlite3.version)

        sql = '''INSERT INTO LOOKUPS (
                    LOOKUP_TYPE,
                    LOOKUP_CODE,
                    LOOKUP_DESCRIPTION,
                    ACTIVE_FLAG,
                    USER_DEFAULT_FLAG,
                    SYSTEM_DEFAULT_FLAG,
                    EDITABLE_FLAG)
                VALUES (
                    'COACH_TYPE',
                    'HC',
                    'HEAD COACH',
                    1,
                    0,
                    1,
                    0);'''

        c = conn.cursor()

        c.execute(sql)
        conn.commit()


    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':

    db = r"C:\sqlite\db\coach_companion.db"

    CreateConnection(db)
    GenerateSystemDefaultLookups(db)