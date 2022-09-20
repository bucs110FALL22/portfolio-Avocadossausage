import random
random_num = random.randrange(1,11)
correct_guess = False

for i in range(3):
  guess_num = int(input("Enter your guess"))
  if guess_num > random_num:
    print("You guessed too high")
  elif guess_num < random_num:
    print("You guessed too low")
  else:
    print("You guessed correctly!")
