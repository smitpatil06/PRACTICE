a = int(input("Enter the 1st value to check big one: "))
b = int(input("Enter the 2nd value to check big one: "))
c = int(input("Enter the 3rd value to check big one: "))

if a > b and a > c:
    print("A is greater")
elif b > a and b > c:
    print("B is greater")
else:
    print("C is greater")

age = int(input("Enter your age to check you are eligible for vote or not: "))

if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

