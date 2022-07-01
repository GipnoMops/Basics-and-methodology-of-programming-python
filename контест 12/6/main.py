from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, param):
        self.param = deepcopy(param)

    def __str__(self):
        strMatrix = ''
        for i in range(len(self.param)):
            for j in range(len(self.param[1])):
                strMatrix += str(self.param[i][j])
                if j != len(self.param[1]) - 1:
                    strMatrix += '\t'
                elif i != len(self.param) - 1:
                    strMatrix += '\n'
        return strMatrix

    def size(self):
        return len(self.param), len(self.param[1])

    def __add__(self, other):
        if len(self.param) == len(other.param) and \
                len(self.param[1]) == len(other.param[1]):
            summ = deepcopy(self.param)
            for i in range(len(self.param)):
                for j in range(len(self.param[1])):
                    summ[i][j] = self.param[i][j] + other.param[i][j]
        else:
            raise MatrixError(self, other)
        return Matrix(summ)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            composition = deepcopy(self.param)
            for i in range(len(self.param)):
                for j in range(len(self.param[1])):
                    composition[i][j] = self.param[i][j] * other
        elif isinstance(other, Matrix) and \
                len(self.param[1]) == len(other.param):
            composition = []
            for i in range(len(self.param)):
                composition.append([])
                for j in range(len(other.param[1])):
                    composition[i].append(0)
            matrix2 = deepcopy((other.transposed()).param)
            for j in range(len(self.param)):
                for f in range(len(matrix2)):
                    for i in range(len(self.param[1])):
                        composition[j][f] += self.param[j][i] * matrix2[f][i]
        else:
            raise MatrixError(self, other)
        return Matrix(composition)

    __rmul__ = __mul__

    def transpose(self):
        transponirovannaya = []
        for i in range(len(self.param[1])):
            newList = []
            for j in range(len(self.param)):
                newList.append(self.param[j][i])
                if j == len(self.param) - 1:
                    transponirovannaya.append(newList)
        self.param = transponirovannaya
        return Matrix(self.param)

    def transposed(self):
        transponirovannaya = []
        for i in range(len(self.param[1])):
            newList = []
            for j in range(len(self.param)):
                newList.append(self.param[j][i])
                if j == len(self.param) - 1:
                    transponirovannaya.append(newList)
        return Matrix(transponirovannaya)


class SquareMatrix(Matrix):
    def __pow__(self, n):
        if n == 0:
            zeropower = []
            for i in range(len(self.param)):
                zeropower.append([])
                for j in range(len(self.param[1])):
                    if i == j:
                        zeropower[i].append(1)
                    else:
                        zeropower[i].append(0)
            return SquareMatrix(zeropower)
        m = self
        t = 1
        while n:
            if n % 2:
                t *= m
            m *= m
            n //= 2
        return t


#exec(stdin.read())
m = SquareMatrix([[1, 1, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 0, 1]]
                )
print(m)
print('----------')
print(m ** 1)
print('----------')
print(m ** 2)
print('----------')
print(m ** 3)
print('----------')
print(m ** 4)
print('----------')
print(m ** 5)