import random
ran = random.randint(0,100)
while True:
  guess = input("guess a number\n")
  if int(guess) > ran:
    print ("it's lower guess again\n")
  elif int(guess) < ran:
   print ("It's higher guess again\n")
  elif int(guess) == ran:
    print ("you won")
    break
    