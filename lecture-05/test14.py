import random
heads = 1
tails = 2
tosses = 10

def tosses_coin():
    for toss in range(tosses):
        result = random.randint(1, 2)
        if result == heads:
            print("Heads")
        else:
            print("Tails")

tosses_coin()