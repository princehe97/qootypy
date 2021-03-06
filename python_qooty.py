#importing packages

import csv
import random
import pandas as pd
import pygame
pygame.init()

#creating the screen, defining the dimensions
ScreenHeight = 400
ScreenWidth = 640

win = pygame.display.set_mode((ScreenWidth, ScreenHeight))

pygame.display.set_caption("PyQooty")

#defining the variables that load the various background images for screens
start_bg = pygame.image.load('start.png')
game_bg = pygame.image.load('gamescreen.png')
general_bg = pygame.image.load('generic.png')
teamSelect_bg = pygame.image.load('team_selection.png')

#defining variables that set the fonts and respective sizes
myfont_main = pygame.font.SysFont("Verdana", 20)
myfont_game = pygame.font.SysFont("Verdana", 28)
myfont_comm = pygame.font.SysFont("Consolas", 16)
myfont_selectTitle = pygame.font.SysFont("Verdana", 36)
myfont_mini = pygame.font.SysFont("Verdana", 8, bold=True)

clock = pygame.time.Clock()

#define colors that will be used when drawing shapes and writing texts on screen
Bluey_Green = (0, 200, 200)
Light_Green = (100, 255, 100)
Green = (0, 255, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Soft_Red = (255, 150, 150)
Blue = (0, 0, 255)
Soft_Blue = (150, 150, 255)
Light_Grey = (210, 210, 210)
Dark_Grey = (80, 80, 80)

# defined under this function is everything to do with the main menu screen
def main_menu():
	win.blit(start_bg, (0,0))
	mouse
	#print(mouse)
	#coordinates1 = (90, 275, 110, 25)
	#coordinates2 = (90, 300, 120, 25)
	#coordinates3 = (90, 325, 120, 25)
	#coordinates4 = (90, 350, 150, 25)
	global main
	global playing_match
	global AddingPlayers
	global AddingTeams
	global Selection
	
	#these determine that if the mouse cursor is between certain coordinates on the screen, texts will have interactions.
	if 90 + 110 > mouse[0] > 90 and 275 + 25 > mouse[1] > 275:
		#this makes the text 'play footy' light up in a "Light Green" colour instead of a Bluey Green colour when the mouse hovers over it
		menu_text1 = myfont_main.render('Play Footy', 1, Light_Green)
		#if a click is made while the mouse is between the above coordinates then the screen is instructed to transfer to a 'playing match' state
		if click[0] == 1:
			
			main = False
			playing_match = True
			AddingTeams = False
			AddingPlayers = False
			Selection = False
			pygame.time.delay(200)
	else:
		menu_text1 = myfont_main.render('Play Footy', 1, Bluey_Green)

	#the following code all follow the same pattern as above
	if 90 + 120 > mouse[0] > 90 and 300 + 25 > mouse[1] > 300:
		menu_text2 = myfont_main.render('Add A Team', 1, Light_Green)
		if click[0] == 1:
			main = False
			playing_match = False
			AddingTeams = True
			AddingPlayers = False
			Selection = False
			pygame.time.delay(80)
	else:
		menu_text2 = myfont_main.render('Add A Team', 1, Bluey_Green)
	if 90 + 120 > mouse[0] > 90 and 325 + 25 > mouse[1] > 325:
		menu_text3 = myfont_main.render('Add Players', 1, Light_Green)
		if click[0] == 1:
			main = False
			playing_match = False
			AddingTeams = False
			AddingPlayers = True
			Selection = False
			pygame.time.delay(80)
	else:
		menu_text3 = myfont_main.render('Add Players', 1, Bluey_Green)
	if 90 + 150 > mouse[0] > 90 and 350 + 25 > mouse[1] > 350:
		menu_text4 = myfont_main.render('Team Selection', 1, Light_Green)
		if click[0] == 1:
			main = False
			playing_match = False
			AddingTeams = False
			AddingPlayers = False
			Selection = True
			SelectionMenu.buffering += 5
			pygame.time.delay(80)
	else:	
		menu_text4 = myfont_main.render('Team Selection', 1, Bluey_Green)
	#this actually makes the text defined in the above code appear on screen, aka calling the variable
	win.blit(menu_text1, (90, 275))
	win.blit(menu_text2, (90, 300))
	win.blit(menu_text3, (90, 325))
	win.blit(menu_text4, (90, 350))
	#this is necessary to ensure the screen is constantly updating because it needs to redetermine the position of the mouse
	pygame.display.update()

'''the main menu code has ended, everything below relates to the Team Creation Screen i.e. the screen in which you create a team to add into the sim's database so you can
select it to play in a game'''
class TeamCreationScreen(object):
	#defining the default variables before anything has happened i.e. the textbox for the team name starts empty
	active = False
	TeamNameText = ""
	ABRV_input = False
	ABRV_Text = ""
	TS_recentAct = False
	latestTeam = ""
	TeamMasterListQueue = []
	InQueue = 0
	newlyAdded = 0
	ChangesSavedNotice = False
	
	#this opens up the initial state of the screen
	def openTCScreen():
		win.blit(general_bg, (0,0))
		mouse
		pygame.draw.rect(win, (0,0,0), (45,100,260,40),0)
		pygame.draw.rect(win, (100, 100, 100), (45, 180, 500, 150), 0)
		
		#creation of the label text including the heading, the labels
		TS_titleText = myfont_selectTitle.render('Add A Team', 1, Green)
		TS_EntryLabel = myfont_main.render('Enter Team Name Here: ', 1, Green)
		TS_NoticeLabel = myfont_main.render('Latest Activity: ', 1, Green)
		win.blit(TS_titleText, (20, 20))
		win.blit(TS_EntryLabel, (50,105))
		win.blit(TS_NoticeLabel, (50, 185))
		
		#this is to define that if a team is entered, it adds into the new team queue awaiting to be confirmed to be added
		if TeamCreationScreen.TS_recentAct:
			TS_Notice1 = myfont_main.render(TeamCreationScreen.latestTeam + ' is in the New Team Queue', 1, White)
			TS_Notice2 = myfont_main.render(str(TeamCreationScreen.InQueue) + ' new team(s) have been entered', 1, White)
			TS_Notice3 = myfont_main.render('Click the SAVE button to confirm the additions', 1, White)
			win.blit(TS_Notice1, (50, 210))
			win.blit(TS_Notice2, (50, 250))
			win.blit(TS_Notice3, (50, 290))
		
		#this is code to define that a notice will be prompted after SAVE has been clicked
		if TeamCreationScreen.ChangesSavedNotice:
			TS_Notice1 = myfont_main.render('Addition(s) saved to Teams.txt', 1, White)
			TS_Notice2 = myfont_main.render(str(TeamCreationScreen.newlyAdded) + ' new team(s) were added', 1, White)
			TS_Notice3 = myfont_main.render('New Team Queue Reset', 1, White)
			win.blit(TS_Notice1, (50, 210))
			win.blit(TS_Notice2, (50, 250))
			win.blit(TS_Notice3, (50, 290))

		if TeamCreationScreen.active:
			colour = White
		else:
			colour = Light_Grey
		team_inputBox = pygame.draw.rect(win, colour, (305, 100, 240, 40), 0)
		
		#save changes button - this code is to develop the save button that interacts; the shade of colour lights up when mouse hovers over it
		if 50 + 80 > mouse[0] > 50 and 350 + 40 > mouse[1] > 350:
			TS_SaveButton = pygame.draw.rect(win, Soft_Red, (50, 350, 80, 40), 0)
			#this code defines that when the SAVE button is clicked, the List of teams entered is written into a txt file
			if click[0] == 1:
				OpenMasterList = open('Teams.txt', 'a')
				for i in TeamCreationScreen.TeamMasterListQueue:
					new_team = str(i) + '\n'
					OpenMasterList.write(new_team)
					pygame.time.delay(120)
				OpenMasterList.close()
				TeamCreationScreen.ChangesSavedNotice = True
				TeamCreationScreen.TS_recentAct = False
				
				TeamCreationScreen.newlyAdded = TeamCreationScreen.InQueue
				TeamCreationScreen.InQueue = 0
				TeamCreationScreen.TeamMasterListQueue = []
		else:
			TS_SaveButton = pygame.draw.rect(win, Red, (50, 350, 80, 40), 0)
		TS_SaveLabel = myfont_main.render('SAVE', 1, White)
		win.blit(TS_SaveLabel, (58, 358))
		
		global main
		global AddingTeams
		#main menu button - this is to return the screen to main menu, create the button and reset the settings to default
		if 320 + 210 > mouse[0] > 320 and 350 + 40 > mouse[1] > 350:
			TS_MainMenuButton = pygame.draw.rect(win, Soft_Red, (320, 350, 210, 40), 0)
			if click[0] == 1:
				main = True
				AddingTeams = False
				
				TeamCreationScreen.active = False
				TeamCreationScreen.TeamNameText = ""
				TeamCreationScreen.TS_recentAct = False
				TeamCreationScreen.latestTeam = ""
				TeamCreationScreen.TeamMasterListQueue = []
				TeamCreationScreen.InQueue = 0
				newlyAdded = 0
				TeamCreationScreen.ChangesSavedNotice = False
				
				pygame.time.delay(200)
		else:
			TS_MainMenuButton = pygame.draw.rect(win, Red, (320, 350, 210, 40), 0)
		TS_MainMenuLabel = myfont_main.render('Back To Main Menu', 1, White)
		win.blit(TS_MainMenuLabel, (328, 358))

		#this code addresses when no team has been entered, it's the default seting for the team selection screen
		teamEntered = False
		if not teamEntered:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					#user clicks on input box - to activate it
					if team_inputBox.collidepoint(event.pos):
						#toggle the active variable
						TeamCreationScreen.active = True
					else:
						TeamCreationScreen.active = False
					if not TeamCreationScreen.active:
						team_inputBox = pygame.draw.rect(win, Light_Grey, (305, 100, 240, 40), 0)
					else:
						team_inputBox = pygame.draw.rect(win, White, (305, 100, 240, 40), 0)
				#this allows things to be typed into the input box and recorded into the 'inserted team queue' upon hitting enter
				if event.type == pygame.KEYDOWN:
					#process typing
					if TeamCreationScreen.active:
						if event.key == pygame.K_RETURN:
							TeamCreationScreen.TeamMasterListQueue.append(TeamCreationScreen.TeamNameText)
							TeamCreationScreen.InQueue += 1
							TeamCreationScreen.TS_recentAct = True
							TeamCreationScreen.ChangesSavedNotice = False
							TeamCreationScreen.latestTeam = str(TeamCreationScreen.TeamNameText)
							TeamCreationScreen.TeamNameText = ""
						elif event.key == pygame.K_BACKSPACE:
							TeamCreationScreen.TeamNameText = TeamCreationScreen.TeamNameText[:-1]
						else:
							TeamCreationScreen.TeamNameText += event.unicode
				txt_surface = myfont_main.render(TeamCreationScreen.TeamNameText, True, Blue)
				win.blit(txt_surface, (310, 105))
							
				pygame.display.update()
				if event.type == pygame.QUIT:
					pygame.quit()

#this class relates to the screen that is invovled with entering Players into the app and recording them into a csv file.
class PlayerCreationScreen(object):
	#default settings of variables
	active = False
	playerNameText = ""
	PS_recentAct = False
	latestPlayer = ""
	PlayerMasterListQueue = []
	InQueue = 0
	newlyAdded = 0
	ChangesSavedNotice = False
	
	def openPCScreen():
		#setting up the visuals of the screen, creating buttons that interact with mouse, textboxs for inputting player names and labels
		win.blit(general_bg, (0,0))
		mouse
		pygame.draw.rect(win, (0,0,0), (45,100,260,40),0)
		pygame.draw.rect(win, (100, 100, 100), (45, 180, 500, 150), 0)
		
		PS_titleText = myfont_selectTitle.render('Add Players', 1, Green)
		PS_EntryLabel = myfont_main.render('Enter Player Name Here: ', 1, Green)
		PS_NoticeLabel = myfont_main.render('Latest Activity: ', 1, Green)
		win.blit(PS_titleText, (20, 20))
		win.blit(PS_EntryLabel, (50,105))
		win.blit(PS_NoticeLabel, (50, 185))
		
		if PlayerCreationScreen.PS_recentAct:
			PS_Notice1 = myfont_main.render(PlayerCreationScreen.latestPlayer + ' was added as a Free Agent', 1, White)
			PS_Notice2 = myfont_main.render(str(PlayerCreationScreen.InQueue) + ' player(s) are in the Free Agent Queue', 1, White)
			PS_Notice3 = myfont_main.render('Click the SAVE button to confirm the additions', 1, White)
			win.blit(PS_Notice1, (50, 210))
			win.blit(PS_Notice2, (50, 250))
			win.blit(PS_Notice3, (50, 290))
		
		if PlayerCreationScreen.ChangesSavedNotice:
			PS_Notice1 = myfont_main.render('Additions saved to MasterList.csv', 1, White)
			PS_Notice2 = myfont_main.render(str(PlayerCreationScreen.newlyAdded) + ' new players were added', 1, White)
			PS_Notice3 = myfont_main.render('Free Agents Queue Reset', 1, White)
			win.blit(PS_Notice1, (50, 210))
			win.blit(PS_Notice2, (50, 250))
			win.blit(PS_Notice3, (50, 290))

		if PlayerCreationScreen.active:
			colour = White
		else:
			colour = Light_Grey
		player_inputBox = pygame.draw.rect(win, colour, (305, 100, 240, 40), 0)
		
		#save changes button
		if 50 + 80 > mouse[0] > 50 and 350 + 40 > mouse[1] > 350:
			PS_SaveButton = pygame.draw.rect(win, Soft_Red, (50, 350, 80, 40), 0)
			if click[0] == 1:
				with open('MasterList.csv', mode = 'a', newline = '') as OpenMasterList:
					for i in PlayerCreationScreen.PlayerMasterListQueue:
						OpenMasterList_Write = csv.writer(OpenMasterList, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						new_player = str(i)
						OpenMasterList_Write.writerow([new_player, 'Free Agent'])
						pygame.time.delay(120)
				OpenMasterList.close()
				PlayerCreationScreen.ChangesSavedNotice = True
				PlayerCreationScreen.PS_recentAct = False
				
				PlayerCreationScreen.newlyAdded = PlayerCreationScreen.InQueue
				PlayerCreationScreen.InQueue = 0
				PlayerCreationScreen.PlayerMasterListQueue = []
		else:
			PS_SaveButton = pygame.draw.rect(win, Red, (50, 350, 80, 40), 0)
		PS_SaveLabel = myfont_main.render('SAVE', 1, White)
		win.blit(PS_SaveLabel, (58, 358))
		
		global main
		global AddingPlayers
		#main menu button
		if 320 + 210 > mouse[0] > 320 and 350 + 40 > mouse[1] > 350:
			PS_MainMenuButton = pygame.draw.rect(win, Soft_Red, (320, 350, 210, 40), 0)
			if click[0] == 1:
				main = True
				AddingPlayers = False
				
				PlayerCreationScreen.active = False
				PlayerCreationScreen.playerNameText = ""
				PlayerCreationScreen.PS_recentAct = False
				PlayerCreationScreen.latestPlayer = ""
				PlayerCreationScreen.PlayerMasterListQueue = []
				PlayerCreationScreen.InQueue = 0
				newlyAdded = 0
				PlayerCreationScreen.ChangesSavedNotice = False
				
				pygame.time.delay(200)
		else:
			PS_MainMenuButton = pygame.draw.rect(win, Red, (320, 350, 210, 40), 0)
		PS_MainMenuLabel = myfont_main.render('Back To Main Menu', 1, White)
		win.blit(PS_MainMenuLabel, (328, 358))
		
		#code related to before a player is entered - i.e. default condition of the screen
		playerEntered = False
		if not playerEntered:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					#user clicks on input box - which activates the box allowing player names to be typed in
					if player_inputBox.collidepoint(event.pos):
						#toggle the active variable
						PlayerCreationScreen.active = True
					else:
						PlayerCreationScreen.active = False
					if not PlayerCreationScreen.active:
						player_inputBox = pygame.draw.rect(win, Light_Grey, (305, 100, 240, 40), 0)
					else:
						player_inputBox = pygame.draw.rect(win, White, (305, 100, 240, 40), 0)
				if event.type == pygame.KEYDOWN:
					#process typing - code enables typing player names into the textbox, upon hitting ENTER puts the input player into the queue to be confirmed with SAVE
					if PlayerCreationScreen.active:
						if event.key == pygame.K_RETURN:
							PlayerCreationScreen.PlayerMasterListQueue.append(PlayerCreationScreen.playerNameText)
							PlayerCreationScreen.InQueue += 1
							#print(PlayerCreationScreen.PlayerMasterListQueue)
							PlayerCreationScreen.PS_recentAct = True
							PlayerCreationScreen.ChangesSavedNotice = False
							PlayerCreationScreen.latestPlayer = str(PlayerCreationScreen.playerNameText)
							PlayerCreationScreen.playerNameText = ""
						elif event.key == pygame.K_BACKSPACE:
							PlayerCreationScreen.playerNameText = PlayerCreationScreen.playerNameText[:-1]
						else:
							PlayerCreationScreen.playerNameText += event.unicode
				txt_surface = myfont_main.render(PlayerCreationScreen.playerNameText, True, Blue)
				win.blit(txt_surface, (310, 105))
						
				pygame.display.update()
				if event.type == pygame.QUIT:
					pygame.quit()
# this class creates the screen for selecting teams, loads the teams that have been inserted within the application and creates a click-option
class SelectionMenu(object):
	buffering = 0
	
	DisplayTeamList = []
	get_Teams = True
	teamCount = 0
	teamListRef = 0

	active_cell1 = False
	active_cell2 = False
	active_cell3 = False
	active_cell4 = False
	active_cell5 = False
	active_cell6 = False
	active_cell7 = False
	active_cell8 = False
	active_cell9 = False
	active_cell10 = False
	active_cell11 = False
	active_cell12 = False
	active_cell13 = False
	active_cell14 = False
	active_cell15 = False
	active_cell16 = False

	teamChosen = False
	teamChosenText = ""

#this code retrieves teams that have already been inserted into the application from a text file
	def retrieveTeamList():
		team_fname = open('Teams.txt', 'r')
		for club in team_fname:
			club0 = club.rstrip()
			SelectionMenu.DisplayTeamList.append(club0)
			#print(SelectionMenu.DisplayTeamList)
			SelectionMenu.teamCount += 1
		SelectionMenu.get_Teams = False
	
	#this prompts the list of teams to be shown in an onscreen range of options
	def showTeamList():
		emptyTeamName = '[Empty]'
		n = SelectionMenu.teamListRef
		teamNameDisText = SelectionMenu.DisplayTeamList
		if n >= 0:
			global team1
			team1 = str(teamNameDisText[0])
			TL_Slot1 = myfont_comm.render(team1, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell1 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot1 = myfont_comm.render(emptyTeamName, 1, White)				
		if n >= 1:
			global team2
			team2 = str(teamNameDisText[1])
			TL_Slot2 = myfont_comm.render(team2, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell2 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot2 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 2:
			global team3
			team3 = str(teamNameDisText[2])
			TL_Slot3 = myfont_comm.render(team3, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell3 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot3 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 3:
			global team4
			team4 = str(teamNameDisText[3])
			TL_Slot4 = myfont_comm.render(team4, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell4 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot4 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 4:
			global team5
			team5 = str(teamNameDisText[4])
			TL_Slot5 = myfont_comm.render(team5, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell5 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot5 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 5:
			global team6
			team6 = str(teamNameDisText[5])
			TL_Slot6 = myfont_comm.render(team6, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell6 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot6 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 6:
			global team7
			team7 = str(teamNameDisText[6])
			TL_Slot7 = myfont_comm.render(team7, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell7 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot7 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 7:
			global team8
			team8 = str(teamNameDisText[7])
			TL_Slot8 = myfont_comm.render(team8, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell8 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot8 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 8:
			global team9
			team9 = str(teamNameDisText[8])
			TL_Slot9 = myfont_comm.render(team9, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell9 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot9 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 9:
			global team10
			team10 = str(teamNameDisText[9])
			TL_Slot10 = myfont_comm.render(team10, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell10 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot10 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 10:
			global team11
			team11 = str(teamNameDisText[10])
			TL_Slot11 = myfont_comm.render(team11, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell11 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot11 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 11:
			global team12
			team12 = str(teamNameDisText[11])
			TL_Slot12 = myfont_comm.render(team12, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell12 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot12 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 12:
			global team13
			team13 = str(teamNameDisText[12])		
			TL_Slot13 = myfont_comm.render(team13, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell13 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot13 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 13:
			global team14
			team14 = str(teamNameDisText[13])
			TL_Slot14 = myfont_comm.render(team14, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell14 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot14 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 14:
			global team15
			team15 = str(teamNameDisText[14])
			TL_Slot15 = myfont_comm.render(team15, 1, White)
			SelectionMenu.teamCount -= 1
			SelectionMenu.active_cell15 = True
			if SelectionMenu.teamCount > 0:
				SelectionMenu.teamListRef += 1
		else:
			TL_Slot15 = myfont_comm.render(emptyTeamName, 1, White)
		if n >= 15:
			global team16
			team16 = str(teamNameDisText[15])
			TL_Slot16 = myfont_comm.render(team16, 1, White)
			SelectionMenu.active_cell16 = True
		else:
			TL_Slot16 = myfont_comm.render(emptyTeamName, 1, White)
		
		win.blit(TL_Slot1, (335, 70))
		win.blit(TL_Slot2, (335, 90))
		win.blit(TL_Slot3, (335, 110))
		win.blit(TL_Slot4, (335, 130))
		win.blit(TL_Slot5, (335, 150))
		win.blit(TL_Slot6, (335, 170))
		win.blit(TL_Slot7,(335, 190))
		win.blit(TL_Slot8,(335, 210))
		win.blit(TL_Slot9, (335, 230))
		win.blit(TL_Slot10, (335, 250))
		win.blit(TL_Slot11, (335, 270))
		win.blit(TL_Slot12, (335, 290))
		win.blit(TL_Slot13, (335, 310))
		win.blit(TL_Slot14, (335, 330))
		win.blit(TL_Slot15, (335, 350))
		win.blit(TL_Slot16, (335, 370))
		
		SelectionMenu.mouseNavList()

# This code enables interactivity of the screen with the mouse, allows teams to be chosen from the options with a click
	def mouseNavList():
		if SelectionMenu.active_cell1:
			if 330 + 270 > mouse[0] > 330 and 65 + 20 > mouse[1] > 65:
				pygame.draw.circle(win, Red, (590, 75), 5)
				if click[0] == 1:
					global team1
					SelectionMenu.teamChosenText = team1
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell2:
			if 330 + 270 > mouse[0] > 330 and 85 + 20 > mouse[1] > 85:
				pygame.draw.circle(win, Red, (590, 95), 5)
				if click[0] == 1:
					global team2
					SelectionMenu.teamChosenText = team2
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell3:
			if 330 + 270 > mouse[0] > 330 and 105 + 20 > mouse[1] > 105:
				pygame.draw.circle(win, Red, (590, 115), 5)
				if click[0] == 1:
					global team3
					SelectionMenu.teamChosenText = team3
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell4:
			if 330 + 270 > mouse[0] > 330 and 125 + 20 > mouse[1] > 125:
				pygame.draw.circle(win, Red, (590, 135), 5)
				if click[0] == 1:
					global team4
					SelectionMenu.teamChosenText = team4
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell5:
			if 330 + 270 > mouse[0] > 330 and 145 + 20 > mouse[1] > 145:
				pygame.draw.circle(win, Red, (590, 155), 5)
				if click[0] == 1:
					global team5
					SelectionMenu.teamChosenText = team5
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell6:
			if 330 + 270 > mouse[0] > 330 and 165 + 20 > mouse[1] > 165:
				pygame.draw.circle(win, Red, (590, 175), 5)
				if click[0] == 1:
					global team6
					SelectionMenu.teamChosenText = team6
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell7:
			if 330 + 270 > mouse[0] > 330 and 185 + 20 > mouse[1] > 185:
				pygame.draw.circle(win, Red, (590, 195), 5)
				if click[0] == 1:
					global team7
					SelectionMenu.teamChosenText = team7
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell8:
			if 330 + 270 > mouse[0] > 330 and 205 + 20 > mouse[1] > 205:
				pygame.draw.circle(win, Red, (590, 215), 5)
				if click[0] == 1:
					global team8
					SelectionMenu.teamChosenText = team8
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell9:
			if 330 + 270 > mouse[0] > 330 and 225 + 20 > mouse[1] > 225:
				pygame.draw.circle(win, Red, (590, 235), 5)
				if click[0] == 1:
					global team9
					SelectionMenu.teamChosenText = team9
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell10:
			if 330 + 270 > mouse[0] > 330 and 245 + 20 > mouse[1] > 245:
				pygame.draw.circle(win, Red, (590, 255), 5)
				if click[0] == 1:
					global team10
					SelectionMenu.teamChosenText = team10
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell11:
			if 330 + 270 > mouse[0] > 330 and 265 + 20 > mouse[1] > 265:
				pygame.draw.circle(win, Red, (590, 275), 5)
				if click[0] == 1:
					global team11
					SelectionMenu.teamChosenText = team11
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell12:
			if 330 + 270 > mouse[0] > 330 and 285 + 20 > mouse[1] > 285:
				pygame.draw.circle(win, Red, (590, 295), 5)
				if click[0] == 1:
					global team12
					SelectionMenu.teamChosenText = team12
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell13:
			if 330 + 270 > mouse[0] > 330 and 305 + 20 > mouse[1] > 305:
				pygame.draw.circle(win, Red, (590, 315), 5)
				if click[0] == 1:
					global team13
					SelectionMenu.teamChosenText = team13
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell14:
			if 330 + 270 > mouse[0] > 330 and 325 + 20 > mouse[1] > 325:
				pygame.draw.circle(win, Red, (590, 335), 5)
				if click[0] == 1:
					global team14
					SelectionMenu.teamChosenText = team14
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell15:
			if 330 + 270 > mouse[0] > 330 and 345 + 20 > mouse[1] > 345:
				pygame.draw.circle(win, Red, (590, 355), 5)
				if click[0] == 1:
					global team15
					SelectionMenu.teamChosenText = team15
					SelectionMenu.teamChosen = True
		if SelectionMenu.active_cell16:
			if 330 + 270 > mouse[0] > 330 and 365 + 20 > mouse[1] > 365:
				pygame.draw.circle(win, Red, (590, 375), 5)
				if click[0] == 1:
					global team16
					SelectionMenu.teamChosenText = team16
					SelectionMenu.teamChosen = True
	#creates the rest of the layout for the default screen when you click team selection from the menu
	def openSelection():
		if SelectionMenu.buffering > 0:
			SelectionMenu.buffering -= 1
		win.blit(general_bg, (0,0))
		mouse
		pygame.draw.rect(win, (0,0,0), (330,25,270,40),0)
		pygame.draw.rect(win, (100, 100, 100), (330, 65, 270, 325), 0)
		pygame.draw.rect(win, (200, 200, 200), (40, 150, 250, 30), 0)
		
		S_titleText = myfont_selectTitle.render('Team Selection', 1, Green)
		S_subtitleText = myfont_main.render('Choose A Team From The List', 1, Light_Green)
		S_teamListLabel = myfont_main.render('Team List', 1, White)
		S_selectedTeamLabel = myfont_main.render('Team Selected: ', 1, Light_Green)
		win.blit(S_titleText, (20, 20))
		win.blit(S_subtitleText, (20, 70))
		win.blit(S_teamListLabel, (335, 35))
		win.blit(S_selectedTeamLabel, (30, 120))

		#main menu button
		global main
		global Selection
		global Pick_Positions
		
		if 45 + 210 > mouse[0] > 45 and 350 + 40 > mouse[1] > 350:
			S_MainMenuButton = pygame.draw.rect(win, Soft_Red, (45, 350, 210, 40), 0)
			if SelectionMenu.buffering == 0:
				if click[0] == 1:
					
					main = True
					Selection = False
					
					SelectionMenu.teamChosen = False
					SelectionMenu.teamChosenText = ""
					pygame.time.delay(200)
		else:
			S_MainMenuButton = pygame.draw.rect(win, Red, (45, 350, 210, 40), 0)
		S_MainMenuLabel = myfont_main.render('Back To Main Menu', 1, White)
		win.blit(S_MainMenuLabel, (53, 358))

		if SelectionMenu.teamChosen:
			ShowChosenTeam = myfont_main.render(SelectionMenu.teamChosenText, 1, Blue)
			win.blit(ShowChosenTeam, (45, 152))
			#continue button
			if 45 + 100 > mouse[0] > 45 and 200 + 40 > mouse[1] > 200:
				S_continueButton = pygame.draw.rect(win, Soft_Blue, (45, 200, 100, 40), 0)
				if click[0] == 1:
					Pick_Positions = True
					Selection = False
					
					pygame.time.delay(200)
			else:
				S_continueButton = pygame.draw.rect(win, Blue, (45, 200, 100, 40), 0)
		else:
			S_continueButton = pygame.draw.rect(win, (100,100,100), (45, 200, 100, 40), 0)
		S_continueLabel = myfont_main.render('Continue', 1, White)
		win.blit(S_continueLabel, (50, 205))
		
		if SelectionMenu.get_Teams:
			SelectionMenu.retrieveTeamList()
		
		SelectionMenu.showTeamList()
		
		pygame.display.update()
		if event.type == pygame.QUIT:
			pygame.quit()

#this menu occurs when you click CONTINUE from the team selection screen after selecting a team. This is currently WIP.
class Select_FieldView(object):
	Fresh_Entry = False
	ThreeAbrv = ""
	showOptions = False
	note1 = "Click on an empty position box, use UP and DOWN arrows to toggle" 
	note2 = "through the player list and ENTER to select."
	warn1 = "Please ensure that there are now empty positions or duplicates." 
	warn2 = "Click on cells and use UP/DOWN/ENTER to select players."
	ClubAbrvLabel = ""
	visible = True
	tempDisable = True
	
	checkPrevTeam = False
	recallComplete = False
	
	ToggleList = []
	processingPlayers_PT1 = False
	processingPlayers_PT2 = False
	Toggle_AP = 0

	ToggleMode = "Include FAs"
	MainMenuLabel = "Home"

	EnteredPlayer_rBP = ""
	EnteredPlayer_FB = ""
	EnteredPlayer_lBP = ""
	EnteredPlayer_rHBF = ""
	EnteredPlayer_CHB = ""
	EnteredPlayer_lHBF = ""
	EnteredPlayer_rW = ""
	EnteredPlayer_C = ""
	EnteredPlayer_lW = ""
	EnteredPlayer_rHFF = ""
	EnteredPlayer_CHF = ""
	EnteredPlayer_lHFF = ""
	EnteredPlayer_rFP = ""
	EnteredPlayer_FF = ""
	EnteredPlayer_lFP = ""
	EnteredPlayer_RUCK = ""
	EnteredPlayer_RR = ""
	EnteredPlayer_R = ""
	EnteredPlayer_INT1 = ""
	EnteredPlayer_INT2 = ""

	SelectionMade = False
	emptyCell = False
	duplicateSelection = False
	Temporary_Notice = False

	def openFieldView():
		win.blit(teamSelect_bg, (0,0))
		mouse
		pygame.draw.rect(win, (0,0,0), (0, 360, 640, 40), 0)

		#backline
		pygame.draw.rect(win, White, (105, 40, 100, 50), 1)
		pygame.draw.rect(win, White, (210, 40, 100, 50), 1)
		pygame.draw.rect(win, White, (315, 40, 100, 50), 1)
		#ruck
		pygame.draw.rect(win, White, (430, 40, 100, 50), 1)
		#halfbackline
		pygame.draw.rect(win, White, (105, 100, 100, 50), 1)
		pygame.draw.rect(win, White, (210, 100, 100, 50), 1)
		pygame.draw.rect(win, White, (315, 100, 100, 50), 1)
		#ruckrover
		pygame.draw.rect(win, White, (430, 100, 100, 50), 1)
		#centreline
		pygame.draw.rect(win, White, (105, 165, 100, 50), 1)
		pygame.draw.rect(win, White, (210, 165, 100, 50), 1)
		pygame.draw.rect(win, White, (315, 165, 100, 50), 1)
		#rover
		pygame.draw.rect(win, White, (430, 165, 100, 50), 1)
		#half forward
		pygame.draw.rect(win, White, (105, 230, 100, 50), 1)
		pygame.draw.rect(win, White, (210, 230, 100, 50), 1)
		pygame.draw.rect(win, White, (315, 230, 100, 50), 1)
		#int1
		pygame.draw.rect(win, White, (430, 230, 100, 50), 1)
		#forwardline
		pygame.draw.rect(win, White, (105, 300, 100, 50), 1)
		pygame.draw.rect(win, White, (210, 300, 100, 50), 1)
		pygame.draw.rect(win, White, (315, 300, 100, 50), 1)
		#int2
		pygame.draw.rect(win, White, (430, 300, 100, 50), 1)
		
		if not Select_FieldView.Fresh_Entry:
			Select_FieldView.OpenExistingRecords()
			Select_FieldView.showOptions = True
		else:
			pygame.draw.rect(win, Bluey_Green, (40, 40, 560, 320), 20)
			pygame.draw.rect(win, Dark_Grey, (40, 40, 560, 320))
			pygame.draw.rect(win, White, (395, 115, 80, 40), 3)
			newClubName_lbText = 'Team: ' + SelectionMenu.teamChosenText
			newClubName_lb = myfont_game.render(newClubName_lbText, 1, White)
			win.blit(newClubName_lb, (60, 60))
			newAbrv_lb = myfont_game.render('3-Letter Abbreviation:', 1, White)
			win.blit(newAbrv_lb, (60, 120))
			newClubPopUp1 = myfont_game.render('Enter an abbreviation code and', 1, White)
			newClubPopUp2 = myfont_game.render('press ENTER to input.', 1, White)
			win.blit(newClubPopUp1, (60, 180))
			win.blit(newClubPopUp2, (60, 240))
			
			if event.type == pygame.KEYDOWN:
				#process typing
				if event.key == pygame.K_RETURN and len(Select_FieldView.ThreeAbrv) == 3:
					existingClub_fname = SelectionMenu.teamChosenText + '.csv'
					with open(existingClub_fname, mode = 'w', newline = '') as existingClub_file:
						existingClub_writer = csv.writer(existingClub_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						existingClub_writer.writerow([SelectionMenu.teamChosenText, Select_FieldView.ThreeAbrv.upper()])
						Select_FieldView.ClubAbrvLabel = Select_FieldView.ThreeAbrv.upper()
						Select_FieldView.Fresh_Entry = False
						Select_FieldView.tempDisable = False
						pygame.time.delay(200)
				elif event.key == pygame.K_BACKSPACE:
					Select_FieldView.ThreeAbrv = Select_FieldView.ThreeAbrv[:-1]
				else:
					if len(Select_FieldView.ThreeAbrv) < 3:
						Select_FieldView.ThreeAbrv += event.unicode
			txt_surface = myfont_game.render(Select_FieldView.ThreeAbrv.upper(), True, Bluey_Green)
			win.blit(txt_surface, (400, 120))
		
		if Select_FieldView.checkPrevTeam:
			Select_FieldView.recallPreviousTeam()
			Select_FieldView.checkPrevTeam = False
			Select_FieldView.SelectionMade = True

		if Select_FieldView.showOptions and not Select_FieldView.tempDisable:
			Show_ClubAbrvLabel = myfont_game.render(Select_FieldView.ClubAbrvLabel, True, White)
			win.blit(Show_ClubAbrvLabel, (10, 5))
			if Select_FieldView.visible:
				if Select_FieldView.emptyCell or Select_FieldView.duplicateSelection:
					UserInstructText1 = myfont_comm.render(Select_FieldView.warn1, 1, Soft_Red)
					UserInstructText2 = myfont_comm.render(Select_FieldView.warn2, 1, Soft_Red)
				else:				
					UserInstructText1 = myfont_comm.render(Select_FieldView.note1, 1, Green)
					UserInstructText2 = myfont_comm.render(Select_FieldView.note2, 1, Green)
				win.blit(UserInstructText1, (20, 365))
				win.blit(UserInstructText2, (20, 380))

			Select_FieldView.callAllFieldPositions()
		
		if Select_FieldView.processingPlayers_PT2:
				
			DisplayToggledPlayer = Select_FieldView.ToggleList[Select_FieldView.Toggle_AP]
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and Select_FieldView.Toggle_AP > 0:
					Select_FieldView.Toggle_AP -= 1
				if event.key == pygame.K_DOWN and Select_FieldView.Toggle_AP < Count_AP - 1:
					Select_FieldView.Toggle_AP += 1
				if event.key == pygame.K_RETURN:
					if CPC_posRef == "rBP":
						#make field positions shown update when player has been delisted
						Select_FieldView.EnteredPlayer_rBP = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "FB":
						Select_FieldView.EnteredPlayer_FB = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "lBP":
						Select_FieldView.EnteredPlayer_lBP = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "rHBF": 
						Select_FieldView.EnteredPlayer_rHBF = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "CHB":
						Select_FieldView.EnteredPlayer_CHB = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "lHBF":
						Select_FieldView.EnteredPlayer_lHBF = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "rW":
						Select_FieldView.EnteredPlayer_rW = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "C":
						Select_FieldView.EnteredPlayer_C = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "lW":
						Select_FieldView.EnteredPlayer_lW = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "rHFF":
						Select_FieldView.EnteredPlayer_rHFF = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "CHF":
						Select_FieldView.EnteredPlayer_CHF = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "lHFF":
						Select_FieldView.EnteredPlayer_lHFF = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "rFP":
						Select_FieldView.EnteredPlayer_rFP = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "FF":
						Select_FieldView.EnteredPlayer_FF = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "lFP":
						Select_FieldView.EnteredPlayer_lFP = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "RUCK":
						Select_FieldView.EnteredPlayer_RUCK = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "RR":
						Select_FieldView.EnteredPlayer_RR = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "R":
						Select_FieldView.EnteredPlayer_R = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "INT1":
						Select_FieldView.EnteredPlayer_INT1 = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					elif CPC_posRef == "INT2":
						Select_FieldView.EnteredPlayer_INT2 = DisplayToggledPlayer
						Select_FieldView.SelectionMade = True
					
					Select_FieldView.updatePlayerStatus(DisplayToggledPlayer)

			if not Select_FieldView.tempDisable:
				pygame.draw.rect(win, (0,0,0), (CPC_coord_x, CPC_coord_y, 100, 50), 0)
				Show_Toggle = myfont_main.render('Player Selected for ' + CPC_posRef + ": " + DisplayToggledPlayer, 1, Green)
				if not Select_FieldView.visible:
					win.blit(Show_Toggle, (20, 365))
				PositionalLabel = myfont_game.render(CPC_posRef, 1, Green)
				win.blit(PositionalLabel, (CPC_coord_x + 10, CPC_coord_y + 5))
		
		if Select_FieldView.SelectionMade:
			#back to main menu button
			global main
			global Pick_Positions
			if 110 + 80 > mouse[0] > 110 and 0 + 20 > mouse[1] > 0:
				pygame.draw.rect(win, Blue, (110, 0, 80, 20), 0)
				if click[0] == 1:
					main = True
					Pick_Positions = False

					Select_FieldView.Fresh_Entry = False
					Select_FieldView.ThreeAbrv = ""
					Select_FieldView.showOptions = False

					Select_FieldView.ClubAbrvLabel = ""
					Select_FieldView.visible = True
					Select_FieldView.tempDisable = True
					
					Select_FieldView.checkPrevTeam = False
					Select_FieldView.recallComplete = False
					
					Select_FieldView.ToggleList = []
					Select_FieldView.processingPlayers_PT1 = False
					Select_FieldView.processingPlayers_PT2 = False
					Select_FieldView.Toggle_AP = 0

					Select_FieldView.EnteredPlayer_rBP = ""
					Select_FieldView.EnteredPlayer_FB = ""
					Select_FieldView.EnteredPlayer_lBP = ""
					Select_FieldView.EnteredPlayer_rHBF = ""
					Select_FieldView.EnteredPlayer_CHB = ""
					Select_FieldView.EnteredPlayer_lHBF = ""
					Select_FieldView.EnteredPlayer_rW = ""
					Select_FieldView.EnteredPlayer_C = ""
					Select_FieldView.EnteredPlayer_lW = ""
					Select_FieldView.EnteredPlayer_rHFF = ""
					Select_FieldView.EnteredPlayer_CHF = ""
					Select_FieldView.EnteredPlayer_lHFF = ""
					Select_FieldView.EnteredPlayer_rFP = ""
					Select_FieldView.EnteredPlayer_FF = ""
					Select_FieldView.EnteredPlayer_lFP = ""
					Select_FieldView.EnteredPlayer_RUCK = ""
					Select_FieldView.EnteredPlayer_RR = ""
					Select_FieldView.EnteredPlayer_R = ""
					Select_FieldView.EnteredPlayer_INT1 = ""
					Select_FieldView.EnteredPlayer_INT2 = ""

					Select_FieldView.SelectionMade = False
					Select_FieldView.emptyCell = False
					Select_FieldView.duplicateSelection = False

					Select_FieldView.Temporary_Notice = False

					pygame.time.delay(200)
					
			else:
				pygame.draw.rect(win, Dark_Grey, (110, 0, 80, 20), 0)
			BackToMenu = myfont_mini.render(Select_FieldView.MainMenuLabel, 1, White)
			win.blit(BackToMenu, (130, 3))

			if Select_FieldView.Temporary_Notice:
				pygame.draw.rect(win, Red, (0, 360, 600, 40), 0)
				TempNoteLabel_L1 = myfont_comm.render("Note: currently WIP, to make changes open [team].csv file", 1, White)
				TempNoteLabel_L2 = myfont_comm.render("in folder and change directly then save", 1, White)
				win.blit(TempNoteLabel_L1, (10, 363))
				win.blit(TempNoteLabel_L2, (10, 380))

			if Select_FieldView.EnteredPlayer_rBP != "":
				pygame.draw.rect(win, (0,0,0), (105, 40, 100, 50), 0)
				Show_rBP = myfont_mini.render(Select_FieldView.EnteredPlayer_rBP, 1, Green)
				win.blit(Show_rBP, (107, 60))
			if Select_FieldView.EnteredPlayer_FB != "":
				pygame.draw.rect(win, (0,0,0), (210, 40, 100, 50), 0)
				Show_FB = myfont_mini.render(Select_FieldView.EnteredPlayer_FB, 1, Green)
				win.blit(Show_FB, (212, 60))
			if Select_FieldView.EnteredPlayer_lBP != "":
				pygame.draw.rect(win, (0,0,0), (315, 40, 100, 50), 0)
				Show_lBP = myfont_mini.render(Select_FieldView.EnteredPlayer_lBP, 1, Green)
				win.blit(Show_lBP, (317, 60))
			if Select_FieldView.EnteredPlayer_rHBF != "":
				pygame.draw.rect(win, (0,0,0), (105, 100, 100, 50), 0)
				Show_rHBF = myfont_mini.render(Select_FieldView.EnteredPlayer_rHBF, 1, Green)
				win.blit(Show_rHBF, (107, 120))
			if Select_FieldView.EnteredPlayer_CHB != "":
				pygame.draw.rect(win, (0,0,0), (210, 100, 100, 50), 0)
				Show_CHB = myfont_mini.render(Select_FieldView.EnteredPlayer_CHB, 1, Green)
				win.blit(Show_CHB, (212, 120))
			if Select_FieldView.EnteredPlayer_lHBF != "":
				pygame.draw.rect(win, (0,0,0), (315, 100, 100, 50), 0)
				Show_lHBF = myfont_mini.render(Select_FieldView.EnteredPlayer_lHBF, 1, Green)
				win.blit(Show_lHBF, (317, 120))
			if Select_FieldView.EnteredPlayer_rW != "":
				pygame.draw.rect(win, (0,0,0), (105, 165, 100, 50), 0)
				Show_rW = myfont_mini.render(Select_FieldView.EnteredPlayer_rW, 1, Green)
				win.blit(Show_rW, (107, 185))
			if Select_FieldView.EnteredPlayer_C != "":
				pygame.draw.rect(win, (0,0,0), (210, 165, 100, 50), 0)
				Show_C = myfont_mini.render(Select_FieldView.EnteredPlayer_C, 1, Green)
				win.blit(Show_C, (212, 185))
			if Select_FieldView.EnteredPlayer_lW != "":
				pygame.draw.rect(win, (0,0,0), (315, 165, 100, 50), 0)
				Show_lW = myfont_mini.render(Select_FieldView.EnteredPlayer_lW, 1, Green)
				win.blit(Show_lW, (317, 185))
			if Select_FieldView.EnteredPlayer_rHFF != "":
				pygame.draw.rect(win, (0,0,0), (105, 230, 100, 50), 0)
				Show_rHFF = myfont_mini.render(Select_FieldView.EnteredPlayer_rHFF, 1, Green)
				win.blit(Show_rHFF, (107, 250))
			if Select_FieldView.EnteredPlayer_CHF != "":
				pygame.draw.rect(win, (0,0,0), (210, 230, 100, 50), 0)
				Show_CHF = myfont_mini.render(Select_FieldView.EnteredPlayer_CHF, 1, Green)
				win.blit(Show_CHF, (212, 250))
			if Select_FieldView.EnteredPlayer_lHFF != "":
				pygame.draw.rect(win, (0,0,0), (315, 230, 100, 50), 0)
				Show_lHFF = myfont_mini.render(Select_FieldView.EnteredPlayer_lHFF, 1, Green)
				win.blit(Show_lHFF, (317, 250))
			if Select_FieldView.EnteredPlayer_rFP != "":
				pygame.draw.rect(win, (0,0,0), (105, 300, 100, 50), 0)
				Show_rFP = myfont_mini.render(Select_FieldView.EnteredPlayer_rFP, 1, Green)
				win.blit(Show_rFP, (107, 320))
			if Select_FieldView.EnteredPlayer_FF != "":
				pygame.draw.rect(win, (0,0,0), (210, 300, 100, 50), 0)
				Show_FF = myfont_mini.render(Select_FieldView.EnteredPlayer_FF, 1, Green)
				win.blit(Show_FF, (212, 320))
			if Select_FieldView.EnteredPlayer_lFP != "":
				pygame.draw.rect(win, (0,0,0), (315, 300, 100, 50), 0)
				Show_lFP = myfont_mini.render(Select_FieldView.EnteredPlayer_lFP, 1, Green)
				win.blit(Show_lFP, (317, 320))
			if Select_FieldView.EnteredPlayer_RUCK != "":
				pygame.draw.rect(win, (0,0,0), (430, 40, 100, 50), 0)
				Show_RUCK = myfont_mini.render(Select_FieldView.EnteredPlayer_RUCK, 1, Green)
				win.blit(Show_RUCK, (432, 60))
			if Select_FieldView.EnteredPlayer_RR != "":
				pygame.draw.rect(win, (0,0,0), (430, 100, 100, 50), 0)
				Show_RR = myfont_mini.render(Select_FieldView.EnteredPlayer_RR, 1, Green)
				win.blit(Show_RR, (432, 120))
			if Select_FieldView.EnteredPlayer_R != "":
				pygame.draw.rect(win, (0,0,0), (430, 165, 100, 50), 0)
				Show_R = myfont_mini.render(Select_FieldView.EnteredPlayer_R, 1, Green)
				win.blit(Show_R, (432, 185))
			if Select_FieldView.EnteredPlayer_INT1 != "":
				pygame.draw.rect(win, (0,0,0), (430, 230, 100, 50), 0)
				Show_INT1 = myfont_mini.render(Select_FieldView.EnteredPlayer_INT1, 1, Green)
				win.blit(Show_INT1, (432, 250))
			if Select_FieldView.EnteredPlayer_INT2 != "":
				pygame.draw.rect(win, (0,0,0), (430, 300, 100, 50), 0)
				Show_INT2 = myfont_mini.render(Select_FieldView.EnteredPlayer_INT2, 1, Green)
				win.blit(Show_INT2, (432, 320))

		if Select_FieldView.ToggleMode == 'Include FAs':
			pygame.draw.rect(win, Red, (310, 0, 110, 30), 0)
			upperButtonText2 = myfont_comm.render('Include FAs', 1, White)
			win.blit(upperButtonText2, (315, 5))
			upperButtonText2 = myfont_comm.render('Include FAs', 1, White)
			win.blit(upperButtonText2, (315, 5))


		if 540 + 100 > mouse[0] > 540 and 0 + 40 > mouse[1] > 0:
			pygame.draw.rect(win, Light_Green, (540, 0, 100, 40), 0)
			if click[0] == 1:
				Select_FieldView.visible = True
				
				confirm_team = [Select_FieldView.EnteredPlayer_rBP, Select_FieldView.EnteredPlayer_FB, Select_FieldView.EnteredPlayer_lBP, Select_FieldView.EnteredPlayer_rHBF, \
				Select_FieldView.EnteredPlayer_CHB, Select_FieldView.EnteredPlayer_lHBF, Select_FieldView.EnteredPlayer_rW, Select_FieldView.EnteredPlayer_C, Select_FieldView.EnteredPlayer_lW, \
				Select_FieldView.EnteredPlayer_rHFF, Select_FieldView.EnteredPlayer_CHF, Select_FieldView.EnteredPlayer_lHFF, Select_FieldView.EnteredPlayer_rFP, Select_FieldView.EnteredPlayer_FF, \
				Select_FieldView.EnteredPlayer_lFP, Select_FieldView.EnteredPlayer_RUCK, Select_FieldView.EnteredPlayer_RR, Select_FieldView.EnteredPlayer_R, Select_FieldView.EnteredPlayer_INT1, \
				Select_FieldView.EnteredPlayer_INT2]
				if "" in confirm_team:
					Select_FieldView.emptyCell = True
				else:
					TeamCheck = set(confirm_team)
				if not Select_FieldView.emptyCell:
					if len(TeamCheck) == 20:
						processTeam_fname = SelectionMenu.teamChosenText + '.csv'
						with open(processTeam_fname, 'w', newline = '\n') as processTeam_write:
							PT_output = csv.writer(processTeam_write)
							PT_output.writerows([
								[SelectionMenu.teamChosenText, Select_FieldView.ThreeAbrv.upper()], \
								['rBP', Select_FieldView.EnteredPlayer_rBP], \
								['FB', Select_FieldView.EnteredPlayer_FB], \
								['lBP', Select_FieldView.EnteredPlayer_lBP], \
								['rHBF', Select_FieldView.EnteredPlayer_rHBF], \
								['CHB', Select_FieldView.EnteredPlayer_CHB], \
								['lHBF', Select_FieldView.EnteredPlayer_lHBF], \
								['rW', Select_FieldView.EnteredPlayer_rW], \
								['C', Select_FieldView.EnteredPlayer_C], \
								['lW', Select_FieldView.EnteredPlayer_lW], \
								['rHFF', Select_FieldView.EnteredPlayer_rHFF], \
								['CHF', Select_FieldView.EnteredPlayer_CHF], \
								['lHFF', Select_FieldView.EnteredPlayer_lHFF], \
								['rFP', Select_FieldView.EnteredPlayer_rFP], \
								['FF', Select_FieldView.EnteredPlayer_FF], \
								['lFP', Select_FieldView.EnteredPlayer_lFP], \
								['RUCK', Select_FieldView.EnteredPlayer_RUCK], \
								['RR', Select_FieldView.EnteredPlayer_RR], \
								['R', Select_FieldView.EnteredPlayer_R], \
								['INT1', Select_FieldView.EnteredPlayer_INT1], \
								['INT2', Select_FieldView.EnteredPlayer_INT2]
							])
					else:
						Select_FieldView.duplicateSelection = True
				
				
		else:
			pygame.draw.rect(win, Bluey_Green, (540, 0, 100, 40), 0)
		submitTeamLb = myfont_main.render("Submit", 1, (0,0,0))
		win.blit(submitTeamLb, (550, 5))
		
		pygame.display.update()
		if event.type == pygame.QUIT:
			pygame.quit()

	def createPlayerChoiceBox(x, y, pos_ref):
		if x + 100 > mouse[0] > x and y + 50 > mouse[1] > y and click[0] == 1:
			global CPC_coord_x
			global CPC_coord_y
			global CPC_posRef
			CPC_coord_x = x
			CPC_coord_y = y
			CPC_posRef = pos_ref
			
			Select_FieldView.visible = False
			
			Select_FieldView.processingPlayers_PT1 = True
			pygame.time.delay(250)
			playerML_fname = 'MasterList.csv'
			player_df = pd.read_csv(playerML_fname, names=['PLAYER_NAME','STATUS'])
			if Select_FieldView.ToggleMode == 'Include FAs':
				Available_Player = player_df.loc[()]
			elif Select_FieldView.ToggleMode == 'Team Only' or Select_FieldView.ToggleMode == 'Delist':
				Available_Player = player_df.loc[(player_df['STATUS'] == Select_FieldView.ClubAbrvLabel)]
			global Count_AP
			if Select_FieldView.processingPlayers_PT1:
				Count_AP = 0
				for row in Available_Player.itertuples(name='player'):
					PLAYER_NAME_NONSTRING = row.PLAYER_NAME
					ToggleListAdd = str(PLAYER_NAME_NONSTRING)
					Select_FieldView.ToggleList.append(ToggleListAdd)
					Count_AP += 1
				#print(Count_AP)
				Select_FieldView.processingPlayers_PT1 = False
				Select_FieldView.processingPlayers_PT2 = True
				Select_FieldView.showOptions = False
			
	def callAllFieldPositions():
		Select_FieldView.createPlayerChoiceBox(105, 40, 'rBP')
		Select_FieldView.createPlayerChoiceBox(210, 40, 'FB')
		Select_FieldView.createPlayerChoiceBox(315, 40, 'lBP')
		Select_FieldView.createPlayerChoiceBox(105, 100, 'rHBF')
		Select_FieldView.createPlayerChoiceBox(210, 100, 'CHB')
		Select_FieldView.createPlayerChoiceBox(315, 100, 'lHBF')
		Select_FieldView.createPlayerChoiceBox(105, 165, 'rW')
		Select_FieldView.createPlayerChoiceBox(210, 165, 'C')
		Select_FieldView.createPlayerChoiceBox(315, 165, 'lW')
		Select_FieldView.createPlayerChoiceBox(105, 230, 'rHFF')
		Select_FieldView.createPlayerChoiceBox(210, 230, 'CHF')
		Select_FieldView.createPlayerChoiceBox(315, 230, 'lHFF')
		Select_FieldView.createPlayerChoiceBox(105, 300, 'rFP')
		Select_FieldView.createPlayerChoiceBox(210, 300, 'FF')
		Select_FieldView.createPlayerChoiceBox(315, 300, 'lFP')
		
		Select_FieldView.createPlayerChoiceBox(430, 40, 'RUCK')
		Select_FieldView.createPlayerChoiceBox(430, 100, 'RR')
		Select_FieldView.createPlayerChoiceBox(430, 165, 'R')
		Select_FieldView.createPlayerChoiceBox(430, 230, 'INT1')
		Select_FieldView.createPlayerChoiceBox(430, 300, 'INT2')

	def OpenExistingRecords():
		try:
			existingClub_fname = SelectionMenu.teamChosenText + '.csv'
			existingClub_file = open(existingClub_fname, mode = 'r')
			existingClub_file
			existingClub_file.close()
			Select_FieldView.tempDisable = False
			if not Select_FieldView.recallComplete:
				Select_FieldView.checkPrevTeam = True
		except:
			Select_FieldView.Fresh_Entry = True
			
			pygame.display.update()
			if event.type == pygame.QUIT:
				pygame.quit()

	def recallPreviousTeam():
		prevTeam_fname = SelectionMenu.teamChosenText + '.csv'
		with open(prevTeam_fname, 'r') as openPrevTeam:
			prevTeamReader = csv.reader(openPrevTeam, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			print(SelectionMenu.teamChosenText)
			for row in prevTeamReader:
				print(row[1])
				if row[0] == SelectionMenu.teamChosenText:
					Select_FieldView.ClubAbrvLabel = row[1]
				if row[0] == 'rBP':
					Select_FieldView.EnteredPlayer_rBP = row[1]
				elif row[0] == 'FB':
					Select_FieldView.EnteredPlayer_FB = row[1]
				elif row[0] == 'lBP':
					Select_FieldView.EnteredPlayer_lBP = row[1]
				elif row[0] == 'rHBF':
					Select_FieldView.EnteredPlayer_rHBF = row[1]
				elif row[0] == 'CHB':
					Select_FieldView.EnteredPlayer_CHB = row[1]
				elif row[0] == 'lHBF':
					Select_FieldView.EnteredPlayer_lHBF = row[1]
				elif row[0] == 'rW':
					Select_FieldView.EnteredPlayer_rW = row[1]
				elif row[0] == 'C':
					Select_FieldView.EnteredPlayer_C = row[1]
				elif row[0] == 'lW':
					Select_FieldView.EnteredPlayer_lW = row[1]
				elif row[0] == 'rHFF':
					Select_FieldView.EnteredPlayer_rHFF = row[1]
				elif row[0] == 'CHF':
					Select_FieldView.EnteredPlayer_CHF = row[1]
				elif row[0] == 'lHFF':
					Select_FieldView.EnteredPlayer_lHFF = row[1]
				elif row[0] == 'rFP':
					Select_FieldView.EnteredPlayer_rFP = row[1]
				elif row[0] == 'FF':
					Select_FieldView.EnteredPlayer_FF = row[1]
				elif row[0] == 'lFP':
					Select_FieldView.EnteredPlayer_lFP = row[1]
				elif row[0] == 'RUCK':
					Select_FieldView.EnteredPlayer_RUCK = row[1]
				elif row[0] == 'RR':
					Select_FieldView.EnteredPlayer_RR = row[1]
				elif row[0] == 'R':
					Select_FieldView.EnteredPlayer_R = row[1]
				elif row[0] == 'INT1':
					Select_FieldView.EnteredPlayer_INT1 = row[1]
				elif row[0] == 'INT2':
					Select_FieldView.EnteredPlayer_INT2 = row[1]
				
				Select_FieldView.recallComplete = True
				Select_FieldView.Temporary_Notice = True
	
	def updatePlayerStatus(player):
		playerML_fname = 'MasterList.csv'
		player_df = pd.read_csv(playerML_fname, names=['PLAYER_NAME','STATUS'])
		Chosen_Player = player_df.loc[(player_df['PLAYER_NAME'] == player)]
		for row in Chosen_Player.itertuples(name='player'):
			if Select_FieldView.ToggleMode == 'Delist':
				player_df.at[row.Index, 'STATUS'] = 'Free Agent'
			else:
				player_df.at[row.Index, 'STATUS'] = Select_FieldView.ClubAbrvLabel
			player_df.to_csv(playerML_fname, index=False, header=False)

############### player identification starts here

class CreatePlayer(object):
	masterList = []
	
	def __init__(self, name):
		self.name = name
		CreatePlayer.masterList.append(self.name)

############### player identification ends here

#this code collates the total team statistics for the home and away teams by the end of the 4th quarter.
class teamStatistics(object):
	homeHO = 0
	homeK = 0
	homeHB = 0
	homeM = 0
	homeT = 0
	homeFF = 0
	homeFA = 0
	
	homeD = 0
	
	awayHO = 0
	awayK = 0
	awayHB = 0
	awayM = 0
	awayT = 0
	awayFF = 0
	awayFA = 0
	
	awayD = 0
	
	def updateTeamStats(teamWithBall, action):
		if teamWithBall == "Home":
			if action == "Roving":
				teamStatistics.homeHO += 1
			elif action == "Kick" or action == "EffectiveKick":
				teamStatistics.homeK += 1
			elif action == "Handball" or action == "EffectiveHandball":
				teamStatistics.homeHB += 1
			elif action == "Mark":
				teamStatistics.homeM += 1
			elif action == "Tackle":
				teamStatistics.homeT += 1
			elif action == "Free Kick":
				teamStatistics.homeFF += 1
				teamStatistics.awayFA += 1
			#elif action == teamStatistics.homeG:
			#	teamStatistics.homeG += 1
			#elif action == teamStatistics.homeB:
			#	teamStatistics.homeB += 1
			print(teamWithBall, action)
		
		elif teamWithBall == "Away":
			if action == "Roving":
				teamStatistics.awayHO += 1
			elif action == "Kick" or action == "EffectiveKick":
				teamStatistics.awayK += 1
			elif action == "Handball" or action == "EffectiveHandball":
				teamStatistics.awayHB += 1
			elif action == "Mark":
				teamStatistics.awayM += 1
			elif action == "Tackle":
				teamStatistics.awayT += 1
			elif action == "Free Kick":
				teamStatistics.awayFF += 1
				teamStatistics.homeFA += 1
			#elif action == teamStatistics.awayG:
			#	teamStatistics.awayG += 1
			#elif action == teamStatistics.awayB:
			#	teamStatistics.awayB += 1
			print(teamWithBall, action)
	
	def GetTotalDisposals():
		teamStatistics.homeD = teamStatistics.homeK + teamStatistics.homeHB
		teamStatistics.awayD = teamStatistics.awayK + teamStatistics.awayHB
		
	def arrangeTeamStats():
		global Home_Hitouts
		Home_Hitouts = "Home HO: " + str(teamStatistics.homeHO)
		global Home_Kicks
		Home_Kicks = "Home K: " + str(teamStatistics.homeK)
		global Home_Handball
		Home_Handball = "Home HB: " + str(teamStatistics.homeHB)
		global Home_Marks
		Home_Marks = "Home M: " + str(teamStatistics.homeM)
		global Home_Tackles
		Home_Tackles = "Home T: " + str(teamStatistics.homeT)
		global Home_FreesFor
		Home_FreesFor = "Home FF: " + str(teamStatistics.homeFF)
		global Home_FreesAgainst
		Home_FreesAgainst = "Home FA: " + str(teamStatistics.homeFA)
		
		global Away_Hitouts
		Away_Hitouts = "Away HO: " + str(teamStatistics.awayHO)
		global Away_Kicks
		Away_Kicks = "Away K: " + str(teamStatistics.awayK)
		global Away_Handball
		Away_Handball = "Away HB: " + str(teamStatistics.awayHB)
		global Away_Marks
		Away_Marks = "Away M: " + str(teamStatistics.awayM)
		global Away_Tackles
		Away_Tackles = "Away T: " + str(teamStatistics.awayT)
		global Away_FreesFor
		Away_FreesFor = "Away FF: " + str(teamStatistics.awayFF)
		global Away_FreesAgainst
		Away_FreesAgainst = "Away FA: " + str(teamStatistics.awayFA)
		
	def write_team_stats():
		statsoutput = open("statsoutput.txt", "w")
			
		statsoutput.write(Home_Hitouts + "\n" + Home_Kicks + "\n"
						+ Home_Handball + "\n" + Home_Marks + "\n"
						+ Home_Tackles + "\n" + Home_FreesFor + "\n"
						+ Home_FreesAgainst + "\n" + Away_Hitouts + "\n"
						+ Away_Kicks + "\n" + Away_Handball + "\n"
						+ Away_Marks + "\n" + Away_Tackles + "\n"
						+ Away_FreesFor + "\n" + Away_FreesAgainst)

#the main function that creates a simulation of the game. Still missing individual identifiable players, a prompt back to main menu and stats summary post-game.
class sim_game(object):
	game_minutes = 0
	game_seconds = 0
	QTR = 1
	stoppage_time = 5
	speed = 4
	homeTeam = "Home Sample"
	homeTeamShort = "HOM"
	home_goals = 0
	home_behinds = 0
	home_score = 0
	awayTeam = "Away Sample"
	awayTeamShort = "AWY"
	away_goals = 0
	away_behinds = 0
	away_score = 0
	play_posLine = 0
	play_posCol = 0
	congestionLimiter = 0
	
	possession = "None"
	transType = "Contest"
	ActionType = "Ball Up"

	left_throwIn = False
	right_throwIn = False
	play_restart = True

	def GamePlayTime():
		QTR_endTime = 20 + sim_game.stoppage_time
		if sim_game.QTR <= 4 and sim_game.game_minutes <= QTR_endTime:
			global match_status
			match_status = "In Progress"
			sim_game.game_seconds += sim_game.speed
			pygame.time.delay(100)
		else:
			match_status = "Finished"
			
			global playing_match
			global main
			teamStatistics.arrangeTeamStats()
			teamStatistics.write_team_stats()
			playing_match = False
			main = True
		if sim_game.game_seconds >= 60:
			sim_game.game_minutes += 1
			sim_game.game_seconds -= 60
			sim_game.stoppage_time = random.randint(5,15)
		if sim_game.game_minutes >= QTR_endTime:
			sim_game.game_minutes = 0
			sim_game.game_seconds = 0
			sim_game.play_posLine = 0
			sim_game.play_posCol = 0
			sim_game.QTR += 1
			sim_game.transType = "Contest"
			sim_game.play_restart = True
			
	
	def PlayBook(play_type, movement, Max_lateralDist, sideways):
		if sim_game.possession == "Home":
			sim_game.play_posLine += movement
			Dir_lateral = random.randint(-1,1)
			if sideways == "sideways":
				sim_game.play_posCol += Dir_lateral * Max_lateralDist
			else:
				sim_game.play_posCol += Dir_lateral * random.randint(0, Max_lateralDist)
		elif sim_game.possession == "Away":
			sim_game.play_posLine -= movement
			Dir_lateral = random.randint(-1,1)
			if sideways == "sideways":
				sim_game.play_posCol += Dir_lateral * Max_lateralDist
			else:
				sim_game.play_posCol += Dir_lateral * random.randint(0, Max_lateralDist)
		global Access_playType
		Access_playType = play_type
	
	def Generate_Play_contest():
		sim_game.speed = 4
		if sim_game.play_restart:
			sim_game.possession = "None"
			sim_game.ActionType = "Ball Up"
		
		if sim_game.possession == "None":
			if sim_game.ActionType == "Ball Up" or sim_game.ActionType == "Goal":
				possessionRoll = random.randint(0,1)
				if possessionRoll == 0:
					sim_game.possession = "Home"
					
				elif possessionRoll == 1:
					sim_game.possession = "Away"
					
				sim_game.ActionType = "Roving"
				sim_game.transType = "Contest"
			else:
				possessionRoll = random.randint(0,1)
				if possessionRoll == 0:
					sim_game.possession = "Home"
				elif possessionRoll == 1:
					sim_game.possession = "Away"
				sim_game.ActionType = "BallGet"
				sim_game.transType = "Defending"

		else:
			freekickRoll = random.randint(1,10)
			if freekickRoll > 9:
				sim_game.ActionType = "Free Kick"
				sim_game.transType = "Carrying"

			else:
				if sim_game.ActionType == "Roving":
					possessionRoll = random.randint(1,3)
					if sim_game.possession == "Home" and possessionRoll == 1:
						sim_game.possession = "Away"
					elif sim_game.possession == "Away" and possessionRoll == 1:
						sim_game.possession = "Home"
					sim_game.ActionType = "BallGet"
					sim_game.transType = "Defending"
				elif sim_game.ActionType == "Kick":
					possessionRoll = random.randint(0,1)
					if possessionRoll == 0:
						sim_game.possession = "Home"
					elif possessionRoll == 1:
						sim_game.possession = "Away"
					aerialRoll = random.randint(1,10)
					if aerialRoll >= 7:
						
						sim_game.ActionType = "Mark"
						sim_game.transType = "Carrying"
					else:
						sim_game.ActionType = "BallGet"
						sim_game.transType = "Defending"
				else:
					possessionRoll = random.randint(0,1)
					if possessionRoll == 0:
						sim_game.possession = "Home"
					elif possessionRoll == 1:
						sim_game.possession = "Away"
					sim_game.ActionType = "BallGet"
					sim_game.transType = "Defending"
	
	def Generate_Play_defender():
		sim_game.speed = 3
		if sim_game.possession == "Home":
			if sim_game.ActionType == "EffectiveKick":
				sim_game.ActionType = "Mark"
				sim_game.transType = "Carrying"
			elif sim_game.ActionType == "EffectiveHandball":
				sim_game.ActionType = "Finds Space"
				sim_game.transType = "Carrying"
			else:
				if sim_game.congestionLimiter < 2:
					turnoverRoll = random.randint(1,10)
					if turnoverRoll <= 2:
						sim_game.possession = "None"
						sim_game.ActionType = "Spills Free"
						sim_game.transType = "Contest"
						
						sim_game.congestionLimiter += 1
					elif 2 < turnoverRoll <= 7:
						sim_game.possession = "Away"
						loseballRoll = random.randint(1,10)
						if loseballRoll <= 4:
							sim_game.ActionType = "Tackle"
							sim_game.transType = "Defending"
							
							sim_game.congestionLimiter += 1
						elif 4 < loseballRoll <= 9:
							sim_game.ActionType = "Dispossession"
							sim_game.transType = "Defending"
							
							sim_game.congestionLimiter += 1
						else:
							sim_game.ActionType = "Free Kick"
							sim_game.transType = "Carrying"
							
							sim_game.congestionLimiter = 0
					else:
						sim_game.possession = "Home"
						sim_game.ActionType = "Finds Space"
						sim_game.transType = "Carrying"
						
						sim_game.congestionLimiter = 0
						
				else:
					sim_game.possession = "Home"
					sim_game.ActionType = "Finds Space"
					sim_game.transType = "Carrying"
					
					sim_game.congestionLimiter = 0
		
		elif sim_game.possession == "Away":
			if sim_game.ActionType == "EffectiveKick":
				sim_game.ActionType = "Mark"
				sim_game.transType = "Carrying"
			elif sim_game.ActionType == "EffectiveHandball":
				sim_game.ActionType = "Finds Space"
				sim_game.transType = "Carrying"
			else:
				if sim_game.congestionLimiter < 2:
					turnoverRoll = random.randint(1,10)
					if turnoverRoll <= 2:
						sim_game.possession = "None"
						sim_game.ActionType = "Spills Free"
						sim_game.transType = "Contest"
						
						sim_game.congestionLimiter += 1
					elif 2 < turnoverRoll <= 7:
						sim_game.possession = "Home"
						loseballRoll = random.randint(1,10)
						if loseballRoll <= 4:
							sim_game.ActionType = "Tackle"
							sim_game.transType = "Defending"
							
							sim_game.congestionLimiter += 1
						elif 4 < loseballRoll <= 9:
							sim_game.ActionType = "Dispossession"
							sim_game.transType = "Defending"
							
							sim_game.congestionLimiter += 1
						else:
							sim_game.ActionType = "Free Kick"
							sim_game.transType = "Carrying"
							
							sim_game.congestionLimiter = 0
					else:
						sim_game.possession = "Away"
						sim_game.ActionType = "Finds Space"
						sim_game.transType = "Carrying"
						
						sim_game.congestionLimiter = 0
				else:
					sim_game.possession = "Away"
					sim_game.ActionType = "Finds Space"
					sim_game.transType = "Carrying"
					
					sim_game.congestionLimiter = 0
		else:
			sim_game.transType = "Contest"

	def Generate_Play_ballCarrier():
		sim_game.speed = 7
		
		if sim_game.ActionType == "Out on the Full" or sim_game.ActionType == "Behind":
			if sim_game.play_posLine == 2:
				sim_game.possession = "Away"
			elif sim_game.play_posLine == -2:
				sim_game.possession = "Home"

		isSideways = random.randint(0,1)
		movementRoll = random.randint(1,100)
		
		if sim_game.play_posLine == 2 and sim_game.possession == "Home":
			if movementRoll > 70:
				sim_game.PlayBook("Short Kick", 1, 0, "forwards")
				sim_game.ActionType = "Kick"
				
			elif 40 < movementRoll <= 70:
				sim_game.PlayBook("Short Kick", 0, 1, "sideways")
				sim_game.ActionType = "Kick"
				
			elif 20 < movementRoll <= 40:
				sim_game.PlayBook("Handball", 0, 1, "sideways")
				sim_game.ActionType = "Handball"
				
			elif 10 < movementRoll <= 20:
				sim_game.PlayBook("Long Kick", 2, 2, "forwards")
				sim_game.ActionType = "Kick"
				
			else:
				sim_game.PlayBook("TORP", 3, 2, "forwards")
				sim_game.ActionType = "Kick"
				
		elif sim_game.play_posLine == -2 and sim_game.possession == "Away":
			if movementRoll > 70:
				sim_game.PlayBook("Short Kick", 1, 0, "forwards")
				sim_game.ActionType = "Kick"
				
			elif 40 < movementRoll <= 70:
				sim_game.PlayBook("Short Kick", 0, 1, "sideways")
				sim_game.ActionType = "Kick"
				
			elif 20 < movementRoll <= 40:
				sim_game.PlayBook("Handball", 0, 1, "sideways")
				sim_game.ActionType = "Handball"
				
			elif 10 < movementRoll <= 20:
				sim_game.PlayBook("Long Kick", 2, 2, "forwards")
				sim_game.ActionType = "Kick"
				
			else:
				sim_game.PlayBook("TORP", 3, 2, "forwards")
				sim_game.ActionType = "Kick"

		
		else:
			if movementRoll > 80:
				if isSideways == 0:
					sim_game.PlayBook("Short Kick", 1, 0, "forwards")
					sim_game.ActionType = "Kick"
				elif isSideways == 1:
					sim_game.PlayBook("Short Kick", 0, 1, "sideways")
					sim_game.ActionType = "Kick"
				
			elif 40 < movementRoll <= 80:
				if isSideways == 0:
					sim_game.PlayBook("Handball", 1, 0, "forwards")
					sim_game.ActionType = "Handball"
				elif isSideways == 1:
					sim_game.PlayBook("Handball", 0, 1, "sideways")
					sim_game.ActionType = "Handball"

			elif 20 < movementRoll <= 40:
				sim_game.PlayBook("Run And Bounce", 1, 0, "forwards")
				sim_game.ActionType = "Run"
			elif 5 < movementRoll <= 20:
				sim_game.PlayBook("Long Kick", 2, 2, "forwards")
				sim_game.ActionType = "Kick"

			else:
				sim_game.PlayBook("TORP", 3, 2, "forwards")
				sim_game.ActionType = "Kick"

		
		effectivenessRoll = random.randint(1,2)
		if effectivenessRoll == 1:
			sim_game.transType = "Contest"
		elif effectivenessRoll == 2:
			sim_game.transType = "Defending"
			if sim_game.ActionType == "Kick":
				sim_game.ActionType = "EffectiveKick"
			elif sim_game.ActionType == "Handball":
				sim_game.ActionType = "EffectiveHandball"
	
	def GamePlayBallPos():	
		sim_game.play_restart = None
		
		if sim_game.play_posCol < -1:
			sim_game.left_throwIn = True
			sim_game.play_posCol = -1
			#print("Left Boundary Throw In")
			sim_game.possession = "None"
			sim_game.ActionType = "Ball Up"
			sim_game.transType = "Contest"
		elif sim_game.play_posCol > 1:
			sim_game.right_throwIn = True
			sim_game.play_posCol = 1
			#print("Right Boundary Throw In")
			sim_game.possession = "None"
			sim_game.ActionType = "Ball Up"
			sim_game.transType = "Contest"
		else:
			sim_game.left_throwIn = False
			sim_game.right_throwIn = False
		
		if sim_game.play_posLine >= 3:
			if sim_game.left_throwIn:
				sim_game.play_posLine = 2
				sim_game.play_posCol = -1
				sim_game.ActionType = "Out on the Full"
				sim_game.transType = "Carrying"

			elif sim_game.right_throwIn:
				sim_game.play_posLine = 2
				sim_game.play_posCol = 1
				sim_game.ActionType = "Out on the Full"
				sim_game.transType = "Carrying"

			else:
				shotRollHome = random.randint(0,1)
				if shotRollHome == 0:
					sim_game.home_behinds += 1
					sim_game.play_posLine = 2
					sim_game.play_posCol = 0
					sim_game.ActionType = "Behind"
					sim_game.transType = "Carrying"

				elif shotRollHome == 1:
					sim_game.home_goals += 1
					sim_game.ActionType = "Goal"
					sim_game.play_restart = True

		if sim_game.play_posLine <= -3:
			if sim_game.left_throwIn:
				sim_game.play_posLine = -2
				sim_game.play_posCol = -1
				sim_game.ActionType = "Out on the Full"
				sim_game.transType = "Carrying"

			elif sim_game.right_throwIn:
				sim_game.play_posLine = -2
				sim_game.play_posCol = 1
				sim_game.ActionType = "Out on the Full"
				sim_game.transType = "Carrying"

			else:
				shotRollAway = random.randint(0,1)
				if shotRollAway == 0:
					sim_game.away_behinds += 1
					sim_game.play_posLine = -2
					sim_game.play_posCol = 0
					sim_game.ActionType = "Behind"
					sim_game.transType = "Carrying"

				elif shotRollAway == 1:
					sim_game.away_goals += 1
					sim_game.ActionType = "Goal"
					sim_game.play_restart = True
		
		if sim_game.play_restart:
			sim_game.play_posLine = 0
			sim_game.play_posCol = 0
			sim_game.transType = "Contest"

		sim_game.home_score = sim_game.home_goals * 6 + sim_game.home_behinds
		sim_game.away_score = sim_game.away_goals * 6 + sim_game.away_behinds
	
	def map_play():
		global Pos_Coordinates
		Pos_Coordinates = (sim_game.play_posCol, sim_game.play_posLine)
		#print(Pos_Coordinates)

		if Pos_Coordinates == (-1,2) and sim_game.possession == "Away":
			away_rBP_display = pygame.draw.rect(win, Soft_Red, (400, 55, 40, 15), 0)
		else:
			away_rBP_display = pygame.draw.rect(win, Red, (400, 55, 40, 15), 0)
		if Pos_Coordinates == (0, 2) and sim_game.possession == "Away":
			away_FB_display = pygame.draw.rect(win, Soft_Red, (470, 55, 40, 15), 0)
		else:
			away_FB_display = pygame.draw.rect(win, Red, (470, 55, 40, 15), 0)
		if Pos_Coordinates == (1, 2) and sim_game.possession == "Away":
			away_lBP_display = pygame.draw.rect(win, Soft_Red, (540, 55, 40, 15), 0)
		else:
			away_lBP_display = pygame.draw.rect(win, Red, (540, 55, 40, 15), 0)
		if Pos_Coordinates == (-1, 2) and sim_game.possession == "Home":
			home_lFP_display = pygame.draw.rect(win, Soft_Blue, (400, 70, 40, 15), 0)
		else:
			home_lFP_display = pygame.draw.rect(win, Blue, (400, 70, 40, 15), 0)
		if Pos_Coordinates == (0, 2) and sim_game.possession == "Home":
			home_FF_display = pygame.draw.rect(win, Soft_Blue, (470, 70, 40, 15), 0)
		else:
			home_FF_display = pygame.draw.rect(win, Blue, (470, 70, 40, 15), 0)
		if Pos_Coordinates == (1, 2) and sim_game.possession == "Home":
			home_rFP_display = pygame.draw.rect(win, Soft_Blue, (540, 70, 40, 15), 0)
		else:
			home_rFP_display = pygame.draw.rect(win, Blue, (540, 70, 40, 15), 0)

		if Pos_Coordinates == (-1, 1) and sim_game.possession == "Away":
			away_rHBF_display = pygame.draw.rect(win, Soft_Red, (400, 100, 40, 15), 0)
		else:
			away_rHBF_display = pygame.draw.rect(win, Red, (400, 100, 40, 15), 0)
		if Pos_Coordinates == (0, 1) and sim_game.possession == "Away":
			away_CHB_display = pygame.draw.rect(win, Soft_Red, (470, 100, 40, 15), 0)
		else:
			away_CHB_display = pygame.draw.rect(win, Red, (470, 100, 40, 15), 0)
		if Pos_Coordinates == (1, 1) and sim_game.possession == "Away":
			away_lHBF_display = pygame.draw.rect(win, Soft_Red, (540, 100, 40, 15), 0)
		else:
			away_lHBF_display = pygame.draw.rect(win, Red, (540, 100, 40, 15), 0)
		if Pos_Coordinates == (-1, 1) and sim_game.possession == "Home":
			home_lHFF_display = pygame.draw.rect(win, Soft_Blue, (400, 115, 40, 15), 0)
		else:
			home_lHFF_display = pygame.draw.rect(win, Blue, (400, 115, 40, 15), 0)
		if Pos_Coordinates == (0, 1) and sim_game.possession == "Home":
			home_CHF_display = pygame.draw.rect(win, Soft_Blue, (470, 115, 40, 15), 0)
		else:
			home_CHF_display = pygame.draw.rect(win, Blue, (470, 115, 40, 15), 0)
		if Pos_Coordinates == (1, 1) and sim_game.possession == "Home":
			home_rHFF_display = pygame.draw.rect(win, Soft_Blue, (540, 115, 40, 15), 0)
		else:
			home_rHFF_display = pygame.draw.rect(win, Blue, (540, 115, 40, 15), 0)

		if Pos_Coordinates == (-1, 0) and sim_game.possession == "Away":
			away_rW_display = pygame.draw.rect(win, Soft_Red, (400, 170, 40, 15), 0)
		else:
			away_rW_display = pygame.draw.rect(win, Red, (400, 170, 40, 15), 0)
		if Pos_Coordinates == (0, 0) and sim_game.possession == "Away":
			away_C_display = pygame.draw.rect(win, Soft_Red, (470, 170, 40, 15), 0)
		else:
			away_C_display = pygame.draw.rect(win, Red, (470, 170, 40, 15), 0)
		if Pos_Coordinates == (1, 0) and sim_game.possession == "Away":
			away_lW_display = pygame.draw.rect(win, Soft_Red, (540, 170, 40, 15), 0)
		else:
			away_lW_display = pygame.draw.rect(win, Red, (540, 170, 40, 15), 0)
		if Pos_Coordinates == (-1, 0) and sim_game.possession == "Home":
			home_lW_display = pygame.draw.rect(win, Soft_Blue, (400, 185, 40, 15), 0)
		else:
			home_lW_display = pygame.draw.rect(win, Blue, (400, 185, 40, 15), 0)
		if Pos_Coordinates == (0, 0) and sim_game.possession == "Home":
			home_C_display = pygame.draw.rect(win, Soft_Blue, (470, 185, 40, 15), 0)
		else:
			home_C_display = pygame.draw.rect(win, Blue, (470, 185, 40, 15), 0)
		if Pos_Coordinates == (1, 0) and sim_game.possession == "Home":
			home_rW_display = pygame.draw.rect(win, Soft_Blue, (540, 185, 40, 15), 0)
		else:
			home_rW_display = pygame.draw.rect(win, Blue, (540, 185, 40, 15), 0)

		if Pos_Coordinates == (-1, -1) and sim_game.possession == "Away":
			away_rHFF_display = pygame.draw.rect(win, Soft_Red, (400, 240, 40, 15), 0)
		else:
			away_rHFF_display = pygame.draw.rect(win, Red, (400, 240, 40, 15), 0)
		if Pos_Coordinates == (0, -1) and sim_game.possession == "Away":
			away_CHF_display = pygame.draw.rect(win, Soft_Red, (470, 240, 40, 15), 0)
		else:
			away_CHF_display = pygame.draw.rect(win, Red, (470, 240, 40, 15), 0)
		if Pos_Coordinates == (1, -1) and sim_game.possession == "Away":
			away_lHFF_display = pygame.draw.rect(win, Soft_Red, (540, 240, 40, 15), 0)
		else:
			away_lHFF_display = pygame.draw.rect(win, Red, (540, 240, 40, 15), 0)
		if Pos_Coordinates == (-1, -1) and sim_game.possession == "Home":
			home_lHBF_display = pygame.draw.rect(win, Soft_Blue, (400, 255, 40, 15), 0)
		else:
			home_lHBF_display = pygame.draw.rect(win, Blue, (400, 255, 40, 15), 0)
		if Pos_Coordinates == (0, -1) and sim_game.possession == "Home":
			home_CHB_display = pygame.draw.rect(win, Soft_Blue, (470, 255, 40, 15), 0)
		else:
			home_CHB_display = pygame.draw.rect(win, Blue, (470, 255, 40, 15), 0)
		if Pos_Coordinates == (1, -1) and sim_game.possession == "Home":
			home_rHBF_display = pygame.draw.rect(win, Soft_Blue, (540, 255, 40, 15), 0)
		else:
			home_rHBF_display = pygame.draw.rect(win, Blue, (540, 255, 40, 15), 0)

		if Pos_Coordinates == (-1, -2) and sim_game.possession == "Away":
			away_rFP_display = pygame.draw.rect(win, Soft_Red, (400, 285, 40, 15), 0)
		else:
			away_rFP_display = pygame.draw.rect(win, Red, (400, 285, 40, 15), 0)
		if Pos_Coordinates == (0, -2) and sim_game.possession == "Away":
			away_FF_display = pygame.draw.rect(win, Soft_Red, (470, 285, 40, 15), 0)
		else:
			away_FF_display = pygame.draw.rect(win, Red, (470, 285, 40, 15), 0)
		if Pos_Coordinates == (1, -2) and sim_game.possession == "Away":
			away_lFP_display = pygame.draw.rect(win, Soft_Red, (540, 285, 40, 15), 0)
		else:
			away_lFP_display = pygame.draw.rect(win, Red, (540, 285, 40, 15), 0)
		if Pos_Coordinates == (-1, -2) and sim_game.possession == "Home":
			home_lBP_display = pygame.draw.rect(win, Soft_Blue, (400, 300, 40, 15), 0)
		else:
			home_lBP_display = pygame.draw.rect(win, Blue, (400, 300, 40, 15), 0)
		if Pos_Coordinates == (0, -2) and sim_game.possession == "Home":
			home_FB_display = pygame.draw.rect(win, Soft_Blue, (470, 300, 40, 15), 0)
		else:
			home_FB_display = pygame.draw.rect(win, Blue, (470, 300, 40, 15), 0)
		if Pos_Coordinates == (1, -2) and sim_game.possession == "Home":
			home_rBP_display = pygame.draw.rect(win, Soft_Blue, (540, 300, 40, 15), 0)
		else:
			home_rBP_display = pygame.draw.rect(win, Blue, (540, 300, 40, 15), 0)
			
		home_RUCK_display = pygame.draw.rect(win, Blue, (590, 302, 40, 15), 0)
		
		home_RR_display = pygame.draw.rect(win, Blue, (590, 322, 40, 15), 0)
		
		home_ROV_display = pygame.draw.rect(win, Blue, (590, 342, 40, 15), 0)
		
		away_RUCK_display = pygame.draw.rect(win, Red, (590, 10, 40, 15), 0)
		
		away_RR_display = pygame.draw.rect(win, Red, (590, 30, 40, 15), 0)
		
		away_ROV_display = pygame.draw.rect(win, Red, (590, 50, 40, 15), 0)
		
		home_Int1_display = pygame.draw.rect(win, Blue, (350, 322, 40, 15), 0)
		
		home_Int2_display = pygame.draw.rect(win, Blue, (350, 342, 40, 15), 0)
		
		away_Int1_display = pygame.draw.rect(win, Red, (350, 10, 40, 15), 0)
		
		away_Int2_display = pygame.draw.rect(win, Red, (350, 30, 40, 15), 0)
		
		away_rBP_display
		away_FB_display
		away_lBP_display
		home_lFP_display
		home_FF_display
		home_rFP_display
		away_rHBF_display
		away_CHB_display
		away_lHBF_display
		home_lHFF_display
		home_CHF_display
		home_rHFF_display
		away_rW_display
		away_C_display
		away_lW_display
		home_lW_display
		home_C_display
		home_rW_display
		away_rHFF_display
		away_CHF_display
		away_lHFF_display
		home_lHBF_display
		home_CHB_display
		home_rHBF_display
		away_rFP_display
		away_FF_display
		away_lFP_display
		home_lBP_display
		home_FB_display
		home_rBP_display
		
		away_RUCK_display
		away_RR_display
		away_ROV_display
		home_RUCK_display
		home_RR_display
		home_ROV_display
		
		away_Int1_display
		away_Int2_display
		home_Int1_display
		home_Int2_display
	
	def comm_contest():
		global commentary
		if sim_game.ActionType == "Roving":
			commentary = sim_game.possession + " get the hit out"
		elif sim_game.ActionType == "BallGet":
			commentary = sim_game.possession + " wins the ball in tight"
		elif sim_game.ActionType == "Mark":
			commentary = sim_game.possession + " take a strong mark"
	
	def comm_defence():
		global commentary
		if sim_game.ActionType == "Spills Free":
			commentary = "Disposal is smothered and the ball spills free"
		elif sim_game.ActionType == "Tackle":
			commentary = sim_game.possession + " lays a hard tackle"
		elif sim_game.ActionType == "Dispossession":
			commentary = sim_game.possession + " dispossesses his opponent"
		elif sim_game.ActionType == "Free Kick":
			commentary = sim_game.possession + " wins a free kick and the ball back"
		elif sim_game.ActionType == "Finds Space":
			commentary = sim_game.possession + " has found some space to work with"
	
	def comm_carry():
		global commentary
		if sim_game.ActionType == "Kick":
			commentary = sim_game.possession + " kicks the ball"
		elif sim_game.ActionType == "Handball":
			commentary = sim_game.possession + " passes by hand"
		elif sim_game.ActionType == "Run":
			commentary = sim_game.possession + " takes a run and bounce"
	
	def match_sim_running():
		sim_running = True
		while sim_running:
			win.blit(game_bg, (0,0))
			QTR_display = myfont_game.render(str(sim_game.QTR), 1, Green)
			win.blit(QTR_display, (100, 15))
			if sim_game.game_seconds < 10:
				displayTime = str(sim_game.game_minutes) + ":0" + str(sim_game.game_seconds)
				GameTime_display = myfont_game.render(displayTime, 1, Green)
			else:
				displayTime = str(sim_game.game_minutes) + ":" + str(sim_game.game_seconds)
				GameTime_display = myfont_game.render(displayTime, 1, Green)
			win.blit(GameTime_display, (240, 15))
			
			homeTeam_display = myfont_game.render(sim_game.homeTeamShort, 1, White)
			win.blit(homeTeam_display, (110, 70))
			
			homeGoals_display = myfont_game.render(str(sim_game.home_goals), 1, White)
			homeBehinds_display = myfont_game.render(str(sim_game.home_behinds), 1, White)
			homeScore_display = myfont_game.render(str(sim_game.home_score), 1, White)
			win.blit(homeGoals_display, (35, 160))
			win.blit(homeBehinds_display, (135, 160))
			win.blit(homeScore_display, (235, 160))
			
			awayTeam_display = myfont_game.render(sim_game.awayTeamShort, 1, White)
			win.blit(awayTeam_display, (110, 220))
			
			awayGoals_display = myfont_game.render(str(sim_game.away_goals), 1, White)
			awayBehinds_display = myfont_game.render(str(sim_game.away_behinds), 1, White)
			awayScore_display = myfont_game.render(str(sim_game.away_score), 1, White)
			win.blit(awayGoals_display, (35, 310))
			win.blit(awayBehinds_display, (135, 310))
			win.blit(awayScore_display, (235, 310))
			
			sim_game.GamePlayTime()
			if match_status == "In Progress":
				if sim_game.transType == "Contest":
					sim_game.Generate_Play_contest()
					sim_game.comm_contest()
					teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
				elif sim_game.transType == "Defending":
					sim_game.Generate_Play_defender()
					sim_game.comm_defence()
					teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
				elif sim_game.transType == "Carrying":
					sim_game.Generate_Play_ballCarrier()
					sim_game.comm_carry()
					teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
				sim_game.GamePlayBallPos()
			pygame.time.delay(80)
			sim_game.map_play()
			comm_display = myfont_comm.render(commentary, 1, Green)
			win.blit(comm_display, (35, 370))
			#print(sim_game.transType)
			
			TestGameLine = "{" + str(sim_game.QTR) + "}" + displayTime + ": " + str(sim_game.home_score) + " -- " + str(sim_game.away_score) + " " + "Ball with " + sim_game.possession + " " + str(Pos_Coordinates) + ">" + sim_game.ActionType + ">" + '\n'
			
			textRecordingTest = open("test.txt", "a")
			textRecordingTest.write(TestGameLine)
			
			
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

run = True
main = True
playing_match = False
AddingPlayers = False
AddingTeams = False
Selection = False

Pick_Positions = False

#the main loop which gets the application running.
while run:
	pygame.event.get()
	
	clock.tick(12)
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if main:
		main_menu()
	
	if playing_match:
		sim_game.match_sim_running()
		
	if AddingTeams:
		TeamCreationScreen.openTCScreen()

	if AddingPlayers:
		PlayerCreationScreen.openPCScreen()
	
	if Selection:
		SelectionMenu.openSelection()
	
	if Pick_Positions:
		Select_FieldView.openFieldView()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
pygame.quit()