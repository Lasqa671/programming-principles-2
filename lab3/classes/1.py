"""
Define a class which has at least two methods: 
getString: to get a string from console input 
printString: to print the string in upper case.
"""
class str_up:
    def getstring(self):
        self.string = input()
    def print_str_up(self):
        print(self.string.upper())

str = str_up()
str.getstring()
str.print_str_up()
