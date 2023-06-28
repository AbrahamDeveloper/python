import random

def coin_toss():
    """Simulates a coin toss."""
    sides = ["Heads", "Tails"]
    result = random.choice(sides)
    return result

def play_coin_toss_game(num_tosses):
    """Plays the coin toss game for the given number of tosses."""
    heads_count = 0
    tails_count = 0

    for _ in range(num_tosses):
        result = coin_toss()
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print(f"Number of tosses: {num_tosses}")
    print(f"Heads count: {heads_count}")
    print(f"Tails count: {tails_count}")

# Play the coin toss game with 10 tosses
play_coin_toss_game(10)
