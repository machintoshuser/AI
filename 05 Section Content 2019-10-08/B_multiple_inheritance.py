# From Learn Web Development with Python by Fabrizio Romano

# Using inheritance often leads to multiple inheritance problems, known as "diamond inheritance"

class A:
  def print_name(self):
    print("a")


class B(A):
  def print_name(self):
    print("b")


class C(A):
  def print_name(self):
    print("c")


class D(B, C):
  pass


# d = D()
# d.print_name()  # label could almost be either c or b! 
# print(d.__class__.__mro__)  # MRO = method resolution order, a way to see how to go up the ladder of inheritance
# print(help(D))