#Partikelklasse 

import pyglet
import math as m

class Particlemanager:
    def __init__(self, positions, passedbatch, fieldmanager):
        self.particles = []
        self.fieldmanager = fieldmanager
        image = pyglet.resource.image("particle.png")
        image.anchor_x, image.anchor_y = image.width/2 , image.height/2
        for i in range(len(positions)):
            self.particles.append(pyglet.sprite.Sprite(image, positions[i][0], positions[i][1],batch = passedbatch))
        for element in self.particles:
            element.scale = 0.3
    def update(self,deltatime):
        ux, uy = self.fieldmanager.velocity[0], self.fieldmanager.velocity[1]

        
        #which velocity gets the particle? it has to be located in the grid
        
        for element in self.particles:
            x = element.position[0]
            y = element.position[1]
            iElement = int(x/self.fieldmanager.DISTANCE)
            jElement = int(y/self.fieldmanager.DISTANCE)
            if (jElement > self.fieldmanager.FIELDSIZE - 1)|(iElement > self.fieldmanager.FIELDSIZE - 1):
                print("Elemet ausser sicht")
            
            else:
                element.update(x + deltatime * ux[iElement][jElement], y + deltatime * uy[iElement][jElement])

