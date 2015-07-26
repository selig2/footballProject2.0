import random, os
def randomizeLines(file):
	lines = 0
	with open(file, "r") as readFile:
		lines = readFile.readlines()
		for i in range(1, len(lines)):
			if(random.uniform(0, 1) < 0.5):
				line = lines[i].split(",")
				if(len(line) != 1):
					cell1 = line[0] + "\n"
					cell2 = line[1][:-1]
					newLine = cell2.strip() + ", " + cell1
					lines[i] = newLine
				
	with open(file, "w+") as writeFile:
		writeFile.writelines(lines)


for file in os.listdir("/Users/lselig/Desktop/footballProject2.0/schedules/"):
	randomizeLines("/Users/lselig/Desktop/footballProject2.0/schedules/" + file)