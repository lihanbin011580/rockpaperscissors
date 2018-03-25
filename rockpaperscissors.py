#Rock,paper,scissors game

from random import randint
import sys
import constants
import genplayerstats
import gengamestats
import logging

#Handle logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('stderr.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False


def play_game(p,c):
    
    if (p == c):
        return constants.TIE
    elif p == constants.ROCK:
        if c == constants.PAPER: return constants.COMPUTER_WINS
        else : return constants.PLAYER_WINS                
    elif p == constants.PAPER:
        if c == constants.SCISSORS: return constants.COMPUTER_WINS 
        else: return constants.PLAYER_WINS
    elif p == constants.SCISSORS:
        if c == constants.ROCK: return constants.COMPUTER_WINS
        else: return constants.PLAYER_WINS

def build_seq_file_by_window():
    write_str = ''
    with open(constants.HIST_FILE,'r') as h:
        #Retrieve last sequence from end of file based on window size
        try:
            h.seek(-constants.WINDOW,2)
            write_str = h.read()
            with open(constants.SEQ_FILE,'a') as s:
                s.write(write_str + '\n')
        #Handle scenario where file length is smaller than window size
        #Do nothing in this case.
        except:
            pass


def get_last_seq():
    last_seq=''
    with open(constants.HIST_FILE,'r') as h:
        try:
            h.seek(-constants.EVAL_SEQ_NUM,2)
            last_seq = h.read()
        except:
            pass
    return last_seq
			
    
			
def gen_computer_move(player_stats_dict,last_seq):
    #When there is no last sequence to check against or when player stats
    #is empty, computer will make a random move

    max_val = 0
    highest_freq_move = ''
    guess_move = ''
    tracker = {}
    
    if not last_seq or not player_stats_dict:
        logger.info('Not enough moves to determine last seq. Computer generates random move.')
        return randint(1,3)
        
    else:
        logger.info('Last Seq: ' + last_seq)
        for k,v in player_stats_dict.items(): 
            if k.startswith(last_seq):
                tracker[k[-1:]] = v
        for k,v in tracker.items():
            if v > max_val:
                max_val = v
                highest_freq_move = k
                if int(highest_freq_move) == constants.ROCK:
                    logger.info('Temp Highest Frequency Move: r')
                elif int(highest_freq_move) == constants.SCISSORS:
                    logger.info('Temp Highest Frequency Move: s')
                else:
                    logger.info('Temp Highest Frequency Move: p')
        try:
            if int(highest_freq_move) == constants.ROCK:
                logger.info('Highest Frequency Move: r')
                return constants.PAPER
            elif int(highest_freq_move) == constants.SCISSORS:
                logger.info('Highest Frequency Move: s')
                return constants.ROCK
            else:
                logger.info('Highest Frequency Move: p')
                return constants.SCISSORS
        except:
            return randint(1,3)

    
if __name__ == '__main__':    
    print 'Rock, Paper, Scissors game'

    num_player_wins = 0
    num_computer_wins = 0
    num_ties = 0
    player = constants.INVALID
    computer_move = 'x'
    player_stats = {}
    seq = ''
    while True:
        player_stats = genplayerstats.create_dict()
        '''get seq for next computer 
           get last EVAL_SEQ_NUM moves from HIST_FILE
        '''
        logger.info('Player Stats: ' + str(sorted(player_stats.items())))
        seq = get_last_seq()
        #Generate move for computer. Computer will make the first move so it can't be accused of cheating
        computer = gen_computer_move(player_stats,seq)
        if computer == constants.ROCK: computer_move = 'r'
        elif computer == constants.PAPER: computer_move = 'p'
        else: computer_move = 's'
		
        player_input = raw_input('Enter r for rock, p for paper, s for scissors, q for quit:')
        if player_input == 'q': 
            print 'Exit game.'
            logger.info('Exit game.')
            break
        if player_input == 'r': player = constants.ROCK
        elif player_input == 'p': player = constants.PAPER
        elif player_input == 's': player = constants.SCISSORS
        #Invalid input
        else:
            player = constants.INVALID
            print 'Invalid move: ' + player_input
            logger.warn('Invalid move: ' + player_input)
            continue
		
		
        result = play_game(player,computer)
        print 'Your move: ' + player_input
        logger.info('Your move: ' + player_input)
        print 'Computer\'s move: ' + computer_move
        logger.info('Computer\'s move: ' + computer_move)
        if result == constants.TIE:
            print 'Tie'
            logger.info('Tie')
            num_ties += 1
        elif result == constants.PLAYER_WINS:
            print 'You win!'
            logger.info('Player wins!')
            num_player_wins += 1
        elif result == constants.COMPUTER_WINS:
            print 'Computer wins!'
            logger.info('Computer wins!')
            num_computer_wins += 1
        else:
            print 'Invalid input.'
            logger.info('Invalid input.')
        print 'Stats for this session: Player: ' + str(num_player_wins) + ' Computer: ' + str(num_computer_wins) + ' Ties: ' + str(num_ties)
        logger.info('Stats for this session: Player: ' + str(num_player_wins) + ' Computer: ' + str(num_computer_wins) + ' Ties: ' + str(num_ties))
        
        if player != constants.INVALID:
            #Output player move to history file
            with open(constants.HIST_FILE,'a') as f:
                f.write(str(player))
        
            with open(constants.GAME_STATS_FILE,'a') as f:
                f.write(str(result))
			
        game_stats = gengamestats.create_dict()	
        
        #Assign value of 0 if dict lookup fails
        hist_stats_player_wins = str(game_stats.get(str(constants.PLAYER_WINS),0))
        hist_stats_computer_wins = str(game_stats.get(str(constants.COMPUTER_WINS),0))
        hist_stats_tie = str(game_stats.get(str(constants.TIE),0))
			
        print 'Historical stats: Player: ' + hist_stats_player_wins \
		    + ' Computer: ' + hist_stats_computer_wins \
            + ' Ties: ' + hist_stats_tie
        logger.info('Historical stats: Player: ' + hist_stats_player_wins \
		    + ' Computer: ' + hist_stats_computer_wins \
            + ' Ties: ' + hist_stats_tie)
			
        build_seq_file_by_window()

                 
        

                
            
        
