from tkinter import DISABLED
import pyglet
import numpy as np
import math


class Fieldmanager():
    def __init__(self, size, distance, passedbatch, velocityfunction):
        self.FIELDSIZE = size
        self.DISTANCE = distance
        self.velocity = np.arange(2*self.FIELDSIZE*self.FIELDSIZE,
                                  dtype=float).reshape(2, self.FIELDSIZE, self.FIELDSIZE)
        # create a 5x5 matrix with every containing to values for velocity vector
        for i in range(self.FIELDSIZE):
            for j in range(self.FIELDSIZE):
                self.velocity[0][i][j], self.velocity[1][i][j] = velocityfunction(
                    i, j)

        # self.velocity[0].fill(1) #initialize the ux values
        # self.velocity[1].fill(1) #initialize the uy values
        print(self.velocity[0])
        print(self.velocity[1])
        # initialize the arrows drawings. The list becomes a 2D array later
        self.arrowsprites = []
        image = pyglet.resource.image("arrow.png")
        image.anchor_x, image.anchor_y = image.width/2, image.height/2
        for i in range(self.FIELDSIZE):
            column = []
            for j in range(self.FIELDSIZE):
                x, y = i*self.DISTANCE, j*self.DISTANCE
                column.append(pyglet.sprite.Sprite(
                    image, x, y, batch=passedbatch))
            self.arrowsprites.append(column)

    def updateArrows(self):
        for i in range(self.FIELDSIZE):
            for j in range(self.FIELDSIZE):
                ux, uy = self.velocity[0][i][j], self.velocity[1][i][j]
                arrowlength = math.sqrt(
                    math.pow(ux, 2)+math.pow(uy, 2))  # betrag vektor

                if(uy >= 0):
                    angle = math.degrees(
                        math.atan(ux/uy)) if (uy > 0) else math.degrees(math.atan(10000000*ux))
                if(uy < 0):
                    angle = 180 - \
                        math.degrees(math.atan(-ux/uy)) if (uy <
                                                            0) else math.degrees(math.atan(10000000*ux))

                # adapt arrow size, orientation related to values
                self.arrowsprites[i][j].update(
                    self.DISTANCE*i, self.DISTANCE*j, angle, 0.1 * arrowlength)
