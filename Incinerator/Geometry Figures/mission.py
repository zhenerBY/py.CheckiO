PI = 3.1415926539


class Parameters:

    def __init__(self, param):
        self.param = param
        self.figure = None

    def choose_figure(self, figure):
        self.figure = figure

    def perimeter(self):
        return self.output(self.figure.perimeter(self.param))

    def area(self):
        return self.output(self.figure.area(self.param))

    def volume(self):
        return self.output(self.figure.volume(self.param))

    @staticmethod
    def output(param):
        return param if param == int(param) else round(param, 2)


class Circle:

    @staticmethod
    def perimeter(param):
        return 2 * param * PI

    @staticmethod
    def area(param):
        return param ** 2 * PI

    @staticmethod
    def volume(param):
        return 0


class Triangle:

    @staticmethod
    def perimeter(param):
        return param * 3

    @staticmethod
    def area(param):
        return (3 ** 0.5 / 4) * param * param

    @staticmethod
    def volume(param):
        return 0


class Square:

    @staticmethod
    def perimeter(param):
        return param * 4

    @staticmethod
    def area(param):
        return param * param

    @staticmethod
    def volume(param):
        return 0


class Pentagon:

    @staticmethod
    def perimeter(param):
        return param * 5

    @staticmethod
    def area(param):
        return (5 ** 0.5) * ((5 + 2 * 5 ** 0.5) ** 0.5) / 4 * param ** 2

    @staticmethod
    def volume(param):
        return 0


class Hexagon:

    @staticmethod
    def perimeter(param):
        return param * 6

    @staticmethod
    def area(param):
        return param * param * (3 * 3 ** 0.5) / 2

    @staticmethod
    def volume(param):
        return 0


class Cube:

    @staticmethod
    def perimeter(param):
        return param * 12

    @staticmethod
    def area(param):
        return param * param * 6

    @staticmethod
    def volume(param):
        return param ** 3


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
