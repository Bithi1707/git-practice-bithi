from datetime import date
from utils import add, subtract, multiply

print("Bithi Akter Eva")
print("Today's date:", date.today())

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")