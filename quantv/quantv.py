from __future__ import print_function

def hello():
    """ Returns a Hello, World! """
    return("Hello, Q User!")

def say_hello():
    """ Prints Hello, World message """
    print(hello())
    
def is_even(x):
        if x%2==0:
            return True
        else:
            return False