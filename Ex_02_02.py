# 1. Write a program that uses input to prompt a user for their name and then welcomes them
# Enter your name: Chuck
# Hello Chuck

name = input('Enter your name: ')
print('Hello', name)


# 2. Write a program to prompt the user for hours and rate per hour to compute gross pay
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
print(hours * rate)


# 3. Assume that we execute the following assignment statements:
#
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression)
#
# width//2
# width/2.0
# height/3
# 1 + 2 * 5

width = 17
height = 12.0

print(type(width//2))
print(type(width/2.0))
print(type(height/3))
print(type(1 + 2 * 5))
