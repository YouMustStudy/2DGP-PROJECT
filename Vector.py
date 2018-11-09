import math

class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def clone(self):
        return Vector(self.x, self.y, self.z)

    def size(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def normalize(self):
        size = self.size()
        self.x /= size
        self.y /= size
        self.z /= size
        return Vector(self.x, self.y, self.z)

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z
        return Vector(self.x, self.y, self.z)

    def mul(self, num):
        self.x *= num
        self.y *= num
        self.z *= num
        return Vector(self.x, self.y, self.z)

    def dot(self, vec):
        return self.x*vec.x + self.y*vec.y + self.z*vec.z

    def cross(self, vec):
        return Vector(self.y * vec.z - self.z * vec.y, self.z * vec.x - self.x * vec.z, self.x * vec.y - self.y * vec.x);