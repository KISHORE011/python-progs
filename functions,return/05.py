def findevenodd(b):
    if (b>=35 and b<=100):
        print(f'your mark is [ {a} ], and You are PASS')
    elif(b<35):
        print(f'your mark is [ {a} ], SORRY,You are FAIL')
    else:
        print('Enter your valid mark')
a=int(input('enter your mark: '))
findevenodd(a)

    
# o/p


#enter your mark: 105
#Enter your valid mark

#enter your mark: 15
#your mark is [ 15 ], SORRY,You are FAIL

#enter your mark: 35
#your mark is [ 35 ], and You are PASS

#enter your mark: 55
#your mark is [ 55 ], and You are PASS
