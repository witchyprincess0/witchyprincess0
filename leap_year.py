x = input('what is the year?')
remainder_4 = int(x) % 4
remainder_100 = int(x) % 100
remainder_400 = int(x) % 400

if remainder_4 == 0 and remainder_100 != 0:
  print (f'{x} is a leap year')
elif remainder_4 == 0 and remainder_100 == 0 and remainder_400 == 0:
  print (f'{x} is a leap year')
else:
  print(f'{x} is not a leap year')
