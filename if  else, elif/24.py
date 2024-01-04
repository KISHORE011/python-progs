n=int(input('enter the number 2 to 20: '))
if (n%2==0):
    if (n>=2 and n<=5):
        print('not weird')
    elif(n>=6 and n<=20):
        print('weird')
    elif(n>20):
        print('not weird')
else:
    print('weirdc')
