# error_handling_lab.py

filename = input("Enter the filename you want to open: ")

try:
    with open(filename, "r") as file:
        data = file.read()
        print("File contents:\n", data)

except FileNotFoundError:
    print("Error: File not found. Please check the filename.")

except PermissionError:
    print("Error: You don’t have permission to read this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
