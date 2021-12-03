class Sudoku:
    def __init__(self):
        self.a = [[0] * 9 for _ in range(9)]

    def set_value(self, i, j, k):
        a[i][j] = k

    def check_possible(self):
        for i in range(9):
            for j in range(9):
                if str(self.a[i][j]).isdigit():
                    return False

        for i in range(9):
            for j in range(9):
                if not (1 <= self.a[i][j] <= 9):
                    return False
        return True

    def check_win(self):
        if not self.check_possible():
            return False

        for i in range(9):
            b = [0] * 9
            for j in range(9):
                b[self.a[i][j] - 1] += 1
            if min(b) < 1:
                return False

        for i in range(9):
            b = [0] * 9
            for j in range(9):
                b[self.a[j][i] - 1] += 1
            if min(b) < 1:
                return False

        for x in range(3):
            for y in range(3):
                b = [0] * 9
                for i in range(3):
                    for j in range(3):
                        b[a[x * 3 + i][y * 3 + j] - 1] += 1
                    if min(b) < 1:
                        return False

        return True


a = []
for i in range(9):
    a.append(input().split())

sud = Sudoku()
for i in range(9):
    for j in range(9):
        sud.set_value(i, j, a[i][j])


print(sud.check_win())