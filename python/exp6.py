# -------------------- Section 1: Basic Printing --------------------
print("-------- 1.1 --------")
print("Yesterday Morning")
print("Yesterday Night")
print("Today Morning")
print("Today Night")

# -------------------- Section 2: Lists --------------------
print("-------- 1.2 --------")
list1 = [10, 20, 30, 40, 50]
print("List1:", list1)

print("-------- 1.3 --------")
list2 = [11, 22, [441, 442, 443, 444, 445], 55]
print("List2:", list2)

print("-------- 1.4 --------")
list3 = [11, 33, 44, 55]
print("List3:", list3)

# -------------------- Section 3: Tuples --------------------
print("======== 2.1 ==========")
t1 = (1, 2, 3, 4)
t2 = (9, 8, 7, 6)
print("Before swapping:")
print("t1:", t1)
print("t2:", t2)

# Swapping
t1, t2 = t2, t1
print("After swapping:")
print("t1:", t1)
print("t2:", t2)

print("======== 2.2 ==========")
tuple1 = (11, 22, 33, 44, 55)
print("Element at index 2 in tuple1:", tuple1[2])

print("======== 2.3 ==========")
tuple2 = (88, 88, 88, 44, 55)
count_88 = tuple2.count(88)
print("Count of 88 in tuple2:", count_88)

# -------------------- Section 4: Dictionaries --------------------
print("======== 3.1 ==========")
dict1 = {'a': 'let US c', 'b': 'Python', 'c': 'harry potter'}
print("Dictionary 1:", dict1)

print("======== 3.2 ==========")
dict2 = {'c': 'harry potter'}
print("Dictionary 2:", dict2)

print("======== 3.3 ==========")
if "Apple" in dict1.values():
    print("Value 'Apple' exists in dict1")
else:
    print("Value 'Apple' does not exist in dict1")
