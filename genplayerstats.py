'''
This program will collect stats on player moves by sequence.
'''

import constants
import time

def create_dict():
    count_lines = 0
    player_stats = {}
    line_array = []
    with open(constants.SEQ_FILE,'r') as s:
        for line in s:
            line_array.append(line.replace('\n',''))
            count_lines += 1
    #Add to dict
    for line_count in range(count_lines):
        if line_array[line_count] not in player_stats.keys():
            player_stats[line_array[line_count]] = 1
        else:
            player_stats[line_array[line_count]] += 1
                  
    return player_stats

'''
Execute getplayerstats.py for troubleshooting as needed
Execution time will be tracked here in case we run into performance issues.
'''
if __name__ == '__main__':
    time_1 = time.time()
    print create_dict()
    time_2 = time.time()
    print 'Exec time: ' + str(time_2 - time_1)
