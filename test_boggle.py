from random import randint

def lottery_numbers():

    numbers = []

    for number in range(0, 10):
         numbers.append(randint(1, 45))

    return numbers



print("This weeks lottery numbers are: %s" % lottery_numbers())


