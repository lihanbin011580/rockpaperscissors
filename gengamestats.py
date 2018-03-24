'''
This program will create stats on game history
'''

import constants
import time

def create_dict():
    count_moves = 0
    game_stats = {}
    move_array = []
    with open(constants.GAME_STATS_FILE,'r') as s:
        for line in s:
            for move in line:
                if move not in game_stats.keys():
                    game_stats[move] = 1
                else:
                    game_stats[move] += 1
                  
    return game_stats

'''
Execute getplayerstats.py for troubleshooting as needed
Execution time will be tracked here in case we run into performance issues.
'''
if __name__ == '__main__':
    time_1 = time.time()
    print create_dict()
    time_2 = time.time()
    print 'Exec time: ' + str(time_2 - time_1)
