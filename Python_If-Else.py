import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
    else:
        if n in range(2, 5):
            print('Not Weird')
        elif n in range(5, 20):
            print("Weird")
        else:
            print('Weird')
