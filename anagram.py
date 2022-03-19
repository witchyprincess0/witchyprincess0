word_1 = input('Enter the first word:')
word_2 = input('Enter the second word:')

word_1_dict = {}
word_2_dict = {}
  
for item in word_1:
  word_1_dict[item] = word_1.count(item)
print(word_1_dict)

for item in word_2:
  word_2_dict[item] = word_2.count(item)
print(word_2_dict)

if word_1_dict == word_2_dict:
  print('It is an anagram')
else:
  print('It is not an anagram')
"""
"""
word_1 = list(input('Enter the first word:'))
word_2 = list(input('Enter the second word:'))
word_1.sort()
print(word_1)
word_2.sort()
print(word_2)

if word_1 == word_2:
  print('It is an anagram')
else:
  print('It is not an anagram')
