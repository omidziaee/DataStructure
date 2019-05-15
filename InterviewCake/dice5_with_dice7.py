<<<<<<< HEAD
'''
Created on Dec 30, 2018

@author: omid
'''
import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    # This is naive to result = rand7() % 5
    # Initialize with a large number to start the proecss first
    result = 7
    while result > 5:
        result = rand7()

    return result


print 'Rolling 5-sided die...'
=======
'''
Created on Dec 30, 2018

@author: omid
'''
import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    # This is naive to result = rand7() % 5
    # Initialize with a large number to start the proecss first
    result = 7
    while result > 5:
        result = rand7()

    return result


print 'Rolling 5-sided die...'
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print rand5()