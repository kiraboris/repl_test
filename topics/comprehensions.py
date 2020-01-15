
def fun1(lst):
    for x in lst:
        yield x**2

def fun2(lst):
   result = []
   for x in lst:
       result.append(x**2)
   return result

def fun2a(lst):
  return [x**2 for x in lst]

def fun1a(lst):
  yield from (x**2 for x in lst)

my_lst = [1, 2, 4]

print(sum(fun1(my_lst)))
print(sum(fun2(my_lst)))
print(sum(fun2a(my_lst)))
print(sum(fun1a(my_lst)))
