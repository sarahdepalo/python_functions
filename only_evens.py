#Write a function that accepts a list of numbers as an argument.
#Return a new list that inlcudes only the even numbers.

def only_evens(list):
    for num in list:
        if num % 2 == 0:
            list.append(num)
        else:
            list.remove(num)
    print(list)
        
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

only_evens(numberList)
