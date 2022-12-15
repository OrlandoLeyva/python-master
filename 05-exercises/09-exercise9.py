approve = 0
noApprove = 0

for number in range(1, 6):
    result = float(input(f'insert the {number} result: '))
    if result < 6:
        noApprove += 1
    else:
        approve += 1

print(f'approve = {approve} \n no approve = {noApprove}')