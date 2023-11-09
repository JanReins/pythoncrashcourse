#try, except Value Error and else: key function
def main ():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
#            print("x is not an interger")

main ()