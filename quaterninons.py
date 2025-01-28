from sympy import sqrt

class quaternion:

    def __init__(self, r, i, j, k):
        self.r = r
        self.i = i
        self.j = j
        self.k = k
    
    @staticmethod
    def mul(a, b):
        r = a.r*b.r - a.i*b.i - a.j*b.j - a.k*b.k
        i = a.r*b.i + b.r*a.i + a.j*b.k - a.k*b.j
        j = a.r*b.j + b.r*a.j - a.i*b.k + a.k*b.i
        k = a.r*b.k + b.r*a.k + a.i*b.j - a.j*b.i
        return quaternion(r, i , j, k)

    def sgnH(self):
        return
    
    def absH(self):
        return 