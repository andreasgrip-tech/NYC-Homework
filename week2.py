#Create an empty List. Add 100 random values into the list. The values should be in the range 100 to 999. Then, find the maximum, th minimum value in the list, and the average of all the values.
#first step is to import the random module to generate random values.
import random
#second step is to create an empty list to store the random values.
random_values = []
#third step is to use a for loop to generate 100 random values in the range 100 to 999 and add them to the list.
for _ in range(100):
    random_values.append(random.randint(100, 999))
#fourth step is to find the maximum, minimum, and average of the values in the list using the max, min, and sum functions.
maximum_value = max(random_values)
minimum_value = min(random_values)
average_value = sum(random_values) / len(random_values)
#fifth step is to print the maximum, minimum, and average values.
print(f"The maximum value in the list is: {maximum_value}")
print(f"The minimum value in the list is: {minimum_value}")
print(f"The average of all values in the list is: {average_value:.2f}") 

#(Bonus) Ask user for a number N (N must be odd, if even, add 1). This number will be the size of the base of a Xmas tree. Draw the tree.
#first step is to ask the user to give a number N and store it in a variable.
N = int(input("Please enter an odd number for the size of the base of the Xmas tree: "))
#second step is to check if N is even, and if so, add 1 to make it odd.
if N % 2 == 0:
    N += 1
#third step is to draw the Xmas tree using a for loop.
for i in range(1, N + 1, 2):
    print(" " * ((N - i) // 2) + "*" * i) 
    