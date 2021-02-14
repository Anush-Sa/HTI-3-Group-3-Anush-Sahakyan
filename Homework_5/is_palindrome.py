def is_palindrome(p):
    if len(p) < 1:
        return True
    else:
        if p[0] == p[-1]:
            return is_palindrome(p[1:-1])
        else:
            return False

s = str(input("Enter string: "))
print("Yes" if is_palindrome(s) == True else "No" )
