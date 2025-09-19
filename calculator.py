# a = float(input())
# b = float(input())
# c = input(" \n 1. Add \n 2.Sub \n 3.Mul \n 4.Divide \n Enter Operation: ")
a = float(os.getenv("NUM1", 0))
b = float(os.getenv("NUM2", 0))
c = float(os.getenv("NUM3", 0))

if c == "1" or c.lower() == "add":
    ans = a + b
elif c == "2" or c.lower() == "sub":
    ans = a - b
elif c == "3" or c.lower() == "mul":
    ans = a * b
elif c == "4" or c.lower() == "divide":
    ans = a / b
else:
    print("Invalid input")

print("ans: ", ans)

input()