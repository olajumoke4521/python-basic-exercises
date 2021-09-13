#Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. Print num1 and num2 on two separate lines.
num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

#Write a program that assigns the floating-point literal 175000.0 to the variable num using E notation and then prints num in the interactive window.
num = 1.75e5
print(num)

#In IDLE’s interactive window, try to find the smallest exponent N for which 2e<N>, where <N> is replaced with your number, returns inf.
print(4e320)

#Write a program called exponent.py that receives two numbers from the user and displays the first number raised to the power of the second number.
base = input("Enter a base: ")
exponent = input("Enter an exponent: ")
result = float(base) ** float(exponent)
print(f"{base} to the power of {exponent} = {result}")

#Write a program that asks the user to input a number and then displays that number rounded to two decimal places.
number = input("Enter a number: ")
newnumber = float(number)
print(f"{newnumber} rounded to 2 decimal places is {round(newnumber, 2)}")

#Write a program that asks the user to input a number and then displays the absolute value of that number.
number = input("Enter a number: ")
newnumber = float(number)
print(f"The absolute value of {newnumber} is {abs(newnumber)}")

#Write a program that asks the user to input two numbers by using input() twice, then displays whether the difference between those two numbers is an integer.
firstnum = float(input("Enter the first number: "))
secondnum = float(input("Enter the second number: "))
print(f"The difference between {firstnum} and {secondnum} is an integer? " f"{(firstnum - secondnum).is_integer()}!")
