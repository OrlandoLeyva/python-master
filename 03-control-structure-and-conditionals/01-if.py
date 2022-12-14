# If works to define some instructions that will be run if some condition if fulfilled.

# The syntax to create an 'if' is the following:

# if <condition>:
    # instructions...

password = 'password'

answer = input('Do you want continue with the download? yes/y or no/n: ').lower()

if answer == 'yes' or answer == 'y':
    # asking for password to find out if the user is allowed to download package
    receivedPassword = input('type your password: ')
    if password == receivedPassword:
        print('downloading the resources...')
        print('done')
    # If the password if wrong we let them know and ask again.
    else:
        receivedPassword = input('wrong password, try again: ')
        if password == receivedPassword:
            print('downloading the resources...')
            print('done')
        # If after two attempts the password is still wrong, we abort the process
        else:
            print('permission denied. the password is incorrect')
else:
    print('aborted')

# else helps to define some code that you want to run if the condition is not fulfilled as shown above.

# You an also que define an elseif which indicates if the first condition is not fulfilled, run the next code but if other condition is fulfilled.

# if name == name1:
#     code...
# elif name == name1:
#      code...

