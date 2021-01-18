a_1 = int(input('Enter first number: '))
a_2 = int(input('Enter second number: '))
n = int(input('Enter N: '))

diff = a_2 - a_1

a_n = a_1 + (n - 1) * diff 

print('N-th value: ', a_n)
