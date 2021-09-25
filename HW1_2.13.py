# define a function reverse that takes the parameter of the number to be reversed
def reverse(numb):
    #set revers, the initial value, to 0
    revers = 0
    # if the number put into the parameter is greater then 0, excecute the following
      while numb > 0:
            remain = numb % 10 #get the remainder for $remain
            revers = (revers * 10) + remain # add remainder to inital value
            numb = numb // 10
    print(revers) #print the result
reverse(2345)
