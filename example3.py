####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Test4'
strategy_name = 'PBOOM'
strategy_description = '''\
Returns a random output for the first 10 rounds, then plays based on what the opponent plays
'''

import random

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history) < 10:
      return random.choice(["b", "c"])
    
    if their_history[-2] == "c":
      if their_history[-1] == "c":
        return "c"
      if their_history[-1] == "b":
        return "b"
    if their_history[-2] == "b":
      if their_history[-1] == "c":
        return "c"
      if their_history[-1] == "b":
        return "b"