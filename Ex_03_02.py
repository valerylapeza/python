# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program.
# The following shows two executions of the program:
#
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    hour = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print("Error, please enter numeric input")
    quit()
if hour > 40:
    print("Overtime")
    reg = hour * rate
    ovt = (hour - 40.0) * (rate * 0.5)
    salary = reg + ovt
else:
    print("Regular")
    salary = hour * rate
print('Pay:', salary)
