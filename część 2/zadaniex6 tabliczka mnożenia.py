# x = [1, 2, 3]
#
# for i in x:
#     print(f"{i:3}", end="")

# list1 = list(range(1,9))
# list2 = range(1,9)

print(" \t", end="")
for x in range(1, 11):
    print(f"{x:4}", end="")
print("\n")


for x in range(1, 11):
    print(f"\n{x}\t", end="")
    for y in range(1, 11):
        print(f"{x*y:4}", end=f"")

