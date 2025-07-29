class Person:
    def __init__(self,name):
        self.name=name
    def printName(self):
        print(self.name)
person=Person("some name")
person.printName()