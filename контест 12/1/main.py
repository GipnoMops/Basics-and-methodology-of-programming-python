#from sys import stdin
from copy import deepcopy


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


#exec(stdin.read())
m = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(m)
print(str(m))
print(m.size())
