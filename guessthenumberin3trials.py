Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:
--------------
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!


def guess_the_number():
  import random
  secret = random.randint(1,20)
  print(secret)
  name = input('Hello, what is your name?')
  print(f' well, {name}, I am thinking of a number between 1 to 20')

  my_range = range(3)
  for item in my_range:
    x = int(input('Guess my number:'))
    if x != secret:
      if x > secret:
        print('Your guess is too high')
      elif x < secret:
        print('Your guess is too low')
    else:
      print(f'Good job, {name}! You guessed my number in 3 guesses!')
      return
  print('You are out of the guesses')

guess_the_number()
  
               
  


  
    
