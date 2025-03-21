from constants import * 
from state_rep import *
import random

class environment:
    def __init__(self, scramble_count):
        self.cube = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        for i in range(scramble_count):
            rnd_key = random.choice(list(moves.keys()))
            self.cube = cubie.mul_vec(self.cube, moves[rnd_key])
        self.scramble_count = scramble_count
        self.moves_made = 0
    def move(self, move):
        self.cube = cubie.mul_vec(self.cube, moves[move])
        self.moves_made += 1
        if self.cube == "aaaaaaaaaaaaaaaaaaaaaaaaaa": rew = 100
        else: rew = min(-1, self.scramble_count-self.moves_made)
        return self.cube, rew
    def reset(self, scr_cnt):
        self.cube = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        for i in range(scramble_count):
            rnd_key = random.choice(list(moves.keys()))
            self.cube = cubie.mul_vec(self.cube, moves[rnd_key])
        self.scramble_count = scramble_count
        self.moves_made = 0
