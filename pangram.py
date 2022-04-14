def check_pangram(st):
  char_list = 'abcdefghijklmnopqrsttuvwxyz'
  new_dict = {}

  for item in st:
    new_dict[item.lower()] = 1

  for value in char_list:
    if value not in new_dict:
      return False

  return True

result = check_pangram('A quick brown fox jumps over the lazy dog')
print(result)
  
