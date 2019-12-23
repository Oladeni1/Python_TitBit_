
# Inheritance from other class
from pythonBasics.OopDemo import Calculator


class inherit(Calculator):
    num2 = 500

    def __init__(self):
        Calculator.__init__(self, 7, 3)

    def getTotal(self):
        return self.num2 + self.num + self.summation()  # Total of 1110 will be printed


obj = inherit()
print(obj.getTotal())

