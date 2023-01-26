# Open file "Data.txt" in read mode
file = open("Data.txt", "r")

# Printing the Options
print("Choose from the Following Options:")
print("1. Count the number of lines in the file")
print("2. Count the number of words in the file")
print("3. Count the number of characters in the file")
print("4. Print each line in the file in reverse order")

# Taking the input from the user
choice = int(input("Enter your choice: "))

# Checking the choice
if choice == 1:
    # Counting the number of lines in the file
    print("Number of lines in the file: ", len(file.readlines()))
elif choice == 2:
    # Counting the number of words in the file
    print("Number of words in the file: ", len(file.read().split()))
elif choice == 3:
    # Counting the number of characters in the file
    print("Number of characters in the file: ", len(file.read()))
elif choice == 4:
    # Printing each line in the file in reverse order
    for line in file.readlines():
        print(line[::-1])
else:
    # If the choice is invalid
    print("Invalid choice")
    
# Closing the file
file.close()
