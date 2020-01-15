
def decorator(fun):
    def wrapper():
        print("Wrapper")
        fun()
    return wrapper


def my_fun():
    print("MyFun")

my_wrapper = decorator(my_fun)
my_wrapper()

@decorator
def my_wrapper2():
    print("MyFun")

my_wrapper2()