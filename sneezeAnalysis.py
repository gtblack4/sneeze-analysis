import csv
import os
from datetime import datetime
import datefinder
import pandas as pd

def sneezeCount(sneezeData):
	sneezeSum = 0
	for row in sneezeData:
		sneezeSum += int(row[0])
	return sneezeSum

def numOfDays(sneezeData):
	days = []
	times = []
	dateTimes = []
	dateformat = " %I:%M %p %m/%d/%Y"
	dayformat = "%m/%d/%Y"
	for row in sneezeData:
		date = row[1]
		date = datetime.strptime(date,dateformat)
		date = format(date,dayformat)
		appendthis = row[0],date
		dateTimes.append(appendthis)
	prevDay = '10/08/2019'
	prevSneezeCount = 0
	totalDaySneezes = 0
	numberOfSneezingFits = 0
	mostSneezingFits = 0
	mostSneezes = 0
	mostSneezesArray = []


	for instance in dateTimes:
		if(instance[1] == prevDay):
			totalDaySneezes += int(instance[0])
		else:
			if(totalDaySneezes > mostSneezes):
				mostSneezes = totalDaySneezes
				mostSneezesArray = prevDay,mostSneezes
			prevSneezeCount = instance[0]
			totalDaySneezes = int(instance[0])

		prevDay = instance[1]
	
	return mostSneezesArray

def sneezeAvg(sneezeData,count):
	return int(count)/int(len(sneezeData))

def lunchTime(sneezeData):
	dateTimes = []
	dateformat = " %I:%M %p %m/%d/%Y"
	dayformat = "%H:%M"
	for row in sneezeData:
		date = row[1]
		date = datetime.strptime(date,dateformat)
		date = format(date,dayformat)
		appendthis = row[0],date
		dateTimes.append(appendthis)
	total = 0
	lunchCount = 0
	for timeStamp in dateTimes:
		total += int(timeStamp[0])
		if(timeStamp[1] >= '11:45' and timeStamp[1] <= '13:15'):
			lunchCount += int(timeStamp[0])
	return(lunchCount,'Sneezes occured during lunch hours(11:45-1:15) or',(lunchCount/total)*100,"percent")


with open(os.path.join('C:\\Users\\gblack\\Desktop','Sneezes.txt')) as csvFile:
	sneezeCSV = csv.reader(csvFile, delimiter=',')
	sneezeArray = []
	for row in sneezeCSV:
		sneezeArray.append(row)

def test():
	a ='foo'
	b = 'bar'
	print("es")
	return a,b

print("The Day with the most Sneezes", numOfDays(sneezeArray))
print(lunchTime(sneezeArray))
print("Total Number of Sneezes",sneezeCount(sneezeArray))
print("Daily Average Sneezes", sneezeAvg(sneezeArray,sneezeCount(sneezeArray)))







