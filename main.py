import arcade
from Toltes import NToltes
from Toltes import PToltes

screenHight = 600
screenWidth = 600

arcade.open_window(screenWidth,screenHight, " MyGame ")
class Toltes:
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)

p_toltes= PToltes(30, 550, 30, arcade.color.RED_BROWN)
n_toltes = NToltes(200, 450, 10, arcade.color.BLUE)

while p_toltes.x <= 600:
    arcade.start_render()
    n_toltes.draw()
    p_toltes.mozog()
    p_toltes.draw()
    arcade.finish_render()


arcade.run()












