#Write a python program to create a function to check whether a number falls in a given range.

def rangecheck(num):
    if num>=99 and num<1000:
        print("number falls in 3 digit number catagory")
    else:
        print("number is not under 3 digit catagory")    

n=int(input("Enter a number :"))       
rangecheck(n) 
