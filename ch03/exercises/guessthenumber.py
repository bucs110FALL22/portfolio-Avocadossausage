import random
random_num = random.randrange(1, 11 ,1)
correct_guess = False

n = 3
for i in range(n):
  if not correct_guess:
    print("Enter your guess")
    guess_num = int(input())
    if guess_num > random_num:
      print("You guessed too high")
    elif guess_num < random_num:
      print("You guessed too low")
    else:
      correct_guess = True
      print("You guessed correctly!")
