class hi():
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input("Input something: ")
    def printString(self):
        print(self.string)
a = hi()
a.getString()
a.printString()

