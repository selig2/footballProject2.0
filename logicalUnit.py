def cond1(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return (actualPPPValue < proposedPPPValue or ((actualNSValue < proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 1):
		return (actualPPPValue < proposedPPPValue or ((actualNSValue < proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG)))
	elif(greaterLessDecimal == 2):
		return (actualPPPValue < proposedPPPValue or ((actualNSValue >= proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 3):
		return (actualPPPValue < proposedPPPValue or ((actualNSValue >= proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG)))
	elif(greaterLessDecimal == 4):
		return (actualPPPValue >= proposedPPPValue or ((actualNSValue < proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 5):
		return (actualPPPValue >= proposedPPPValue or ((actualNSValue >= proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG)))
	elif(greaterLessDecimal == 6):
		return (actualPPPValue >= proposedPPPValue or ((actualNSValue >= proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 7):
		return (actualPPPValue >= proposedPPPValue or ((actualNSValue < proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG)))

def cond2(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return (actualPPPValue < proposedPPPValue and ((actualNSValue < proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 1):
		return (actualPPPValue < proposedPPPValue and ((actualNSValue < proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG)))
	elif(greaterLessDecimal == 2):
		return (actualPPPValue < proposedPPPValue and ((actualNSValue >= proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 3):
		return (actualPPPValue < proposedPPPValue and ((actualNSValue >= proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG)))
	elif(greaterLessDecimal == 4):
		return (actualPPPValue >= proposedPPPValue and ((actualNSValue < proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 5):
		return (actualPPPValue >= proposedPPPValue and ((actualNSValue >= proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG)))
	elif(greaterLessDecimal == 6):
		return (actualPPPValue >= proposedPPPValue and ((actualNSValue >= proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG)))
	elif(greaterLessDecimal == 7):
		return (actualPPPValue >= proposedPPPValue and ((actualNSValue < proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG)))

def cond3(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return ((actualPPPValue < proposedPPPValue or (actualNSValue < proposedNSValue)) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 1):
		return ((actualPPPValue < proposedPPPValue or (actualNSValue < proposedNSValue)) and (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 2):
		return ((actualPPPValue < proposedPPPValue or (actualNSValue >= proposedNSValue)) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 3):
		return ((actualPPPValue < proposedPPPValue or (actualNSValue >= proposedNSValue)) and (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 4):
		return ((actualPPPValue >= proposedPPPValue or (actualNSValue < proposedNSValue)) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 5):
		return ((actualPPPValue >= proposedPPPValue or (actualNSValue >= proposedNSValue)) and (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 6):
		return ((actualPPPValue >= proposedPPPValue or (actualNSValue >= proposedNSValue)) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 7):
		return ((actualPPPValue >= proposedPPPValue or (actualNSValue < proposedNSValue)) and (actualOPPYPGValue >= proposedOPPYPG))

def cond4(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return ((actualPPPValue < proposedPPPValue and (actualNSValue < proposedNSValue)) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 1):
		return ((actualPPPValue < proposedPPPValue and (actualNSValue < proposedNSValue)) or (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 2):
		return ((actualPPPValue < proposedPPPValue and (actualNSValue >= proposedNSValue)) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 3):
		return ((actualPPPValue < proposedPPPValue and (actualNSValue >= proposedNSValue)) or (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 4):
		return ((actualPPPValue >= proposedPPPValue and (actualNSValue < proposedNSValue)) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 5):
		return ((actualPPPValue >= proposedPPPValue and (actualNSValue >= proposedNSValue)) or (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 6):
		return ((actualPPPValue >= proposedPPPValue and (actualNSValue >= proposedNSValue)) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 7):
		return ((actualPPPValue >= proposedPPPValue and (actualNSValue < proposedNSValue)) or (actualOPPYPGValue >= proposedOPPYPG))

def cond5(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return ((actualPPPValue < proposedPPPValue or (actualOPPYPGValue < proposedOPPYPG)) and (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 1):
		return ((actualPPPValue < proposedPPPValue or (actualOPPYPGValue < proposedOPPYPG)) and (actualNSValue >= proposedNSValue))
	elif(greaterLessDecimal == 2):
		return ((actualPPPValue < proposedPPPValue or (actualOPPYPGValue >= proposedOPPYPG)) and (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 3):
		return ((actualPPPValue < proposedPPPValue or (actualOPPYPGValue >= proposedOPPYPG)) and (actualNSValue >= proposedNSValue))
	elif(greaterLessDecimal == 4):
		return ((actualPPPValue >= proposedPPPValue or (actualOPPYPGValue < proposedOPPYPG)) and (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 5):
		return ((actualPPPValue >= proposedPPPValue or (actualOPPYPGValue >= proposedOPPYPG)) and (actualNSValue >= proposedNSValue))
	elif(greaterLessDecimal == 6):
		return ((actualPPPValue >= proposedPPPValue or (actualOPPYPGValue >= proposedOPPYPG)) and (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 7):
		return ((actualPPPValue >= proposedPPPValue or (actualOPPYPGValue < proposedOPPYPG)) and (actualNSValue >= proposedNSValue))

def cond6(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return ((actualPPPValue < proposedPPPValue and (actualOPPYPGValue < proposedOPPYPG)) or (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 1):
		return ((actualPPPValue < proposedPPPValue and (actualOPPYPGValue < proposedOPPYPG)) or (actualNSValue >= proposedNSValue))
	elif(greaterLessDecimal == 2):
		return ((actualPPPValue < proposedPPPValue and (actualOPPYPGValue >= proposedOPPYPG)) or (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 3):
		return ((actualPPPValue < proposedPPPValue and (actualOPPYPGValue >= proposedOPPYPG)) or (actualNSValue >= proposedNSValue))
	elif(greaterLessDecimal == 4):
		return ((actualPPPValue >= proposedPPPValue and (actualOPPYPGValue < proposedOPPYPG)) or (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 5):
		return ((actualPPPValue >= proposedPPPValue and (actualOPPYPGValue >= proposedOPPYPG)) or (actualNSValue >= proposedNSValue))
	elif(greaterLessDecimal == 6):
		return ((actualPPPValue >= proposedPPPValue and (actualOPPYPGValue >= proposedOPPYPG)) or (actualNSValue < proposedNSValue))
	elif(greaterLessDecimal == 7):
		return ((actualPPPValue >= proposedPPPValue and (actualOPPYPGValue < proposedOPPYPG)) or (actualNSValue >= proposedNSValue))
		
def cond7(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return (actualPPPValue < proposedPPPValue or (actualNSValue < proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 1):
		return (actualPPPValue < proposedPPPValue or (actualNSValue < proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 2):
		return (actualPPPValue < proposedPPPValue or (actualNSValue >= proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 3):
		return (actualPPPValue < proposedPPPValue or (actualNSValue >= proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 4):
		return (actualPPPValue >= proposedPPPValue or (actualNSValue < proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 5):
		return (actualPPPValue >= proposedPPPValue or (actualNSValue >= proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 6):
		return (actualPPPValue >= proposedPPPValue or (actualNSValue >= proposedNSValue) or (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 7):
		return (actualPPPValue >= proposedPPPValue or (actualNSValue < proposedNSValue) or (actualOPPYPGValue >= proposedOPPYPG))

def cond8(actualPPPValue, proposedPPPValue, actualNSValue, proposedNSValue, actualOPPYPGValue, proposedOPPYPG, greaterLessDecimal):
	if(greaterLessDecimal == 0):
		return (actualPPPValue < proposedPPPValue and (actualNSValue < proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 1):
		return (actualPPPValue < proposedPPPValue and (actualNSValue < proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 2):
		return (actualPPPValue < proposedPPPValue and (actualNSValue >= proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 3):
		return (actualPPPValue < proposedPPPValue and (actualNSValue >= proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 4):
		return (actualPPPValue >= proposedPPPValue and (actualNSValue < proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 5):
		return (actualPPPValue >= proposedPPPValue and (actualNSValue >= proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG))
	elif(greaterLessDecimal == 6):
		return (actualPPPValue >= proposedPPPValue and (actualNSValue >= proposedNSValue) and (actualOPPYPGValue < proposedOPPYPG))
	elif(greaterLessDecimal == 7):
		return (actualPPPValue >= proposedPPPValue and (actualNSValue < proposedNSValue) and (actualOPPYPGValue >= proposedOPPYPG))



def formatVar(cell):
	cell = cell.strip()
	if(cell[-1] == "%"):
		cell = float(cell[:-1])
	elif(":" in cell):
		cell = float(cell[:2]) + (float(cell[3:5]) / 60)
	elif("--" in cell):
		cell = 0
	return float(cell)