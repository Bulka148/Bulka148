class Vector2D:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def add(self, vec):
        return Vector2D(self.x + vec.x, self.y + vec.y)

    def add2(self, vec):
        self.x += vec.x
        self.y += vec.y

    def sub(self, vec):
        return Vector2D(self.x - vec.x, self.y - vec.y)

    def sub2(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def mult(self, k):
        return Vector2D(self.x * k, self.y * k)

    def mult2(self, k):
        self.x *= k
        self.y *= k

    def str(self):
        return str(self.x) + ' ' + str(self.y)

    def len(self):
        return (self.x**2 + self.y**2)**0.5

    def scalarProduct(self, vec):
        return self.x*vec.x + self.y*vec.y

    def cos(self, vec):
        return self.scalarProduct(vec) / self.len() / (vec.x**2 + vec.y**2)**0.5

    def equals(self, vec):
        return True if self.x == vec.x and self.y == vec.y else False


vector1 = Vector2D(3, 4)
vector2 = Vector2D(3, 4)

print(vector.equals(vector2))