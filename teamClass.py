class team:
	def __init__(self, name, gamesWon, gamesLost, stat, stat2):
		self.name = name
		self.gamesWon = gamesWon
		self.gamesLost = gamesLost
		self.stat = stat
		self.stat2 = stat2
	def getName(self):
		return self.name
	def getGamesWon(self):
		return self.gamesWon
	def getGamesLost(self):
		return self.gamesLost
	def getStat(self):
		return self.stat
	def getStat2(self):
		return self.stat2

	def incrementGamesWon(self):
		self.gamesWon += 1
	def incrementGamesLost(self):
		self.gamesLost += 1
	def setStat(self, stat):
		self.stat = stat
	def setStat2(self, stat2):
		self.stat2 = stat2
