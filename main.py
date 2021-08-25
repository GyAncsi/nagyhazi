import arcade

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
    def mozog(self):
        self.x += 0.25



p_toltes= Toltes(30, 550, 30, arcade.color.RED_BROWN)
n_toltes = Toltes(200, 450, 10, arcade.color.BLUE)

while p_toltes.x != 600:
    arcade.start_render()
    n_toltes.draw()
    p_toltes.mozog()
    p_toltes.draw()
    arcade.finish_render()


arcade.run()












