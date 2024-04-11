import random

print("Welcome to the Guess the Number game!")

print("I'm thinking of a number between 1 and 100. Can you guess it?")

number = random.randint(1,100)

guess = 0

attempts = 0

while guess != number :
    
    guess = int(input("Enter The Number Which You Are Trying to Guess:"))
    
    attempts += 1
    
    if (guess < number):
        
        print("Guess a Highr Number...")
     
    elif(guess > number ):
        
        print("Guess a Lower Number...")
        
    else:
        print("You Won ")
        
        
    
print("You find the number after",attempts,"attempt")