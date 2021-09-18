********NEED TO REDO*******

def revers(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    print(rev)
revers(2345)
    
