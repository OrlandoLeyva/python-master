# params are variables that functions receive when the are called.

'''
def validateEmail(email: str):
    validating email...
'''

'''
when you call a function you can send values as arguments.
validateEmail('myEmail.com')
'''

currentEmail = 'email.com'

# if then you call the function you forgot to send the param, python won't trow any error util the execution time.
def validateEmail(email: str):
    if not email == currentEmail:
        return False
    else: 
        return True

def changeEmail(newEmail: str):
    currentEmail = newEmail
