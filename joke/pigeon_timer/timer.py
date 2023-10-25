import playsound
import time
import argparse
import random
from src import ascii
from src import voice
import sys
sys.dont_write_bytecode = True

parser = argparse.ArgumentParser()
parser.add_argument("--s", type=int, default=60)
args = parser.parse_args()
asc = ascii.pigeons_ascii

def timer(seconds):
    for second in range(seconds, -1, -1):
        time.sleep(1)
        print("\r"+str(second)+"/"+str(seconds),end="")
    print("\r"+str("Nice Bird..."),end="")

timer(args.s)
print(asc)
playsound.playsound("src/voice/" + random.choice(voice.voice_list))