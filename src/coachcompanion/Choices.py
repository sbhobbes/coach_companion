# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/31/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/1/2022

from coachcompanion.Players import Players
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from coachcompanion.Players import *
from coachcompanion.HomeScreen import *

class ChoicesScreen(HomeScreen):
    def __init__(self, choice, db, app):
        super().__init__(db, app)

        self.NEW_TEAM = 'NEW_TEAM'
        self.choice = choice

    def DisplayScreen(self):

        if self.choice == self.NEW_TEAM:
            choiceLabel = toga.Label(
                'What would you like to do next?',
                style = Pack(padding = (0, 50))
            )

            createRosterButton = toga.Button(
                'Create Roster',
                on_press = self.CreateRoster,
                style = Pack(padding = 5)
            )

            createScheduleButton = toga.Button(
                'Create Schedule',
                on_press = self.CreateSchedule,
                style = Pack(padding = 5)
            )

            choiceBox = toga.Box(style = Pack(direction = ROW, padding = 5))
            buttonsBox = toga.Box(style = Pack(direction = ROW, padding = 5))

            choiceBox.add(choiceLabel)
            buttonsBox.add(createRosterButton)
            buttonsBox.add(createScheduleButton)

            self.mainBox.add(choiceBox)
            self.mainBox.add(buttonsBox)

            return self.mainBox


    def CreateRoster(self, widget):
        
        self.RemoveChildren()
        player = Players(self.DB, self.APP)
        self.mainBox.add(player.DisplayForm())


    def CreateSchedule(self, widget):
        pass
        
        # remove children
        # add a call to a new create schedule class object

    def RemoveChildren(self):

        for child in reversed(self.mainBox.children):
            self.mainBox.remove(child)