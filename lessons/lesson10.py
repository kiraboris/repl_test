import os
import os.path

#print(os.listdir('.'))
files = [f for f in os.listdir('.') if f [-3:]== ".py" ] 
print(files)

# ======

names = os.listdir('.') 
for f in (names):
  x= f.split(".")
  #print(x)
  #print(x[-1])
  if len(x)==2 and x[0] != '':
    print(x[-1])


# =====

def strings_to_ints_list(strings):
  result = []
  for x in strings:
    result.append(int(x))
  # result = [int(x) for x in strings] 

def strings_to_ints_generator(strings):
  for x in strings:
    yield int(x)
  # yield from (int(x) for x in strings) 

values = "4,5,6"
ints_as_strings = values.split(',')
print(ints_as_strings)

ints1 = map(int, ints_as_strings)
ints2 = (int(x) for x in ints_as_strings)

print(ints1)
print(ints2)
print(list(ints1))
print(list(ints2))

