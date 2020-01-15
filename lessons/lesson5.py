print("Lesson 5")

# 1
def hello_user(username):
    """
    Says "Hello, %username%!":
        in: username
        out: "Hello, %username%!"
    """
    c="Hello, "+ username + "!"
    return c

assert hello_user("Kirill") == "Hello, Kirill!"
assert hello_user("Max") == "Hello, Max!"
assert hello_user("Alex") == "Hello, Alex!"
print("1st done!")


# 2
def add_squares(numbers):
  """
    Adds up all numbers in a sequence:
    in: numbers (e.g. [1,2,...])
    out: sum of squres of numbers
  """
  result = 0
  # for i,x in enumerate(numbers):

  for x in numbers:
   result= result + x**2

  return result

assert(add_squares([1,2,4]) == 21)
assert(add_squares([0,0,1,1]) == 2)


print("2nd done!")


# 3
my_lst = [1, 2, 4, 6, 3, 7]
print(my_lst)

def fun2(lst):
   result = []
   for x in lst:
      result.append(x**2)
   return result
lst_sqrs = fun2(my_lst)

print(lst_sqrs)

# 4
# list comprehension 
all_lists = [my_lst, my_lst, my_lst]

lst_sqrs = [x**2 for _ in all_lists for x in _]
print(lst_sqrs)

# 5
# generator function
def fun1(lst):
  for x in lst:
    yield x ** 2

my_lst = [4, 5, 6]

print(fun1)
print(fun1(my_lst))
print(list(fun1(my_lst)))
print(sum(fun1(my_lst)))
print(sum(list(fun1(my_lst))))

#for x in range(0, 100000000000001):
#  print(x)

# 6
# modules/libraries
import time as my_time

print(my_time)
print(my_time.time)
print(my_time.time())

import my_module

print(my_module)
print(my_module.hello)
print(my_module.hello())