n = int(input("number of x: "))
z = 0

for x in range(999999):
    if z != n:
        for y in range(x + 1):
            if z != n:
                z += 1
                print(z, end="\t")
            elif z == n:
                print("", end="\t")
        print("\n")
