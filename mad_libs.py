# #Write a function that accepts two arguments: a name and a subject.
# The function should return a String with the name and subject interpolated in.

def mad_lib(name, subject):
    return ("%s's favorite subject is %s." % (name, subject))

name = input("What is your name? ")
subject = input("What is your favorite subject? ")

mad_lib_sentence = mad_lib(name, subject)
print(mad_lib_sentence)