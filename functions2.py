#Write a function to convert a string to uppercase

def convert_to_uppercase(str):
    return str.upper()

user_input = input("Type a word of your choice! ")
#Always check your functions to make sure they work using statements like the one below to double check
# print("User Input is: " + user_input)
my_uppercase = convert_to_uppercase(user_input)

print(my_uppercase)