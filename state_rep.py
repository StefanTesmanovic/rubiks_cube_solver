from constants import *
import numpy as np



class rotation:
    def __init__(self):
        self.orientation = '0' # nothing
        return
    def __init__(self, orientation):
        self.orientation = orientation
        return
    
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        """Override NumPy ufuncs for custom behavior."""
        
        if method != "__call__":
            return NotImplemented  

        values = [x.orientation if isinstance(x, rotation) else x for x in inputs]

        if ufunc == np.multiply:
            if values[0] == '0' or values[1] == '0': return rotation('0') 
            result = mul_table[ord(values[0]) - ord('a')][ord(values[1]) - ord('a')]
        else:
            result = ufunc(*values, **kwargs)  

        return rotation(result)
    
    def __mul__(self, b):
        if(self.orientation != '0' and b.orientation != '0'):
            print(self.orientation, b.orientation, self.mul(b))
        return rotation(self.mul(b))
    
    def __add__(self, b):
        if b.orientation == '0': return rotation(self.orientation)
        if self.orientation == '0': return rotation(b.orientation)
        return rotation(self.orientation)

    def mul(self, b):
        if self.orientation == '0' or b.orientation == '0': return rotation('0')
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
    
    vec_to_matrix_dict = {} # name of cubie, rotation, location
    for i in cubies_order_no_empty:
        vec_to_matrix_dict[i] = {}
        for q in orientations.keys():
            sides = rot_cubie(q, cubies[i])
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
            vec_to_matrix_dict[i][q] = cubies_order[l_i*3 + w_i + h_i*length*width]
        

    @staticmethod
    def vec_to_matrix(vec):
        matrix = np.full((26, 26), rotation('0'), dtype=object)
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
                print(j)
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
                h_i = 0'''
            #print(cubies_order[l_i*3 + w_i + h_i*length*width])
        for i in range(len(vec)):
            pos = cubie.vec_to_matrix_dict[chr(ord("A")+i)][vec[i]]
            matrix[i][ord(pos)-ord('A')] = rotation(vec[i])
        return matrix # make it be a numpy matrix

    def mul_vec(vec1, vec2):
        resault = []
        for i in range(len(vec1)):
            pos = cubie.vec_to_matrix_dict[chr(ord("A")+i)][vec1[i]]
            print(chr(ord("A")+i),vec1[i], pos)
            print(vec2[ord(pos) - ord('A')], mul_table[ord(vec1[i]) - ord('a')][ord(vec2[ord(pos) - ord('A')]) - ord('a')])
            resault.append(mul_table[ord(vec1[i]) - ord('a')][ord(vec2[ord(pos) - ord('A')]) - ord('a')]) # just multiplication of orientations
        return resault




#print(cubie.rot_cubie('e', cubies['A']))
#cubie.vec_to_matrix("okplokplkookplplolkpgjifaa")
#print(cubie.vec_to_matrix_dict['A']['w'])
''' numpy stuff doesn't work and is probably inefficient because of how sparse the matrix is
A = cubie.vec_to_matrix("okplokplkookplplolkpgjifaa")
B = cubie.vec_to_matrix("aaaaaaaaaaaaaaaaaaaaaaaaaa") # cubie.vec_to_matrix("aaffaaffaaaaffffaaaaaafaaa")

resault = np.matmul(A, B)
for row in resault:
            print([obj.orientation for obj in row])'''
print(cubie.mul_vec("okplokplkookplplolkpgjifaa", moves["U"])) 