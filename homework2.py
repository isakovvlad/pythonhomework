import math

class Complex():
    
    def __init__(self, other, i):
        self.other = other
        self.i = i

    def __add__(self, a):     
        return Complex(self.other + a.other, self.i + a.i)

    def __sub__(self, a):
        return Complex(self.other - a.other, self.i - a.i)

    def __mul__(self, a):
        return Complex(self.other * a.other - self.i * a.i, self.other * a.i + self.i * a.other)

    def __truediv__(self, a):
        return Complex((self.other * a.other + self.i * a.i) / (a.other ** 2 + a.i ** 2), (self.i * a.other - self.other * a.i) / (a.other ** 2 + a.i ** 2))

    def __abs__(self):
        return Complex((self.other ** 2 + self.i ** 2) ** 0.5, 0)
        
    def angle(self):
        return math.atan2(self.other, self.i)
        
    def __eq__(self, a):
        return self.other == a.other and self.i == a.i
        
    def trig(self):
        mod = (self.other ** 2 + self.i ** 2) ** 0.5
        alpha = math.atan(abs(self.i / self.other))
        if self.i >= 0 and self.other >= 0:
            beta = alpha
        if self.i < 0 and self.other >= 0:
            beta = math.pi * 2 - alpha
        if self.i >= 0 and self.other < 0:
            beta = math.pi - alpha
        if self.i < 0 and self.other < 0:
            beta = math.pi + alpha
        return '%.2f(cos(%.2f) + i*sin(%.2f))' % (mod, beta, beta)
        
    def __str__(self):
        if self.i == 0:
            return '%.2f + 0.00i' % (self.other)
        elif self.other == 0:
            if self.i >= 0:
                return '0.00 + %.2fi' % (self.i)
            else:
                return '0.00 - %.2fi' % (abs(self.i))
        elif self.i > 0:
            return '%.2f + %.2fi' % (self.other, self.i)
        elif self.i < 0:
            return '%.2f - %.2fi' % (self.other, abs(self.i))
