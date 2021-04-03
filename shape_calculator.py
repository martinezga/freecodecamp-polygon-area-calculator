class Rectangle:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        picture = ''
        line_sep = '\n'
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            for i in range(self.height):
                picture += '*' * self.width + line_sep
            return picture

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self) -> str:
        if self.__class__.__name__ == 'Rectangle':
            return f'Rectangle(width={self.width}, height={self.height})'
        elif self.__class__.__name__ == 'Square':
            return f'Square(side={self.width})'
        else:
            return 'Error'


class Square(Rectangle):
    def __init__(self, side):
        super(Rectangle, self).__init__()
        self.side = 0
        self.set_side(side)

    def set_side(self, side):
        self.side = side
        self.set_width(side)
        self.set_height(side)
