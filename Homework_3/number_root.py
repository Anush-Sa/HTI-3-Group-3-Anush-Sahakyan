def numberroot(n):
    if int(n) < 10:
        return n
    else:
        res = [int(i) for i in str(n)]
        n = sum(res)
        return numberroot(n)

n = str(input("Input a number: "))
print("Root is: ", numberroot(n))
