# library.py

# Part 1: User relies on library functions to be defined
# Implements the foo method that user.py expects 
class Base():
  def foo():
    return "base foo"



# Part 2: Library relies on user to define libraries

# Example where you expect the user to implement bar()
class Base():
  def foo(self):
    return self.bar() 

# Ways to check for 
old_bc = __build_class__
def my_bc(fun, name, base=None, **kwargs):
  if base is Base:
    print('check if bar method is defined')
  if base is not None:
    return old_bc(fun, name, base, **kwargs)
  return old_bc(fun, name, **kwargs)

import builtins
builtins.__build_class__ = my_bc

builtins.__build_class__ = old_bc


# Using a metaclass
class BaseMeta(type):
  def __new__(cls, name, bases, body):
    print('BaseMeta.__new__', cls, name, bases, body)
    if name != 'Base' and 'bar' not in body:
      print("Error!!!!!!!!!!!!!!!!!!!!!!!")

    return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
  def foo(self):
      return self.bar()


# Using python 3.6 __init_subclass__
class Base():
  def foo(self):
    return self.bar()

  def __init_subclass__(self, *a, **kw):
    print('init_subclass', a, kw)
    return super().__init_subclass__(*a, **kw)