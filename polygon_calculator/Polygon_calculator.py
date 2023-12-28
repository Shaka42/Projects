class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.height+self.width)

    def get_diagonal(self):
        return ((self.width**2)+(self.height**2))**.5

    def get_picture(self):
        if self.height >= 50:
            print('Too big for picture')
        elif self.width >= 50:
            return 'Too big for picture'
        else:
            for i in range(self.height):
                print('*'*self.width)
            return''

    def get_amount_inside(self,shape):
        a = shape.get_area()
        return self.get_area()/a

    def __repr__(self):
        return f'Rectangle(width = {self.width},height = {self.height})'

class Square(Rectangle):
    def __init__(self,side):
        self.width = side
        self.height = side

    def set_side(self,side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f'Square(side={self.width})'
