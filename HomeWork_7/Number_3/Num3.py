import math


class ComplexNumber:
    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x, y

    def add(self, num):
        x = self.x + num.x
        y = self.y + num.y
        return ComplexNumber(x, y)

    def add2(self, num):
        new = self.add(num)
        self.x, self.y = new.x, new.y

    def sub(self, num):
        return self.add(ComplexNumber(-num.x, -num.y))

    def sub2(self, num):
        new = self.add(ComplexNumber(-num.x, -num.y))
        self.x, self.y = new.x, new.y

    def multNumber(self, k):
        return ComplexNumber(self.x * k, self.y * k)

    def multNumber2(self, k):
        self.x, self.y = self.x * k, self.y * k

    def mult(self, num):
        x = self.x * num.x - self.y * num.y
        y = self.x * num.y + self.y * num.x
        return ComplexNumber(x, y)

    def mult2(self, num):
        new = self.mult(num)
        self.x, self.y = new.x, new.y

    def div(self, num):
        num.y = -num.y
        new = self.mult(num)
        k = num.x**2 + num.y**2
        if k == 0:
            print('Нельзя делить на нулевое комплексное число')
            return None
        new.x, new.y = new.x / k, new.y / k
        return new

    def div2(self, num):
        new = self.div(num)
        self.x, self.y = new.x, new.y

    def len(self):
        return (self.x**2 + self.y**2)**0.5

    def str(self):
        if self.x == 0:
            return str(self.y) + '*i'
        if self.y == 0:
            return str(self.x)
        if self.y == 1:
            return str(self.x) + ' + i'
        else:
            return str(self.x) + ' + ' + str(self.y) + '*i' if self.y > 0 \
                else str(self.x) + ' - ' + str(abs(self.y)) + '*i'

    def arg(self):
        if self.x == 0:
            self.x = 0.00000001
        return math.atan(self.y / self.x)

    def pow(self, k):
        f = self.arg()
        l = self.len() ** k
        self.x, self.y = l * math.cos(f*k), l * math.sin(f*k)

    def equals(self, num):
        return True if self.x == num.x and self.y == num.y else False


k = ComplexNumber(1, 1)

k.add2(ComplexNumber(5, 7))

print(k.str())