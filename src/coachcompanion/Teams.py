# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/27/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/1/2022

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from datetime import date
from coachcompanion.HomeScreen import *
from coachcompanion.Choices import *
import coachcompanion.SportChooser as sc
from coachcompanion.SQL_Insert import *
from coachcompanion.SQL_Extracts import *

# This class creates a form that can be used to add a new team
class Teams(HomeScreen):
    def __init__(self, sport, db, app):
        super().__init__(db, app)

        # Declare class variables
        self.LOOKUPS_COLUMNS = ('LOOKUP_ID, LOOKUP_DESCRIPTION, SYSTEM_DEFAULT_FLAG, USER_DEFAULT_FLAG')
        self.LOOKUPS_CONDITIONS = ('LOOKUP_TYPE = \'OT_RULES\' AND ACTIVE_FLAG = 1')
        # self.TEAMS_COLUMNS = ('MAX_PERIODS', 'OVERTIME_RULE_FLAG', 'OVERTIME_RULE_LOOKUP_ID',
        #                         'NAME', 'COLOR', 'SPONSOR', 'ACTIVE_FLAG', 'AGE_GROUP', 'YEAR',
        #                         'SEASON', 'DEFAULT_FLAG', 'CREATED_DATE', 'CREATED_BY_USER_ID',
        #                         'LAST_MODIFIED_DATE', 'LAST_MODIFIED_BY_USER_ID')
        self.TEAMS_CONDITIONS = 'ACTIVE_FLAG = 1'
        self.CURRENT_YEAR = date.today().year
        self.MIN_INNINGS = 1
        self.MAX_INNINGS = 9
        self.DEFAULT_INNINGS = 9
        self.YES = 'Yes'
        self.NO = 'No'

        self.sport = sport
        self.overtimeRulesDF = pd.DataFrame
        # self.overtimeRulesList = []
        
        self.overtimeRulesDF = ExtractData(self.DB, self.LOOKUPS_TABLE, self.ALL_COLUMNS, self.LOOKUPS_CONDITIONS)
        self.overtimeRulesDF.sort_values(by = ['USER_DEFAULT_FLAG', 'SYSTEM_DEFAULT_FLAG'], ascending = False, inplace = True)
        self.activeTeamsDF = ExtractData(self.DB, self.TEAMS_TABLE, self.ALL_COLUMNS, self.TEAMS_CONDITIONS)


    # This function creates the new team form
    def DisplayForm(self):

        # If the sport for the new team is baseball then create a label for the maximum periods
        if self.sport == self.BASEBALL or self.sport == self.TEEBALL:
            maxPeriodsLabel = toga.Label(
                'Maximum Innings: ',
                style = Pack(padding = (0, 0, 0, 50))
            )

        # create labels
        overtimeRuleFlagLabel = toga.Label(
            'Is overtime allowed? ',
            style = Pack(padding = (0, 0, 0, 50))
        )
        self.overtimeRuleLookupIDLabel = toga.Label(
            'What is the primary overtime rule? ',
            style = Pack(padding = (0, 0, 0, 50),
                visibility = 'hidden')
        )
        nameLabel = toga.Label(
            'Team Name: ',
            style = Pack(padding = (0, 0, 0, 50))
        )
        colorLabel = toga.Label(
            'Team Color: ',
            style = Pack(padding = (0, 0, 0, 50))
        )
        sponsorLabel = toga.Label(
            'Team Sponsor: ',
            style = Pack(padding = (0, 0, 0, 50))
        )
        ageGroupLabel = toga.Label(
            'Age Group: ',
            style = Pack(padding = (0, 0, 0, 50))
        )
        yearLabel = toga.Label(
            'Year: ',
            style = Pack(padding = (0, 0, 0, 50))
        )
        seasonLabel = toga.Label(
            'Season: ',
            style = Pack(padding = (0, 0, 0, 50))
        )
        for i in self.activeTeamsDF.index:
            if self.activeTeamsDF['DEFAULT_FLAG'][i] == 1:
                defaultFlagLabel = toga.Label(
                    'You already have a default team',
                    style = Pack(padding = (0, 0, 0, 50))
                )
            else:
                defaultFlagLabel = toga.Label(
                    'Do you want to set this team as your default? ',
                    style = Pack(padding = (0, 0, 0, 50))
                )
        self.missingInputsLabel = toga.Label(
            'You must fill out all fields',
            style = Pack(padding = (5),
                visibility = 'hidden',
                color = '#ff0000',
                text_align = 'center',
                flex = 1)
        )

        # Create inputs
        if self.sport in (self.BASEBALL, self.TEEBALL): 
            self.maxPeriodsInput = toga.NumberInput(
                            style = Pack(flex = 1, padding = (0, 50, 0, 0)),
                            min_value = self.MIN_INNINGS,
                            max_value = self.MAX_INNINGS,
                            default = self.DEFAULT_INNINGS
                        )
        self.overtimeRuleFlagInput = toga.Selection(
                            items = ['No', 'Yes'],
                            style = Pack(flex = 1, padding = (0, 50, 0, 0)),
                            on_select = self.ToggleOvertimeRuleLookup
                        )
        self.overtimeRuleLookupIDInput = toga.Selection(
                            items = self.overtimeRulesDF['LOOKUP_DESCRIPTION'], 
                            style = Pack(flex = 1, padding = (0, 50, 0, 0),
                                visibility = 'hidden'),
                            on_select = self.Test
                        )
        self.nameInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        self.colorInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        self.sponsorInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        self.ageGroupInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        self.yearInput = toga.NumberInput(
                            style = Pack(flex = 1, padding = (0, 50, 0, 0)),
                            min_value = self.CURRENT_YEAR - 5,
                            max_value = self.CURRENT_YEAR + 5,
                            default = self.CURRENT_YEAR
                        )
        self.seasonInput = toga.TextInput(style = Pack(flex = 1, padding = (0, 50, 0, 0)))
        for i in self.activeTeamsDF.index:
            if self.activeTeamsDF['DEFAULT_FLAG'][i] == 1:
                self.defaultFlagInput = toga.Selection(
                                    items = ['No', 'Yes'],
                                    style = Pack(flex = 1, padding = (0, 50, 0, 0)),
                                    enabled = False
                )
            else:
                self.defaultFlagInput = toga.Selection(
                                    items = ['Yes', 'No'],
                                    style = Pack(flex = 1, padding = (0, 50, 0, 0)),
                                    enabled = False
                                )

        # Create layout boxes
        if self.sport in (self.BASEBALL, self.TEEBALL): 
            maxPeriodsBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        overTimeRuleFlagBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        overtimeRuleLookupIDBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        nameBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        colorBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        sponsorBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        ageGroupBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        yearBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        seasonBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        defaultFlagBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        missingInputsBox = toga.Box(style = Pack(direction = ROW, padding = 5))
        buttonsBox = toga.Box(style = Pack(direction = ROW, padding = 5))

        # Create buttons
        saveButton = toga.Button(
            'Save',
            on_press = self.SaveTeam,
            style = Pack(padding = (5, self.SCREEN_WIDTH / 5, 5, (self.SCREEN_WIDTH / 5 * 3) - 100), width = 50)
        )
        cancelButton = toga.Button(
            'Cancel',
            on_press = self.Cancel,
            style = Pack(padding = (5, 0, 5, self.SCREEN_WIDTH / 5), width = 50)
        )

        # Create lists of widgets if baseball
        if self.sport in (self.BASEBALL, self.TEEBALL):
            labelsList = [maxPeriodsLabel, overtimeRuleFlagLabel, self.overtimeRuleLookupIDLabel, nameLabel,
                    colorLabel, sponsorLabel, ageGroupLabel, yearLabel,
                    seasonLabel, defaultFlagLabel]

            inputsList = [self.maxPeriodsInput, self.overtimeRuleFlagInput, self.overtimeRuleLookupIDInput, self.nameInput,
                    self.colorInput, self.sponsorInput, self.ageGroupInput, self.yearInput,
                    self.seasonInput, self.defaultFlagInput]

            boxesList = [maxPeriodsBox, overTimeRuleFlagBox, overtimeRuleLookupIDBox, nameBox,
                    colorBox, sponsorBox, ageGroupBox, yearBox, seasonBox,
                    defaultFlagBox]
        # Create lists of widgets if not baseball
        else:
            labelsList = [overtimeRuleFlagLabel, self.overtimeRuleLookupIDLabel, nameLabel,
                    colorLabel, sponsorLabel, ageGroupLabel, yearLabel,
                    seasonLabel, defaultFlagLabel]

            inputsList = [self.overtimeRuleFlagInput, self.overtimeRuleLookupIDInput, self.nameInput,
                    self.colorInput, self.sponsorInput, self.ageGroupInput, self.yearInput,
                    self.seasonInput, self.defaultFlagInput]

            boxesList = [overTimeRuleFlagBox, overtimeRuleLookupIDBox, nameBox,
                    colorBox, sponsorBox, ageGroupBox, yearBox, seasonBox,
                    defaultFlagBox]

        # Add widgets to layout boxes
        for i in range(len(labelsList)):
            boxesList[i].add(labelsList[i])
            boxesList[i].add(inputsList[i])
            self.mainBox.add(boxesList[i])



        ############################################################################################################
        # Need to find a place to implement this in the Players form, I believe, but for now suffice it to say that it works...
        # table = toga.Table(
        #     ['Lookup_ID', 'Lookup_Desc', 'Default_Flag', 'User_Default']
        # )

        # for i in self.overtimeRulesDF.index:
        #     table.data.insert(i, self.overtimeRulesDF['LOOKUP_ID'][i], self.overtimeRulesDF['LOOKUP_DESCRIPTION'][i],
        #         self.overtimeRulesDF['SYSTEM_DEFAULT_FLAG'][i], self.overtimeRulesDF['USER_DEFAULT_FLAG'][i])

        # self.mainBox.add(table)
        ############################################################################################################

        
        missingInputsBox.add(self.missingInputsLabel)
        
        buttonsBox.add(cancelButton)
        buttonsBox.add(saveButton)

        self.mainBox.add(missingInputsBox)
        self.mainBox.add(buttonsBox)

        # Return main layout box to the calling function
        return self.mainBox


    # This function clears the display
    def RemoveChildren(self):
        for child in reversed(self.mainBox.children):
            self.mainBox.remove(child)

    # Commit the new team to the database and display the next form
    def SaveTeam(self, widget):

        teamsInsertColumns = []
        missingInputFlag = ''
        # missingTeamNameInputFlag = ''
        # missingTeamColorInputFlag = ''
        # missingTeamSponsorInputFlag = ''
        # missingAgrGroupInputFlag = ''
        # missingSeasonInputFlag = ''
        # missingInputFlagList = []

        teamsInsertColumns.append('MAX_PERIODS')
        if self.sport in (self.BASEBALL, self.TEEBALL):
            teamsInsertValues = '(' + str(self.maxPeriodsInput.value)
        else:
            teamsInsertValues = '(' + str(4)
        
        teamsInsertColumns.append('OVERTIME_RULE_FLAG')
        if self.overtimeRuleFlagInput.value == self.YES:
            teamsInsertValues = teamsInsertValues + ', ' + str(1)
            teamsInsertColumns.append('OVERTIME_RULE_LOOKUP_ID')
            teamsInsertValues = teamsInsertValues + ', ' + \
                str(self.overtimeRulesDF['LOOKUP_ID'][self.overtimeRulesDF.LOOKUP_DESCRIPTION == self.overtimeRuleLookupIDInput.value][1])
        else:
            teamsInsertValues = teamsInsertValues + ', ' + str(0)
        
        if self.nameInput.value:
            teamsInsertColumns.append('NAME')
            teamsInsertValues = teamsInsertValues + ', "' + str(self.nameInput.value)
        else:
            missingInputFlag = True
            self.nameInput.style.background_color = '#ffcccb'
        
        if self.colorInput.value:
            teamsInsertColumns.append('COLOR')
            teamsInsertValues = teamsInsertValues + '", "' + str(self.colorInput.value)
        else:
            missingInputFlag = True
            self.colorInput.style.background_color = '#ffcccb'
        
        if self.sponsorInput.value:
            teamsInsertColumns.append('SPONSOR')
            teamsInsertValues = teamsInsertValues + '", "' + str(self.sponsorInput.value)
        else:
            missingInputFlag = True
            self.sponsorInput.style.background_color = '#ffcccb'
        
        teamsInsertColumns.append('ACTIVE_FLAG')
        teamsInsertValues = teamsInsertValues + '", ' + str(1)

        if self.ageGroupInput.value:
            teamsInsertColumns.append('AGE_GROUP')
            teamsInsertValues = teamsInsertValues + ', "' + str(self.ageGroupInput.value)
        else:
            missingInputFlag = True
            self.ageGroupInput.style.background_color = '#ffcccb'

        teamsInsertColumns.append('YEAR')
        teamsInsertValues = teamsInsertValues + '", ' + str(self.yearInput.value)

        if self.seasonInput.value:
            teamsInsertColumns.append('SEASON')
            teamsInsertValues = teamsInsertValues + ', "' + str(self.seasonInput.value)
        else:
            missingInputFlag = True
            self.seasonInput.style.background_color = '#ffcccb'
        
        teamsInsertColumns.append('DEFAULT_FLAG')
        if self.defaultFlagInput.value == self.YES:
            teamsInsertValues = teamsInsertValues + '", ' + str(1)
        else:
            teamsInsertValues = teamsInsertValues + ', ' + str(0)

        teamsInsertColumns.append('CREATED_DATE')
        teamsInsertValues = teamsInsertValues + ', ' + '\'' + str(date.today()) + '\''

        # teamsInsertColumns.append('CREATED_BY_USER_ID')
        # teamsInsertValues = teamsInsertValues + ', ' + str('SBHOBBES')

        teamsInsertColumns.append('LAST_MODIFIED_DATE')
        teamsInsertValues = teamsInsertValues + ', ' + '\'' + str(date.today()) + '\''

        # teamsInsertColumns.append('LAST_MODIFIED_BY_USER_ID')
        # teamsInsertValues = teamsInsertValues + ', ' + str('SBHOBBES')
        teamsInsertValues = teamsInsertValues + ')'

        # Commit the team to the database
        if not missingInputFlag:
            InsertIntoTables(self.DB, self.TEAMS_TABLE, tuple(teamsInsertColumns), teamsInsertValues, valueType = 'string')

            # Clear all widgets from the screen
            self.RemoveChildren()

            # Display the choices screen
            choice = ChoicesScreen('NEW_TEAM', self.DB, self.APP)
            self.mainBox.add(choice.DisplayScreen())
        else:
            self.missingInputsLabel.style.visibility = 'visible'
            print('this')

    def Cancel(self, widget):
        home = sc.HomeScreen(self.DB, self.APP)
        self.RemoveChildren()
        self.mainBox.add(home.DisplayForm())

    def Test(self, widget):
        print(self.overtimeRulesDF['LOOKUP_ID'][self.overtimeRulesDF.LOOKUP_DESCRIPTION == self.overtimeRuleLookupIDInput.value])

    def ToggleOvertimeRuleLookup(self, widget):
        if self.overtimeRuleFlagInput.value == 'Yes':
            self.overtimeRuleLookupIDInput.style.visibility = 'visible'
            self.overtimeRuleLookupIDLabel.style.visibility = 'visible'
        else:
            self.overtimeRuleLookupIDInput.style.visibility = 'hidden'
            self.overtimeRuleLookupIDLabel.style.visibility = 'hidden'

    def RemoveChildren(self):
        for child in reversed(self.mainBox.children):
            self.mainBox.remove(child)