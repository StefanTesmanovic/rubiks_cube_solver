from constants import *
import numpy as np



class rotation:
    def __init__(self):
        self.orientation = 'a'
        return
    def __init__(self, orientation):
        self.orientation = orientation
        return
    
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        """Override NumPy ufuncs for custom behavior."""
        
        if method != "__call__":
            return NotImplemented  # Only handle function calls

        values = [x.orientation if isinstance(x, rotation) else x for x in inputs]

        # Custom multiplication rule: Multiply and add 1
        if ufunc == np.multiply:
            result = mul_table[ord(values[0]) - ord('a')][ord(values[0]) - ord('a')]
        else:
            result = ufunc(*values, **kwargs)  # Apply NumPy's default function

        return rotation(result)
    
    def mul(self, b):
        return mul_table[ord(self.orientation) - ord('a')][ord(b.orientation) - ord('a')]

    def set_rotation(self, rot):
        if 0 <= ord(rot) - ord('a') <= ord('x') - ord('a'):
            self.orientation = rot
            return True
        return False
    
class cubie:
    def __init__(self, name):
        # sides = [0:front, 1:back, 2:right, 3:left, 4:up, 5:bottom]
        return
    
    @staticmethod
    # (rotation, sides)
    def rot_cubie(q, sides_orig:list):
        sides = sides_orig.copy()
        q = orientations_v2[q]
        for i in q:
            match i:
                case 'i':
                    sides[0], sides[5], sides[1], sides[4] = sides[5], sides[1], sides[4], sides[0]
                case 'j':
                    sides[0], sides[2], sides[1], sides[3] = sides[2], sides[1], sides[3], sides[0]
                case 'k':
                    sides[4], sides[2], sides[5], sides[3] = sides[3], sides[4], sides[2], sides[5]
                case 'w':
                    sides[0], sides[5], sides[1], sides[4] = sides[4], sides[0], sides[5], sides[1]
                case 'a':
                    sides[0], sides[2], sides[1], sides[3] = sides[3], sides[0], sides[2], sides[1]
                case 's':
                    sides[4], sides[2], sides[5], sides[3] = sides[2], sides[5], sides[3], sides[4]
        return sides
    
    
    @staticmethod
    def vec_to_matrix(vec):
        matrix = []
        '''
        for i in range(len(vec)):
            c = chr(ord('A') + i)
            sides = cubie.rot_cubie(vec[i], cubies[c])
            if i < len(cubies_corners):
                for j in cubies_corners:
                    cnt = 0
                    for k in zip(sides, cubies[j]):
                        if k[0] == k[1] == 'n':
                            cnt += 1
                    if(cnt == 3):
                        print(j)
                        break
            elif i < len(cubies_corners) + len(cubies_edges):
                for j in cubies_edges:
                    cnt = 0
                    for k in zip(sides, cubies[j]):
                        if k[0] == k[1] == 'n':
                            cnt += 1
                    if(cnt == 4):
                        print(j)
                        break
        else:
            for j in cubies_centers:
                print(j)'''
        for i in range(len(vec)):
            c = chr(ord('A') + i)
            sides = cubie.rot_cubie(vec[i], cubies[c])
            l_i, w_i, h_i = 1, 1, 1
            if sides[0] != 'n':
                l_i = 0
            if sides[1] != 'n':
                l_i = length-1
            if sides[2] != 'n':
                w_i = width-1
            if sides[3] != 'n':
                w_i = 0
            if sides[4] != 'n':
                h_i = height-1
            if sides[5] != 'n':
                h_i = 0
            print(cubies_order[l_i*3 + w_i + h_i*length*width])
                

        
        return matrix # make it be a numpy matrix



#print(cubie.rot_cubie('e', cubies['A']))
cubie.vec_to_matrix("okplokplkookplplolkpgjifaa")