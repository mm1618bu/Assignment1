# Ask user for a number
enterNumber = input("Enter a number: ")
# set inital variable to zero
totalnum = 0
# for each integer, add 1
for integer in str(enterNumber):
    totalnum += int(integer)
    
print(totalnum)
