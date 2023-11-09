"""while True:
    n = int(input("What's n?"))
    if n > 0:
        break

cat = 3
while cat != 0:
    print('meow')
    cat = cat -1


for _ in range(n):
    print("meow")"""

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n  > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()



