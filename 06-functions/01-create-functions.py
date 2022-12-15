# To create a function you got to utilize the reserved word def:

'''
def functionName(param):
    instructions
'''

# function are used to define a piece of code which you can use wherever you want throughout the app

password = 'password'
email = 'example@main.com'

# validate the password and the email of the user
def validateCredentials(sentPassword: str, sentEmail: str):
    if sentEmail == email:
        if sentPassword == password:
            return True
        else:
            return False
    else:
        return False

userEmail = input('Insert your email: ')
userPassword = input('Insert your password: ')

if validateCredentials(userPassword, userEmail):
    print('welcome aboard')
else:
    print('incorrect email or password')