# Program 1: Count the total number of digits in a number
n = int(input("Enter number to count digits: "))
d = 0
count = 0

while n > 0:
    d = n % 10
    n = n // 10
    count = count + 1

print("Total digits:", count)

print("\n---------------------------------------\n")

# Program 2: Print all prime numbers within a given range
print("To print all the prime numbers in a range")
m = int(input("Enter starting range: "))
n = int(input("Enter ending range: "))

print(f"Prime numbers between {m} and {n} are:")
for num in range(m, n):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

print("\n---------------------------------------\n")

# Program 3: Display Fibonacci series up to n terms
n = int(input("Enter the number of terms for Fibonacci series: "))
a = 0
b = 1

print(f"Fibonacci series up to {n} terms:")
print(a, end=" ")

for i in range(1, n):
    print(b, end=" ")
    a, b = b, a + b

print("\n---------------------------------------\n")

# Program 4: Reverse a given number
n = int(input("Enter number to reverse: "))
d = 0
rev = 0

while n > 0:
    d = n % 10
    n = n // 10
    rev = (rev * 10) + d

print("Number reversed:", rev)
