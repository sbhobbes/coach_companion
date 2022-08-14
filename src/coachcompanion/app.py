# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/14/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/3/2022

"""
My first application
"""
import toga
import os
import pandas as pd
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from coachcompanion.Create_Database import *
from coachcompanion.SportChooser import *
from coachcompanion.HomeScreen import *
from coachcompanion.Players import *

class CoachCompanion(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        self.TEAMS_TABLE = 'TEAMS'
        self.TEAMS_COLUMNS = 'TEAM_ID'
        self.TEAMS_CONDITIONS = 'ACTIVE_FLAG = 1'
        
        self.main_window = toga.MainWindow(title=self.formal_name)

        dirname = os.path.dirname(__file__)
        self.DB = os.path.join(dirname, 'db/coachcompanion.db')
        self.mainBox = toga.Box(style = Pack(direction = COLUMN))

        # Check to see if database exists and create if not
        CreateDatabase(self.DB)

        

        # Check to see if an active team exists and display splash screen if not
        activeTeam = ExtractData(self.DB, self.TEAMS_TABLE, self.TEAMS_COLUMNS, self.TEAMS_CONDITIONS)
        print(activeTeam)
        if len(activeTeam) == 0:
            sportChooser = SportChooserScreen(self.DB, self.app)
            self.mainBox.add(sportChooser.DisplayForm())
        else:
            home = HomeScreen(self.DB, self.app)
            self.mainBox.add(home.DisplayForm())


        sportChooserCommand = toga.Command(
            self.SportChooser,
            label = 'New Team'
        )

        editTablesCommand = toga.Command(
            self.EditTables,
            label = 'Update Saved Data'
        )

        changeDefaultTeamCommand = toga.Command(
            self.ChangeDefaultTeam,
            label = 'Change Default Team'
        )

        addPlayersToTeamCommand = toga.Command(
            self.AddPlayersToTeam,
            label = 'Add Players'
        )
        
        self.commands.add(sportChooserCommand, editTablesCommand, changeDefaultTeamCommand, addPlayersToTeamCommand)

        
        # self.main_window.toolbar.add(baseballCommand)
        self.main_window.content = self.mainBox
        self.main_window.show()

    def SportChooser(self, widget):
        self.RemoveChildren()
        sportChooser = SportChooserScreen(self.DB, self.app)
        self.mainBox.add(sportChooser.DisplayForm())
        # pass

    def EditTables(self, widget):
        pass

    def ChangeDefaultTeam(self, widget):
        pass

    def AddPlayersToTeam(self, widget):
        self.RemoveChildren()
        player = Players(self.DB, self.app)
        self.mainBox.add(player.DisplayForm())

    def RemoveChildren(self):
        for child in reversed(self.mainBox.children):
            self.mainBox.remove(child)


def main():
    return CoachCompanion()