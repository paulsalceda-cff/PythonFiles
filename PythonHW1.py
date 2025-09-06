
# 1.1
print("\n-- 1.1 --")
for i in range(1,51):
    print(i)

# 1.2
print("\n-- 1.2 --")
a = int(input("Enter a starting number: "))
for i in range(0,101,a):
    print(i)

# 1.3
print("\n-- 1.3 --")
b = int(input("Enter a starting number: "))
while (b>0):
    print(b)
    b -= 1
print("Blast off!")

# 2.1
print("\n-- 2.1 --")
def add(a, b):
    return a+b 

def subtract(a, b):
    return a-b 

def multiply(a, b):
    return a*b 

def divide(a, b):
    return a/b

print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

c = int(input("Enter choice: "))
d = int(input("Enter first number: "))
e = int(input("Enter second number: "))
f = 0
if (c == 1):
    f = add(d,e)
elif (c == 2):
    f = subtract(d,e)
elif (c == 3):
    f = multiply(d,e)
elif (c == 4):
    f = divide(d,e)
else:
    f = "Invalid Setting"

print("Result:", f)

# 2.2
print("\n-- 2.2 --")
import random 
def guess_number():
    secret_number = random.randint(1,20)
    while (True):
        guess = int(input("Guess a number from 1 to 20: "))
        if (guess > secret_number):
            print(guess, "is too high")
        elif (guess < secret_number):
            print(guess, "is too low")
        elif (guess == secret_number):
            print(guess, "is correct! :D")
            break

guess_number()