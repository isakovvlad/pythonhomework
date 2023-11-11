class Matrix():
    
    def __init__(self, rows, cols, matrix = None):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix or []

    def __add__(self, m):
        if (self.rows != m.rows or self.cols != m.cols):
            return 'Неверно задана размерность'
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            res.matrix.append(list(map(lambda x, y : x + y, self.matrix[i], m.matrix[i])))
        return res
     
    def __sub__(self, m):
        if (self.rows != m.rows or self.cols != m.cols):
            return 'Неверно задана размерность'
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            res.matrix.append(list(map(lambda x, y : x - y, self.matrix[i], m.matrix[i])))
        return res

    def __mul__(self, el):
        if isinstance(el, int):
            r = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                r.matrix.append(list(map(lambda x : el * x, self.matrix[i])))
            return r
        elif isinstance(el, Matrix):
            if (self.cols != el.rows):
                return 'Неверно задана размерность'
            r = Matrix(self.rows, el.cols)
            for i in range(self.rows):
                mascp = []
                for j in range(el.cols):
                    c = 0
                    for k in range(self.cols):
                        c += (self.matrix[i][k] * el.matrix[k][j])
                    mascp.append(c)
                r.matrix.append(mascp)
            return r
        else:
            return 'Неверные данные'

    def transpose(self, m):
        return [list(i) for i in zip(*m)]

    def getTranspose(self):
        return self.transpose(self.matrix)
    
    def gauss(self):
        for i in range(self.rows):
            mxr = i
            mx = abs(self.matrix[i][i])
            for k in range(i + 1, self.cols):
                if abs(self.matrix[k][i]) > mx:
                    mxr = k
                    mx = abs(self.matrix[k][i])
            self.matrix[i], self.matrix[mxr] = self.matrix[mxr], self.matrix[i]
            for j in range(i + 1, self.rows):
                c = -self.matrix[j][i] / self.matrix[i][i]
                for k in range(i, self.rows):
                    if i != j:
                        self.matrix[j][k] += c * self.matrix[i][k]
                    else:
                        self.matrix[j][k] = 0
    
    def gauss_answer(self, v):
        for i in range(self.rows):
            mxr = i
            mx = abs(self.matrix[i][i])
            for k in range(i + 1, self.cols):
                if abs(self.matrix[k][i]) > mx:
                    mxr = k
                    mx = abs(self.matrix[k][i])
            v[i], v[mxr] = v[mxr], v[i]
            self.matrix[i], self.matrix[mxr] = self.matrix[mxr], self.matrix[i]
            for j in range(i + 1, self.rows):
                c = -self.matrix[j][i] / self.matrix[i][i]
                for k in range(i, self.rows):
                    if i != j:
                        self.matrix[j][k] += c * self.matrix[i][k]
                    else:
                        self.matrix[j][k] = 0
                v[j] += c * v[i]
        x = [0 for i in range(self.rows)]
        for i in range(self.rows - 1, -1, -1):
            x[i] = v[i] / self.matrix[i][i]
            for k in range(i - 1, -1, -1):
                v[k] -= self.matrix[k][i] * x[i]
        return x

    def __str__(self):
        out = ''
        for i in range(self.rows):
            out += str(self.matrix[i])
        return out
