# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 8/2/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/2/2022

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from coachcompanion.HomeScreen import *
from coachcompanion.SQL_Extracts import *


class Players(HomeScreen):
    def __init__(self, db, app):
        super().__init__(db, app)
        

    def DisplayForm(self):

        TEAMS_COLUMNS = '*'
        TEAMS_CONDITIONS = 'ACTIVE_FLAG = 1 AND DEFAULT_FLAG = 1'

        defaultTeamDF = ExtractData(self.DB, self.TEAMS_TABLE, TEAMS_COLUMNS, TEAMS_CONDITIONS)
        print(defaultTeamDF)
        defaultTeamName = defaultTeamDF['NAME'][0]

        teamIDLabel = toga.Label (
            f'Add a new Player to: {defaultTeamName}',
            style = Pack(padding = 5, font_size = self.HEADER_FONT_SIZE)
        )

        firstNameLabel = toga.Label(
            'First Name: ',
            style = Pack(padding = 5)
        )

        lastNameLabel = toga.Label(
            'Last Name: ',
            style = Pack(padding = 5)
        )

        jerseyLabel = toga.Label(
            'Jersey Number: ',
            style = Pack(padding = 5)
        )

        phoneLabel = toga.Label(
            'Phone Number: ',
            style = Pack(padding = 5)
        )

        emailLabel = toga.Label(
            'Email Address: ',
            style = Pack(padding = 5)
        )

        contactPreferenceLabel = toga.Label(
            'Contact Preference: ',
            style = Pack(padding = 5)
        )

        birthDateLabel = toga.Label(
            'Date of Birth: ',
            style = Pack(padding = 5)
        )

        favoritePositionLabel = toga.Label(
            'Favorite Position: ',
            style = Pack(padding = 5)
        )

        bestPositionLabel = toga.Label(
            'Best Position: ',
            style = Pack(padding = 5)
        )

        defaultPositionLabel = toga.Label(
            'Default Position: ',
            style = Pack(padding = 5)
        )

        firstNameInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        lastNameInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        jerseyInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        phoneInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        emailInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        contactPreferenceInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        birthDateInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        favoritePositionInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        bestPositionInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        defaultPositionInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))

        saveButton = toga.Button(
            'Save',
            on_press = self.SavePlayer,
            style = Pack(padding = (5, self.SCREEN_WIDTH / 5, 5, (self.SCREEN_WIDTH / 5 * 3) - 100), width = 50)
        )
        cancelButton = toga.Button(
            'Cancel',
            on_press = self.Cancel,
            style = Pack(padding = (5, 0, 5, self.SCREEN_WIDTH / 5), width = 50)
        )

        teamIDBox = toga.Box(style = Pack(direction = ROW))
        firstNameBox = toga.Box(style = Pack(direction = ROW))
        lastNameBox = toga.Box(style = Pack(direction = ROW))
        jerseyBox = toga.Box(style = Pack(direction = ROW))
        phoneBox = toga.Box(style = Pack(direction = ROW))
        emailBox = toga.Box(style = Pack(direction = ROW))
        contactPreferenceBox = toga.Box(style = Pack(direction = ROW))
        birthDateBox = toga.Box(style = Pack(direction = ROW))
        FavoritePositionBox = toga.Box(style = Pack(direction = ROW))
        bestPositionBox = toga.Box(style = Pack(direction = ROW))
        defaultPositionBox = toga.Box(style = Pack(direction = ROW))
        buttonsBox = toga.Box(style = Pack(direction = ROW))

        labelsList = [firstNameLabel, lastNameLabel, jerseyLabel, phoneLabel, emailLabel,
                        contactPreferenceLabel, birthDateLabel, favoritePositionLabel,
                        bestPositionLabel, defaultPositionLabel]

        inputsList = [firstNameInput, lastNameInput, jerseyInput, phoneInput, emailInput,
                        contactPreferenceInput, birthDateInput, favoritePositionInput,
                        bestPositionInput, defaultPositionInput]

        boxesList = [firstNameBox, lastNameBox, jerseyBox, phoneBox, emailBox,
                        contactPreferenceBox, birthDateBox, FavoritePositionBox,
                        bestPositionBox, defaultPositionBox]

        teamIDBox.add(teamIDLabel)
        self.mainBox.add(teamIDBox)

        for i, value in enumerate(labelsList):
            boxesList[i].add(labelsList[i])
            boxesList[i].add(inputsList[i])
            self.mainBox.add(boxesList[i])

        buttonsBox.add(saveButton)
        buttonsBox.add(cancelButton)
        self.mainBox.add(buttonsBox)
        
        return self.mainBox

    def SavePlayer(self, widget):
        pass

    def Cancel(self, widget):
        pass

        # TEAM_ID
        # FIRST_NAME
        # LAST_NAME
        # FULL_NAME
        # JERSEY
        # PHONE
        # EMAIL
        # CONTACT_PREFERENCE_LOOKUP_ID
        # DOB
        # FAVORITE_POSITION_LOOKUP_ID
        # BEST_POSITION_LOOKUP_ID
        # DEFAULT_POSITION_LOOKUP_ID
        # CREATED_DATE
        # CREATED_BY_USER_ID
        # LAST_MODIFIED_DATE
        # LAST_MODIFIED_BY_USER_ID