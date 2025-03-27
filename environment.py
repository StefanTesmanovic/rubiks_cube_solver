from constants import * 
from state_rep import *
import random

class environment:
    def __init__(self, scramble_count):
        self.cube = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        for i in range(scramble_count):
            rnd_key = random.randint(0, 11)
            self.cube = cubie.mul_vec(self.cube, moves_list[rnd_key])
        self.scramble_count = scramble_count
        self.moves_made = 0

    def set(self, cube):
        self.cube = cube

    def solved(self):
        return self.cube == "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    
    def move(self, move):
        self.cube = cubie.mul_vec(self.cube, moves_list[move])
        self.moves_made += 1
        if self.cube == "aaaaaaaaaaaaaaaaaaaaaaaaaa": rew = 3
        else: rew = -1 # min(r, self.scramble_count-self.moves_made)
        return self.cube, rew # mozda ubaciti da ako dodje u stanje u kom je vec bio dobije vecu negativnu nagradu jer se vrti u krug
    
    def reset(self, scr_cnt):
        self.cube = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        for i in range(scr_cnt):
            rnd_key = random.randint(0, 11)
            self.cube = cubie.mul_vec(self.cube, moves_list[rnd_key])
        self.scramble_count = scr_cnt
        self.moves_made = 0
