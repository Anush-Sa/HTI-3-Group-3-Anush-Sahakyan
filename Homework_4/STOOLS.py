def stools(line):
    a = line.split()
    res = [int(i) for i in a]
    m = max([res[i] for i in range(0, len(res))])
    total = sum([m-res[i] for i in range(0, len(res))])
    return total

heights = input("Input the heights: ")
print(stools(heights))
