#Partikelklasse 

import graphics
import pyglet


class Particle:
    def __init__(self) -> None:
        self.image = pyglet.sprite.Sprite(graphics.particle, 0, 0)
        self.image.scale = 0.3
