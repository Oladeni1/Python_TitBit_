
# Classes are user defined prototype
# Classes can be any of the following:- methods, class Variables, instance variables, constructors
# self Keyword is mandatory for calling variable names into method
# instance and class variable have whole diff purpose
# constructor name should be __init___
# "new" keyword is not required in python

# Class declaration:


class Calculator:
    num = 300

    def __init__(self, a, b):  # syntax to create constructor in python
        self.firstNumber = a
        self.secondNumber = b
        print("I am a constructor: been called when an object is created")

    def getText(self):
        print("Method within the class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # syntax to create object in python
obj.getText()
print(obj.summation())

obj2 = Calculator(7, 3)  # syntax to create object in python
obj2.getText()
print(obj2.summation())









