import random

choice = int(input("Press 1 if you want to guess a number, press 2 if you want computer to guess your number: "))
a = random.randint(1,100)
guess = random.randint(1,100)
low = 1
high = 100

if(choice == 1):
    #Code where user has to guess number(The number changes dynamically according to the range).
    print("I have guessed a number, please try to guess it.")
    c = 5
    for x in range (0,6,1):
        if(c-x == 0):
            print("Too many attempts, play a new game")
            break
        else:
            print("Attempts left",c - x)
            b = int(input("Guess the number(If you want to exit enter 0):"))
            if(b == 0):
                print("The number is",a)
                break
            elif(b > a):
                if(b-5 > a):
                    print("Too high please guess lower")
                else:
                    print("You are close, try guessing lower")
                temp = random.randint(a,b)
            elif(b < a):
                if(b+5 < a):
                    print("Too low please guess higher")
                else:
                    print("You are close, try guessing higher")
                temp = random.randint(b,a)
            elif(a == b):
                print("You have guessed right.")
                break
            a = temp

elif(choice == 2):
    #Code where computer guesses your number, is very smart and could probably guess a non-changing number in 10 attempts.
    while(1):
        print(f"Is your number {guess}, press 'h' if its higher else 'l' if lower, press 0 if you want to end game and press 1 if the number is correct: ")
        choice = input("Enter your choice: ")

        if(choice == 'l'):
            high = guess - 1

        elif(choice == 'h'):
            low = guess + 1
        
        elif(choice == '0'):
            print("Thanks for playing")
            break

        elif(choice == '1'):
            print("Haha! I guessed it.")
            break
        
        else:
            print("Wrong choice choose again")
            continue
        
        guess = random.randint(low,high)
        print(f"This is high: {high}, this is low:{low}")