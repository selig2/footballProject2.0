from bs4 import BeautifulSoup
import requests

def getSchedule(address, outFile):
	response = requests.get(address)
	html = response.text
	soup = BeautifulSoup(html)
	tableBody = soup.tbody
	trTags = soup.find_all("td")
	captions = soup.find_all("caption")
	earliestDate = captions[0].get_text().split(",")[1].strip()#take the text from the first caption, split it on comma, take the second one, split it on whitespace, 
	with open(outFile, "w+") as file:
		file.write(earliestDate + "\n")
		for i in range(2, len(trTags), 6):
			score = str(trTags[i].get_text())
			file.write(score + "\n")

for i in range(2003, 2015): # for years 2003 through 2014
	for j in range(1, 18): # for weeks 1 through 17
		getSchedule("http://espn.go.com/nfl/schedule/_/year/" + str(i) + "/week/" + str(j), "/Users/lselig/Desktop/pythonProjects/sideProjects/footballPredictor/schedules/" + str(i) + "-" + str(j) + ".txt")


