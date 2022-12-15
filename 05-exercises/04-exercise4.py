'''
ask for two numbers a perform all the basic operation: +, *, -, /
'''

try:
    number1 = float(input('insert the first number: '))
    number2 = float(input('insert the second number: '))

    print(f'multiply: {number1} x {number2} = {number1 * number2}')
    print(f'division: {number1} / {number2} = {number1 / number2}')
    print(f'sum: {number1} + {number2} = {number1 + number2}')
    print(f'subtraction: {number1} - {number2} = {number1 - number2}')
except:
    print('insert a proper number')