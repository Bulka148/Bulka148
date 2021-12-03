class RationalFraction:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        if self.y == 0:
            print('Деление на ноль!')
            exit()

    def _NOD(self, a, b):
        while a > 0 and b > 0:
            (a, b) = (b, a) if b > a else (a, b)
            a = a % b
        return a + b

    def reduce(self):
        nod = self._NOD(self.x, self.y)
        self.x, self.y = self.x // nod, self.y // nod

    def add(self, num):
        x = self.x * num.y + num.x * self.y
        y = self.y * num.y
        nod = self._NOD(x, y)
        return RationalFraction(x // nod, y // nod)

    def add2(self, num):
        new = self.add(num)
        self.x, self.y = new.x, new.y

    def sub(self, num):
        return self.add(RationalFraction(-num.x, num.y))

    def sub2(self, num):
        new = self.add(RationalFraction(-num.x, num.y))
        self.x, self.y = new.x, new.y

    def mult(self, num):
        x = self.x * num.x
        y = self.y * num.y
        nod = self._NOD(x, y)
        return RationalFraction(x // nod, y // nod)

    def mult2(self, num):
        new = self.mult(num)
        self.x, self.y = new.x, new.y

    def div(self, num):
        num.x, num.y = num.y, num.x
        new = self.mult(num)
        nod = self._NOD(new.x, new.y)
        return RationalFraction(new.x // nod, new.y // nod)

    def div2(self, num):
        new = self.div(num)
        self.x, self.y = new.x, new.y

    def str(self):
        if self.x == 0:
            return 0
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + '/' + str(self.y)

    def value(self):
        return self.x / self.y

    def equals(self, num):
        return True if self.x / self.y == num.x / num.y else False

    def numberPart(self):
        return self.x // self.y


k = RationalFraction(12, 112)

k.add2(RationalFraction(1, 1))
k.div(RationalFraction())

print(k.str())