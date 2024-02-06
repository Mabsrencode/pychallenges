try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 + num2

    print("Result:", result)

except ValueError:
    print("Error: Input is not numerical.")
except TypeError:
    print("Error: Input is not numerical.")
