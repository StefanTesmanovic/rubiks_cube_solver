from sympy import sqrt
import quaternions
from quaternions import quaternion

def get_key(dict, value):
    for i in dict.keys():
        if dict[i].absH() == value.absH():
            return i

orientations = {
    'a':quaternion(1, 0, 0, 0), # alpha
    'b':quaternion(0, 1, 0, 0), # beta
    'c':quaternion(0, 0, 1, 0), # gamma
    'd':quaternion(0, 0, 0, 1), # delta
    'e':quaternion(sqrt(2)/2, sqrt(2)/2, 0, 0), # epsilon
    'f':quaternion(sqrt(2)/2, 0, sqrt(2)/2, 0), # zeta
    'g':quaternion(sqrt(2)/2, 0, 0, sqrt(2)/2), # eta
    'h':quaternion(sqrt(2)/2, -sqrt(2)/2, 0, 0), # theta
    'i':quaternion(sqrt(2)/2, 0, -sqrt(2)/2, 0), # iota
    'j':quaternion(sqrt(2)/2, 0, 0, -sqrt(2)/2), # kappa 
    'k':quaternion(1/2, 1/2, 1/2, 1/2), # lambda
    'l':quaternion(1/2, 1/2, -1/2, -1/2), # mu
    'm':quaternion(1/2, 1/2, -1/2, 1/2), # nu
    'n':quaternion(1/2, 1/2, 1/2, -1/2), # xi
    'o':quaternion(1/2, -1/2, 1/2, -1/2), # omicron
    'p':quaternion(1/2, -1/2, -1/2, 1/2), # pi
    'q':quaternion(1/2, -1/2, 1/2, 1/2), # rho
    'r':quaternion(1/2, -1/2, -1/2, -1/2), # sigma
    's':quaternion(0, 0, sqrt(2)/2, sqrt(2)/2), # tau
    't':quaternion(0, 0, sqrt(2)/2, -sqrt(2)/2), # upsilon
    'u':quaternion(0, sqrt(2)/2, 0, sqrt(2)/2), # phi
    'v':quaternion(0, -sqrt(2)/2, 0, sqrt(2)/2), # chi
    'w':quaternion(0, sqrt(2)/2, -sqrt(2)/2, 0), # psi
    'x':quaternion(0, sqrt(2)/2, sqrt(2)/2, 0) # omega
}

orientations_v2 = { # -i = w, -j = a, -k = s
    'a':"", # alpha   
    'b':"ii", # beta ααζζααζζααααζζζζααααααζααα
    'c':"jj", # gamma
    'd':"kk", # delta
    'e':"i", # epsilon
    'f':"j", # zeta
    'g':"k", # eta
    'h':"w", # theta
    'i':"a", # iota
    'j':"s", # kappa 
    'k':"ij", # lambda
    'l':"ia", # mu
    'm':"ai", # nu
    'n':"ji", # xi
    'o':"wj", # omicron
    'p':"wa", # pi
    'q':"jw", # rho
    'r':"aw", # sigma
    's':"ijj", # tau
    't':"wjj", # upsilon
    'u':"jkk", # phi
    'v':"akk", # chi
    'w':"sii", # psi
    'x':"kii" # omega
}

for i in orientations.keys():
    orientations[i] = orientations[i].absH()

mul_table = [] # the row number times the column number, different from the blog; a*b = matrix[a][b] (ord(a)-ord('a') and ord(b)-ord('b'))
for i in orientations.keys():
    temp = []
    for j in orientations.keys():
        temp.append(get_key(orientations, quaternion.mul(orientations[i], orientations[j])))
    mul_table.append(temp)
cubies_order_no_empty = "AIBKXLEJFQURYZTVSCMDOWPGNH"
cubies_order = "AIBKXLEJFQURY0ZTVSCMDOWPGNH"
cubies_corners = "ABCDEFGH"
cubies_edges = "IJKLMNOPQRST"
cubies_centers = "UVWXYZ"

cubies = {}
width = 3
length = 3
height = 3
colors = ['g', 'b', 'r', 'o', 'w', 'y']# [0:front, 1:back, 2:right, 3:left, 4:up, 5:bottom]
for i in range(len(cubies_order)):
    if cubies_order[i] == "0": continue
    (front, back, right, left, up, bottom) = ('n', 'n', 'n', 'n', 'n', 'n') # n is for inside the cube
    w_i = i % 3
    l_i = (i % (width*height)) // 3
    h_i = i // (width*height)
    if w_i == 0: left = colors[3]
    if w_i == width-1: right = colors[2]
    if l_i == 0: front = colors[0]
    if l_i == length-1: back = colors[1]
    if h_i == 0: bottom = colors[5]
    if h_i == height-1: up = colors[4]
    cubies[cubies_order[i]] = [front, back, right, left, up, bottom]

    




