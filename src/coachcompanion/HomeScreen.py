# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 8/3/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/3/2022


import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from coachcompanion.SportChooser import *

class HomeScreen():
    def __init__(self, db, app):

        # Declare app attribute constants
        self.DB = db
        self.APP = app
        self.SCREEN_SIZE = self.APP.main_window.size
        self.SCREEN_WIDTH = self.APP.main_window.size[0]
        self.SCREEN_HEIGHT = self.APP.main_window.size[1]
        self.HEADER_FONT_SIZE = self.SCREEN_HEIGHT / 35

        # Declare SQL class constants
        self.BATTING_ORDERS_TABLE = 'BATTING_ORDERS'
        self.COACHES_TABLE = 'COACHES'
        self.GAME_COACHES_TABLE = 'GAME_COACHES'
        self.GAMES_TABLE = 'GAMES'
        self.LINEUPS_TABLE = 'LINEUPS'
        self.LOCATIONS_TABLE = 'LOCATIONS'
        self.LOOKUPS_TABLE = 'LOOKUPS'
        self.PERIODS_TABLE = 'PERIODS'
        self.PLAYERS_TABLE = 'PLAYERS'
        self.POSITION_HISTORY_TABLE = 'POSITION_HISTORY'
        self.POSITIONS_TABLE = 'POSITIONS'
        self.STATISTICS_TABLE = 'STATISTICS'
        self.TEAMS_TABLE = 'TEAMS'
        self.USERS_TABLE = 'USERS'
        self.ALL_COLUMNS = '*'

        # Declare sport class constants
        self.BASEBALL = 'BASEBALL'
        self.TEEBALL = 'TEEBALL'
        self.SOCCER = 'SOCCER'
        self.HOCKEY = 'HOCKEY'
        self.FOOTBALL = 'FOOTBALL'
        self.BASKETBALL = 'BASKETBALL'

        # Declare main app widgets
        self.mainBox = toga.Box(style = Pack(direction = COLUMN))

        # sportChooserCommand = toga.Command(
        #     self.SportChooser,
        #     label = 'New Team'
        # )

        # editTablesCommand = toga.Command(
        #     self.EditTables,
        #     label = 'Update Saved Data'
        # )

        # changeDefaultTeamCommand = toga.Command(
        #     self.ChangeDefaultTeam,
        #     label = 'Change Default Team'
        # )
        
        # self.APP.commands.add(sportChooserCommand, editTablesCommand, changeDefaultTeamCommand)

    def DisplayForm(self):

        return self.mainBox


    # def SportChooser(self, widget):
    #     # self.RemoveChildren()
    #     # sportChooser = SportChooserScreen(self.DB, self.APP)
    #     # self.mainBox.add(sportChooser.DisplayForm())
    #     pass

    # def EditTables(self, widget):
    #     pass

    # def ChangeDefaultTeam(self, widget):
    #     pass

    # def RemoveChildren(self):
    #     for child in reversed(self.mainBox.children):
    #         self.mainBox.remove(child)