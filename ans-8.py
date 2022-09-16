#Write a python program to multiply all the numbers in a list.

def mul(l1=[]):
    print("list is: ",l1)
    multiply=1
    for i in l1:
        multiply=multiply*i
    print("multiply of list: ",multiply)

mul([5,5,7,2,1])   