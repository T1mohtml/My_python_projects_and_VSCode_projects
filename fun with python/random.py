import random
import time

def flip_the_coin():
    print("flipping the coin please wait...")
    time.sleep(2)
    result = random.choice(["heads", "tails"])

    return result

if __name__ == "__main__":
    print(f"the coin landed on: {flip_the_coin()}")