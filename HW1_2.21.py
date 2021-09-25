
accountbnal = 100 # set the initial account balance
interest = 1.05 # set the interest rate for the account
months = 6 # set the number of months
totalmonth = months-1 # remove the end month from being factored in
final = (accountbnal*interest) # calculate the balance with the interest
for i in range(totalmonth): # for each month, add 5% interest
    final *= 1.05
print(int(final))# print result
    
