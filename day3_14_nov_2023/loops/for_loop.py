# For loop demo
print("Example 1 :")
x, y, z = int(input("Start : ")), int(input("End : ")), int(input("Interval : "))

for i in range(x, y, z):
    print(i, end="\t")
print()
print("Out of the loop")