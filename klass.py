from sys import stdin
import copy


class Matrix:
    def __init__(self, arr) -> None:
        self.arr = copy.deepcopy(arr)

    def __str__(self) -> str:
        res = ""
        for string in self.arr:
            for elem in string:
                res += str(elem) + "\t"
            res = res[:-1] + "\n"
        return res[:-1]

    def size(self):
        return (len(self.arr), len(self.arr[0]))

    def transpose(self):
        matrix = list(zip(*self.arr))
        self.arr = matrix
        return Matrix(matrix)

    def transposed(self):
        matrix = list(zip(*self.arr))
        return Matrix(matrix)

    def __add__(self, other):
        if len(self.arr) == len(other.arr):
            lenght = len(self.arr[0])
            for row in self.arr:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.arr:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.arr)):
                for j in range(len(self.arr[0])):
                    summa = other.arr[i][j] + self.arr[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.arr[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other: int) -> list:
        new_arr = []
        for string in self.arr:
            new_arr.append([x * other for x in string])
        return Matrix(new_arr)

    __rmul__ = __mul__


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2) -> None:
        self.matrix1 = matrix1
        self.matrix2 = matrix2


exec(stdin.read())
