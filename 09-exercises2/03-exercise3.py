value = ''

if len(value.strip()) <= 0:
    value = 'Hello, I want to see you'.lower()
    print(value.upper())
else:
    print('it is not empty')
print(value)