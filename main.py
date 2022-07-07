import pyglet
import graphics
from particle import Particle

window = pyglet.window.Window(fullscreen=False)

batch = pyglet.graphics.Batch()
particule = pyglet.resource.image('particle.png')
particle1 = Particle()


@window.event
def on_draw():
    window.clear()
    particle1.image.draw()


pyglet.app.run()

#test