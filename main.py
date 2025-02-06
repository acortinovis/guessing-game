#generate random number
import random
number= random.randint(1, 50)
tentatives=0

#give the user 6 chances and provide feedbacks
print ("guess the number between 1 and 50! ")
while True:
    if tentatives<6:

        guess = float (input ("write your number ").strip())
        tentatives= tentatives+1
        if guess==number:
           print("congratulation, you guessed the number! ")
        else:
            if guess<number:
              print("too low, try again")
            else:
              print("too high, try again")
    else:
        print("you didn't guess, the number was ",number)
        break


