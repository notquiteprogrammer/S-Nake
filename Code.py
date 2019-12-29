#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 00:53:24 2019

@author: notquiteprogrammer
"""

'''
S-nake is a tetris bot coded on Python.
Functions coded by notquiteprogrammer (check out his GitHub!)
'''

'''
Section for game rule vars.  Current vars are based on PPT.
'''

#line clear values
combodamage = (0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5)
tspindamage = (2, 4, 6)
normaldamage = (0, 1, 2, 4)
b2bbonus = 1

#time delay values
holdtime = 1 #hold piece
hshifttime = 1 #shift horizontally
softdroptime = 1 #approximate
locktime = 5 #time between piece locks
cleartime = (22, 24, 25, 27) #single is 22, double is 24, etc. Found by counting frames on youtube videos.


'''
Section for game state.
'''

class boardstate(main):
    '''
    This acts as a board state.
    '''
    def __init__(self):
        pass

'''
Section for game state vars.
'''

currentcombo = 0
tspin = False



def main(boardstate, queue):
    '''Allocates time between different search methods.
    Allocations depend on risk-reward function;  that is,
    main tries to maximize "promising" methods which provide
    large damage sent in small amount of time.
    Modeled after A* pathfinding algorithms.
    Takes in current board state and queue.
    Outputs series of moves.
    '''
    pass

'''
Stacking methods go here.
All methods use current board state, and current queue.
Certain methods (notably, survival and pcfinder) use opponent's board state.
'''

def downstack(boardstate, queue):
    '''
    Finds the longest downstack possible.
    If two downstacks last to end of queue, submits endstates to
    eval function to determine which sequence is more likely to
    continue.
    Submits the longest continuation it can find.
    '''
    pass

def disrupt(boardstate, queue):
    '''
    Finds shortest path to send lines, prioritizes odd number of lines.
    Used mainly to disrupt perfect clears in vs. bot play, or to spike opponent.
    '''

def survival(boardstate, queue):
    '''
    Finds shortest path
    '''
   
def fourwide(boardstate, queue):
    '''
    Finds optimal sequence for building a 4-wide.
    Only activated when 4-wide mode is on.
    '''
   
def pcfinder(boardstate, opponentboardstate, queue, opponentqueue):
    '''
    Finds fastest method for a perfect clear.
    Uses "disrupt" method on the opponent's board.  
    '''
   
'''
Helper functions go here.
'''

def movetype(boardstate, move, piece):
    '''
    Determines what type of line clear takes place.
    Requires board state, move sequence, and piece.
    '''
    if piece == 't':
        #calculate whether piece is a t-spin
    else:
        #calculate whether piece is a line clear
        pass
    pass

def timecalc(moveplan):
    '''
    Calculates the time it takes for the inputted move, or series of moves, to be executed.
    '''
    pass

def timetospike(boardstate, queue):
    '''
    Heuristic for estimating time to sending 2+ or 4+ lines.
    Takes in board state and piece queue, outputs time taken.
    '''
    pass

def pathfinder(boardstate, piece, position):
    '''
    Takes in current board state, piece, and position.
    Outputs a boolean for whether path is feasible, inputs required,
    amount of paths, amount of
    '''
    pass

def heuristic(boardstate):
    '''
    Takes in a board state.
    Returns statistics on:
        - How many holes?
        -
    '''
