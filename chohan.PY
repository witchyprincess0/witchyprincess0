"""
When you run chohan.py, the output will look like this:
Cho-Han, by Al Sweigart al@inventwithpython.com
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
You have 5000 mon. How much do you bet? (or QUIT)
> 400
The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet.
 CHO (even) or HAN (odd)?
> cho
The dealer lifts the cup to reveal:
 GO - GO
 5 - 5
You won! You take 800 mon.
The house collects a 40 mon fee.
"""

import random

total_money = 5000 

while True:
  bet_amount = input(f'You have {total_money} mon. How much do you bet? (or QUIT)')
  if bet_amount == 'QUIT' or int(bet_amount) > total_money:
    quit()
    
  JAPANESE_NUMBERS = {
    1: 'ICHI', 
    2: 'NI', 
    3: 'SAN',
    4: 'SHI',
    5: 'GO', 
    6: 'ROKU'
  }
  guess_even_odd =input('CHO (even) or HAN (odd):' )
  
  list1 = [1,2,3,4,5,6]
  d1 = random.choice(list1) 
  d2 = random.choice(list1) 
  print(f'{d1} - {d2}')
  japanese_numbers_d1 = JAPANESE_NUMBERS.get(d1)
  japanese_numbers_d2 = JAPANESE_NUMBERS.get(d2)
  print(f'{japanese_numbers_d1} -{japanese_numbers_d2}')
  
  sum_of_d1d2 = d1 + d2
  
  amount_won = 0
  house_fee = 0
  if ((sum_of_d1d2 %2 == 0 and guess_even_odd == 'CHO') or (sum_of_d1d2 %2 != 0 and guess_even_odd == 'HAN')):
    amount_won = int(bet_amount) * 2
    house_fee = 40
    print(f'You won! The amount won is {amount_won}')
    print(f'The house collects {house_fee}')
  else:
    amount_won = -1*int(bet_amount)
    house_fee = 0
    print('You lost!')
  
  total_money = total_money + amount_won - house_fee
    
    
