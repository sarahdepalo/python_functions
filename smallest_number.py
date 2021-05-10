#Use a for loop to find the smallest number in a list.
#Write a function that accepts a list of numbers and returns the smallest number in the list

def find_smallest(list_of_numbers):
    smallest = list_of_numbers[0]
    for num in list_of_numbers:
        if num < smallest:
            smallest = num
    print("the smallest number is %s" % str(smallest))  
        

myListofNums = [3, 2, 1]
find_smallest(myListofNums)

#Write a function that accepts a list of numbers as an argument and returns the largest number in the list.

def largest(list_of_numbers):
    largest = list_of_numbers[0]
    for num in list_of_numbers:
        if num > largest:
            largest = num
    print("The largest number is %s" % str(largest))

myListofNums = [4, 5, 55]
largest(myListofNums)

#Make a function that gets the shortest string out of a list:

def shortest_string(list_of_strings):
    start = list_of_strings[0] #starts by looking at the first string.
    for string in list_of_strings: #goes through every string in the list
        if len(string) < len(start): 
            start = string #assigns start the smallest string each time. 
    print("The shortest word is: " + start)


myWords = ["Foo", "their", "alakazam"]
shortest_string(myWords)

#Make a function that gets the longest string out of a list:

def longest_string(list_of_strings):
    start = list_of_strings[0]
    for string in list_of_strings:
        if len(string) > len(start):
            start = string
    print("The longest word is: " + start)
    
longest_string(myWords)