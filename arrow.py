#Arrow/Gitterpunktklasse 

import graphics
import pyglet


class Arrow:
    def __init__(self) -> None:
        self.image = pyglet.sprite.Sprite(graphics.arrow, 0, 0)
        self.image.scale = 5
