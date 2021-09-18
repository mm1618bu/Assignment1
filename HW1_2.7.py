def calculateTime():
    minutes = int(input("Number of minutes"))
    years = float(minutes/525600)
    days = (float(years)-(int(years)))*365
    print('\n',minutes,'minutes is approximently',int(years),'and',int(days),'days')
    
calculateTime()
