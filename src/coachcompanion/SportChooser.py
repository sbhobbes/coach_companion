# Author: Seth Hobbes, member of Springboro Technologies, LLC DBA Monarch Technologies
# Created: 7/27/2022
# Copyright: Springboro Technologies, LLC DBA Monarch Technologies all rights reserved
# Last Modified: 8/1/2022


import toga
import pandas as pd
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from coachcompanion.Teams import *
from coachcompanion.HomeScreen import *

class SportChooserScreen(HomeScreen):
    def __init__(self, db, app):
        super().__init__(db, app)


    def DisplayForm(self):

        chooseSportLabel = toga.Label(
            'Pick a Sport',
            style = Pack(padding = 5, text_align = 'center', font_size = self.HEADER_FONT_SIZE)
        )

        baseballButton = toga.Button(
            'New Baseball/Softball Team',
            on_press = self.NewBaseballTeam,
            style = Pack(padding = (5, ((self.SCREEN_WIDTH / 2) - (self.SCREEN_WIDTH / 8))), background_color = '#007700', 
            color = 'white', height = self.SCREEN_HEIGHT / 10, width = self.SCREEN_WIDTH / 4, font_weight = 'bold')
        )
        print(((self.SCREEN_WIDTH / 2) - (self.SCREEN_WIDTH / 8)))

        teeballButton = toga.Button(
            'New Tee-Ball Team',
            on_press = self.NewTeeballTeam,
            style = Pack(
                padding = (5, ((self.SCREEN_WIDTH / 2) - (self.SCREEN_WIDTH / 8))), background_color = '#007700', 
                color = 'white', height = self.SCREEN_HEIGHT / 10, width = self.SCREEN_WIDTH / 4, font_weight = 'bold'
            )
        )

        footballButton = toga.Button(
            'New Football Team',
            on_press = self.NewFootballTeam,
            style = Pack(
                padding = (5, ((self.SCREEN_WIDTH / 2) - (self.SCREEN_WIDTH / 8))), background_color = '#007700', 
                color = 'white', height = self.SCREEN_HEIGHT / 10, width = self.SCREEN_WIDTH / 4, font_weight = 'bold'
            )
        )

        soccerButton = toga.Button(
            'New Soccer Team',
            on_press = self.NewSoccerTeam,
            style = Pack(
                padding = (5, ((self.SCREEN_WIDTH / 2) - (self.SCREEN_WIDTH / 8))), background_color = '#007700', 
                color = 'white', height = self.SCREEN_HEIGHT / 10, width = self.SCREEN_WIDTH / 4, font_weight = 'bold'
            )
        )

        hockeyButton = toga.Button(
            'New Hockey Team',
            on_press = self.NewHockeyTeam,
            style = Pack(
                padding = (5, ((self.SCREEN_WIDTH / 2) - (self.SCREEN_WIDTH / 8))), background_color = '#007700', 
                color = 'white', height = self.SCREEN_HEIGHT / 10, width = self.SCREEN_WIDTH / 4, font_weight = 'bold'
            )
        )

        basketballButton = toga.Button(
            'New Basketball Team',
            on_press = self.NewBasketballTeam,
            style = Pack(
                padding = (5, ((self.SCREEN_WIDTH / 2) - (self.SCREEN_WIDTH / 8))), background_color = '#007700', 
                color = 'white', height = self.SCREEN_HEIGHT / 10, width = self.SCREEN_WIDTH / 4, font_weight = 'bold'
            )
        )

        self.mainBox = toga.Box(style = Pack(direction = COLUMN, width = self.SCREEN_WIDTH))

        buttonList = [baseballButton, teeballButton, footballButton, soccerButton, hockeyButton, basketballButton]

        self.mainBox.add(chooseSportLabel)

        for button in buttonList:
            self.mainBox.add(button)

        
        return self.mainBox



    def NewBaseballTeam(self, widget):
        self.CreateTeam(self.BASEBALL)
        print(self.SCREEN_HEIGHT)
        print(self.SCREEN_WIDTH)


    def NewTeeballTeam(self, widget):
        self.CreateTeam(self.TEEBALL)


    def NewFootballTeam(self, widget):
        self.CreateTeam(self.FOOTBALL)


    def NewSoccerTeam(self, widget):
        self.CreateTeam(self.SOCCER)

    
    def NewHockeyTeam(self, widget):
        self.CreateTeam(self.HOCKEY)

    def NewBasketballTeam(self, widget):
        self.CreateTeam(self.BASKETBALL)


    
    def RemoveChildren(self):
        for child in reversed(self.mainBox.children):
            self.mainBox.remove(child)


    def CreateTeam(self, sport):
        
        self.RemoveChildren()
        newTeam = Teams(sport, self.DB, self.APP)
        
        self.mainBox.add(newTeam.DisplayForm())