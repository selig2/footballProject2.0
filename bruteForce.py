import time, random, math
from logicalUnit import *
def getMaxMin(fileName):
	cells = []
	with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + fileName) as csv:
		lines = csv.readlines()
		for i in range(1, len(lines)):
			line = lines[i].split(",")
			for j in range(1, len(line)):
				cells.append(float(line[j]))
	return (max(cells), min(cells))

def getRange(maxMin):
	cutOff = range(0, 32)
	increment = (maxMin[0] - maxMin[1]) / 32.0
	values = []
	for i in range(32):
		values.append(maxMin[1] + (i*increment))
	return dict(zip(cutOff, values))

def getFitness(bitList):
	gamesCorrect = 0
	nameDict = {"ARI": "Arizona", "ATL": "Atlanta", "BAL": "Baltimore", "BUF": "Buffalo", "CAR": "Carolina", "CHI": "Chicago", "CIN": "Cincinnati", "CLE": "Cleveland", "DAL": "Dallas", "DEN": "Denver", "DET": "Detriot", "GB": "Green Bay", "HOU": "Houston", "IND": "Indianapolis", "JAX": "Jacksonville", "KC": "Kansas City", "MIA": "Miami", "MIN": "Minnesota", "NYG": "NY Giants", "NYJ": "NY Jets", "NE": "New England", "NO": "New Orleans", "OAK": "Oakland", "PHI": "Philadelphia", "PIT": "Pittsburgh", "SD": "San Diego", "SF": "San Fransisco", "SEA": "Seattle", "STL": "St Louis", "TB": "Tampa Bay", "TEN": "Tennessee", "WSH": "Washington"}
	team1Var1, team2Var1 = 0, 0
	team1Var2, team2Var2 = 0, 0
	team1Var3, team2Var3 = 0, 0


	# pppMaxMin = getMaxMin("Points_per_Play.csv")
	# numSacksMaxMin = getMaxMin("Opponent_Points_per_Game.csv")
	# oppypgMaxMin = getMaxMin("Red_Zone_Scores_per_Game_(TDs_only).csv")

 # 	pppDict = getRange(pppMaxMin)
	# nsDict = getRange(numSacksMaxMin) 
	# oppYPGDict = getRange(oppypgMaxMin)

	# bl = self.getBitList()
	bl = bitList#['0', '0', '0', '0', '1',       '1', '0', '1', '0', '0',     '0', '1', '1', '0', '1',    '1', '1', '1',    '0', '0', '0']

	# pppString = bl[:5]
	# nsString = bl[5:10]
	# oppYPGString = bl[10:15]
	logicalGroupingString = bl[:3]
	greaterLessString = bl[3:6]


	# proposedPPPValue = pppDict[int("".join(pppString), 2)]
	# proposedNSValue = nsDict[int("".join(nsString), 2)]
	# proposedOPPYPGValue = oppYPGDict[int("".join(oppYPGString), 2)]
	logicalGroupingDecimal = int("".join(logicalGroupingString), 2)
	greaterLessDecimal = int("".join(greaterLessString), 2)

	# print "Proposed OPP YPG:", proposedOPPYPGValue, type(proposedOPPYPGValue)
	# print "Proposed NS:", proposedNSValue, type(proposedNSValue)
	# print "Proposed PPP:", proposedPPPValue, type(proposedPPPValue)
	# print "Logical Grouping Decimal:", logicalGroupingDecimal, type(logicalGroupingDecimal)
	# print "Greater Less Decimal:", greaterLessDecimal, type(greaterLessDecimal)
	weeks = ["2003-17.txt", "2004-17.txt", "2005-17.txt", "2006-17.txt", "2007-17.txt", "2008-17.txt", "2009-17.txt", "2010-17.txt", "2011-17.txt", "2012-17.txt", "2013-17.txt"]#, \
			# "2003-3.txt", "2004-3.txt", "2005-3.txt", "2006-3.txt", "2007-3.txt", "2008-3.txt", "2009-3.txt", "2010-3.txt", "2011-3.txt", "2012-3.txt", "2013-3.txt",\
			# "2003-4.txt", "2004-4.txt", "2005-4.txt", "2006-4.txt", "2007-4.txt", "2008-4.txt", "2009-4.txt", "2010-4.txt", "2011-4.txt", "2012-4.txt", "2013-4.txt",\
			# "2003-5.txt", "2004-5.txt", "2005-5.txt", "2006-5.txt", "2007-5.txt", "2008-5.txt", "2009-5.txt", "2010-5.txt", "2011-5.txt", "2012-5.txt", "2013-5.txt",\
			# "2003-6.txt", "2004-6.txt", "2005-6.txt", "2006-6.txt", "2007-6.txt", "2008-6.txt", "2009-6.txt", "2010-6.txt", "2011-6.txt", "2012-6.txt", "2013-6.txt",\
			# "2003-7.txt", "2004-7.txt", "2005-7.txt", "2006-7.txt", "2007-7.txt", "2008-7.txt", "2009-7.txt", "2010-7.txt", "2011-7.txt", "2012-7.txt", "2013-7.txt",\
			# "2003-8.txt", "2004-8.txt", "2005-8.txt", "2006-8.txt", "2007-8.txt", "2008-8.txt", "2009-8.txt", "2010-8.txt", "2011-8.txt", "2012-8.txt", "2013-8.txt",\
			# "2003-9.txt", "2004-9.txt", "2005-9.txt", "2006-9.txt", "2007-9.txt", "2008-9.txt", "2009-9.txt", "2010-9.txt", "2011-9.txt", "2012-9.txt", "2013-9.txt",\
			# "2003-10.txt", "2004-10.txt", "2005-10.txt", "2006-10.txt", "2007-10.txt", "2008-10.txt", "2009-10.txt", "2010-10.txt", "2011-10.txt", "2012-10.txt", "2013-10.txt",\
			# "2003-11.txt", "2004-11.txt", "2005-11.txt", "2006-11.txt", "2007-11.txt", "2008-11.txt", "2009-11.txt", "2010-11.txt", "2011-11.txt", "2012-11.txt", "2013-11.txt",\
			# "2003-12.txt", "2004-12.txt", "2005-12.txt", "2006-12.txt", "2007-12.txt", "2008-12.txt", "2009-12.txt", "2010-12.txt", "2011-12.txt", "2012-12.txt", "2013-12.txt",\
			# "2003-13.txt", "2004-13.txt", "2005-13.txt", "2006-13.txt", "2007-13.txt", "2008-13.txt", "2009-13.txt", "2010-13.txt", "2011-13.txt", "2012-13.txt", "2013-13.txt",\
			# "2003-14.txt", "2004-14.txt", "2005-14.txt", "2006-14.txt", "2007-14.txt", "2008-14.txt", "2009-14.txt", "2010-14.txt", "2011-14.txt", "2012-14.txt", "2013-14.txt",\
			# "2003-15.txt", "2004-15.txt", "2005-15.txt", "2006-15.txt", "2007-15.txt", "2008-15.txt", "2009-15.txt", "2010-15.txt", "2011-15.txt", "2012-15.txt", "2013-15.txt",\
			# "2003-16.txt", "2004-16.txt", "2005-16.txt", "2006-16.txt", "2007-16.txt", "2008-16.txt", "2009-16.txt", "2010-16.txt", "2011-16.txt", "2012-16.txt", "2013-16.txt",\
			# "2003-17.txt", "2004-17.txt", "2005-17.txt", "2006-17.txt", "2007-17.txt", "2008-17.txt", "2009-17.txt", "2010-17.txt", "2011-17.txt", "2012-17.txt", "2013-17.txt"]
	
	columns = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320]
	for m in range(len(weeks)):

		with open("/Users/lselig/Desktop/footballProject2.0/schedules/" + weeks[m], "r") as scheduleFile:
			scheduleLines = scheduleFile.readlines()
			for i in range(1, len(scheduleLines)):
				line = scheduleLines[i].split(",")
				team1Abrv = line[0].split()[0]
				team2Abrv = line[1].split()[0]
				team1Score = int(line[0].split()[1])
				team2Score = int(line[1].split()[1])
				with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + "Points_per_Play.csv") as pppcsv:
					pppcsvLines = pppcsv.readlines()
					for j in range(1, len(pppcsvLines)):
						teamLine = pppcsvLines[j].split(",")
						if(teamLine[0] == nameDict[team1Abrv]):
							team1Var1 = float(teamLine[columns[m]])
						elif(teamLine[0] == nameDict[team2Abrv]):
							team2Var1 = float(teamLine[columns[m]])


				with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + "Opponent_Points_per_Game.csv") as sacksCsv:
					sackCSVLines = sacksCsv.readlines()
					for k in range(1, len(sackCSVLines)):
						teamLine = sackCSVLines[k].split(",")
						if(teamLine[0] == nameDict[team1Abrv]):
							team1Var2 = float(teamLine[columns[m]])
						elif(teamLine[0] == nameDict[team2Abrv]):
							team2Var2 = float(teamLine[columns[m]])


				with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + "Red_Zone_Scores_per_Game_(TDs_only).csv") as oppYPGCsv:
					oppYPGValueLines = oppYPGCsv.readlines()
					for l in range(1, len(oppYPGValueLines)):
						teamLine = oppYPGValueLines[l].split(",")
						if(teamLine[0] == nameDict[team1Abrv]):
							team1Var3 = float(teamLine[columns[m]])
						elif(teamLine[0] == nameDict[team2Abrv]):
							team2Var3 = float(teamLine[columns[m]])

				# print "Team1 Name:", team1Abrv, "-- Team2 Name:", team2Abrv
				# print "Team1 Score:", team1Score, type(team1Score), "-- Team2 Score:", team2Score, type(team2Score)
				# print "Team1 PPP:", actualPPPValue, type(actualPPPValue)
				# print "Team1 NS:", actualNSValue, type(actualNSValue)
				# print "Team1 OPPYPG:", actualOPPYPGValue, type(actualOPPYPGValue)

				team1Win = False
				team2Win = False
				if(logicalGroupingDecimal == 0):
					team1Win = cond1(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond1(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				elif(logicalGroupingDecimal == 1):
					team1Win = cond2(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond2(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				elif(logicalGroupingDecimal == 2):
					team1Win = cond3(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond3(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				elif(logicalGroupingDecimal == 3):
					team1Win = cond4(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond4(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				elif(logicalGroupingDecimal == 4):
					team1Win = cond5(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond5(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				elif(logicalGroupingDecimal == 5):
					team1Win = cond6(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond6(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				elif(logicalGroupingDecimal == 6):
					team1Win = cond7(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond7(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				elif(logicalGroupingDecimal == 7):
					team1Win = cond8(team1Var1, team2Var1, team1Var2, team2Var2, team1Var3, team2Var3, greaterLessDecimal)
					team2Win = cond8(team2Var1, team1Var1, team2Var2, team1Var2, team2Var3, team1Var3, greaterLessDecimal)

				else:
					print "Error"
					sys.exit(1)

				# 1 -- we could say Team1 Wins and they actually won
				# 2 -- team1 wins and they actually lost
				# 3 -- team 1 loses and they actually lost
				# 4 -- team 1 loses and they actually won

				# 5 -- team 2 wins and they actually win
				# 6 -- team2 wins they actually lost
				# 7 -- team 2 loses and they actually lose
				# 8 -- team 2 loses and they actually win
				# if(1 and 7) or (3 and 5)
				exp1 = (team1Win and (team1Score >= team2Score)) and ((not team2Win) and (team2Score < team1Score))
				exp2 = ((not team1Win) and (team1Score < team2Score)) and (team2Win and (team2Score >= team1Score))
				
				if(exp1 or exp2):
					gamesCorrect += 1
	return gamesCorrect

def getKey(item):
	return item[1]


def bruteForce():
	pppMaxMin = getMaxMin("Points_per_Play.csv")
	numSacksMaxMin = getMaxMin("Opponent_Points_per_Game.csv")
	oppypgMaxMin = getMaxMin("Red_Zone_Scores_per_Game_(TDs_only).csv")

	pppDict = getRange(pppMaxMin)
	nsDict = getRange(numSacksMaxMin) 
	oppYPGDict = getRange(oppypgMaxMin)

	start_time = time.time()
	pairs = []
	for i in range(2 ** 6):
		print "Iteration -- ", i
		bitList = '{0:06b}'.format(i)
		bitList = list(bitList)
		# print bitList
		gamesCorrectForBitList = getFitness(bitList)
		pairs.append((bitList, gamesCorrectForBitList))
	print "--- %s seconds ---" % (time.time() - start_time)

	print "CALCULATING MAX"
	pairs = sorted(pairs, reverse=True, key = getKey)
	# print pairs
	# print "\n\n"
	# print "Max games correct: ", pairs[0][1], "String:", pairs[0][0]
	for pair in pairs:
		print "Max games correct: ", pair[1], "String:", pair[0]
print bruteForce()
def simulatedAnnealing():
	

	start_time = time.time()
	allBitStrings = []

	#  set up all of the bitstrings
	for i in range(2 ** 21):
		allBitStrings.append(list('{0:021b}'.format(i)))

	x = random.randint(0, len(allBitStrings)-1) # generate random solution
	y = fitness(allBitStrings[x]) # calculate energy of random solution
	temperature = 90 # set initial temperature

	while(temperature > 0): # while we are still hot
		newX = x
		# print "Temperature", temperature
		print newX, fitness(allBitStrings[newX])
		for i in range(20): #  for n iterations do:

			randomMovement = random.randint(1, 1000)
			if(random.uniform(0, 1) < 0.5): # half the time move in the negative direction
				newX = newX - randomMovement # adjust test solution
			else:
				newX = newX + randomMovement

			newY = fitness(allBitStrings[newX])
			delta = newY - y

			if(delta > 0): # if we found a better energy value
				y = newY
				x = newX
				# break
			elif(math.exp(  (float(delta * -1) / temperature)  ) > random.uniform(0, 1)):
				y = newY
				x = newX
				break

		temperature -= 1
	print "--- %s seconds ---" % (time.time() - start_time)
	return (x, startY)
# print simulatedAnnealing()

	
