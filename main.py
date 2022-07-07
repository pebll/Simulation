import pyglet
import graphics
from particle import Particle

window = pyglet.window.Window(fullscreen=False)

<<<<<<< HEAD
batch = pyglet.graphics.Batch()
particule = pyglet.resource.image('particle.png')
=======
particle1 = Particle()
>>>>>>> fe84f14c7bf0903166152cf0526fbdfa29a4690b


@window.event
def on_draw():
    window.clear()
    particle1.image.draw()


pyglet.app.run()
