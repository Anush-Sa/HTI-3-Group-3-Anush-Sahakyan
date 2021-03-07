low = 0
high = 1000

start = input("Think of a number between 1 and 999. Input 0 once you’re ready to play.\n")
if start == '0':
    guess = int((high + low) / 2)
    guessing = True
    i = 1
    while guessing:
        
        print(f"My guess number {i}: ",  guess)
        inputed_value = input("In: ")
        #Input 1 if this number is smaller, Input -1 if this number is bigger, input 0 if this number is correct

        if inputed_value == '-1':
            high = guess
            guess = int((high + low) / 2)
        elif inputed_value == '1':
            low = guess
            guess = int((high + low) / 2)
        else:
            if inputed_value == '0':
                guessing = False
                print(f"I guessed in {i} steps!")
                break
            else:
                print("Invalid input")
        
        i += 1
        if i > 10:
            print("I couldn’t guess in 10 steps! This means you cheated!")
            break
    
else:
    print("Invalid input")

#Input 1 if this number is smaller, Input -1 if the number is bigger, input 0 if this number is correct
