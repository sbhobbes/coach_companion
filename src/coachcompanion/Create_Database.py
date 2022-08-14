# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/14/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/3/2022

# import sqlite3
# import os
import pandas as pd
# from sqlite3 import Error
from coachcompanion.SQL_Insert import *
from coachcompanion.SQL_Create_Table import *
from coachcompanion.SQL_Extracts import *



def CreateDatabase(DB):

    LOOKUPS = 'LOOKUPS'
    POSITIONS = 'POSITIONS'
    # DB = r"C:\sqlite\db\coach_companion.db"

    # dirname = os.path.dirname(__file__)
    # DB = os.path.join(dirname, 'db/coachcompanion.db')

    checkSettingsTable = 'LOOKUPS'
    checkSettingsColumns = 'LOOKUP_ID'
    checkSettingsCondition = 'LOOKUP_ID = 1'

    try:
        if ExtractData(DB, checkSettingsTable, checkSettingsColumns, checkSettingsCondition) == None:
            tables = ('BATTING_ORDERS', 'COACHES', 'GAMES', 'LINEUPS', 'LOCATIONS',
                        'LOOKUPS', 'PERIODS', 'PLAYERS', 'POSITION_HISTORY', 'POSITIONS',
                        'STATISTICS', 'TEAMS', 'USERS', 'GAME_COACHES')

            tableColumns = [    # 
                                (   # Columns for the BATTING_ORDERS table
                                    '(BATTING_ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    PERIOD_ID INTEGER REFERENCES PERIODS (PERIOD_ID), \
                                    PLAYER_ID INTEGER REFERENCES PLAYERS (PLAYER_ID), \
                                    ORDER_NUMBER INTEGER, \
                                    INSERT_FLAG INTEGER, \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the COACHES table
                                    '(COACH_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    TEAM_ID INTEGER REFERENCES TEAMS (TEAM_ID), \
                                    FIRST_NAME TEXT NOT NULL, \
                                    LAST_NAME TEXT NOT NULL, \
                                    FULL_NAME TEXT NOT NULL, \
                                    PHONE TEXT, \
                                    EMAIL TEXT, \
                                    CONTACT_PREFERENCE_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    COACH_TYPE_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the GAMES table
                                    '(GAME_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    START_TIME DATETIME, \
                                    LOCATION_ID INTEGER REFERENCES LOCATIONS (LOCATION_ID), \
                                    TEAM_ID INTEGER REFERENCES TEAMS (TEAM_ID), \
                                    OPPONENT TEXT, \
                                    HOME_FLAG INTEGER, \
                                    PLAYED_FLAG INTEGER, \
                                    ACTIVE_FLAG INTEGER, \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the LINEUPS table
                                    '(LINEUP_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    PERIOD_ID INTEGER REFERENCES PERIODS (PERIOD_ID), \
                                    POSITION_ID INTEGER REFERENCES POSITIONS (POSITION_ID), \
                                    PLAYER_ID INTEGER REFERENCES PLAYERS (PLAYER_ID), \
                                    INSERT_FLAG INTEGER, \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the LOCATIONS table
                                    '(LOCATION_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    DESCRIPTION TEXT, \
                                    ADDRESS_LINE_1 TEXT, \
                                    ADDRESS_LINE_2 TEXT, \
                                    CITY TEXT, \
                                    STATE_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    ZIP INTEGER, \
                                    ACTIVE_FLAG INTEGER, \
                                    DEFAULT_FLAG INTEGER, \
                                    FIELD_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the LOOKUPS table
                                    '(LOOKUP_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    LOOKUP_TYPE TEXT, \
                                    LOOKUP_CODE TEXT, \
                                    LOOKUP_DESCRIPTION TEXT, \
                                    ACTIVE_FLAG INTEGER DEFAULT 1, \
                                    USER_DEFAULT_FLAG INTEGER, \
                                    SYSTEM_DEFAULT_FLAG INTEGER, \
                                    EDITABLE_FLAG INTEGER, \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the PERIODS table
                                    '(PERIOD_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    GAME_ID INTEGER REFERENCES GAMES (GAME_ID), \
                                    PERIOD_NUMBER INTEGER, \
                                    PLAYED_FLAG INTEGER DEFAULT O, \
                                    ACTIVE_FLAG INTEGER DEFAULT 0, \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the PLAYERS table
                                    '(PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    TEAM_ID INTEGER REFERENCES TEAMS (TEAM_ID), \
                                    FIRST_NAME TEXT NOT NULL, \
                                    LAST_NAME TEXT NOT NULL, \
                                    FULL_NAME TEXT NOT NULL, \
                                    JERSEY INTEGER, \
                                    PHONE TEXT, \
                                    EMAIL TEXT, \
                                    CONTACT_PREFERENCE_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    DOB DATE, \
                                    FAVORITE_POSITION_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    BEST_POSITION_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    DEFAULT_POSITION_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the POSITION_HISTORY table
                                    '(POSITION_HISTORY_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    PERIOD_ID INTEGER REFERENCES PERIODS (PERIOD_ID), \
                                    POSITION_ID INTEGER REFERENCES POSITIONS (POSITION_ID), \
                                    PLAYER_ID INTEGER REFERENCES PLAYERS (PLAYER_ID), \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the POSITIONS table
                                    '(POSITION_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    DESCRIPTION TEXT, \
                                    CODE TEXT, \
                                    POSITION_CATEGORY_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    SPORT_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the STATISTICS table
                                    '(STATISTIC_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    POSITION_HISTORY_ID INTEGER REFERENCES POSITION_HISTORY (POSITION_HISTORY_ID), \
                                    STATISTIC_TYPE_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    RESULT DOUBLE, \
                                    CREATED_DATE DATETIME, \
                                    CREATD_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the TEAMS table
                                    '(TEAM_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    MAX_PERIODS INTEGER, \
                                    OVERTIME_RULE_FLAG INTEGER DEFAULT 0, \
                                    OVERTIME_RULE_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    SPORT_LOOKUP_ID, \
                                    NAME TEXT, \
                                    COLOR TEXT, \
                                    SPONSOR TEXT, \
                                    ACTIVE_FLAG INTEGER DEFAULT 1, \
                                    AGE_GROUP TEXT, \
                                    YEAR INTEGER, \
                                    SEASON TEXT, \
                                    DEFAULT_FLAG INTEGER, \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the USERS table
                                    '(USER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    USER_TYPE_LOOKUP_ID INTEGER REFERENCES LOOKUPS (LOOKUP_ID), \
                                    COACH_ID INTEGER REFERENCES COACHES (COACH_ID), \
                                    PLAYER_ID INTEGER REFERENCES PLAYERS (PLAYER_ID), \
                                    FIRST_NAME TEXT NOT NULL, \
                                    LAST_NAME TEXT NOT NULL, \
                                    FULL_NAME TEXT NOT NULL, \
                                    EMAIL TEXT, \
                                    PHONE TEXT, \
                                    USERNAME TEXT, \
                                    PASSWORD TEXT, \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                ),
                                (   # Columns for the GAME_COACHES table
                                    '(GAME_COACHES_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, \
                                    GAME_ID INTEGER REFERENCES GAMES (GAME_ID), \
                                    COACH_ID INTEGER REFERENCES COACHES (COACH_ID), \
                                    CREATED_DATE DATETIME, \
                                    CREATED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID), \
                                    LAST_MODIFIED_DATE DATETIME, \
                                    LAST_MODIFIED_BY_USER_ID INTEGER REFERENCES USERS (USER_ID))'
                                )
                            ]

            lookupColumns = ('LOOKUP_TYPE', 'LOOKUP_CODE', 'LOOKUP_DESCRIPTION',
                                'ACTIVE_FLAG', 'USER_DEFAULT_FLAG', 'SYSTEM_DEFAULT_FLAG',
                                'EDITABLE_FLAG')

            lookupValues = [('COACH_TYPES', 'AC', 'Assistant Coach', 1, 0, 1, 0),           # 1
                            ('COACH_TYPES', 'TM', 'Team Manager', 1, 0, 1, 0),              # 2
                            ('SPORTS', 'SOCCER', 'Soccer', 1, 0, 1, 0),                     # 3
                            ('SPORTS', 'FOOTBALL', 'Football', 1, 0, 1, 0),                 # 4
                            ('SPORTS', 'BASEBALL', 'Baseball', 1, 0, 1, 0),                 # 5
                            ('SPORTS', 'HOCKEY', 'Hockey', 1, 0, 1, 0),                     # 6
                            ('SPORTS', 'BASKETBALL', 'Basketball', 1, 0, 1, 0),             # 7
                            ('SPORTS', 'SOFTBALL', 'Softball', 1, 0, 1, 0),                 # 8
                            ('CONTACT_PREFERENCES', 'EMAIL', 'Email', 1, 0, 1, 0),          # 9
                            ('CONTACT_PREFERENCES', 'PHONE', 'Phone', 1, 0, 1, 0),          # 10
                            ('CONTACT_PREFERENCES', 'TEXT', 'Text', 1, 0, 1, 0),            # 11
                            ('POSITION_CATEGORIES', 'OFFENSE', 'Offense', 1, 0, 1, 0),      # 12
                            ('POSITION_CATEGORIES', 'DEFENCE', 'Defence', 1, 0, 1, 0),      # 13
                            ('POSITION_CATEGORIES', 'OF', 'Outfield', 1, 0, 1, 0),          # 14
                            ('POSITION_CATEGORIES', 'IF', 'Infield', 1, 0, 1, 0),           # 15
                            ('STATISTIC_TYPES', 'BAVG', 'Batting Average', 1, 0, 1, 0),     # 16
                            ('USER_TYPES', 'COACH', 'Coach User', 1, 0, 1, 0),              # 17
                            ('STATES', 'AL', 'Alabama', 1, 0, 1, 0),                        # 18
                            ('STATES', 'AK', 'Alaska', 1, 0, 1, 0),                         # 19
                            ('STATES', 'AZ', 'Arizona', 1, 0, 1, 0),                        # 20
                            ('STATES', 'AR', 'Arkansas', 1, 0, 1, 0),                       # 21
                            ('STATES', 'CA', 'California', 1, 0, 1, 0),                     # 22
                            ('STATES', 'CO', 'Colorado', 1, 0, 1, 0),                       # 23
                            ('STATES', 'CT', 'Connecticut', 1, 0, 1, 0),                    # 24
                            ('STATES', 'DE', 'Delaware', 1, 0, 1, 0),                       # 25
                            ('STATES', 'DC', 'District of Columbia', 1, 0, 1, 0),           # 26
                            ('STATES', 'FL', 'Florida', 1, 0, 1, 0),                        # 27
                            ('STATES', 'GA', 'Georgia', 1, 0, 1, 0),                        # 28
                            ('STATES', 'HI', 'Hawaii', 1, 0, 1, 0),                         # 29
                            ('STATES', 'ID', 'Idaho', 1, 0, 1, 0),                          # 30
                            ('STATES', 'IL', 'Illinois', 1, 0, 1, 0),                       # 31
                            ('STATES', 'IN', 'Indiana', 1, 0, 1, 0),                        # 32
                            ('STATES', 'IA', 'Iowa', 1, 0, 1, 0),                           # 33
                            ('STATES', 'KS', 'Kansas', 1, 0, 1, 0),                         # 34
                            ('STATES', 'KY', 'Kentucky', 1, 0, 1, 0),                       # 35
                            ('STATES', 'LA', 'Louisiana', 1, 0, 1, 0),                      # 36
                            ('STATES', 'ME', 'Maine', 1, 0, 1, 0),                          # 37
                            ('STATES', 'MD', 'Maryland', 1, 0, 1, 0),                       # 38
                            ('STATES', 'MA', 'Massachusetts', 1, 0, 1, 0),                  # 39
                            ('STATES', 'MI', 'Michigan', 1, 0, 1, 0),                       # 40
                            ('STATES', 'MN', 'Minnesota', 1, 0, 1, 0),                      # 41
                            ('STATES', 'MS', 'Mississippi', 1, 0, 1, 0),                    # 42
                            ('STATES', 'MO', 'Missouri', 1, 0, 1, 0),                       # 43
                            ('STATES', 'MT', 'Montana', 1, 0, 1, 0),                        # 44
                            ('STATES', 'NE', 'Nebraska', 1, 0, 1, 0),                       # 45
                            ('STATES', 'NV', 'Nevada', 1, 0, 1, 0),                         # 46
                            ('STATES', 'NH', 'New Hampshire', 1, 0, 1, 0),                  # 47
                            ('STATES', 'NJ', 'New Jersey', 1, 0, 1, 0),                     # 48
                            ('STATES', 'NM', 'New Mexico', 1, 0, 1, 0),                     # 49
                            ('STATES', 'NY', 'New York', 1, 0, 1, 0),                       # 50
                            ('STATES', 'NC', 'North Carolina', 1, 0, 1, 0),                 # 51
                            ('STATES', 'ND', 'North Dakota', 1, 0, 1, 0),                   # 52
                            ('STATES', 'OH', 'Ohio', 1, 0, 1, 0),                           # 53
                            ('STATES', 'OK', 'Oklahoma', 1, 0, 1, 0),                       # 54
                            ('STATES', 'OR', 'Oregon', 1, 0, 1, 0),                         # 55
                            ('STATES', 'PA', 'Pennsylvania', 1, 0, 1, 0),                   # 56
                            ('STATES', 'PR', 'Puerto Rico', 1, 0, 1, 0),                    # 57
                            ('STATES', 'RI', 'Rhode Island', 1, 0, 1, 0),                   # 58
                            ('STATES', 'SC', 'South Carolina', 1, 0, 1, 0),                 # 59
                            ('STATES', 'SD', 'South Dakota', 1, 0, 1, 0),                   # 60
                            ('STATES', 'TN', 'Tennessee', 1, 0, 1, 0),                      # 61
                            ('STATES', 'TX', 'Texas', 1, 0, 1, 0),                          # 62
                            ('STATES', 'UT', 'Utah', 1, 0, 1, 0),                           # 63
                            ('STATES', 'VT', 'Vermont', 1, 0, 1, 0),                        # 64
                            ('STATES', 'VA', 'Virginia', 1, 0, 1, 0),                       # 65
                            ('STATES', 'VI', 'Virgin Islands', 1, 0, 1, 0),                 # 66
                            ('STATES', 'WA', 'Washington', 1, 0, 1, 0),                     # 67
                            ('STATES', 'WV', 'West Virginia', 1, 0, 1, 0),                  # 68
                            ('STATES', 'WI', 'Wisconsin', 1, 0, 1, 0),                      # 69
                            ('STATES', 'WY', 'Wyoming', 1, 0, 1, 0),                        # 70
                            ('COACH_TYPES', 'HC', 'Head Coach', 1, 0, 1, 0),                # 71
                            ('COACH_TYPES', '1BC', '1st Base Coach', 1, 0, 1, 0),           # 72
                            ('COACH_TYPES', '3BC', '3rd Base Coach', 1, 0, 1, 0),           # 73
                            ('OT_RULES', 'SHOOTOUT', 'Shootout', 1, 0, 0, 0),               # 74
                            ('OT_RULES', 'EX_PER', 'Extra Innings/Periods', 1, 0, 1, 0),    # 75
                            ('SPORTS', 'TEEBALL', 'Tee-Ball', 1, 0, 1, 0),                  # 76
                            ]

            positionColumns = ('DESCRIPTION', 'CODE', 'POSITION_CATEGORY_LOOKUP_ID', 'SPORT_LOOKUP_ID')
            
            positionValues = [  # Baseball
                                ('First Base', '1B', 15, 5),
                                ('Second Base', '2B', 15, 5),
                                ('Third Base', '3B', 15, 5),
                                ('Short Stop', 'SS', 15, 5),
                                ('Pitcher', 'P', 15, 5),
                                ('Catcher', 'C', 15, 5),
                                ('Left Field', 'LF', 14, 5),
                                ('Right Field', 'RF', 14, 5),
                                ('Center Field', 'CF', 14, 5),
                                
                                # Softball
                                ('First Base', '1B', 15, 8),
                                ('Second Base', '2B', 15, 8),
                                ('Third Base', '3B', 15, 8),
                                ('Short Stop', 'SS', 15, 8),
                                ('Pitcher', 'P', 15, 8),
                                ('Catcher', 'C', 15, 8),
                                ('Left Field', 'LF', 14, 8),
                                ('Right Field', 'RF', 14, 8),
                                ('Center Field', 'CF', 14, 8),

                                # Tee-Ball
                                ('First Base', '1B', 15, 76),
                                ('Second Base', '2B', 15, 76),
                                ('Third Base', '3B', 15, 76),
                                ('Short Stop', 'SS', 15, 76),
                                ('Pitcher', 'P', 15, 76),
                                ('Catcher', 'C', 15, 76),
                                ('Left Field', 'LF', 14, 76),
                                ('Right Field', 'RF', 14, 76),
                                ('Center Field', 'CF', 14, 76)

                                # Basketball

                                # Soccer

                                # Football

                                # Hockey
                            ]

            CreateTables(DB, tables, tableColumns)
            InsertIntoTables(DB, LOOKUPS, lookupColumns, lookupValues)
            InsertIntoTables(DB, POSITIONS, positionColumns, positionValues)

    except ValueError as e:
        print(e)
        print('Database found.')
    

# if __name__ == '__main__':
#     CreateDatabase()