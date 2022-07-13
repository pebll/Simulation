# Partikelklasse

import pyglet
import math as m
import random


class Particlemanager:
    def __init__(self, positions, passedbatch, fieldmanager):
        self.particles = []
        self.accelerations = []
        self.fieldmanager = fieldmanager
        image = pyglet.resource.image("particle.png")
        image.anchor_x, image.anchor_y = image.width/2, image.height/2
        for i in range(len(positions)):
            self.particles.append([pyglet.sprite.Sprite(
                image, positions[i][0], positions[i][1], batch=passedbatch), [0, 0]])

        for element in self.particles:
            element[0].scale = 0.1
            if random.random() > 0.99:
                element[0].scale = 0.3
            element[0].scale = random.random()*2

    def update(self, deltatime):
        ux, uy = self.fieldmanager.velocity[0], self.fieldmanager.velocity[1]

        # which velocity gets the particle? it has to be located in the grid

        for element in self.particles:
            x = element[0].position[0]
            y = element[0].position[1]
            iElement = int(x/self.fieldmanager.DISTANCE)
            jElement = int(y/self.fieldmanager.DISTANCE)
            iElement = max(iElement, 0)
            iElement = min(iElement, self.fieldmanager.FIELDSIZE-1)
            jElement = max(jElement, 0)
            jElement = min(jElement, self.fieldmanager.FIELDSIZE-1)

            element[1][0] += deltatime * ux[iElement][jElement]
            element[1][1] += deltatime * uy[iElement][jElement]
            element[0].update(x + element[1][0], y + element[1][1])
            color = min(255, 25 * (abs(element[1][0])+abs(element[1][1])))
            element[0].color = (color, color, color)
