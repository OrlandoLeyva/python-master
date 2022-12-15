number1 = int(input('insert the first number: '))
number2 = int(input('insert the second number: '))

if number1 < number2:
    for value in range(number1, number2 + 1):
        print(value)
else:
    print('the first number must be less than the second number')