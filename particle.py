import graphics
import pyglet


class Particle:
    def __init__(self) -> None:
        sprite = pyglet.sprite.Sprite(graphics.particule, 0, 0)
