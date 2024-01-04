u_username='kishore'
p_password='1234'

uname=input('Enter Your username: ')
pword=input('Enter Your password: ')


def validate():
    if (u_username==uname and p_password==pword):
        print('correct')
    else:
        print('wrong')

validate()


