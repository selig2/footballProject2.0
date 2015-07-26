from individual import *


def geneticAlgorithm(popSize, stringLen, crossOverRate, mutationRate, generations):
	# 211 stats
	gen1 = []
	# weeks = ["2003-17.txt", "2004-17.txt", "2005-17.txt", "2006-17.txt", "2007-17.txt", "2008-17.txt", "2009-17.txt", "2010-17.txt", "2011-17.txt", "2012-17.txt", "2013-17.txt"]
	weeks = ["2010-2.txt", "2010-3.txt", "2010-4.txt", "2010-5.txt", "2010-6.txt", "2010-7.txt", "2010-8.txt", "2010-9.txt",\
			"2010-10.txt", "2010-11.txt", "2010-12.txt", "2010-13.txt", "2010-14.txt", "2010-15.txt", "2010-16.txt", "2010-17.txt",\
			 "2011-2.txt", "2011-3.txt", "2011-4.txt", "2011-5.txt", "2011-6.txt", "2011-7.txt", "2011-8.txt", "2011-9.txt",\
			"2011-10.txt", "2011-11.txt", "2011-12.txt", "2011-13.txt", "2011-14.txt", "2011-15.txt", "2011-16.txt", "2011-17.txt",\
			 "2012-2.txt", "2012-3.txt", "2012-4.txt", "2012-5.txt", "2012-6.txt", "2012-7.txt", "2012-8.txt", "2012-9.txt",\
			"2012-10.txt", "2012-11.txt", "2012-12.txt", "2012-13.txt", "2012-14.txt", "2012-15.txt", "2012-16.txt", "2012-17.txt",\
			 "2013-2.txt", "2013-3.txt", "2013-4.txt", "2013-5.txt", "2013-6.txt", "2013-7.txt", "2013-8.txt", "2013-9.txt",\
			"2013-10.txt", "2013-11.txt", "2013-12.txt", "2013-13.txt", "2013-14.txt", "2013-15.txt", "2013-16.txt", "2013-17.txt"]
	# columns = [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320]
	columns = range(1, 65) 
	for i in range(popSize): #loop over all individualas
		indvBitList = []
		print "SETTING UP BITLISTS", " -- ", i
		for j in range(stringLen): # set up their bit string
			if(random.uniform(0,1) < .5):
				indvBitList.append("0")
			else:
				indvBitList.append("1")
		while(int("".join(indvBitList[0:8]), 2) > 210 or (int("".join(indvBitList[8:16]), 2) > 210) or (int("".join(indvBitList[16:24]), 2) > 210)):
			indvBitList = []
			print "SETTING UP BITLISTS", " -- ", i
			for k in range(stringLen): # set up their bit string
				if(random.uniform(0,1) < .5):
					indvBitList.append("0")
				else:
					indvBitList.append("1")

		x = individual(indvBitList)
		gen1.append((x, x.getFitness(weeks, columns), x.getLogicalGroupingString(), x.getGreaterLessString(), x.getStat1(), x.getStat2(), x.getStat3()))

 
	gen1 = sorted(gen1, reverse=True, key=getKey) # sort by fitness values

	 
	previousGen = gen1
	numGenerations = 0
	for i in range(generations):
		previousGen[popSize-1] = previousGen[0] #delete the worst and replace it with the best
		# print "\n\n"
		# print previousGen
		print "WORKING ON GENERATION:", i
		nextGen = []
		for j in range(popSize):
			parent1 = previousGen[random.randint(0, popSize-1)][0] # 0 <= x <= popSize-1
			parent2 = previousGen[random.randint(0, popSize-1)][0]
			while(parent2 == parent1):
				parent2 = previousGen[random.randint(0, popSize-1)][0]

			if(random.uniform(0,1) < crossOverRate): # perform crossover 60 percent of the time
				randomCutoffPoint = random.randint(0, stringLen-2) # stringLen-2 or stringLen-1
				childBitList = parent1.getBitList()[0:randomCutoffPoint] + parent2.getBitList()[randomCutoffPoint:]

				while(int("".join(childBitList[0:8]), 2) > 210 or (int("".join(childBitList[8:16]), 2) > 210) or (int("".join(childBitList[16:24]), 2) > 210)):
					randomCutoffPoint = random.randint(0, stringLen-2) # stringLen-2 or stringLen-1
					childBitList = parent1.getBitList()[0:randomCutoffPoint] + parent2.getBitList()[randomCutoffPoint:]

				mutate(childBitList, mutationRate)
				newChild = individual(childBitList)
				nextGen.append((newChild, newChild.getFitness(weeks, columns), newChild.getLogicalGroupingString(), newChild.getGreaterLessString(), newChild.getStat1(), newChild.getStat2(), newChild.getStat3()))

			else:
				if(parent1.getFitness(weeks, columns) > parent2.getFitness(weeks, columns)):
					mutate(parent1.getBitList(), mutationRate)
					nextGen.append((parent1, parent1.getFitness(weeks, columns), parent1.getLogicalGroupingString(), parent1.getGreaterLessString(), parent1.getStat1(), parent1.getStat2(), parent1.getStat3()))

				else:
					mutate(parent2.getBitList(), mutationRate)
					nextGen.append((parent2, parent2.getFitness(weeks, columns), parent2.getLogicalGroupingString(), parent2.getGreaterLessString(), parent2.getStat1(), parent2.getStat2(), parent2.getStat3()))
		nextGen = sorted(nextGen, reverse=True, key=getKey) # sort by fitness values
		for indiv in nextGen:
			print "Fitness:", indiv[1], "  ||  Logical Code: ", indiv[2], "  ||  Greater / Less Code:", indiv[3], "  ||  Stat 1", indiv[4], "  ||  Stat 2", indiv[5], "  ||  Stat 3", indiv[6]
		previousGen = nextGen

		

	
	print "--------------------------------------------"
	print "Number of Generations:", generations







# (popSize, stringLen, crossOverRate, mutationRate, generations)
print geneticAlgorithm(50, 30, .50, .001, 25)
