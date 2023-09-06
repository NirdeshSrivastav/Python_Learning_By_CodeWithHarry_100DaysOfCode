# this is used to  give documentation into the code without commenting out.
# the Docstring is not ignored by the python interpreter.
# to write docstring you have to write docstring at the top in a function body
def square(n):
    """ Takes in a number n ,
    returns the square of n"""
    print(n**2)


def square2(n):
    print(n)
    # This is not treated as docstring
    """ Takes in a number n ,
    returns the square of n"""
    print(n**2)


square(5)
# to print the docstring on the console
print(square.__doc__)
print(square2.__doc__)

# to get ZEN of python
# this us a poem created by zen to create a consistent python code
# >>> import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
