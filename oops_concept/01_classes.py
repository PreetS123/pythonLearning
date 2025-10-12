#Classes and object in python

"""
Class is a blueprint of creating an object

"""

class Student:
    def __init__(self,name):
        self.name= name
        print("Student added in database")

# creating object (instance / instance of class)
s1= Student("Preeti")
print(s1.name)


# constructor 
"""All classes have function called __init__(), 
which is always executed when the class is being initiated."""
# __init__ function