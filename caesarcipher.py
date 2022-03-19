def caesar_cipher_encrypt(x, key):

  my_char = list('abcdefghijklmnopqrstuvwxyz')
  R = []
  S = ""
  for i in range(len(x)):
    item = x[i]
    if item in my_char:
      index = my_char.index(item)

      new_index = (index + key) % 26

      R.append(my_char[new_index]) 

    if item not in my_char:
      R.append(item)

    #print(f"item={item}, new_index={new_index}, R={R}")


  return S.join(R)
  #return R

x = list(input('Enter your sentence:'))
key = int(input('Enter your key:'))

result = caesar_cipher_encrypt(x, key)
print(result)


def caesar_cipher_decrypt(x, key):
  my_char = list('abcdefghijklmnopqrstuvwxyz')
  R = []
  S = ""
  for i in range(len(x)):
    item = x[i]

    if item in my_char:
      index = my_char.index(item)
      new_index = index - key
      R.append(my_char[new_index])

    if item not in my_char:
      R.append(item)

  return S.join(R)

x = list(input('Enter your sentence:'))
key = int(input('Enter your key:'))

result = caesar_cipher_decrypt(x, key)
print(result)
