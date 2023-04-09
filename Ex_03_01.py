# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours.
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hour = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hour > 40:
    print("Overtime")
    reg = hour * rate
    ovt = (hour - 40.0) * (rate * 0.5)
    salary = reg + ovt
else:
    print("Regular")
    salary = hour * rate
print('Pay:', salary)
