line = input()  

divider = len(line) // 2
line1 = line[:divider]
line2 = line[divider:]  

sum_1 = sum([int(i) for i in list(line1)]) 
sum_2 = sum([int(i) for i in list(line2)])


if sum_1 == sum_2:
    print('Yes')
else:
    print('No')
    