salary = int(input('salary'))
age= int(input('age'))
if (salary>=20000 or age <=25):
    loan=int(input('loan amount: '))
    if (loan>50000):
        print ('sorry, max loan amount is 50000')
    else:
        print('you are elgible for loan')
else:
    print ("you are not elgible")
