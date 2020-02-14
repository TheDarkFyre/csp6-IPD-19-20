####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Test1'
strategy_name = 'Parlov'
strategy_description = 'Check if opponent is using Tit for Tat, Suspicious Tit For Tat, or Other and will play based on that.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player plays the Parlov Strategy.
    strategy = ''

    if len(my_history) == 0:
      return 'c'
    elif len(my_history) < 7:
      return their_history[-1]
    elif len(my_history) > 7:
      if their_history[0:-5] == my_history[-1:-6]:
        strategy = 'TFT'
      elif their_history[0:-5] == ['b', 'c', 'b', 'c', 'b', 'c']:
        strategy = "STFT"
      else:
        strategy = 'R'
    
    if strategy == "TFT":
      return their_history[-1]
    if strategy == "STFT":
      if their_history[-1] == "b" and their_history[-2] == "b":
        return "b"
      else:
        return "c"
      if strategy == "R":
        return "b"