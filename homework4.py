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
    
    def determinant(self):
        if self.rows != self.cols:
            return 'Неверные данные'
        acp = Matrix(self.rows, self.cols, self.matrix)
        for q in range(self.rows):
            for i in range(q + 1, self.rows):
                if acp.matrix[q][q] == 0:
                    acp.matrix[q][q] == 10 ** 18
                k = acp.matrix[i][q] / acp.matrix[q][q] 
                for j in range(self.rows): 
                    acp.matrix[i][j] = acp.matrix[i][j] - k * acp.matrix[q][j]
        det = 1
        for i in range(self.rows):
            det *= acp.matrix[i][i] 
        return det
    
    def LU(self):
        if self.rows != self.cols:
            return 'Неверные данные'
        L, U = Matrix(self.rows, self.cols, [[0] * self.rows for i in range(self.rows)]), Matrix(self.rows, self.cols, [[0] * self.rows for i in range(self.rows)])
        for i in range(self.rows):
            L.matrix[i][i] = 1
            for h in range(i, self.rows):
                U.matrix[i][h] = self.matrix[i][h] - sum(L.matrix[i][k] * U.matrix[k][h] for k in range(i))
            for h in range(i + 1, self.rows):
                L.matrix[h][i] = self.matrix[h][i] / U.matrix[i][i] - sum(L.matrix[h][k] * U.matrix[k][i] for k in range(i)) / U.matrix[i][i]
        return L, U
        
    def QR(self):
        Q, R = Matrix(self.rows, self.cols, [[0.] * self.cols for i in range(self.rows)]), Matrix(self.rows, self.cols, [[0.] * self.cols for i in range(self.cols)])
        for j in range(self.cols):
            v = [self.matrix[i][j] for i in range(self.rows)]
            for i in range(j):
                R.matrix[i][j] = sum(q * w for q, w in zip(Q.matrix[i], v))
                v = [q + w for q, w in zip(v, [-R.matrix[i][j] * e for e in Q.matrix[i]])]
            R.matrix[j][j] = sum(q * w for q, w in zip(v, v)) ** 0.5
            Q.matrix[j] = [q / R.matrix[j][j] for q in v]
        return Q, R

    def __str__(self):
        out = ''
        for i in range(self.rows):
            out += str(self.matrix[i])
        return out
