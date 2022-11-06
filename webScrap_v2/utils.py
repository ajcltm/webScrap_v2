import time
import random

def randomSleep(func):
    def wrapper(*args, **kwargs):
        range_option = {'quicker': [0, .5], 'slower': [.5, 2], 'stop': [10, 15]}
        sleepLevel = random.choices(['quicker', 'slower', 'stop'], weights=[.6, .39, .01])
        range = range_option.get(sleepLevel[0])
        if sleepLevel[0] == 'stop' : print('Now taking a rest in a seconds')
        time.sleep(random.uniform(range[0], range[1]))
        return func(*args, **kwargs)
    return wrapper
