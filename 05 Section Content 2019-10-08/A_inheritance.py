# Examples from "Learn Python 3 the Hard Way" by Zed A Shaw

class Parent(object):
    def __init__(self):
      self.phone_type = "iphone"
      # self.mood = "happy" # if I change this attribute here, it won't get inherited!

    def implicit(self):
      print("I am a person!")

    def override(self):
      print("I have an {}".format(self.phone_type))

    def altered(self):
      self.mood = "happy"
      print("Time to hug child!")


class Child(Parent):  # Child will inherit from Parent
    def __init__(self):
      self.phone_type = "samsung"
      self.mood = "sad"

    def override(self):
      print("Override in Child")
      print("I have an {}".format(self.phone_type))

    def altered(self):
      print("My current mood is {}".format(self.mood))
      super().altered() 
      print("And now my mood is {}".format(self.mood))

# parent = Parent()
# child = Child()

# parent.implicit()
# child.implicit()  # we'll inherit directly from the Parent class

# parent.override()
# child.override()  # we override the parent class. We want the functionality of this class to behave differently

# child.altered()
