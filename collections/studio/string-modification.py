my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

first_string = my_string[0:3]
second_string = my_string [3:]
print(f"{second_string}{first_string}")

# Use a template literal to print the original and modified string in a descriptive phrase.

my_string = "LaunchCode"

# Remove first 3 characters and add them to the end
modified_string = my_string[3:] + my_string[:3]

# Print original and modified string using a template literal
print(f"The original string was '{my_string}' and after moving the first 3 letters to the end, it becomes '{modified_string}'.")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

n = int(input("Enter the number of letters to move from the start to the end: "))
modified_string = my_string[n:] + my_string[:n]
print(f"The original string was '{my_string}' and after moving the first {n} letters to the end, it becomes '{modified_string}'.")


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
user_input = int(input("Enter the number of letters to move from the start to the end: "))
pif user_input > len(my_string):
    print(f"Error: input ({user_input}) is longer than the word. Defaulting to 3 letters.")
    n = 3
else: n = user_input
modified_string = my_string[n:] + my_string[:n]
print(f"The original string was '{my_string}' and after moving the first {n} letters to the end, it becomes '{modified_string}'.")