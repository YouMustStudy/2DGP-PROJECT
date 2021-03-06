import math

class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def set(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def clone(self):
        return Vector(self.x, self.y, self.z)

    def size(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def normalize(self):
        size = self.size()
        if size == 0:
            return self
        self.x /= size
        self.y /= size
        self.z /= size
        return Vector(self.x, self.y, self.z)

    def add(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def mul(self, num):
        return Vector(self.x * num, self.y * num, self.z * num)

    def dot(self, vec):
        return self.x*vec.x + self.y*vec.y + self.z*vec.z

    def cross(self, vec):
        return Vector(self.y * vec.z - self.z * vec.y, self.z * vec.x - self.x * vec.z, self.x * vec.y - self.y * vec.x);

    def rotateX(self, degree):
        radian = math.radians(degree)
        cos = math.cos(radian)
        sin = math.sin(radian)
        self.y, self.z = cos*self.y - sin*self.z, sin*self.y + cos*self.z
        return Vector(self.x, self.y, self.z)

    def rotateY(self, degree):
        radian = math.radians(degree)
        cos = math.cos(radian)
        sin = math.sin(radian)
        self.x, self.z = cos*self.x + sin*self.z, -sin*self.x + cos*self.z
        return Vector(self.x, self.y, self.z)

    def rotateZ(self, degree):
        radian = math.radians(degree)
        cos = math.cos(radian)
        sin = math.sin(radian)
        self.x, self.y = cos*self.x - sin*self.y, sin*self.x + cos*self.y
        return Vector(self.x, self.y, self.z)