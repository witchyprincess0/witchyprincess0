#generate a number between 1-10
# input from the user
#check the input is between 1-10
#check the guess is correct or not. otherwise ask again



import random
random_number = random.randint(1,10)
print(random_number)

while True:
  try:
    user_number = int(input('Guess a number:'))

    #if user_number > 0 and user_number <11:
    if user_number in list(range(1,10)):
      if user_number == random_number:
        print('You guess is correct')
        break
      else:
        print('Please guess again')
    else:
      print('Please enter a number between 1-10')
        
  except ValueError: 
    print('Please enter a number')
    continue
