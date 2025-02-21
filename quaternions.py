from sympy import sqrt, simplify, Rational


class quaternion:

    def __init__(self, r, i, j, k):
        self.r = r
        self.i = i
        self.j = j
        self.k = k
    
    def __eq__(self, other):
        if isinstance(other, quaternion):
            return self.r.evalf() == other.r.evalf() and self.i.evalf() == other.i.evalf() and self.j.evalf() == other.j.evalf() and self.k.evalf() == other.k.evalf()
            #return simplify(self.r - other.r) == 0 and simplify(self.i - other.i) == 0 and simplify(self.j - other.j) == 0 and simplify(self.k - other.k) == 0
        return False 

    @staticmethod
    def mul(a, b):
        r = a.r*b.r - a.i*b.i - a.j*b.j - a.k*b.k
        i = a.r*b.i + b.r*a.i + a.j*b.k - a.k*b.j
        j = a.r*b.j + b.r*a.j - a.i*b.k + a.k*b.i
        k = a.r*b.k + b.r*a.k + a.i*b.j - a.j*b.i
        return quaternion(r, i , j, k)

    def sgnH(self):
        if self.r > 0 or (self.r == 0 and self.i > 0) or (self.r == self.i == 0 and self.j > 0) or (self.r == self.i == self.j == 0 and self.k > 0): return 1
        if self.r == self.i == self.j == self.k == 0: return 0
        return -1
        
    def absH(self):
        sgn = self.sgnH()
        return quaternion(Rational(sgn)*self.r, Rational(sgn)*self.i, Rational(sgn)*self.j, Rational(sgn)*self.k)
    