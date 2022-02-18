u = 0
l= 0
sentence = input('print your sentence:')
for item in sentence:
  if item.islower():
    l = l+1
  if item.isupper():
    u = u +1

print(f' {sentence} has {u} uppercase letter.')
print (f' {sentence} has {l} lowercase letter.')
