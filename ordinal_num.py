list  = []
for _ in range(10):
    list.append(_)
print(list)

for n in list:
    if n == 1:
        print(f"{n}st")
    if n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    elif n == 4:
        print(f"{n}th")
    elif n == 5:
        print(f"{n}th")
    else:
        print(f"{n}th")