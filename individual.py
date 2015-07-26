import random, sys, operator, os
from logicalUnit import *

class individual:
	
	def __init__(self, bitList):
		self.bitList = bitList

	def getBitList(self):
		return self.bitList

	def setString(self, newBitList):
		self.bitList = newBitList


	def getStat1(self):
		stat1 = int("".join(self.bitList)[0:8], 2)
		return stat1

	def getStat2(self):
		stat2 = int("".join(self.bitList)[8:16], 2)
		return stat2

	def getStat3(self):
		stat3 = int("".join(self.bitList)[16:24], 2)
		return stat3

	def getLogicalGroupingString(self):
		logicalGroupingString = "".join(self.bitList)[24:27]
		return logicalGroupingString

	def getGreaterLessString(self):
		greaterLessString = "".join(self.bitList)[27:30]
		return greaterLessString

	def getFitness(self, weeks, columns):
		gamesCorrect = 0



		statIDs = ['Opponent_Extra_Points_Made_per_Game', 'Third_Down_Conversions_per_Game', 'Opponent_Special_Teams_Points_per_Game_(Estimated)', 'Opponent_Completions_per_Game', 'Opponent_Takeaway_Fumble_Recovery_Percentage', 'Red_Zone_Scores_per_Game_(TDs_only)', 'Average_Scoring_Margin', 'Punt_Blocked_Percentage', '4th_Quarter_Time_of_Possession_Share_%', 'Opponent_Interceptions_Thrown_Percentage', 'Yards_per_Play', 'Points_per_Play_Margin', '2nd_Half_Time_of_Possession_Share_%', 'Rushing_Attempts_per_Game', 'Opponent_2nd_Half_Points_Game', 'Giveaways_per_Game', 'Rushing_Play_Percentage', 'Field_Goal_Got_Blocked_Percentage', 'Fumbles_Lost_per_Game', 'Opponent_Two_Point_Conversion_Attempts_per_Game', 'Average_Time_of_Possession_(Excluding_OT)', 'Yards_per_Pass_Attempt', 'Red_Zone_Scoring_Percentage_(TD_only)', 'Special_Teams_Touchdowns_per_Game', 'QB_Sacked_Percentage', 'Opponent_Penalties_per_Play', 'Opponent_Field_Goal_Attempts_per_Game', 'Opponent_Rushing_First_Downs_per_Game', 'Opponent_Punts_per_Offensive_Score', '3rd_Quarter_Time_of_Possession_Share_%', 'Opponent_Two_Point_Conversion_Percentage', 'Red_Zone_Scoring_Attempts_per_Game', 'Punts_per_Play', 'Opponent_Punts_per_Play', 'Passing_Touchdown_Percentage', 'Offensive_Point_Share_Percentage_(Estimated)', 'Rushing_Yards_per_Game', 'Opponent_Passing_Play_Percentage', 'Opponent_Third_Down_Conversion_Percentage', 'Fourth_Down_Conversions_per_Game', 'Opponent_Third_Down_Conversions_per_Game', 'Passing_Yards_Percentage', 'Opponent_Field_Goal_Conversion_Percentage_(Net_of_Blocks)', 'Sacks_per_Game', 'Fumbles_per_Game', 'Opponent_Pass_Attempts_per_Game', 'Defensive_Touchdowns_per_Game', 'Interceptions_Thrown_Percentage', 'Passing_Play_Percentage', 'Third_Down_Conversion_Percentage', 'Pass_Attempts_per_Game', 'Opponent_Red_Zone_Scores_per_Game_(TDs_only)', 'Yards_per_Point_Margin', 'Points_per_Play', '1st_Half_Time_of_Possession_Share_%', 'Passing_First_Down_Percentage', 'Opponent_Yards_per_Pass_Attempt', 'Opponent_Rushing_Yards_Percentage', 'Interceptions_Thrown_per_Game', 'Opponent_Net_Yards_per_Punt_Attempt', 'Opponent_Rushing_First_Down_Percentage', 'Opponent_Extra_Point_Conversion_Percentage', 'Field_Goal_Attempts_per_Game', 'Defensive_Points_per_Game_(Estimated)', 'Fumble_Recovery_Percentage', 'Offensive_Points_per_Game_(Estimated)', 'Opponent_Completion_Percentage', 'Overtime_Points_Game', 'Turnover_Margin_per_Game', '1st_Quarter_Time_of_Possession_Share_%', 'Yards_per_Game', 'Fumbles_Not_Lost_per_Game', 'Field_Goal_Conversion_Percentage', 'Opponent_Fourth_Down_Conversions_per_Game', '2nd_Quarter_Points_Game', 'Yards_per_Point', 'Offensive_Touchdowns_per_Game', 'Penalties_per_Play', '1st_Quarter_Points_Game', 'Fourth_Downs_per_Game', 'Opponent_Gross_Punt_Yards_per_Game', 'Opponent_Giveaway_Fumble_Recovery_Percentage', 'Opponent_Fumbles_Lost_per_Game', 'Field_Goals_Made_per_Game', 'Average_Team_Passer_Rating', 'Opponent_Passing_First_Down_Percentage', 'Opponent_Defensive_Points_per_Game_(Estimated)', 'Rushing_Touchdown_Percentage', 'Takeaway_Fumble_Recovery_Percentage', '2nd_Quarter_Time_of_Possession_Share_%', 'Opponent_Net_Punt_Yards_per_Game', 'Rushing_First_Down_Percentage', 'Opp_2nd_Quarter_Points_Game', 'Opponent_Rushing_Attempts_per_Game', 'Opponent_Yards_per_Play', 'QB_Sacked_per_Game', 'Passing_Touchdowns_per_Game', 'Opp_4th_Quarter_Points_Game', 'Opponent_Points_per_Field_Goal_Attempt', 'Opponent_Fumble_Recovery_Percentage', 'Opponent_Rushing_Touchdowns_per_Game', 'Net_Yards_per_Successful_Punt', 'Kickoff_Touchback_Percentage', 'Opponent_Touchbacks_per_Game', 'Field_Goals_Got_Blocked_per_Game', 'Opponent_Two_Point_Conversions_per_Game', 'Opponent_Yards_per_Completion', 'First_Downs_per_Play', 'Opponent_Passing_Yards_Percentage', 'Penalty_First_Downs_per_Game', 'Takeaways_per_Game', 'Opponent_Plays_per_Game', 'Block_Field_Goal_Percentage', 'Rushing_Touchdowns_per_Game', 'Safeties_per_Game', 'Rushing_Yards_Percentage', 'Incompletions_per_Game', 'Opponent_Red_Zone_Scoring_Percentage_(TD_only)', 'Penalty_Yards_per_Game', 'Opponent_Passing_Yards_per_Game', 'Extra_Point_Conversion_Percentage', 'Opponent_Gross_Yards_per_Successful_Punt', 'Yards_per_Completion', 'Opponent_Yards_per_Rush_Attempt', 'Block_Punt_Percentage', 'Passing_First_Downs_per_Game', 'Opponent_Rushing_Yards_per_Game', 'Touchbacks_per_Game', 'Opponent_Fumbles_Not_Lost_per_Game', 'Opponent_Passing_Touchdown_Percentage', 'Opponent_Points_per_Game', 'Opponent_Passing_First_Downs_per_Game', 'Gross_Punt_Yards_per_Game', 'Two_Point_Conversion_Attempts_per_Game', 'Opponent_Average_Team_Passer_Rating', 'Opponent_Field_Goal_Conversion_Percentage', 'Opponent_First_Downs_per_Game', 'Extra_Point_Attempts_per_Game', 'Punt_Attempts_per_Game', 'Opponent_Kickoff_Touchback_Percentage', 'Punts_per_Offensive_Score', 'Third_Downs_per_Game', 'Sack_Percentage', 'Opponent_Interceptions_Thrown_per_Game', 'Opponent_Penalty_First_Downs_per_Game', 'Opponent_Yards_per_Game', 'Opponent_Incompletions_per_Game', 'Giveaway_Fumble_Recovery_Percentage', 'Opponent_Field_Goals_Made_per_Game', 'Opponent_Net_Yards_per_Successful_Punt', 'Opponent_Extra_Point_Attempts_per_Game', 'Opponent_Points_per_Play', 'Gross_Yards_per_Successful_Punt', 'Fourth_Down_Conversion_Percentage', 'Opponent_Rushing_Play_Percentage', 'Opponent_Fourth_Downs_per_Game', 'Opponent_Offensive_Touchdowns_per_Game', 'Opponent_Non-Offensive_Touchdowns_per_Game', 'Opponent_Time_of_Possession_Percentage_(Net_of_OT)', 'Opp_3rd_Quarter_Points_Game', 'Opponent_Red_Zone_Scoring_Attempts_per_Game', 'Non-Offensive_Touchdowns_per_Game', 'Yards_per_Rush_Attempt', 'Completions_per_Game', 'Net_Yards_per_Punt_Attempt', 'Time_of_Possession_Percentage_(Net_of_OT)', 'Opponent_Fourth_Down_Conversion_Percentage', 'Penalty_Yards_per_Penalty', 'Opponent_Passing_Touchdowns_per_Game', 'Opponent_Punt_Attempts_per_Game', 'Points_per_Field_Goal_Attempt', 'Opponent_Safeties_per_Game', 'Special_Teams_Points_per_Game_(Estimated)', '1st_Half_Points_Game', 'Rushing_First_Downs_per_Game', 'Two_Point_Conversion_Percentage', 'Opponent_Kickofs_per_Game', 'Opponent_Defensive_Touchdowns_per_Game', 'Opponent_First_Downs_per_Play', 'Opp_1st_Quarter_Points_Game', 'Plays_per_Game', 'Opponent_Offensive_Point_Share_Percentage_(Estimated)', 'Opponent_Third_Downs_per_Game', 'Punts_Blocked_per_Game', 'First_Downs_per_Game', 'Opp_Yards_per_Point', 'Opp_Overtime_Points_Game', 'Field_Goals_Blocked_per_Game', 'Completion_Percentage', '4th_Quarter_Points_Game', 'Opponent_Penalty_Yards_per_Game', 'Passing_Yards_per_Game', '3rd_Quarter_Points_Game', 'Opponent_1st_Half_Points_Game', 'Two_Point_Conversions_per_Game', '2nd_Half_Points_Game', 'Points_per_Game', 'Touchdowns_per_Game', 'Opponent_Penalty_Yards_per_Penalty', 'Opponent_Penalties_per_Game', 'Extra_Points_Made_per_Game', 'Opponent_Average_Time_of_Possession_(Net_of_OT)', 'Opponent_Offensive_Points_per_Game_(Estimated)', 'Opponent_Rushing_Touchdown_Percentage', 'Net_Punt_Yards_per_Game', 'Opponent_Touchdowns_per_Game', 'Opponent_Special_Teams_Touchdowns_per_Game', 'Kickoffs_per_Game', 'Opponent_Fumbles_per_Game', 'Penalties_per_Game', 'Field_Goal_Conversion_Percentage_(Excluding_Blocks)']
		

		nameDict = {"ARI": "Arizona", "ATL": "Atlanta", "BAL": "Baltimore", "BUF": "Buffalo", "CAR": "Carolina", "CHI": "Chicago", "CIN": "Cincinnati", "CLE": "Cleveland", "DAL": "Dallas", "DEN": "Denver", "DET": "Detriot", "GB": "Green Bay", "HOU": "Houston", "IND": "Indianapolis", "JAX": "Jacksonville", "KC": "Kansas City", "MIA": "Miami", "MIN": "Minnesota", "NYG": "NY Giants", "NYJ": "NY Jets", "NE": "New England", "NO": "New Orleans", "OAK": "Oakland", "PHI": "Philadelphia", "PIT": "Pittsburgh", "SD": "San Diego", "SF": "San Fransisco", "SEA": "Seattle", "STL": "St Louis", "TB": "Tampa Bay", "TEN": "Tennessee", "WSH": "Washington"}
		team1Var1, team2Var1 = 0, 0
		team1Var2, team2Var2 = 0, 0
		team1Var3, team2Var3 = 0, 0


		bitList = self.getBitList()
		xString = bitList[:8]
		yString = bitList[8:16]
		zString = bitList[16:24]
		logicalGroupingString = bitList[24:27]
		greaterLessString = bitList[27:30]


		xValue = int("".join(xString), 2)
		yValue = int("".join(yString), 2)
		zValue = int("".join(zString), 2)

		# print xValue, yValue, zValue
		logicalGroupingDecimal = int("".join(logicalGroupingString), 2)
		greaterLessDecimal = int("".join(greaterLessString), 2)

		# weeks = ["2003-17.txt", "2004-17.txt", "2005-17.txt", "2006-17.txt", "2007-17.txt", "2008-17.txt", "2009-17.txt", "2010-17.txt", "2011-17.txt", "2012-17.txt", "2013-17.txt"]#, \
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
		
		for m in range(len(weeks)):

			with open("/Users/lselig/Desktop/footballProject2.0/schedules/" + weeks[m], "r") as scheduleFile:
				scheduleLines = scheduleFile.readlines()
				for i in range(1, len(scheduleLines)):
					line = scheduleLines[i].split(",")
					team1Abrv = line[0].split()[0]
					team2Abrv = line[1].split()[0]
					team1Score = int(line[0].split()[1])
					team2Score = int(line[1].split()[1])
					with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + statIDs[xValue] + ".csv") as xCSV:
						xCSVLines = xCSV.readlines()
						for j in range(1, len(xCSVLines)):
							teamLine = xCSVLines[j].split(",")
							if(teamLine[0] == nameDict[team1Abrv]):
								team1Var1 = formatVar(teamLine[columns[m]])

							elif(teamLine[0] == nameDict[team2Abrv]):
								team2Var1 = formatVar(teamLine[columns[m]])
								
					with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + statIDs[yValue] + ".csv") as yCSV:
						yCSVLines = yCSV.readlines()
						for k in range(1, len(yCSVLines)):
							teamLine = yCSVLines[k].split(",")
							if(teamLine[0] == nameDict[team1Abrv]):
								team1Var2 = formatVar(teamLine[columns[m]])
								
							elif(teamLine[0] == nameDict[team2Abrv]):
								team2Var2 = formatVar(teamLine[columns[m]])
								


					with open("/Users/lselig/Desktop/footballProject2.0/csvFiles/" + statIDs[zValue] + ".csv") as zCSV:
						zCSVLines = zCSV.readlines()
						for l in range(1, len(zCSVLines)):
							teamLine = zCSVLines[l].split(",")
							if(teamLine[0] == nameDict[team1Abrv]):
								team1Var3 = formatVar(teamLine[columns[m]])
								
							elif(teamLine[0] == nameDict[team2Abrv]):
								team2Var3 = formatVar(teamLine[columns[m]])
								


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

def mutate(bitList, mutationRate):
	for i in range(len(bitList)): # loop over each index of the new child's bitstring
		if(random.uniform(0, 1) < mutationRate): #mutate the index with propability .001
			if(bitList[i] == "0"):
				bitList[i] = "1"
			else:
				bitList[i] = "0"
		while(int("".join(bitList[0:8]), 2) > 210 or (int("".join(bitList[8:16]), 2) > 210) or (int("".join(bitList[16:24]), 2) > 210)):
			for i in range(len(bitList)): # loop over each index of the new child's bitstring
				if(random.uniform(0, 1) < mutationRate): #mutate the index with propability .001
					if(bitList[i] == "0"):
						bitList[i] = "1"
					else:
						bitList[i] = "0"

	return bitList