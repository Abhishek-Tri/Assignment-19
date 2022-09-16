#Write a python program to create a function which expects an unknown number of arguments.

def unknown(*t):
    print(t)

unknown(22)    
unknown(22,33)
unknown(22,33,44)