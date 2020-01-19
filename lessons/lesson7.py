
data1 = [
  "Ананас",
  "Абрикос",
  "Груша",
  "Банан",
  "Апельсин",
  "Лимон"
]

datat2 = [
  True, False, False, True
]

data3 = [
  0, 3, 5, 2, 1, 0, 6, 4, 6
]

for i,x in enumerate(data1):
  print(str(i+1) + ". " + x)

print("=====")

i=0
while True:
  x = data1[i]
  print(str(i+1) + ". " + x)
  i= i+1
  if i == (len(data1)):
    break
    
my_new_data =[]
for i,x in enumerate(data3):
  if i % 2 == 0:
   my_new_data.append(x)
 

print(my_new_data)
