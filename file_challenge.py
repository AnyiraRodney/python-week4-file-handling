# file_challenge.py

# Read from one file and write a modified version to another file
try:
    with open("input.txt", "r") as infile:
        data = infile.read()

    # Modify the data (example: make all text uppercase)
    modified_data = data.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(modified_data)

    print("File has been read and modified successfully! Check output.txt")

except FileNotFoundError:
    print("Error: input.txt not found. Please create the file first.")
