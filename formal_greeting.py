def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

# mustard = make_formal_greeting("Mustard", "Colonel")
# print(mustard)

def ask_for_user_info():
    user_name = input("What is your name? ")
    user_title = input("What is your title? ")
    print(make_formal_greeting(user_name, user_title)) #This is a callback

ask_for_user_info() #Both ask_for_user_info and make_formal_greeting can rely on each other. ask_for_user_info can be thought of as a step 2.  