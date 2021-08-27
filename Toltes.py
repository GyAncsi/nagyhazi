import arcade


class Toltes():
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)


class PToltes(Toltes):
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color

    def mozog(self):
        deltaX = 0.25
        deltaY = 0
        self.x += deltaX
        self.y += deltaY

class NToltes(Toltes):
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color

