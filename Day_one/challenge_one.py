# This first challenge asks the programmer to print "Hello, World" to the console
# The programmer uses the print function

# I will further customize this file by adding a function to print "Hello, " and the user's name
# I will also create a function that prints as many "Hello, World's" as required by the user to the console

# this line prints "Hello, World" to the console using "f strings"
print(f"Hello, World!")


# This function accepts one argument and prints "Hello, " and username
def print_username(username):
    # It uses "f strings"
    print(f"Hello, {username}")

# This function uses a while loop to output "Hello, World" as many times as the user asks of
def hello_world(num_of_times):
    i = 0
    while i < num_of_times:
        print("Hello, World")
        i += 1
    print("You have printed 'Hello, World' {} times".format(num_of_times))


# A variable is created to accept any name as input from user
name = input("Enter your name: ")
# We call the function here
print_username(name)

print(f"-----------------------------------------------------------")

# calls the function hello_world
hello_world(5)
