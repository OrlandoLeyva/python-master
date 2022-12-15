numbers = [1,5,7,9,43,6,63,36]

print('unordered list')
for number in numbers:
    print(number)

print('ordered list')
numbers.sort()
for number in numbers:
    print(number)

print(f'list size: {len(numbers)}')