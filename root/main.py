import time
import random

fastest_time = None
for attempt in range(5):
    print("ATTEMPT 1", attempt +1)
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    start_time = time.monotonic()
    input("Click enter RIGHT NOW or U NEED FOOD")

    end_time = time.monotonic()
    reaction_time = end_time - start_time

    if fastest_time is None:
        fastest_time = reaction_time

    if reaction_time < fastest_time:
        fastest_time = reaction_time


    print("Reaction time:", round(reaction_time, 3))
    print(f"Displayed fastest time",fastest_time)
    print("well done")



