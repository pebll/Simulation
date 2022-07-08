from fieldmanager import Fieldmanager
import pyglet
import graphics
from particle import Particle
import math as m
def velocityAt(x,y): #definiert das geschwindigkeitsfeld. das wäre das was wir in ströle errechnen täten
    #return(1,0.5)
    return (x,y)
    return (x , m.sin(x))
    return (0.2*m.pow(x-4,2) + 0.2*m.pow(y-4,2),  0.2*m.pow(y-4,2))#0.2*m.pow(y-4,2))
    return (m.sqrt(2 - 0.02*m.pow(y,2)),m.sqrt(2 - 0.02*m.pow(y,2)))

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