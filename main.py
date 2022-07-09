
import pyglet
from particlemanager import Particlemanager
from fieldmanager import Fieldmanager
import math as m


def velocityAt(x, y):  # definiert das geschwindigkeitsfeld. das wäre das was wir in ströle errechnen täten
    center = (25, 25)
    vector = getVectorToCenter(center, (x, y), 5)
    dist = m.pow(vector[0], 2) + m.pow(vector[1], 2)
    return(-vector[1] - 0.005*dist, vector[0] + 0.005*dist)

    # return (m.sqrt(1000+m.pow(x, 2)-m.pow(y, 2)), m.pow(x, 2))
    # return (50, -50)
    # return(-0.1*m.pow(x-20, 3), m.pow(x, 2))  # nice :)
    # return(1*m.pow(x,2),0.5)
    # return (x,y)
    # return (x , m.sin(x))
    # return (0.2*m.pow(x-4,2) + 0.2*m.pow(y-4,2),  0.2*m.pow(y-4,2))#0.2*m.pow(y-4,2))
    return (m.sqrt(2 - 0.02*m.pow(y, 2)), m.sqrt(2 - 0.02*m.pow(y, 2)))


def getVectorToCenter(center, point, factor=1):
    return ((point[0] - center[0])*factor, (point[1] - center[1])*factor)


window = pyglet.window.Window(fullscreen=False, width=700, height=700)
clock = pyglet.clock
batchOfArrows = pyglet.graphics.Batch()
batchOfParticles = pyglet.graphics.Batch()
field = Fieldmanager(50, 15, batchOfArrows, velocityAt)
#particlepositions = ((250, 0), (250, 50))
particlepositions = []
for i in range(0, 375, 2):
    particlepositions.append((375, i))
particleswarm = Particlemanager(particlepositions, batchOfParticles, field)


field.updateArrows()
pyglet.clock.schedule(particleswarm.update)


@window.event
def on_draw():
    dt = clock.tick()
    # particleswarm.update(dt)
    window.clear()

    batchOfArrows.draw()
    # pyglet.sprite.Sprite(pyglet.image.load("particle.png"),0,0).draw()
    batchOfParticles.draw()


pyglet.app.run()

# test
