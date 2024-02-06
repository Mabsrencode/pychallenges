numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
try:
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


