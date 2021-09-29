import arcade
import self as self

from Toltes import NToltes
from Toltes import PToltes
screenHight = 600
screenWidth = 600

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.DARK_BLUE)
    def setup(self):
        pass
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            n_toltes = NToltes(x, y,10, arcade.color.PINK)
            arcade.start_render()
            n_toltes.draw()
            arcade.finish_render()

    def on_draw(self):
        arcade.start_render()
        arcade.finish_render()

    """"
        p_toltes = PToltes(30, 550, 30, arcade.color.RED_BROWN)
        while p_toltes.x <= 600:
            arcade.start_render()
            p_toltes.mozog()
            p_toltes.draw()
            arcade.finish_render()
    """
    def update(self, delta_time):
        pass








game = MyGame(screenWidth, screenHight)
game.setup()
arcade.run()





