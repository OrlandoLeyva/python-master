# optional params are params that is not obligatory. you can send them or not.
# to define an optional param you got to assign a default values, take a look at the following example

#In this part of the course I am having a little problem with the scope of the variables. It seems that i can't redefine its values within my function. as I keep learning i'm sure I will be able to find the solution. I'll be back when It happens. I hope to remember it.

'''
userEmail = ''
userPassword = ''
userPhone = ''

def registerUser(email: str, password: str, phone = 'null'):
    userEmail = email
    userPassword = password
    userPhone = phone

registerUser('usermail.com', 'user123')

print(f'email = {userEmail} \n password = {userPassword} \n phone = {userPhone}')
'''

# It seems  i've found the solution.

def registerUser(email: str, password: str, phone = 'null'):
    global userEmail, userPassword, userPhone
    userEmail = email
    userPassword = password
    userPhone = phone

registerUser('usermail.com', 'user123')

# print(f'email = {userEmail} \n password = {userPassword} \n phone = {userPhone}')

