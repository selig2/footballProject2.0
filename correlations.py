from teamClass import *
import os, numpy

def correlate(stat):
	masterX, masterY1, masterY2, masterY3 = [], [], [], []
	# only correlate for 2003- 2013
	abrvToName = {"ARI": "Arizona", "ATL": "Atlanta", "BAL": "Baltimore", "BUF": "Buffalo", "CAR": "Carolina", "CHI": "Chicago", "CIN": "Cincinnati", "CLE": "Cleveland", "DAL": "Dallas", "DEN": "Denver", "DET": "Detroit", "GB": "Green Bay", "HOU": "Houston", "IND": "Indianapolis", "JAX": "Jacksonville", "KC": "Kansas City", "MIA": "Miami", "MIN": "Minnesota", "NYG": "NY Giants", "NYJ": "NY Jets", "NE": "New England", "NO": "New Orleans", "OAK": "Oakland", "PHI": "Philadelphia", "PIT": "Pittsburgh", "SD": "San Diego", "SF": "San Francisco", "SEA": "Seattle", "STL": "St Louis", "TB": "Tampa Bay", "TEN": "Tennessee", "WSH": "Washington"}
	nameToAbrv = {v: k for k, v in abrvToName.items()}
	acceptableYears = ["2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"]
	print stat
	for j in range(len(acceptableYears)): # for years 2003-2013
		teams = [team("ARI", 0, 0, [], []), team("ATL", 0, 0, [], []), team("BAL", 0, 0, [], []), team("BUF", 0, 0, [], []), team("CAR", 0, 0, [], []), team("CHI", 0, 0, [], []), team("CIN", 0, 0, [], []), team("CLE", 0, 0, [], []), team("DAL", 0, 0, [], []), team("DEN", 0, 0, [], []), team("DET", 0, 0, [], []), team("GB", 0, 0, [], []), team("HOU", 0, 0, [], []), team("IND", 0, 0, [], []), team("JAX", 0, 0, [], []), team("KC", 0, 0, [], []), team("MIA", 0, 0, [], []), team("MIN", 0, 0, [], []), team("NE", 0, 0, [], []), team("NO", 0, 0, [], []), team("NYG", 0, 0, [], []), team("NYJ", 0, 0, [], []), team("OAK", 0, 0, [], []), team("PHI", 0, 0, [], []), team("PIT", 0, 0, [], []), team("SD", 0, 0, [], []), team("SF", 0, 0, [], []), team("SEA", 0, 0, [], []), team("STL", 0, 0, [], []), team("TB", 0, 0, [], []), team("TEN", 0, 0, [], []), team("WSH", 0, 0, [], [])]
		for file in os.listdir("/Users/lselig/Desktop/footballProject2.0/schedules/"):
			if(file[:4] == acceptableYears[j]):
				with open("/Users/lselig/Desktop/footballProject2.0/schedules/" + file, "r") as scheduleFile:
					lines = scheduleFile.readlines()
					for i in range(1, len(lines)):
						line = lines[i].split(",")
						team1Name = line[0].split()[0]
						team2Name = line[1].split()[0]
						for element in teams:
							if(element.getName() == team1Name):
								element.incrementGamesWon()
							elif(element.getName() == team2Name):
								element.incrementGamesLost()
		with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + stat,  "r") as csvFile:
			lines = csvFile.readlines()
			for i in range(1, len(lines)):
				line = lines[i].split(",")
				for element in teams:
					if(element.getName() == nameToAbrv[line[0]]):
						value = line[16 + (16 * j)]
						if(value[-1] == "%"): # handle the parentheses case
							value = value[:-1]
						elif(":" in value): # handle time of possesion
							value = float(value[:2]) + (float(value[3:5]) / 60) 
						elif("--" in value): # handle value dne case
							value = 0
						element.setStat(float(value))

					if(stat == "Average_Scoring_Margin.csv" and element.getName() == nameToAbrv[line[0]]):
						# print "INNNN"
						value = line[16 + (16 * j)]
						if(value[-1] == "%"): # handle the parentheses case
							value = value[:-1]
						elif(":" in value): # handle time of possesion
							value = float(value[:2]) + (float(value[3:5]) / 60) 
						elif("--" in value): # handle value dne case
							value = 0
						element.setStat2(float(value))

		for element in teams: # dump the stats from this year, into the master list
			masterX.append(element.getStat())
			masterY1.append(element.getGamesWon())
			masterY2.append(element.getGamesLost())
			masterY3.append(element.getStat2())
		print masterY3

			# print element.getName(), element.getGamesWon(), element.getGamesLost(), element.getStatArray()
	# print len(masterX), len(masterY1), len(masterY2)
	# print max(masterY1), max(masterX), max(masterY2)
	# for i in range(len(masterX)):
	# 	print masterX[i], masterY1[i]
	return numpy.corrcoef(masterX, masterY3)
corrs = []
def getKey(item):
	return item[0]

for file in os.listdir("/Users/lselig/Desktop/footballProject2.0/csvFiles"):
	# print file, correlate(file)[0][1]
	corrs.append((correlate(file)[0][1], file))
corrs = correlate("Average_Scoring_Margin.csv")[0][1]
print corrs
# sorted = sorted(corrs, key = getKey, reverse = True)
# for x in sorted:
# 	print x
