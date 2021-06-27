


def function(x=6):
    # x = 42
    y = 56
    if x < y:
        print("No baby")

# If you will not provide any argument then by default it will pick x= 6
function()

# But if you provide the argument value then it will take it as priority
function(59)


# x = " 7 {} {}".format(8, 9)
# y = " 7 {0} {1}".format(8, 9)
# z = " 7 {1} {0}".format(8, 9)
# print("x =", x, "\ny =", y, "\nz =", z)
#
# print(f'{x}')


"""
Drwaback of python
x = .1 + .1 + .1 - .3
print(x)

x = .1
y = .2
z = .3
print(x + y - z)
Instead of 0 it is printing output as : 5.551115123125783e-17

To overcome from this issue:
from decimal import *

x = Decimal('.1')
y = Decimal('.2')
z = Decimal('.3')
print(x + y - z)

Now output will be 0.0
"""

# x = (1, 2, [3, 4], 5)
# y = (1, 2, [3, 4], 5)
# # type of data
# print(type(x))
#
# # memory location or memory address
# print(id(x))
#
# # To compare 2 data types:
# print(isinstance(x[2], list))
# print(isinstance(x, tuple))
# print(isinstance(x, type(y)))

"""def main():
    # kitten('meow', 'grr', 'purr', 'hello')
    # OR 
    x = ('meow', 'grr', 'purr', 'hello')
    kitten(*x)

# *args means it will take all input in one go
def kitten(*args):
    if len(args):
        for i in args:
            print(i)

    else:
        print("Meow Meow")

if __name__ == '__main__':
    main()
"""


"""
def main():
    # kitten(Buffy='meow', Zilla='grr', Angel='purr', Tanya='hello DC')
    # OR
    x = dict(Buffy='meow', Zilla='grr', Angel='purr', Tanya='hello DC')
    kitten(**x)

# **kwargs means it will take all input in one go kw stands for keyword
def kitten(**kwargs):
    if len(kwargs):
        for i in kwargs:
            print(f'{i} says {kwargs[i]}')

    else:
        print("Meow Meow")

if __name__ == '__main__':
    main()
"""

"""def f1():
    print("this is f1")

x = f1
x()

def f1():
    def f2():
        print("this is f2")

    # if you will not return f2 then it will not give output
    return f2 
x = f1()
x()
"""

"""# decorator 
def f1(f):
    print("Press F1 for dancing")

    def f2():
        print("Press F2 for watching")
        f()
    # if you will not return f2 then it will not give output
    return f2

def f3():
    print("Press F3 for playing music")

x = f1(f3)
x()"""

"""
def f1(f):
    print("Press F1 for dancing")

    def f2():
        print("Press F2 for watching")
        f()
    # if you will not return f2 then it will not give output
    return f2

'''Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. 
Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists,'''

@f1
def f3():
    print("Press F3 for playing music")
# here f1 data will be automatically pick up when f3 will be call and f3 will be pass as argument in f1

f3()"""


"""
def main():

    seq = range(1, 15)
    seq2 = [x * 2 for x in seq]
    # Creating List with condition
    seq3 = [x for x in seq if x % 3 != 0]
    # Creating Tuple inside list
    seq4 = [(x, x**2) for x in seq if x % 3 != 0]
    # Creating Dictionary
    seq5 = {x: x ** 2 for x in seq}
    # Creating set
    seq6 = {x for x in "superduper" if x not in 'pd'}

    print(seq)
    print(seq2)
    print(seq3)
    print(seq4)
    print(seq5)
    print(seq6)


if __name__ == '__main__':
    main()

"""

# class Animal:
#     def __init__(self, type_var, name, sound):
#         self.name = name
#         self.type_var = type_var
#         self.sound = sound
#
#     def sound(self):
#         return










