line = input()  
a = line.split()

res = [int(i) for i in a]

m = max([res[i] * res[i + 1] for i in range(0, len(res) - 1)])

print(m)
