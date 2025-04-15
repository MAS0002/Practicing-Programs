firstname=input("please enter your first name:")
print("hello",firstname)

firstname = input("please enter your first name")
surname = input("please enter your surname")
print("hello",firstname,surname)

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)


sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



for i in range(1, 6):
    print("*" * i)


numbers = [1, 2, 3, 4, 5, 6, 7]
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

