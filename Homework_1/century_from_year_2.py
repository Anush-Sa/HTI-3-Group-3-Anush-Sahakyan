year = int(input('Enter the year: '))

century = year // 100
if year % 100 != 0:
    century += 1

print('Century: ', century)
