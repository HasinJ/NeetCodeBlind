for i in range(5,5):
    print(i)

if "cba" == "bca": print(true)

#print({{'test': 'test'}: "hello"})


import random

l = [1, 2, 3, 4, 5]
i = 0
while i < len(l):
  if random.choice([True, False]):
    del l[i]
  else:
    i += 1

print(f'{l=}')
