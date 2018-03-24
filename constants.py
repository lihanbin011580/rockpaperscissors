'''
This file will define constants as needed in this project.
There is no logic control in this file except assigning values.
'''

#Constants that represent moves
INVALID = 0
ROCK = 1
PAPER = 2
SCISSORS = 3

#Constants that represent game status
PLAYER_WINS = 1
COMPUTER_WINS = 2 
TIE = 3

#File constants
MAX_RECORDS = 1000
HIST_FILE = 'player_move_history.txt'
EVAL_SEQ_NUM = 2
WINDOW = EVAL_SEQ_NUM + 1
SEQ_FILE = 'player_move_sequence.txt'
GAME_STATS_FILE='game_stats.txt'

#Collect stats
# How many games to play before collecting stats
GAMES_PER_STATS_COLLECTION = WINDOW

