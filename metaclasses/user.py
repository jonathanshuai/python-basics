from library import Base

# Part 1: User relies on library functions to be defined

print("Part 1")
# A check to learn early whether foo was defined 
assert hasattr(Base, 'foo'), 'no foo method!' 

# Relies on Base.foo() to be available
class Derived(Base):
  def bar(self):
    return self.foo()



print("Part 2")
# Part 2: Library relies on user to define libraries

# Implements the bar function that library.py expects 
class Derived(Base):
  def bar(self):
    return("bar!")


d = Derived()
print(d.bar())
