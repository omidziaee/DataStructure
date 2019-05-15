'''
Created on Dec 28, 2018

@author: omid
'''
import random

def get_random(floor, cieling):
    return random.randrange(floor, cieling + 1)


print get_random(1, 5)