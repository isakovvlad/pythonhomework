class Polynom:
    
    def __init__(self, coefs = None):
        self.coefs = coefs or [0]

    def __add__(self, poly):
        res = Polynom(list(map(lambda x, y : x + y, self.coefs, poly.coefs)))
        res.coefs.extend(self.coefs[len(poly.coefs):] if len(self.coefs) > len(poly.coefs) else poly.coefs[len(self.coefs):])
        return res 

    def __sub__(self, v):
        res = self + (-1) * v
        return res

    def __mul__(self, v):
        if isinstance(v, int) or isinstance(v, float):
            return Polynom(list(map(lambda x : x * v, self.coefs)))
        else:
            res = Polynom([0 for i in range(len(self.coefs) + len(v.coefs) - 1)])
            for i in range(len(self.coefs)):
                for j in range(len(v.coefs)):
                    res.coefs[i + j] += self.coefs[i] * v.coefs[j]
            return res

    def __rmul__(self, v):
        return Polynom(list(map(lambda x : x * v, self.coefs)))

    def __floordiv__(self, v):
        if len(self.coefs) < len(v.coefs):
            return Polynom([0])
        res = Polynom([0 for i in range(len(self.coefs) - len(v.coefs) + 1)])
        f = Polynom(self.coefs)
        for i in range(len(res.coefs) - 1, -1, -1):
            res.coefs[i] = f.coefs[-1] / v.coefs[-1]
            s = Polynom([0 for j in range(i + 1)])
            s.coefs[-1] = res.coefs[i]
            f -= s * v
            f.coefs = f.coefs[:len(f.coefs) - 1]
        return res
    
    def __mod__(self, arg):
        if len(self.coefs) < len(arg.coefs):
            return self
        else:
            res = self - arg * (self // arg)
            return res
    
    def derivative(self):
        res = Polynom([0 for i in range(len(self.coefs) - 1)])
        for i in range(len(self.coefs) - 1):
            res.coefs[i] = self.coefs[i + 1] * (i + 1)
        return res
    
    def FindValue(self, point):
        result = 0
        if len(self.coefs) == 0:
            return result 
        for i in range(len(self.coefs)):
            result += self.coefs[i] * (point ** i)
        return result
        
    def __str__(self):
        res = ""
        for i in range(len(self.coefs) - 1, -1, -1):
            if self.coefs[len(self.coefs) - i - 1] != 0:
                if (i == len(self.coefs) - 1) and (len(self.coefs) != 1):
                    if self.coefs[len(self.coefs) - i - 1] > 0:
                        res += " {}x^{}".format(self.coefs[len(self.coefs) - i - 1], i)
                    else:
                        if self.coefs[len(self.coefs) - i - 1] < 0:
                            res += " - {}x^{}".format(abs(self.coefs[len(self.coefs) - i - 1]), i)
                else:
                    if (len(self.coefs) == 1):
                        if self.coefs[len(self.coefs) - i - 1] > 0:
                            res += " {}".format(self.coefs[len(self.coefs) - i - 1])
                        else:
                            res += " - {}".format(abs(self.coefs[len(self.coefs) - i - 1]))
                    else:
                        if i == 0:
                            if self.coefs[len(self.coefs) - i - 1] > 0:
                                res += " + {}".format(self.coefs[len(self.coefs) - i - 1])
                            else:
                                res += " - {}".format(abs(self.coefs[len(self.coefs) - i - 1]))
                        else:
                            if self.coefs[len(self.coefs) - i - 1] == 0:
                                continue
                            elif abs(self.coefs[len(self.coefs) - i - 1]) == 1:
                                if self.coefs[len(self.coefs) - i - 1] == -1:
                                    res += " - x^{}".format(len(self.coefs) - i - 1)
                                else:
                                    res += " + x^{}".format(len(self.coefs) - i - 1)
                            else:
                                if self.coefs[len(self.coefs) - i - 1] > 0:
                                    res += " + {}x^{}".format(self.coefs[len(self.coefs) - i - 1], i)
                                else:
                                    res += " - {}x^{}".format(abs(self.coefs[len(self.coefs) - i - 1]), i)
        return res

def Newton(points, values):
    res = Polynom([values[0]])
    p = Polynom([1])
    for i in range(1, len(values)):
        buf = Polynom([1])
        p *= Polynom([-points[i - 1], 1])
        buf *= values[i] - res.FindValue(points[i])
        for j in range(0, i):
            buf *= (1 / (points[i] - points[j]))
        res += buf * p
    return res

def Sturm(polynom):
    sturm = []
    sturm.append(polynom)
    sturm.append(polynom.derivative())
    while True:
        p = -1 * sturm[-2] % sturm[-1]
        sturm.append(p)
        if len(p.coefs) == 1:
            break
    return sturm

def Secushaya_method(f, l, r):
    rt = l - ((r - l) * f(l)) / (f(r) - f(l))
    while abs(f(rt)) < 10**(-8):
        if f(rt) * f(l) < 0:
            r = rt
        elif f(rt) * f(r) < 0:
            l = rt
        rt = l - ((r - l) * f(l)) / (f(r) - f(l))
    return rt

def RootCount(left, right, sturm):
    ChangeLeft = 0
    ChangeRight = 0
    LeftVal = sturm[0].FindValue(left)
    RightVal = sturm[0].FindValue(right)
    for i in sturm:
        if LeftVal * i.FindValue(left) < 0:
            ChangeLeft += 1
            LeftVal = i.FindValue(left)      
    for i in sturm:
        if RightVal * i.FindValue(right) < 0:
            ChangeRight += 1
            RightVal = i.FindValue(right)   
    return ChangeLeft - ChangeRight
 
def Tangent(func, deriv, initial, left, right):
    x_k = initial
    c = 0
    while abs(func(x_k)) > 1e-08 and c < 10000:
        if x_k > right or x_k < left:
            print("Something wrong")
            break
        x_k = x_k - func(x_k) / deriv(x_k)
        c += 1
    return x_k

def MegaLutiPoisk(function, l, r):
    mid = 0
    while r - l - 10**(-8) > 0:
        mid = (r + l) / 2
        if abs(function(mid)) < 10**(-8):
            return mid
        if function(mid) * function(l) < 0:
            r = mid
        elif function(mid) * function(r) < 0:
            l = mid
    return mid

def PolynomRoots(function, sturm, l, r):
    if RootCount(sturm, l, r) == 0:
        return ["bruh..........."]
    elif RootCount(l, r, sturm) == 1:
        return [MegaLutiPoisk(function, l, r)]
    else:
        return (PolynomRoots(function, sturm, l, (r + l) / 2) + PolynomRoots(function, sturm, (r + l) / 2, r))
