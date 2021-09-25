def calculateTime():
    minutes = int(input("Number of minutes"))
    years = float(minutes/525600) #input number of minutes and divide by number of minutes in a year
    days = (float(years)-(int(years)))*365 #subtract number of minutes and multiply by 365 days of the year
    print('\n',minutes,'minutes is approximently',int(years),'and',int(days),'days') #print result
    
calculateTime()
