
import pyglet
from particlemanager import Particlemanager
from fieldmanager import Fieldmanager
import math as m
import random


def velocityAt(x, y):  # definiert das geschwindigkeitsfeld. das wäre das was wir in ströle errechnen täten
    center = (25, 25)
    factor = 0.01
    drehfactor_x = -0.5
    drehfactor_y = 0.4
    vector = getVectorToCenter(center, (x, y), 5)
    dist = m.pow(vector[0], 2) + m.pow(vector[1], 2)
    return((-vector[0] + vector[1]*drehfactor_x)*factor, (-vector[1] + vector[0]*drehfactor_y)*factor)

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


ABSTAND = 50
AMOUNT = 15
randomness = 200

window = pyglet.window.Window(fullscreen=False, width=700, height=700)
clock = pyglet.clock
batchOfArrows = pyglet.graphics.Batch()
batchOfParticles = pyglet.graphics.Batch()
field = Fieldmanager(ABSTAND, AMOUNT, batchOfArrows, velocityAt)
#particlepositions = ((250, 0), (250, 50))
particlepositions = []

for x in range(0, ABSTAND*AMOUNT, 45):
    for y in range(0, ABSTAND*AMOUNT, 45):
        particlepositions.append(
            (x + random.randint(-randomness, randomness), y + random.randint(-randomness, randomness)))
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
