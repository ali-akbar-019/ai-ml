num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
remainder = num1 % num2
square_of_num_1 = num1 ** 2
cube_of_num2 = num2 ** 3
int_div = num1 // num2
num3 = 40
avg = (num1 + num2 + num3)/3

mins = 140
hours = mins/60

# print all
print(f"""Number 1: {num1}
Number 2: {num2}
Number 3: {num3}
Addition: {addition}
Subtraction: {subtraction}
Multiplication: {multiplication}
Division: {division}
Remainder: {remainder}
Square of number 1: {square_of_num_1}
Cube of number 2: {cube_of_num2}
integer Division: {int_div}
Average of the three Numbers: {avg}
==================================
Minutes = {mins}
Hours = {hours:.2f}""")