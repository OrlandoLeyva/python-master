# for in: the code is executed one time for each element of the list, and stores that element in a variable

"""
countries = ['norway', 'mexico', 'usa', 'germany']

for country in countries:
    print(country)

for number in range(2, 43):
    print(number)
"""

# Multiply table

def generateTable(value: int):
    for number in range(1, 11):
        print(f'{number}. {number * value}')
    else:
        print('completed')
try:
    table = int(input('insert the table: '))
    if not table > 1:
        print('the value must be greater than 0')
    else:
        generateTable(table)
except:
    print('please, insert a valid integer number.')

