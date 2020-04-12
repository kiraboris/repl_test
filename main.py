


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
