try:
    file_path = input("Enter the file path: ")
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The specified file was not found.")
