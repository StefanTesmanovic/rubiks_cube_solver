from sympy import sqrt
from quaterninons import quaternion

a = quaternion(sqrt(2)/2, 0, 0, -sqrt(2)/2)
b = quaternion(0, 1, 0, 0)
c = quaternion.mul(a, b)

print(f"({c.r}, {c.i}, {c.j}, {c.k})")

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


