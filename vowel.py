letter = input('what is the letter?')
vowel = ['a', 'e', 'i', 'o', 'u']
x = letter in vowel
if x == True:
  print(f'{letter} is a vowel')
else:
  print(f'{letter} is not a vowel')
