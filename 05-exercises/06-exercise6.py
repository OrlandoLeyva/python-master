counter = 1

while counter <= 10:
    print(f'=TABLE OF {counter}=')
    for number in range(1, 11):
        print(f'{counter} * {number} = {counter * number}')
    print('\n')
    counter += 1;