def greeting():
    print("Hello World") #print statements do not need an explicit return statement. 
    
# This tells python that you wrote a function and to go and find it.
greeting()

def square(x):
    print(x * x) 

square(5) #Any number you put here will use the function above!

global_variable_example = "Foo"

def local_scope_function():
    local_variable_example = "Bar"
    print(global_variable_example + " is global" + local_variable_example + " is local") #local_variable_example is only available to call on in the local scope function. It technically only exists in the localScopeFunction
local_scope_function()

