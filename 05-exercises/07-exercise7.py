number = int(input('insert the amount: '))
percentage = int(input('insert the discount: '))

print(f'price = {number}. This product has a discount of {percentage}% total to pay: {(percentage * number) / 100}')