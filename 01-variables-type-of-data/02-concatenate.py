
# Concatenate works for joining two strings.

name = 'orlando'
age = 20
country = 'mx'

# number one: use the character '+':
print('Hi, i am ' + name)
 
# number two: pass the values as argument: 
#This will automatically generate spaces between values.
print('Hi, i am', name)

# number three: use f and store the value you want to concatenate within two {}
print(f'Hi i am {name}')

# special way: using the format method you can pass as an argument the values you want to concatenate.
print("Hi i am {} i like to {} and i love {}".format(name, 'code', 'tere'))