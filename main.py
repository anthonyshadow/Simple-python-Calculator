# program to make a simple calculator

import re

print("Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    if equation == 'quit':
        print("Goodbye")
        run = False
    else:
        # Most important step, by using Regex ensures that no invalid characters are being used and thus causing the calculator to crash
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()

