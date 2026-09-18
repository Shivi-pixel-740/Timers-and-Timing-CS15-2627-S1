import time
import random

def play_round(attempt):
    input(f"Attempt {attempt}: Press Enter to start...")

    # Wait a random time between 2 and 5 seconds
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    print("GO!")
    start_time = time.monotonic()  # time when GO appears

    input()  # wait for player to press Enter

    end_time = time.monotonic()  # time when player reacts

    reaction_time = end_time - start_time
    print(f"Reaction time: {reaction_time:.3f} seconds\n")

    return reaction_time


def main():
    print("Reaction Time Game!")
    print("Press Enter as soon as you see GO!\n")

    reaction_times = []

    for attempt in range(1, 6):
        rt = play_round(attempt)
        reaction_times.append(rt)

    fastest_time = min(reaction_times)
    print(f"Fastest reaction time: {fastest_time:.3f} seconds")


main()