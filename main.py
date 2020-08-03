import random
import time
import os

outcomes = list(range(1,7))

while True:
    i = random.randint(1,6)
    temp = outcomes[i]
    print("Rolling the Dice...")
    time.sleep(1)
    print("Outcome >>>",temp)

    userInp = input("Do you want to Roll the Dice again?(y/n) ")
    if userInp.lower() == "y":
        continue
    if userInp.lower() == "n":
        exit()
    else:
        continue
     