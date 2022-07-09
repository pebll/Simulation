
import pyglet
from particlemanager import Particlemanager
from fieldmanager import Fieldmanager
import math as m
def velocityAt(x,y): #definiert das geschwindigkeitsfeld. das wäre das was wir in ströle errechnen täten
    return (m.sqrt(1000+m.pow(x,2)-m.pow(y,2)),m.pow(x,2))
    #return (2,200)
    return(-0.1*m.pow(x-20,3),m.pow(x,2)) #nice :)
    #return(1*m.pow(x,2),0.5)
    #return (x,y)
    #return (x , m.sin(x))
    #return (0.2*m.pow(x-4,2) + 0.2*m.pow(y-4,2),  0.2*m.pow(y-4,2))#0.2*m.pow(y-4,2))
    return (m.sqrt(2 - 0.02*m.pow(y,2)),m.sqrt(2 - 0.02*m.pow(y,2)))

window = pyglet.window.Window(fullscreen=False)
clock = pyglet.clock
batchOfArrows = pyglet.graphics.Batch()
batchOfParticles = pyglet.graphics.Batch()
field = Fieldmanager(20, 25 ,batchOfArrows, velocityAt)
particlepositions = ((0,0),(10,200),(40,40))
particleswarm = Particlemanager(particlepositions,batchOfParticles,field)

  

field.updateArrows()
pyglet.clock.schedule(particleswarm.update)
@window.event
def on_draw():
    dt = clock.tick()
    #particleswarm.update(dt)
    window.clear()
    
    batchOfArrows.draw()
    #pyglet.sprite.Sprite(pyglet.image.load("particle.png"),0,0).draw()
    batchOfParticles.draw()
    
    
    


pyglet.app.run()

#test