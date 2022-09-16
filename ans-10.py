#Write a python program to create a function to check whether a given number is even or odd

def evenodd(num):
    if num%2==0:
        print(num , "is even")
    else:
        print(num , "is odd")    

n=int(input("Enter a number :"))       
evenodd(n) 