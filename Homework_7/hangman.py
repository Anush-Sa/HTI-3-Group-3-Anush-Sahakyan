import random

random_number = random.choice(range(20))

with open('fruits.txt') as f:
    for _ in range(random_number):
        f.readline()
    word = f.readline().strip()

turns = 5

print(f"Guess the word. {turns} mistakes left")

guesses = ''
 
while turns > 0:
    
    failed = 0
     
    for char in word: 
         
        if char in guesses: 
            print(char, end = " ")
             
        else: 
            print("_", end = " ")

            failed += 1          
 
    if failed == 0:

        print("\nYou won the game.") 
        break
     
    print("")
    guess = input("Guess a letter: ")
     
    guesses += guess 

    if guess not in word:
         
        turns -= 1    
         
        if turns == 0:
            print("You lost the game.")
        else:
            print(f"Guess the word. {turns} mistakes left")
    else:
        print(f"Guess the word. {turns} mistakes left")

    
