#Ask user to give a number and identify if the number is odd or even. Even numbers are divisible by 2, which means if divided by 2 they give a remainder of zero.
#first step is to ask the user to give a number and store it in a variable.
number = int(input("Please enter a number: "))
#second step is to check if the number is even or odd using the modulus operator.
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

#Ask user for a temperature in Celsius (this will be a floating point number, so you need to read with float(input("Give Celsius temperature: "). Then, calculate and print the conversion to Fahrenheit. Formula for conversion: °F = °C * 9/5 + 32 

#first step is to ask the user to give a temperature in Celsius and store it in a variable.
celsius = float(input("Please enter a temperature in Celsius: "))
#second step is to convert the Celsius temperature to Fahrenheit using the formula.
fahrenheit = celsius * 9/5 + 32
#third step is to print the converted temperature in Fahrenheit.
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f} °F")

#Ask for the width and the height of a rectangle, then calculate the perimeter and the area of the rectangle (search to find the formulas)

#first step is to ask the user to give the width and height of a rectangle and store them in variables.
width = float(input("Please enter the width of the rectangle: "))
height = float(input("Please enter the height of the rectangle: "))
#second step is to calculate the perimeter and area of the rectangle using the formulas.
perimeter = 2 * (width + height)
area = width * height
#third step is to print the calculated perimeter and area of the rectangle.
print(f"The perimeter of the rectangle is: {perimeter:.2f}")
print(f"The area of the rectangle is: {area:.2f}")

#Ask user for 2 numbers, then print all values from the smaller to the larger value. For example if a=3 and b=6, print 3, 4, 5, 6. If a=8 and b=6, print 6, 7, 8.

#first step is to ask the user to give two numbers and store them in variables.
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
#second step is to determine the smaller and larger number using the min and max functions.
smaller = min(num1, num2)
larger = max(num1, num2)
#third step is to print all values from the smaller to the larger number using a for loop.
print(f"All values from {smaller} to {larger}:")
for i in range(smaller, larger + 1):
    print(i)