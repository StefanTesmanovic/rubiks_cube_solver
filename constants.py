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

for i in orientations.keys():
    orientations[i] = orientations[i].absH()

mul_table = [] # the row number times the column number, different from the blog; a*b = matrix[a][b] (ord(a)-ord('a') and ord(b)-ord('b'))
for i in orientations.keys():
    temp = []
    for j in orientations.keys():
        temp.append(get_key(orientations, quaternion.mul(orientations[i], orientations[j])))
    mul_table.append(temp)
print_matrix(mul_table)



