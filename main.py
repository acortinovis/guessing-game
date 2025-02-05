#generate random number
import random
number= random.randint(1, 50)
tentatives=0

#give the user 6 chances and provide feedbacks
print ("guess the number between 1 and 50! ")
if tentative<6:

    guess = float (input ("write your number ").strip())

    if guess==number:
        print("congratulation, you guessed the number! ")
    else:
        if guess<number:
            print("too low, try again")

