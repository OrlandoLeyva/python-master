# List of predefined functions

name = 'orlando leyva'

# print a value in the console.
print()

# return the type of data of the variable.
type(name)

# detect the type. It will help you to determinate if some variable is the type of data you're indicating
detectType = isinstance(name, str)

# remove whitespaces from both the beginning and the end of the string
name.strip()

# remove variables.
del name

lastName = 'leyva'

# determinate is a variable is empty. len() allows you to know the length of the string. if it is 0, the variable is empty.
len(lastName)
'''
if len(lastName.strip()) <= 0:
    print('is empty:', len(lastName))
else:
    print('not empty:', len(lastName.strip()))
'''

# find characters or phrases withing the text. returns the position where the phrase or letter starts.
text = 'live is beautiful, bitch'
text.find('beautiful')

# replace words
text.replace('bitch', '***')

# UPPERCASE and LOWERCASE

# covert some string to uppercase

text.upper()

# convert some string to lowercase

# text.lower()

print(text)

#NOTE: they don't replace the original text, but generate a new one.



