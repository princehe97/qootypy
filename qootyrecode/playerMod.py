import pandas as pd
import random

class Player(object):
	homeTeam = ''
	awayTeam = ''
	homePlayers = []
	awayPlayers = []
	homePosIndex = []
	awayPosIndex = []
	stat_categories = ['HO', 'K', 'M', 'HB', 'T', 'FF', 'FA', 'G', 'B', 'DT']
	
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
		KeyON = "h_INT1"
		KeyOFF = random.sample(list(Player.homePos_Players), 1)
		KeyOFF = KeyOFF[0]
		print("ON: " + KeyON)
		print("OFF: " + KeyOFF)
		
		print(Player.homePos_Players[KeyOFF])
		Player.homePos_Players[KeyON], Player.homePos_Players[KeyOFF] = Player.homePos_Players[KeyOFF], Player.homePos_Players[KeyON]
		print(Player.homePos_Players[KeyOFF])
		print("ON: " + Player.homePos_Players[KeyON])
		
		
		#key1, key2 = random.sample(list(d), 2)
		#d[key1], d[key2] = d[key2], d[key1]
	
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
				print(playerWithBall, Player.homeStats[playerWithBall])

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
				print(playerWithBall, Player.awayStats[playerWithBall])
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
				print(playerWithBall, Player.awayStats[playerWithBall])
			
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
				print(playerWithBall, Player.homeStats[playerWithBall])

############### player identification ends here


Player.Initiate()
Player.Interchange()
