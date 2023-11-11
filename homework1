class Vector():
    
    def __init__(self, *p):
        self.p = p 
    
    def __add__(self, t):
        k = []
        for i in range(len(self.p)):
            k.append(self.p[i] + t.p[i])
        return Vector(k)
        
    def __sub__(self, t):
        k = []
        for j in range(len(self.p)):
            k.append(self.p[j] - t.p[j])
        return Vector(k)
        
    def __mul__(self, t):
        k = 0
        for l in range(len(self.p)):
            k += self.p[l] * t.p[l]
        return k
    
    def __abs__(self):
        mod = ((self * self) ** 0.5)
        return mod
          
    def anglevectors(self, t):
        ang = ((self * t) / ((abs(self)) * (abs(t))))
        return ang

    def __str__(self):
        return str(*self.p)
