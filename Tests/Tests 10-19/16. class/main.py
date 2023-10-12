#import another_module
#print(another_module.another_variable)

'''turtle example'''
#from turtle import Turtle, Screen
#dark = Turtle()
#print(dark)
#dark.shape('turtle')
#dark.color("red")
#dark.forward(100)
#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

'''Pretty table example'''
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Picachu", "Electric"])
table.add_row(["Squrtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)
