accountbnal = 100
interest = 1.05
months = 6
totalmonth = months-1
final = (accountbnal*interest)
for i in range(totalmonth):
    final *= 1.05
print(int(final))
    
