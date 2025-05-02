def harmonic(n):
    if n <= 0:
        return 0
    sum = 0.0
    for i in range(1, n+1 ):
        if i != 1:
            print(f"+ 1 / {i} ",end="")
        sum += 1 / (i)
    return sum

print("NAME: SMIT A PATIl")
print("UID: 24003169")

n = int(input("Enter the number of terms: "))
print("1 ", end="")

result = harmonic(n)
print(f"harmonic sum od series to {n} terms is {result}")
