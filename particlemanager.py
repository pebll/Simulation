# Partikelklasse

import pyglet
import math as m
import random


class Particlemanager:
    def __init__(self, passedbatch, fieldmanager):
        self.particles = []
        self.fieldmanager = fieldmanager
        image = pyglet.resource.image("particle.png")
        image.anchor_x, image.anchor_y = image.width/2, image.height/2
        positions = self.get_positions()
        for i in range(len(positions)):
            self.particles.append([pyglet.sprite.Sprite(
                image, positions[i][0], positions[i][1], batch=passedbatch), [0, 0]])

        for element in self.particles:
            element[0].scale = 0.1

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
            #color = min(255, 25 * (abs(element[1][0])+abs(element[1][1])))
            #element[0].color = (color, color, color)

    def get_positions(self):
        SIZE = self.fieldmanager.FIELDSIZE
        DISTANCE = self.fieldmanager.DISTANCE
        RANDOMNESS = 0
        INCREMENT = 4  # multiple of size, d.h. alle wieviel pfeile man ein particle setzt
        particlepositions = []
        for x in range(0, SIZE*DISTANCE, DISTANCE*INCREMENT+1):
            for y in range(0, SIZE*DISTANCE, DISTANCE*INCREMENT+1):
                particlepositions.append(
                    (x + random.randint(-RANDOMNESS, RANDOMNESS), y + random.randint(-RANDOMNESS, RANDOMNESS)))

        return particlepositions

    def reset(self):
        positions = self.get_positions()
        for i in range(len(positions)):
            element = self.particles[i]
            element[0].position = positions[i]
            element[1] = [0, 0]
