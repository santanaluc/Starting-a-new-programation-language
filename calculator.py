import re
'''
def add (x,y): return x + y
def sub (x,y): return x - y
def mult (x,y): return x * y
def div (x,y): return x / y
'''
def performMath():
    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Bye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.()" "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

print("Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

while run: 
    performMath()