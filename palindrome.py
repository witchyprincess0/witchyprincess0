word = input('what is the word?')

reverse = (word[::-1])
if word == reverse:
  print (f' {word} is a palindrome')
else:
  print(f' {word} is not a palindrome')
