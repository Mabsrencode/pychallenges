try:
    user_input = input("Enter an integer: ")
    integer_value = int(user_input)
    print("Input is a valid integer:", integer_value)
except ValueError:
    print("Error: Input is not a valid integer.")
