#Guess a number between 1-10

import random
random_number = random.randint(1,10)
print(random_number)

while True:
  try:
    x = int(input('Guess a number between 1 to 10:'))
    if x > 0 and x <11:
      if x == random_number:
        print('Your guess is correct')
        break
      else:
        ('Guess again')
    else:
      print('Please guess a number between 1 to 10')

  except ValueError:
    print('Please guess a number between 1 to 10')
    continue
