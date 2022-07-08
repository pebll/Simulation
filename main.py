from fieldmanager import Fieldmanager
import pyglet
import graphics
from particle import Particle
import math as m
def velocityAt(x,y): #definiert das geschwindigkeitsfeld. das wäre das was wir in ströle errechnen täten
    return (0.2*(x^2) + 0.3*(y^2), -0.4*(x^2) - 0.2)

window = pyglet.window.Window(fullscreen=False)

batchOfArrows = pyglet.graphics.Batch()
field = Fieldmanager(10, batchOfArrows, velocityAt)


#particule = pyglet.resource.image('particle.png') #deleten?
particle1 = Particle()



    

field.updateArrows()
@window.event
def on_draw():
    window.clear()
    
    batchOfArrows.draw()
    particle1.image.draw()
    
    


pyglet.app.run()

#test