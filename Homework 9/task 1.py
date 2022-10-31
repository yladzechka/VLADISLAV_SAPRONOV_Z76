class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @a.setter
    def a(self, value):
        self._a = value

    @b.setter
    def b(self, value):
        self._b = value

    @c.setter
    def c(self, value):
        self._c = value

    def triangle_check(self):
        if self._a + self._b > self._c and self._a + self._c > self._b and self._b + self._c > self._a:
            print("Треугольник существует")
        else:
            print("Треугольник не существует")


obj = Triangle(3, 4, 5)
obj.triangle_check()