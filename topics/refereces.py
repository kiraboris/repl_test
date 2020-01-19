

def fun1(x):
  x = x + 1
  print(x)

def fun2(lst):
  lst.append(4)
  print(lst)


a = 10 
print(a)
fun1(a)
print(a)

print("---")

lst = [3]
print(lst)
fun2(lst)
print(lst)