# a = float(input())
# b = float(input())
# c = input(" \n 1. Add \n 2.Sub \n 3.Mul \n 4.Divide \n Enter Operation: ")
import os


a = float(os.getenv("NUM1", 0))
b = float(os.getenv("NUM2", 0))
c = (os.getenv("NUM3", "0"))

print (a, b, c) 

if c == "1":
    ans = a + b
elif c == "2":
    ans = a - b
elif c == "3":
    ans = a * b
elif c == "4":
    ans = a / b
else:
    print("Invalid input")

print("ans: ", ans)

input()




