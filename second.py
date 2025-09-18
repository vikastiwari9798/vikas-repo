import os
num1 = float(os.getenv("NUM1", 0))
num2 = float(os.getenv("NUM2", 0))


sum = num1+num2

print("The sum of", num1, "and", num2, "is", sum)