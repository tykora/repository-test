# guess the number game
import random
num1 = random.randrange(1, 100)
guess = 0
while guess != num1:
  guess = input("guess a number 1 to 100")
  history.append(guess)
  if guess.isdigit:
    if guess > num1:
      print("to big! try again.")
    if guess < num1:
      print("to small! try again.")
    if guess < 1 or guess > 100:
      print("out of bounds! try again.")
    if guess == num1:
      print("you found me! ah ha ha!")
      break
  else:
    if guess = "history"
      print(history)
