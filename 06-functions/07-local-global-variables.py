'''
global variables: are the ones declared outside the function and you can access to it everywhere.

local variables: are defined within a function and you can access to it outside the function.
'''

# Global variables:

secretKey = 'secret'

def getKey(newKey):
    # This is a different variable than the global variable available only within the function.
    # You have access to the global variables within a function but if you create a variable with the same than the global variable the local one takes precedence.* 
    secretKey = newKey

    # you can convert local variables into global variables:
    # you have globally access to it only if have run the function that declares it.
    global site
    site = 'carsverse.com'

# here you first run the function. This function creates the variable and defines it as global.
getKey('new key')
# then, you have access to it globally.
print(site)

# in conclusion, If you want to globally use local variables created within a function you can use the reserved word 'global' and through comma separated define all the local variables you want to declare as global.