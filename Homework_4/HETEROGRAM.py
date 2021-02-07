def heterogram(t):
    result1 = list(t.replace(" ", "").lower())
    result2 = list(set(t.replace(" ", "").lower()))
    return "Yes" if len(result1) == len(result2) else "No"


text_example = str(input("Input the text: "))
print(heterogram(text_example))
