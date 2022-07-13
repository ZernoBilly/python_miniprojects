list1 = [1, 2, 3, 4, 5]

for ind, val in enumerate(list1):
    if val == 3:
        list1[ind] = 10
print(list1)
