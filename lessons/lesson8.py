my_check_fun = lambda elem: elem < 5

def my_check_fun(elem):
  return elem < 5

def myfilter(check_function, sequence):
  for x in sequence:
    if check_function(x):
      yield x


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list(myfilter(my_check_fun, a)))

print([elem for elem in a if elem < 5])