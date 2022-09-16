# Write a python program to create a function that finds a maximum of four numbers.

def max1(*greatest):
    print("max is: ",max(greatest))

print("enter four numbers :")
n1,n2,n3,n4=int(input()),int(input()),int(input()),int(input())
max1(n1,n2,n3,n4)    