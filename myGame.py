
import arcade
screenHight = 600
screenWidth = 600


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.DARK_BLUE)

