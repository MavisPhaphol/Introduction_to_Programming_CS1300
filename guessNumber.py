import random

print("Welcome to Guess the Number!")

number = random.randint(1, 100)
attempts = 0

print("The goal is to guess the right number in 7 attempts.")
print("Will you chose the right number in 7 attempts? GOOD LUCK!")

while attempts < 7:
  user_guess = int(input("Pick a number from 1 to 100: "))
  attempts += 1
  if user_guess > 100:
    print("Please Pick between 1 and 100")
  if user_guess > number:
    print("Too high")
  elif user_guess < number:
    print("Too low")
  elif user_guess == number:
    break
  elif attempts == 7:
    break
if user_guess == number:
  print("Right on the spot!")
  print("Congratulations! You Won! You have guessed", attempts, "times!")
else:
  print("Good luck next time! The correct number is", number)