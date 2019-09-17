a = [
    [5, 12, 17, 21, 23],
    [1, 2, 4, 6, 8],
    [12, 14, 18, 19, 27],
    [3, 7, 9, 15, 25]
]


class Sort2D:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def sort(self):
        for i in range(len(self.matrix) - 1):
            for j in range(len(self.matrix[i])):
                r = self.find_min(i + 1)
                if self.matrix[i][j] > self.matrix[r][0]:
                    self.swap(j, i, 0, r)
                    # self.reorder_by_increase(r)
                    self.bubble_reorder(r)

    def bubble_reorder(self, r):
        length = len(self.matrix[r])
        for i in range(1, length):
            swapped = False
            for j in range(length - i):
                if self.matrix[r][j] > self.matrix[r][j + 1]:
                    swapped = True
                    self.swap(j, r, j + 1, r)
            if not swapped:
                break

    def reorder_by_increase(self, r):
        length = len(self.matrix[r])
        for i in range(1, length):
            while i > 0 and self.matrix[r][i] < self.matrix[r][i - 1]:
                self.swap(i, r, i - 1, r)
                i -= 1

    def swap(self, x_1, y_1, x_2, y_2):
        self.matrix[y_1][x_1], self.matrix[y_2][x_2] = self.matrix[y_2][x_2], self.matrix[y_1][x_1]

    def find_min(self, v):
        r = v
        for i in range(v, len(self.matrix)):
            if self.matrix[r][0] > self.matrix[i][0]:
                r = i
        return r


if __name__ == '__main__':
    s = Sort2D(a)
    s.sort()
    print(s.matrix)
