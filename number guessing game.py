from random import randint #import random module
rand=randint(1,100)
n=0
attempts=0
while n!=rand:
    attempts=attempts+1
    n=int(input("please enter number 1 to 100 "))
    if n<rand:    
        print("please enter larger number")
    if n>rand:
        print("please enter smaller number")
    if n==rand:
        print("you have guessed correct number")
print("number of attempts you have taken to guess correctly", attempts)