from random import randint, choice
lottery_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
my_ticket = 3
counter = 0
for number in lottery_numbers:
    winning_number = choice(lottery_numbers)
    if winning_number == my_ticket:
        counter += 1
print(counter)