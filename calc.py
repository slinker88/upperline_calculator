# Python program to find roots of quadratic equation
import math

# function for finding roots
def equationroots( a, b, c):

	# calculating discriminant using formula
	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))
	
	# checking condition for discriminant
	if dis > 0:
		print(" real and different roots ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	
	elif dis == 0:
		print(" real and same roots")
		print(-b / (2 * a))
	
	# when discriminant is less than 0
	else:
		print("Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val)
		print(- b / (2 * a), " - i", sqrt_val)

# Driver Program
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# If a is 0, then incorrect equation
if a == 0:
		print("Input correct quadratic equation")

else:
	equationroots(a, b, c)

def add (x,y):
    return str(x + y) 

def subtract (x,y):
    return str(x - y) 

def multiply (x,y):
    return str(x * y)

def divide (x,y):
    return str(x / y) 

def exponents (x,y): 
    return str(x ** y)

print("1. Add " + "2. Subtract " + "3. Multiply " + "4. Divide " + "5. Exponent")
choice = input("Select an option:")

if choice in ("1", "2", "3", "4", "5", "6"):
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if choice == "1":
        print(str(x) + "+" + str(y) + "=" + add(x,y))
    elif choice == "2":
        print(str(x) + "-" + str(y) + "=" + subtract(x,y))
    elif choice == "3":
        print(str(x) + "*" + str(y) + "=" + multiply(x,y))
    elif choice == "4":
        print(str(x) + "/" + str(y) + "=" + divide(x,y))
    elif choice == "5":
        print(str(x) + "^" + str(y) + "=" + exponents(x,y))
   
else:
    print("Invalid input")

