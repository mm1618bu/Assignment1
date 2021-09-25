# Population 312,032,486
# Days a year 365
# 84600 seconds a day = 31,557,600 a year


#One birth every 7 seconds (7/60 = 0.1166)
#one death every 13 seconds (13/60 = 0.2166)
# One imigrant every 45 seconds (45/60 = 0.75)

#This section will determine the inital variables
yrs = int(input("Enter the number of years: ")) # How many years are in the time period we are evaluating
population = 312032486
seconds = 31557600
birthrate = 7/60
deathrate = 13/60
immigratrate = 45/60
year = 365

born = (yrs*seconds) * birthrate #Determine the number of people born
die = (yrs*seconds) * deathrate # Determine the number of people who died
imigrate = (yrs*seconds) * immigratrate #Determine the number of people who immigrated

final = population + born - die + immigratrate  #take current population, and births, remove deaths, add immigrants and determine total
print("The population in ",yrs," years is: ",int(final)) # print the total population and time span
