def make_formal_greeting(name, title):
    return ("This is %s, the %s" % (name, title))

def ask_for_user_info():
    user_name = input("What is your name? ")
    user_title = input("What is your title? ")
    return [user_name, user_title]

def ask_for_user_info_dictionary():
    user_name = input("What is your name? ")
    user_title = input("What is your title? ")
    return {
        "name": user_name,
        "title": user_title
    }
# print(ask_for_user_info()) 

user_info = ask_for_user_info_dictionary()
greeting = make_formal_greeting(user_info["name"], user_info["title"])
print(greeting)

