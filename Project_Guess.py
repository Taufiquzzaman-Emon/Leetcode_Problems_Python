'''We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module.'''
from random import randint


def guess_the_number():
  Guess = randint(1,10)
  n = -1
  guesses = 0
  while Guess != n:
    guesses+=1
    n= int(input("Enter The number: "))
    if n>Guess:
       print("Please enter a lower number")
    elif n<Guess:
       print("Please enter a higher number")
    else:
       print(f"You have Guessed the number {Guess} and you guessed for {guesses} times")

guess_the_number()
