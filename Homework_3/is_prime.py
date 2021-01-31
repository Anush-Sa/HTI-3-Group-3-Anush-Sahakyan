def isprime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return "No"
        else:
            return "Yes"
    else:
        return "No"

n = int(input("Input a number: "))
print(isprime(n))
