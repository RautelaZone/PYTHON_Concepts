'''
Decorators allows programmers to modify the behavior of function.
Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
without permanently modifying it.

Because of function's feature - first class object only decorator concept is complete.
'''

def decorator_fun(func):
    print("Inside decorator")
    def inner():
        print("Inside inner function")
        print("Decorated the function")
        # do operations with func
        func()
    return inner

@decorator_fun
def func_to():
    print("Inside actual function")
func_to()

print("*"*50)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    print(a/b)

# div = smart_div(div)  # instead of this line, we can use @
div(3,9)


