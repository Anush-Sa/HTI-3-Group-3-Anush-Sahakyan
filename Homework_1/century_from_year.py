year = int(input('Enter the year: '))

if year % 100 == 0:
    century = int(year / 100)
else:
    century = year // 100 + 1

print('Century: ', century)
