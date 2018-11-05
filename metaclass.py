class T:
  a = 1
  food = 'tomato'
  def __init__(self):
    pass

class B(T):
  a = 2
  food = 'bread'
  def __init__(self):
    pass
class A(T):
  food = 'apple'
  def __init__(self):
    pass

class C(A, B):
  #food = 'coffee'
  def __init__(self):
    #self.food = 'crayon'
    pass

  def __get__(self, obj, objtype):
    print("Getting: {}".format(self.food))
    return self.food


class D(B, A):
  #food = 'dinner'
  def __init__(self):
    #self.food = 'dessert'
    pass
    
  def __get__(self, obj, objtype):
    print("Getting: {}".format(self.food))
    return self.food

class Cup:
  x = C()
  z = C()
  def __init__(self):
    self.y = C()
    self.z = C()
    pass



def read_only_properties(*attrs):

    def class_rebuilder(cls):
        "The class decorator"

        class NewClass(cls):
            "This is the overwritten class"
            def __setattr__(self, name, value):
                if name not in attrs:
                    pass
                elif name not in self.__dict__:
                    pass
                else:
                    raise AttributeError("Can't modify {}".format(name))
                print(self.__dict__)
                super().__setattr__(name, value)
        return NewClass
    return class_rebuilder


def class_factory():
  return type('Dog', (), {})


i = class_factory()
print(i)


a = A()
b = B()
c = C()
d = D()
cup = Cup()
cup.x
cup.y
cup.z
Cup.z #__get__ doesn't work in the __init__