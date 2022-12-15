try:
    number = int(input('insert a number: '))
except:
    print('only integer numbers allowed')

while not number == 111:
    try:
        number = int(input('wrong, try again. insert a number: '))
    except:
        print('only integer numbers allowed')
        break
