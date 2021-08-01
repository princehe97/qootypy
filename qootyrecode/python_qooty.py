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

pygame.display.set_caption("QootyPy")

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
	
	#these determine that if the mouse cursor is between certain coordinates on the screen, texts will have interactions.
	if 90 + 110 > mouse[0] > 90 and 275 + 25 > mouse[1] > 275:
		#this makes the text 'play footy' light up in a "Light Green" colour instead of a Bluey Green colour when the mouse hovers over it
		menu_text1 = myfont_main.render('Play Footy', 1, Light_Green)
		#if a click is made while the mouse is between the above coordinates then the screen is instructed to transfer to a 'playing match' state
		if click[0] == 1:
			
			main = False
			playing_match = True
			pygame.time.delay(200)
	else:
		menu_text1 = myfont_main.render('Play Footy', 1, Bluey_Green)

	#this actually makes the text defined in the above code appear on screen, aka calling the variable
	win.blit(menu_text1, (90, 275))

	#this is necessary to ensure the screen is constantly updating because it needs to redetermine the position of the mouse
	pygame.display.update()

'''the main menu code has ended, everything below relates to the Team Creation Screen i.e. the screen in which you create a team to add into the sim's database so you can
select it to play in a game'''


############### player identification starts here

class Player(object):
	homeTeam = ''
	awayTeam = ''
	homePlayers = []
	awayPlayers = []
	homePosIndex = []
	awayPosIndex = []
	stat_categories = ['HO', 'K', 'M', 'HB', 'T', 'FF', 'FA', 'G', 'B']
	
	homeStats = {}
	awayStats = {}
	RevDict_FieldPosition = {}
	Dict_FieldPosition = {}
	
	homePos_Players = {}
	awayPos_Players = {}
	homePos_Oppo = {}
	awayPos_Oppo = {}
	
	Current_Player = ''
	Current_Oppo = ''
	
	FollowWithBall = False
	
	def Initiate():
		Player.Read_players()
		Player.Assign_Positions()
		Player.Assign_MatchUps()
		Player.PlayerStatSheet()
		Player.Possession_Index()
	
	def Read_players():
		df = pd.read_excel('TeamSelection.xls', header = 0)
		Player.homeTeam = df.iloc[0,1]
		#print(Player.homeTeam)
		Player.awayTeam = df.iloc[0,3]
		#print(Player.awayTeam)
		Player.homePlayers = df.iloc[1:21,1].values.tolist()
		#print(Player.homePlayers)
		Player.awayPlayers = df.iloc[1:21,3].values.tolist()
		#print(Player.awayPlayers)
		#print('read_player check!')
	
	def Assign_Positions():
		df = pd.read_excel('TeamSelection.xls', header = 0)
		Player.homePosIndex = df.iloc[1:21,0].values.tolist()
		Player.awayPosIndex = df.iloc[1:21,2].values.tolist()
		Player.homePos_Players = dict(zip(Player.homePosIndex, Player.homePlayers))
		Player.awayPos_Players = dict(zip(Player.awayPosIndex, Player.awayPlayers))
		
		#print(Player.homePos_Players)
		#print(Player.homePos_Players['h_rW'])
		#print('assign positions check!')	

	def Interchange():
			SubstitutionEvent = random.randint(1,40)
			if SubstitutionEvent == 1:
				WhichBench = random.randint(1,2)
				if sim_game.possession == "Home":
					if WhichBench == 1:
						KeyON = "h_INT1"
						KeyOFF = random.sample(list(Player.homePos_Players), 1)
						KeyOFF = KeyOFF[0]
						InterchangeCommentary = open("Commentary.txt", "a")
						InterchangeCommentary.write("<<<" + "ON: " + Player.homePos_Players[KeyON] + " | " + "OFF: " + Player.homePos_Players[KeyOFF] + ">>>" + '\n')
						#print("ON: " + Player.homePos_Players[KeyON], KeyON)
						#print("OFF: " + Player.homePos_Players[KeyOFF], KeyOFF)
						Player.homePos_Players[KeyON], Player.homePos_Players[KeyOFF] = Player.homePos_Players[KeyOFF], Player.homePos_Players[KeyON]
					elif WhichBench == 2:
						KeyON = "h_INT2"
						KeyOFF = random.sample(list(Player.homePos_Players), 1)
						KeyOFF = KeyOFF[0]
						InterchangeCommentary = open("Commentary.txt", "a")
						InterchangeCommentary.write("<<<" + "ON: " + Player.homePos_Players[KeyON] + " | " + "OFF: " + Player.homePos_Players[KeyOFF] + ">>>" + '\n')
						#print("ON: " + Player.homePos_Players[KeyON], KeyON)
						#print("OFF: " + Player.homePos_Players[KeyOFF], KeyOFF)
						Player.homePos_Players[KeyON], Player.homePos_Players[KeyOFF] = Player.homePos_Players[KeyOFF], Player.homePos_Players[KeyON]
				elif sim_game.possession == "Away":
					if WhichBench == 1:
						KeyON = "a_INT1"
						KeyOFF = random.sample(list(Player.awayPos_Players), 1)
						KeyOFF = KeyOFF[0]
						InterchangeCommentary = open("Commentary.txt", "a")
						InterchangeCommentary.write("<<<" + "ON: " + Player.awayPos_Players[KeyON] + " | " + "OFF: " + Player.awayPos_Players[KeyOFF] + ">>>" + '\n')
						#print("ON: " + Player.awayPos_Players[KeyON], KeyON)
						#print("OFF: " + Player.awayPos_Players[KeyOFF], KeyOFF)
						Player.awayPos_Players[KeyON], Player.awayPos_Players[KeyOFF] = Player.awayPos_Players[KeyOFF], Player.awayPos_Players[KeyON]
					elif WhichBench == 2:
						KeyON = "a_INT2"
						KeyOFF = random.sample(list(Player.awayPos_Players), 1)
						KeyOFF = KeyOFF[0]
						InterchangeCommentary = open("Commentary.txt", "a")
						InterchangeCommentary.write("<<<" + "ON: " + Player.awayPos_Players[KeyON] + " | " + "OFF: " + Player.awayPos_Players[KeyOFF] + ">>>" + '\n')
						#print("ON: " + Player.awayPos_Players[KeyON], KeyON)
						#print("OFF: " + Player.awayPos_Players[KeyOFF], KeyOFF)
						Player.awayPos_Players[KeyON], Player.awayPos_Players[KeyOFF] = Player.awayPos_Players[KeyOFF], Player.awayPos_Players[KeyON]

	def Assign_MatchUps():
		Player.homePos_Oppo = {'h_rBP':'a_lFP','h_FB':'a_FF','h_lBP':'a_rFP','h_rHBF':'a_lHFF','h_CHB':'a_CHF','h_lHBF':'a_rHFF', \
		'h_rW':'a_lW','h_C':'a_C','h_lW':'a_rW','h_rHFF':'a_lHBF','h_CHF':'a_CHB','h_lHFF':'a_rHBF', 'h_rFP':'a_lBP','h_FF':'a_FB', \
		'h_lFP':'a_rBP','h_RUCK':'a_RUCK','h_RR':'a_RR','h_R':'a_R'}
		Player.awayPos_Oppo = {value : key for (key, value) in Player.homePos_Oppo.items()}
		
		#for i in Player.homePos_Oppo:
		#	print(Player.homePos_Oppo[i])
		#for i in Player.awayPos_Oppo:
		#	print(Player.awayPos_Oppo[i])
	
	def PlayerStatSheet():
		for i in Player.homePlayers:
			Player.homeStats[i] = dict.fromkeys(Player.stat_categories, 0)
		#print(Player.homeStats['Blacky']['HO'])
		for j in Player.awayPlayers:
			Player.awayStats[j] = dict.fromkeys(Player.stat_categories, 0)
		#print(Player.awayStats['Tom Papley']['HO'])
	
	def Possession_Index():
		Player.RevDict_FieldPosition = {'a_rBP' : ((-1,2), "Away"), 'h_lFP' : ((-1,2), "Home"), 'a_FB' : ((0,2), "Away"), \
		'h_FF' : ((0,2), "Home"), 'a_lBP' : ((1,2), "Away"), 'h_rFP' : ((1,2), "Home"), 'a_rHBF' : ((-1,1), "Away"), \
		'h_lHFF' : ((-1,1), "Home"), 'a_CHB' : ((0,1), "Away"), 'h_CHF' : ((0,1), "Home"), 'a_lHBF' : ((1,1), "Away"), \
		'h_rHFF' : ((1,1), "Home"), 'a_rW' : ((-1,0), "Away"), 'h_lW' : ((-1,0), "Home"), 'a_C' : ((0,0), "Away"), \
		'h_C' : ((0,0), "Home"), 'a_lW' : ((1,0), "Away"), 'h_rW' :((1,0), "Home"), 'a_rHFF' : ((-1,-1), "Away"), \
		'h_lHBF' : ((-1,-1), "Home"), 'a_CHF' : ((0,-1), "Away"), 'h_CHB' : ((0,-1), "Home"), 'a_lHFF' : ((1,-1), "Away"), \
		'h_rHBF' : ((1,-1), "Home"), 'a_rFP' : ((-1,-2), "Away"), 'h_lBP' : ((-1,-2), "Home"), 'a_FF' : ((0,-2), "Away"), \
		'h_FB' : ((0,-2), "Home"), 'a_lFP' : ((1,-2), "Away"), 'h_rBP' : ((1,-2), "Home")}
		
		#print(Player.RevDict_FieldPosition['a_CHB'])
		
		Player.Dict_FieldPosition = {value : key for (key, value) in Player.RevDict_FieldPosition.items()}
		#print(Player.Dict_FieldPosition[((0,-2), "Home")])
		
		#print('pos index check!')
	
	def RuckContest():
		if sim_game.ActionType == "Ball Up":
			if sim_game.possession == "Home":
				Player.Current_Player = Player.homePos_Players['h_RUCK']
				Player.Current_Oppo = Player.awayPos_Players['a_RUCK']
			elif sim_game.possession == "Away":
				Player.Current_Player = Player.awayPos_Players['a_RUCK']
				Player.Current_Oppo = Player.homePos_Players['h_RUCK']
			sim_game.ActionType = "Rucking"
	
	def Follower():
		FOLL_Roll = random.randint(0,1)
		if FOLL_Roll == 0:
			sim_game.possession = "Home"
			PLAYER_Roll = random.randint(1,10)
			if PLAYER_Roll <= 2:
				Player.Current_Player = Player.homePos_Players['h_RUCK']
				Player.Current_Oppo = Player.awayPos_Players['a_RUCK']
				Player.FollowWithBall = True
			elif 2 < PLAYER_Roll <= 5:
				Player.Current_Player = Player.homePos_Players['h_RR']
				Player.Current_Oppo = Player.awayPos_Players['a_RR']
				Player.FollowWithBall = True
			elif 5 < PLAYER_Roll <= 8:
				Player.Current_Player = Player.homePos_Players['h_R']
				Player.Current_Oppo = Player.awayPos_Players['a_R']
				Player.FollowWithBall = True
			else:
				Player.UpdatePlayerInPossession()
		else:
			sim_game.possession = "Away"
			PLAYER_Roll = random.randint(1,10)
			if PLAYER_Roll <= 2:
				Player.Current_Player = Player.awayPos_Players['a_RUCK']
				Player.Current_Oppo = Player.homePos_Players['h_RUCK']
				Player.FollowWithBall = True
			elif 2 < PLAYER_Roll <= 5:
				Player.Current_Player = Player.awayPos_Players['a_RR']
				Player.Current_Oppo = Player.homePos_Players['h_RR']
				Player.FollowWithBall = True
			elif 5 < PLAYER_Roll <= 8:
				Player.Current_Player = Player.awayPos_Players['a_R']
				Player.Current_Oppo = Player.homePos_Players['h_R']
				Player.FollowWithBall = True
			else:
				Player.UpdatePlayerInPossession()

	def UpdatePlayerInPossession():
		Pos_Lookup = ((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession)
		if -1 <= sim_game.play_posCol <= 1 and -2 <= sim_game.play_posLine <= 2 and sim_game.possession != "None":
			Current_Pos = Player.Dict_FieldPosition[Pos_Lookup]
			if sim_game.possession == "Home":
				try:
					Player.Current_Player = Player.homePos_Players[Current_Pos]
					#Player.homeStats[Player.Current_Player]['HO'] += 1
					#print(Player.homeStats[Player.Current_Player]['HO'])
				except KeyError:
					Player.Current_Player = Player.awayPos_Players[Current_Pos]
			elif sim_game.possession == "Away":
				try:
					Player.Current_Player = Player.awayPos_Players[Current_Pos]
					#Player.awayStats[Player.Current_Player]['HO'] += 1
					#print(Player.awayStats[Player.Current_Player]['HO'])
				except KeyError:
					Player.Current_Player = Player.homePos_Players[Current_Pos]
			#print(Pos_Lookup, Player.Current_Player)
		else:
			Player.Follower()
	
	def UpdateOpponent():
		
		Pos_Lookup = ((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession)
		Current_Pos = Player.Dict_FieldPosition[Pos_Lookup]
		if sim_game.possession == "Home":
			OppoLookup = Player.homePos_Oppo[Current_Pos]
			Player.Current_Oppo = Player.awayPos_Players[OppoLookup]
		elif sim_game.possession == "Away":
			OppoLookup = Player.awayPos_Oppo[Current_Pos]
			Player.Current_Oppo = Player.homePos_Players[OppoLookup]
		

	def updatePlayerStats(teamWithBall, action, playerWithBall):
		if teamWithBall == "Home":
			try:
				if action == "Rucking":
					Player.homeStats[playerWithBall]['HO'] += 1
				elif action == "Kick" or action == "EffectiveKick":
					Player.homeStats[playerWithBall]['K'] += 1
				elif action == "Handball" or action == "EffectiveHandball":
					Player.homeStats[playerWithBall]['HB'] += 1
				elif action == "Mark":
					Player.homeStats[playerWithBall]['M'] += 1
				elif action == "Tackle":
					Player.awayStats[playerWithBall]['T'] += 1
				elif action == "Free Kick":
					Player.homeStats[playerWithBall]['FF'] += 1

					Pos_Lookup = ((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession)
					Current_Pos = Player.Dict_FieldPosition[Pos_Lookup]
					OppoLookup = Player.homePos_Oppo[Current_Pos]
					OppoPlayer = Player.awayPos_Players[OppoLookup]
					
					Player.awayStats[OppoPlayer]['FA'] += 1
				elif action == "Goal":
					Player.homeStats[playerWithBall]['G'] += 1
				elif action == "Behind":
					Player.homeStats[playerWithBall]['B'] += 1
				#print(playerWithBall, Player.homeStats[playerWithBall])

			except KeyError:
				if action == "Rucking":
					Player.awayStats[playerWithBall]['HO'] += 1
				elif action == "Kick" or action == "EffectiveKick":
					Player.awayStats[playerWithBall]['K'] += 1
				elif action == "Handball" or action == "EffectiveHandball":
					Player.awayStats[playerWithBall]['HB'] += 1
				elif action == "Mark":
					Player.awayStats[playerWithBall]['M'] += 1
				elif action == "Free Kick":
					Player.awayStats[playerWithBall]['FF'] += 1
					
					Pos_Lookup = ((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession)
					Current_Pos = Player.Dict_FieldPosition[Pos_Lookup]
					OppoPlayer = Player.homePos_Players[Current_Pos]
					
					Player.homeStats[OppoPlayer]['FA'] += 1
				elif action == "Goal":
					Player.awayStats[playerWithBall]['G'] += 1
				elif action == "Behind":
					Player.awayStats[playerWithBall]['B'] += 1
				#print(playerWithBall, Player.awayStats[playerWithBall])
		elif teamWithBall == "Away":
			try:
				if action == "Rucking":
					Player.awayStats[playerWithBall]['HO'] += 1
				elif action == "Kick" or action == "EffectiveKick":
					Player.awayStats[playerWithBall]['K'] += 1
				elif action == "Handball" or action == "EffectiveHandball":
					Player.awayStats[playerWithBall]['HB'] += 1
				elif action == "Mark":
					Player.awayStats[playerWithBall]['M'] += 1
				elif action == "Tackle":
					Player.homeStats[playerWithBall]['T'] += 1
				elif action == "Free Kick":
					Player.awayStats[playerWithBall]['FF'] += 1
					
					Pos_Lookup = ((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession)
					Current_Pos = Player.Dict_FieldPosition[Pos_Lookup]
					OppoLookup = Player.awayPos_Oppo[Current_Pos]
					OppoPlayer = Player.homePos_Players[OppoLookup]
					
					Player.homeStats[OppoPlayer]['FA'] += 1
				elif action == "Goal":
					Player.awayStats[playerWithBall]['G'] += 1
				elif action == "Behind":
					Player.awayStats[playerWithBall]['B'] += 1
				#print(playerWithBall, Player.awayStats[playerWithBall])
			
			except KeyError:
				if action == "Rucking":
					Player.homeStats[playerWithBall]['HO'] += 1
				elif action == "Kick" or action == "EffectiveKick":
					Player.homeStats[playerWithBall]['K'] += 1
				elif action == "Handball" or action == "EffectiveHandball":
					Player.homeStats[playerWithBall]['HB'] += 1
				elif action == "Mark":
					Player.homeStats[playerWithBall]['M'] += 1
				elif action == "Free Kick":
					Player.homeStats[playerWithBall]['FF'] += 1
					
					Pos_Lookup = ((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession)
					Current_Pos = Player.Dict_FieldPosition[Pos_Lookup]
					OppoPlayer = Player.awayPos_Players[Current_Pos]
					
					Player.awayStats[OppoPlayer]['FA'] += 1
				elif action == "Goal":
					Player.homeStats[playerWithBall]['G'] += 1
				elif action == "Behind":
					Player.homeStats[playerWithBall]['B'] += 1
				#print(playerWithBall, Player.homeStats[playerWithBall])

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
	homeG = 0
	homeB = 0
	
	homeD = 0
	
	awayHO = 0
	awayK = 0
	awayHB = 0
	awayM = 0
	awayT = 0
	awayFF = 0
	awayFA = 0
	awayG = 0
	awayB = 0
	
	awayD = 0
	
	def updateTeamStats(teamWithBall, action):
		if teamWithBall == "Home":
			if action == "Rucking":
				teamStatistics.homeHO += 1
			elif action == "Kick" or action == "EffectiveKick":
				teamStatistics.homeK += 1
			elif action == "Handball" or action == "EffectiveHandball":
				teamStatistics.homeHB += 1
			elif action == "Mark":
				teamStatistics.homeM += 1
			elif action == "Tackle":
				teamStatistics.awayT += 1
			elif action == "Free Kick":
				teamStatistics.homeFF += 1
				teamStatistics.awayFA += 1
			elif action == "Goal":
				teamStatistics.homeG += 1
			elif action == "Behind":
				teamStatistics.homeB += 1
			print(teamWithBall, action)
		
		elif teamWithBall == "Away":
			if action == "Rucking":
				teamStatistics.awayHO += 1
			elif action == "Kick" or action == "EffectiveKick":
				teamStatistics.awayK += 1
			elif action == "Handball" or action == "EffectiveHandball":
				teamStatistics.awayHB += 1
			elif action == "Mark":
				teamStatistics.awayM += 1
			elif action == "Tackle":
				teamStatistics.homeT += 1
			elif action == "Free Kick":
				teamStatistics.awayFF += 1
				teamStatistics.homeFA += 1
			elif action == "Goal":
				teamStatistics.awayG += 1
			elif action == "Behind":
				teamStatistics.awayB += 1
			print(teamWithBall, action)
	
	def GetTotalDisposals():
		teamStatistics.homeD = teamStatistics.homeK + teamStatistics.homeHB
		teamStatistics.awayD = teamStatistics.awayK + teamStatistics.awayHB
		
	def write_team_stats():
		with open("statsoutput_Team.csv", "w", newline="") as statsoutput_Team:
			writer = csv.writer(statsoutput_Team, delimiter = ',')
			writer.writerow(["Team Stats",Player.homeTeam,Player.awayTeam])
			writer.writerow(["HO",teamStatistics.homeHO,teamStatistics.awayHO])
			writer.writerow(["K",teamStatistics.homeK,teamStatistics.awayK])
			writer.writerow(["HB",teamStatistics.homeHB,teamStatistics.awayHB])
			writer.writerow(["M",teamStatistics.homeM,teamStatistics.awayM])
			writer.writerow(["T",teamStatistics.homeT,teamStatistics.awayT])
			writer.writerow(["FF",teamStatistics.homeFF,teamStatistics.awayFF])
			writer.writerow(["FA",teamStatistics.homeFA,teamStatistics.awayFA])
			writer.writerow(["G",teamStatistics.homeG,teamStatistics.awayG])
			writer.writerow(["B",teamStatistics.homeB,teamStatistics.awayB])
		
		statsoutput_Team.close()

#the main function that creates a simulation of the game. Still missing individual identifiable players, a prompt back to main menu and stats summary post-game.
class sim_game(object):
	game_minutes = 0
	game_seconds = 0
	QTR = 1
	stoppage_time = 5
	speed = 4
	home_goals = 0
	home_behinds = 0
	home_score = 0
	away_goals = 0
	away_behinds = 0
	away_score = 0
	play_posLine = 0
	play_posCol = 0
	congestionLimiter = 0

	areaOfGround = "Contest"
	possession = "None"
	transType = "Contest"
	ActionType = "Ball Up"

	left_throwIn = False
	right_throwIn = False
	play_restart = True
	
	sim_running = False

	def BallPosition():
		if sim_game.possession != "None":
			sim_game.areaOfGround = Player.Dict_FieldPosition[((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession)]
		else:
			sim_game.areaOfGround = "Contest"

	def EndOfQuarterComm():
		EndOfQuarterScore = open("Commentary.txt", "a")
		homeScoreline = Player.homeTeam + ": " + str(sim_game.home_goals) + "." + str(sim_game.home_behinds) + "." + str(sim_game.home_score)
		awayScoreline = Player.awayTeam + ": " + str(sim_game.away_goals) + "." + str(sim_game.away_behinds) + "." + str(sim_game.away_score)
		EndOfQuarterScore.write("====================" + '\n' + "END OF QUARTER " + str(sim_game.QTR - 1) + '\n' + homeScoreline + '\n' + awayScoreline + '\n' + "====================" + '\n')

	def ScoreUpdateComm():
		Commentary_UpdateScore = open("Commentary.txt", "a")
		homeScoreline = Player.homeTeam + ": " + str(sim_game.home_goals) + "." + str(sim_game.home_behinds) + "." + str(sim_game.home_score)
		awayScoreline = Player.awayTeam + ": " + str(sim_game.away_goals) + "." + str(sim_game.away_behinds) + "." + str(sim_game.away_score)
		Commentary_UpdateScore.write("--------------------" + '\n' + homeScoreline + '\n' + awayScoreline + '\n' + "--------------------" + '\n')

	def GamePlayTime():
		QTR_endTime = 20 + sim_game.stoppage_time
		if sim_game.QTR <= 4 and sim_game.game_minutes <= QTR_endTime:
			global match_status
			match_status = "In Progress"
			sim_game.game_seconds += sim_game.speed
			pygame.time.delay(100)
		elif sim_game.QTR == 5:
			match_status = "Finished"
			
			global playing_match
			global main
			teamStatistics.write_team_stats()
			
			FullStats = {**Player.homeStats, **Player.awayStats}
			df = pd.DataFrame(FullStats)
			df = df.transpose()
			df.to_csv('PlayerStats.csv')
			
			playing_match = False
			main = True
			sim_game.sim_running = False

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
			sim_game.EndOfQuarterComm()
			
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
				
				Player.RuckContest()
				print(Player.Current_Player, Player.Current_Oppo)

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
				if sim_game.ActionType == "Rucking":
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
				Player.Current_Player = Player.Current_Oppo
			elif sim_game.play_posLine == -2:
				sim_game.possession = "Home"
				Player.Current_Player = Player.Current_Oppo

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
			if movementRoll > 75:
				if isSideways == 0:
					sim_game.PlayBook("Short Kick", 1, 0, "forwards")
					sim_game.ActionType = "Kick"
				elif isSideways == 1:
					sim_game.PlayBook("Short Kick", 0, 1, "sideways")
					sim_game.ActionType = "Kick"
				
			elif 30 < movementRoll <= 75:
				if isSideways == 0:
					sim_game.PlayBook("Handball", 1, 0, "forwards")
					sim_game.ActionType = "Handball"
				elif isSideways == 1:
					sim_game.PlayBook("Handball", 0, 1, "sideways")
					sim_game.ActionType = "Handball"

			elif 15 < movementRoll <= 30:
				sim_game.PlayBook("Run And Bounce", 1, 0, "forwards")
				sim_game.ActionType = "Run"
			elif 5 < movementRoll <= 15:
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
			
			Player.RuckContest()
			teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
			Player.updatePlayerStats(sim_game.possession, sim_game.ActionType, Player.Current_Player)
			print("throw in ruck contest")

		elif sim_game.play_posCol > 1:
			sim_game.right_throwIn = True
			sim_game.play_posCol = 1
			#print("Right Boundary Throw In")
			sim_game.possession = "None"
			sim_game.ActionType = "Ball Up"
			sim_game.transType = "Contest"
			
			Player.RuckContest()
			teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
			Player.updatePlayerStats(sim_game.possession, sim_game.ActionType, Player.Current_Player)
			print("throw in ruck contest")

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
					
					teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
					Player.updatePlayerStats(sim_game.possession, sim_game.ActionType, Player.Current_Player)

				elif shotRollHome == 1:
					sim_game.home_goals += 1
					sim_game.ActionType = "Goal"
					
					teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
					Player.updatePlayerStats(sim_game.possession, sim_game.ActionType, Player.Current_Player)
					
					sim_game.play_restart = True
				sim_game.home_score = sim_game.home_goals * 6 + sim_game.home_behinds
				sim_game.away_score = sim_game.away_goals * 6 + sim_game.away_behinds
				sim_game.ScoreUpdateComm()

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
					
					teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
					Player.updatePlayerStats(sim_game.possession, sim_game.ActionType, Player.Current_Player)

				elif shotRollAway == 1:
					sim_game.away_goals += 1
					sim_game.ActionType = "Goal"
					
					teamStatistics.updateTeamStats(sim_game.possession, sim_game.ActionType)
					Player.updatePlayerStats(sim_game.possession, sim_game.ActionType, Player.Current_Player)
					
					sim_game.play_restart = True
				sim_game.home_score = sim_game.home_goals * 6 + sim_game.home_behinds
				sim_game.away_score = sim_game.away_goals * 6 + sim_game.away_behinds
				sim_game.ScoreUpdateComm()
		
		if sim_game.play_restart:
			sim_game.play_posLine = 0
			sim_game.play_posCol = 0
			sim_game.transType = "Contest"
	
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
		if sim_game.ActionType == "Rucking":
			commentary = Player.Current_Player + " gets the hit out"
		elif sim_game.ActionType == "BallGet":
			commentary = Player.Current_Player + " wins the ball in tight"
		elif sim_game.ActionType == "Mark":
			commentary = Player.Current_Player + " takes a strong mark"
	
	def comm_defence():
		global commentary
		if sim_game.ActionType == "Spills Free":
			commentary = "Disposal is smothered and the ball spills free"
		elif sim_game.ActionType == "Tackle":
			commentary = Player.Current_Oppo + " lays a hard tackle"
		elif sim_game.ActionType == "Dispossession":
			commentary = Player.Current_Oppo + " dispossesses his opponent"
		elif sim_game.ActionType == "Free Kick":
			commentary = Player.Current_Oppo + " wins a free kick and the ball back"
		elif sim_game.ActionType == "Finds Space":
			commentary = Player.Current_Player + " has found some space to work with"
	
	def comm_carry():
		global commentary
		if sim_game.ActionType == "Kick":
			commentary = Player.Current_Player + " kicks the ball"
		elif sim_game.ActionType == "Handball":
			commentary = Player.Current_Player + " passes by hand"
		elif sim_game.ActionType == "Run":
			commentary = Player.Current_Player + " takes a run and bounce"
	
	def match_sim_running():
		Player.Initiate()
		sim_game.sim_running = True
		while sim_game.sim_running:
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
			
			homeTeam_display = myfont_game.render(Player.homeTeam, 1, White)
			win.blit(homeTeam_display, (110, 70))
			
			homeGoals_display = myfont_game.render(str(sim_game.home_goals), 1, White)
			homeBehinds_display = myfont_game.render(str(sim_game.home_behinds), 1, White)
			homeScore_display = myfont_game.render(str(sim_game.home_score), 1, White)
			win.blit(homeGoals_display, (35, 160))
			win.blit(homeBehinds_display, (135, 160))
			win.blit(homeScore_display, (235, 160))
			
			awayTeam_display = myfont_game.render(Player.awayTeam, 1, White)
			win.blit(awayTeam_display, (110, 220))
			
			awayGoals_display = myfont_game.render(str(sim_game.away_goals), 1, White)
			awayBehinds_display = myfont_game.render(str(sim_game.away_behinds), 1, White)
			awayScore_display = myfont_game.render(str(sim_game.away_score), 1, White)
			win.blit(awayGoals_display, (35, 310))
			win.blit(awayBehinds_display, (135, 310))
			win.blit(awayScore_display, (235, 310))
			
			sim_game.GamePlayTime()
			if match_status == "In Progress":
				
				if sim_game.ActionType != "Run":
					follower_involve = random.randint(1,5)
					if follower_involve == 1:
						Player.Follower()
					else:
						Player.UpdatePlayerInPossession()
						if not Player.FollowWithBall:
							Player.UpdateOpponent()
						else:
							Player.FollowWithBall = False

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

				if Player.Current_Player != '':
					Player.updatePlayerStats(sim_game.possession, sim_game.ActionType, Player.Current_Player)
					#print("CURRENT: " + Player.Current_Player)
				#print((sim_game.play_posCol, sim_game.play_posLine), sim_game.possession, sim_game.transType, sim_game.ActionType)
				
				sim_game.GamePlayBallPos()
				
				Player.Interchange()
				
			pygame.time.delay(40)
			
			sim_game.map_play()
			comm_display = myfont_comm.render(commentary, 1, Green)
			win.blit(comm_display, (35, 370))
			#print(sim_game.transType)
			
			#TestGameLine = "{" + str(sim_game.QTR) + "}" + displayTime + ": " + str(sim_game.home_score) + " -- " + str(sim_game.away_score) + " " + "Ball with " + sim_game.possession + " " + str(Pos_Coordinates) + ">" + sim_game.ActionType + ">" + '\n'

			sim_game.BallPosition()
			PrintCommentary = "{" + str(sim_game.QTR) + "}" + "[" + sim_game.areaOfGround + "] " + displayTime + ": " + commentary

			#textRecordingTest = open("test.txt", "a")
			#textRecordingTest.write(TestGameLine)
			
			textcommentaryTest = open("Commentary.txt", "a")
			textcommentaryTest.write(PrintCommentary + '\n')
			
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

run = True
main = True
playing_match = False


#the main loop which gets the application running.
while run:
	pygame.event.get()
	
	clock.tick(20)
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if main:
		main_menu()
	
	if playing_match:
		sim_game.match_sim_running()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
pygame.quit()
