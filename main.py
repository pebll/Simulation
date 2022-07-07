import pyglet
import graphics
from particle import Particle

window = pyglet.window.Window(fullscreen=False)

particle1 = Particle()


@window.event
def on_draw():
    window.clear()
    particle1.draw()


pyglet.app.run()
