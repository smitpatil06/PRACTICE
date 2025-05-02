print("------- CALCULATOR -------")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = int(input("Choose any number from above: "))

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if choice == 1:
    print("Sum of numbers is:", a + b)
elif choice == 2:
    print("Subtraction of numbers is:", a - b)
elif choice == 3:
    print("Multiplication of numbers is:", a * b)
elif choice == 4:
    if b != 0:
        print("Division of numbers is:", a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid choice")



print("------- ARMSTRONG NUMBER -------")

num = int(input("Enter any number you want to check: "))
sum = 0
temp = num
order = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print("ARMSTRONG NUMBER")
else:
    print("NOT ARMSTRONG NUMBER")



print("------- FIBONACCI SERIES -------")

n = int(input("How many Fibonacci numbers to print: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()
