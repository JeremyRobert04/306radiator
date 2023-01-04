import src.my_print as Print

MAX_ITER = 100

class Radiator():
    def __init__(self, n: int, nPow: int, ir: int, jr: int, i: int, j: int) -> None:
        self.room_size = n
        self.room_size_pow = nPow
        self.coordinate_radiator = [ir, jr]
        self.coordinate_point = [i, j]
        self.matrixA = [[0] * nPow for _ in range(nPow)]
        self.vectorX = [0 for _ in range(nPow)]
        self.vectorY = [0 for _ in range(nPow)]
        self.h = 0.5

    def calculate_vectorX(self):
        for iteration in range(MAX_ITER):
            for j in range(self.room_size_pow):
                sum_mul = 0
                for k in range(self.room_size_pow):
                    if k != j:
                        sum_mul += self.matrixA[j][k] * self.vectorX[k]
                    self.vectorX[j] = (self.vectorY[j] - sum_mul) / self.matrixA[j][j]

    def calculate_matrix_A(self):
        n = self.room_size
        n2 = self.room_size_pow

        for i in range(n2):
            if i <= n - 1 or i >= n2 - n or i % n == 0 or i % n == n - 1:
                self.matrixA[i][i] = 1
            else:
                self.matrixA[i][i - n] = 1 / (self.h ** 2)
                self.matrixA[i][i - 1] = 1 / (self.h ** 2)
                self.matrixA[i][i] = -4 / (self.h ** 2)
                self.matrixA[i][i + 1] = 1 / (self.h ** 2)
                self.matrixA[i][i + n] = 1 / (self.h ** 2)

    def radiator(self):
        self.calculate_matrix_A()
        self.vectorY[self.coordinate_radiator[0] + self.coordinate_radiator[1] * self.room_size] = -300
        self.calculate_vectorX()
        if any(value is None for value in self.coordinate_point):
            Print.print_matrix(self.matrixA)
            Print.print_vec_result(self.vectorX)
        else:
            Print.print_specific_point(self.vectorX, self.room_size, self.coordinate_point)