import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.plot([0, 1, 2], [0, 1, 2])
plt.savefig('graph.png')

s= input()
print(type(s))
a= float(s)
print(type(a))
print(a**5)

def my_fun(x):
  return x**2

def my_fun2():
  print("Love")
  return 42


print(my_fun)
print(str(my_fun))
print(type(my_fun))



####
# a=10
# x
# sin x
# sin(x)

a = []
a = [1, 2]

b = [4, "hello"]
c= a + b

c.append(6)


print(c)

print(len(c))
print(len("hello_world"))