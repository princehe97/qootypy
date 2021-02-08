https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame

class PlayerEntry:
	def __init__(name, team, position):
		self.name = name
		self.team = team
		self.position = position
	
	def printName(self):
		print self.name

def importPlayers():

	playerList = []
	
	for i in range(0, 20):
		playerList.append(PlayerEntry("", "", ""))
		
	playerList.append(PlayerEntry("luke", "", ""))
	playerList.append(PlayerEntry("simon" "", ""))

	player = Player("", "", "")
	
	
	
	
	player("hP01","Home","rFPh")
	player("hP02","Home","FFh")
	player("hP03","Home","lFPh")
	player("hP04","Home","rHFFh")
	player("hP05","Home","CHFh")
	player("hP06","Home","lHFFh")
	player("hP07","Home","rWh")
	player("hP08","Home","Ch")
	player("hP09","Home","lWh")
	player("hP10","Home","rHBFh")
	player("hP11","Home","CHBh")
	player("hP12","Home","lHBFh")
	player("hP13","Home","rBPh")
	player("hP14","Home","FBh")
	player("hP15","Home","lBPh")
	player("hP16","Home","RUCKh")
	player("hP17","Home","RRh")
	player("hP18","Home","Rh")
	player("hP19","Home","INT1h")
	player("hP20","Home","INT2h")
	
	player("aP01","Away","rFPa")
	player("aP02","Away","FFa")
	player("aP03","Away","lFPa")
	player("aP04","Away","rHFFa")
	player("aP05","Away","CHFa")
	player("aP06","Away","lHFFa")
	player("aP07","Away","rWa")
	player("aP08","Away","Ca")
	player("aP09","Away","lWa")
	player("aP10","Away","rHBFa")
	player("aP11","Away","CHBa")
	player("aP12","Away","lHBFa")
	player("aP13","Away","rBPa")
	player("aP14","Away","FBa")
	player("aP15","Away","lBPa")
	player("aP16","Away","RUCKa")
	player("aP17","Away","RRa")
	player("aP18","Away","Ra")
	player("aP19","Away","INT1a")
	player("aP20","Away","INT2a")

class player(object):
	RUCK_POScol = 0
	RUCK_POSline = 0
	RR_POScol = 0
	RR_POSline = 0
	R_POScol = 0
	RR_POSline = 0
	
	def __init__(self, name, team, position):
		self._name = name
		self._team = team
		self._position = position
		self._stats = {
			"Hitouts": 0,
			"Kicks": 0,
			"Handballs": 0,
			"Marks": 0,
			"Tackles": 0,
			"Frees For": 0,
			"Fress Against": 0,
			"Goals": 0,
			"Behinds": 0
		}

	def DefinePositions():
		rFPh = (1, 2, "Home")
		FFh = (0, 2, "Home")
		lFPh = (-1, 2, "Home")
		rHFFh = (1, 1, "Home")
		CHFh = (0, 1, "Home")
		lHFFh = (-1, 1, "Home")
		rWh = (1, 0, "Home")
		Ch = (0, 0, "Home")
		lWh = (-1, 0, "Home")
		rHBFh = (1, -1, "Home")
		CHBh = (0, -1, "Home")
		lHBFh = (-1, -1, "Home")
		rBPh = (1, -2, "Home")
		FBh = (0, -2, "Home")
		lBPh = (-1, -2, "Home")
		RUCKh = (player.RUCK_POScol, player.RUCK_POSline, "Home")
		RRh = (player.RR_POScol, player.RR_POSline, "Home")
		Rh = (player.R_POScol, player.R_POSline, "Home")
		INT1h = (-4, -4, "Home")
		INT2h = (-5, -5, "Home")
		
		lBPa = (1, 2, "Away")
		FBa = (0, 2, "Away")
		rBPa = (-1, 2, "Away")
		lHBFa = (1, 1, "Away")
		CHBa = (0, 1, "Away")
		rHBFa = (-1, 1, "Away")
		lWa = (1, 0, "Away")
		Ca = (0, 0, "Away")
		rWa = (-1, 0, "Away")
		lHFFa = (1, -1, "Away")
		CHFa = (0, -1, "Away")
		rHFFa = (-1, -1, "Away")
		lFPa = (1, -2, "Away")
		FFa = (0, -2, "Away")
		rFPa = (-1, -2, "Away")
		RUCKa = (player.RUCK_POScol, player.RUCK_POSline, "Away")
		RRa = (player.RR_POScol, player.RR_POSline, "Away")
		Ra = (player.R_POScol, player.R_POSline, "Away")
		INT1a = (4, 4, "Away")
		INT2a = (5, 5, "Away")