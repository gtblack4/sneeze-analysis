import csv
import os
from datetime import datetime
import datefinder
from collections import Counter
dateFormat = "%I:%M %p %m/%d/%Y"
timeFormat = "%H:%M"
dayFormat = "%m/%d/%y"

def working_days(start_dt,end_dt):
    num_days = (end_dt -start_dt).days +1
    num_weeks =(num_days)//7
    a=0
    #condition 1
    if end_dt.strftime('%a')=='Sat':
        if start_dt.strftime('%a') != 'Sun':
            a= 1
    #condition 2
    if start_dt.strftime('%a')=='Sun':
        if end_dt.strftime('%a') !='Sat':
            a =1
    #condition 3
    if end_dt.strftime('%a')=='Sun':
        if start_dt.strftime('%a') not in ('Mon','Sun'):
            a =2
    #condition 4        
    if start_dt.weekday() not in (0,6):
        if (start_dt.weekday() -end_dt.weekday()) >=2:
            a =2
    working_days =num_days -(num_weeks*2)-a

    return working_days

def sneezeCount(sneezeData):
	sneezeSum = 0
	for row in sneezeData:
		sneezeSum += int(row[0])
	print('The total number of sneezes since {} is {}'.format(sneezeData[0][2],sneezeSum))

def sneeziestDay(sneezeData):
	daySum = 0
	maxSneeze = [int(),'']
	for row in range(0,len(sneezeData)):
		if(sneezeData[row][2]!= sneezeData[row-1][2]):
			if(int(daySum)>=int(maxSneeze[0])):
				maxSneeze = daySum,sneezeData[row-1][2]
			daySum = int(sneezeData[row][0])
		else:
			daySum += int(sneezeData[row][0])
			if(int(daySum)>=int(maxSneeze[0])):
				maxSneeze = daySum,sneezeData[row-1][2]
		prevRow = row
	print('{} had the most sneezes at {}'.format(maxSneeze[1],maxSneeze[0]))

def	sneezeDailyCount(sneezeData):
	daySum = 0
	maxSneeze = [int(),'']
	count = []
	for row in range(0,len(sneezeData)):
		if(sneezeData[row][2]!= sneezeData[row-1][2]):
			count.append(daySum)
			daySum = int(sneezeData[row][0])
			
		else:
			daySum += int(sneezeData[row][0])
			#count.append(daySum)
			
		prevRow = row
	print(Counter(count))
	print(len(count))
def sneeziestWeek(sneezeData):
	weekSum = 0
	weekMax = [0,'']
	for row in range(0 ,len(sneezeData)):
		if(sneezeData[row][3]==sneezeData[row-1][3]):
			weekSum += int(sneezeData[row][0])
		if(sneezeData[row][3]!=sneezeData[row-1][3]):
			weekSum = int(sneezeData[row][0])			
		if(int(weekSum) > int(weekMax[0])):
			weekMax = weekSum,sneezeData[row-1][3],format(datetime.strptime(str(sneezeData[row-1][2]),dayFormat),"%Y")
	#weekthin = format(weekMax[1],"%u")
	maxWeekStart = weekMax[2],weekMax[1]-1
	monday = format(datetime.strptime(str(maxWeekStart) + '-1',"('%Y', %W)-%w"),dayFormat)
	print("The week of {} had the most sneezes at {}".format(monday,weekMax[0]))

def sneeziestMonth(sneezeData):
	weekSum = 0
	weekMax = [0,'']
	for row in range(0 ,len(sneezeData)):

		if(sneezeData[row][2].split('/')[0]==sneezeData[row-1][2].split('/')[0]):
			weekSum += int(sneezeData[row][0])
		if(sneezeData[row][2].split('/')[0]!=sneezeData[row-1][2].split('/')[0]):
			weekSum = int(sneezeData[row][0])			
		if(int(weekSum) > int(weekMax[0])):
			weekMax = weekSum,datetime.strftime(datetime(1900,int(sneezeData[row][2].split('/')[0]),1),"%B")
	print("The month of {} had the most sneezes at {}".format(weekMax[1],weekMax[0]))

def sneezeFits(sneezeData):
	breakDown = sneezeHourly(sneezeData)
	totalSneeze = 0
	modeSneeze = []
	mode = 0
	for row in sneezeData:
		totalSneeze += int(row[0])
		modeSneeze.append(row[0])
	mode = Counter(modeSneeze).most_common(1)
	totalFit = len(sneezeData)
	mode = str(mode[0]).split()[0].strip("(),'"),str(mode[0]).split()[1].strip("()")
	fitAverage = totalSneeze/int(len(sneezeData))
	print("There have been {} sneezing fits averaging {} a session".format(int(len(sneezeData)),round(fitAverage,2)))
	print("The most common number of sneezes in a fit is {} occuring {} times".format(mode[0],mode[1]))
	print(breakDown)
	formatBreakdown = [breakDown[0],round(int(breakDown[0])/totalFit*100,2),
	breakDown[1],round(int(breakDown[1])/totalFit*100,2),
	breakDown[2],round(int(breakDown[2])/totalFit*100,2),
	breakDown[3],round(int(breakDown[3])/totalFit*100,2)]
	print(formatBreakdown)
	print("{0}({1}%) Sneezing fits occured between 10:00PM and 6:00AM. {2}({3}%) Sneezing fits occured between 6:00AM and 12:00PM. {4}({5}%) Sneezing fits occured in Between 12:00PM and 4:00PM. {6}({7}%) Sneezing Fits occured between 4:00PM and 10:00PM".format(formatBreakdown[0],formatBreakdown[1],formatBreakdown[2],formatBreakdown[3],formatBreakdown[4],formatBreakdown[5],formatBreakdown[6],formatBreakdown[7]))
	

	

def sneezeHourly(sneezeData):
	breakDown = [0,0,0,0]
	for row in sneezeData:
		if(row[1] < '05:00'):
			breakDown[0] += 1
		elif(row[1] >= '05:00' and row[1] <= '11:00'):
			breakDown[1] += 1
		elif(row[1] > '11:00' and row[1] <= '17:00'):
			breakDown[2] += 1
		elif(row[1] > '17:00' and row[1] <= '23:00'):
			breakDown[3] += 1	
		elif(row[1] > '23:00'):
			breakDown[0] += 1	
	return breakDown

def sneezeLessDays(sneezeData):
	startDate = datetime.strptime(sneezeData[0][2],dayFormat)
	endDate = datetime.strptime(sneezeData[len(sneezeData)-1][2],dayFormat)
	workingDays = working_days(startDate,endDate)
	sneezeDays = []
	numDays = 0
	for row in sneezeData:
		sneezeDays.append(row[2])
	sneezeDays = Counter(sneezeDays)
	for x in sneezeDays:
		numDays +=1
	
	realPercent = round(numDays / 365,3)*100
	percentDays = round(100-(int(numDays)/int(365)*100),2)
	sneezePercent = round((int(numDays)/int(365)*100),2)
	sneezelessday = 365- numDays
	
	print("There have been 365 days since 1/1/20, and {}({}%) days have had sneezes. Which means there are {}({}%) sneezeless days".format(numDays,sneezePercent,int(sneezelessday),percentDays))

with open(os.path.join('C:\\Users\\Gage\\Downloads\\sneezeAnalysis-master\\sneezeAnalysis-master','Sneezes.txt')) as csvFile:
	sneezeCSV = csv.reader(csvFile, delimiter=',')
	sneezeArray = []
	for row in sneezeCSV:
		dateData = row[1]
		dateData = datetime.strptime(dateData,dateFormat)
		time = format(dateData,timeFormat)
		date = format(dateData,dayFormat)
		week = datetime.strptime(date,dayFormat).isocalendar()[1]
		appendthis = row[0],time,date,week
		sneezeArray.append(appendthis)




sneezeCount(sneezeArray)
sneezeFits(sneezeArray)
sneeziestDay(sneezeArray)
sneeziestWeek(sneezeArray)
sneeziestMonth(sneezeArray)
sneezeHourly(sneezeArray)
sneezeLessDays(sneezeArray)
sneezeDailyCount(sneezeArray)


