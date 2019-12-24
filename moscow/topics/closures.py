
def fun1():
    return a

a = 8
print(a)
print(fun1())
print("---")

def print_fun1():
    a = 10 # shadows global a
    print(a)
    print(fun1())

print_fun1()
print("---")

def get_fun2():
    a = 10 # shadows global a
    def fun2():
        return a
    return fun2

fun2_closure = get_fun2()
print(a)
print(fun2_closure())