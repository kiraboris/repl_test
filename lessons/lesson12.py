def all_unique(nums):
  x_already_seen =[]
  for x in nums:
    if x in x_already_seen:
      return False

  
    x_already_seen.append(x)
  return True
#from lessons import lesson9

print("***")

def test_all_unique():
  x = [1,2,3]
  y = all_unique(x)
  assert y == True

  
def test_all_unique2():
  x = [0.3] 
  y = all_unique(x)
  assert y == True 

def test_all_unique3():
  x = [4,11,134,4,11]
  y = all_unique(x)
  assert y== False

test_all_unique()
test_all_unique2()
test_all_unique3()


# ==============

def fun1(color):
  print("fun1")
  if color == "red":
    return "fire"
  else:
    return "water"


def fun2(color):
  print("fun2")
  if color == "red" or color == "blue":
    return fun1(color)
  elif color == "green":
    return "grass"
  return "default"


print(fun2("red"))
print(fun2("blue"))
print(fun2("green"))
print(fun2("white"))

"""
fun2
fun1
fire
fun2
fun1
water
fun2
grass
fun2
default
"""
