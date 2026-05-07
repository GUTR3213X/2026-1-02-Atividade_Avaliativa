import random
import time
from playsound3 import playsound
for i in range(10):
    random_value = random.randint(1, 100)
    if random_value == 0x43:
        random_value = f'\033[33m{random_value}\033[0m'
        playsound('SQlv2Xv.mp3')
    print(random_value)
    time.sleep(1)

