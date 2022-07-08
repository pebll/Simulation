import pyglet
import numpy as np
import math

class Fieldmanager():
    def __init__(self,size, passedbatch,velocityfunction):
        self.FIELDSIZE = size
        self.velocity = np.arange(2*self.FIELDSIZE*self.FIELDSIZE, dtype = float).reshape(2,self.FIELDSIZE,self.FIELDSIZE)
         #create a 5x5 matrix with every containing to values for velocity vector
        for i in range(self.FIELDSIZE):
            for j in range(self.FIELDSIZE):
                self.velocity[0][i][j], self.velocity[1][i][j] = velocityfunction(i,j)
        


        #self.velocity[0].fill(3.2) #initialize the ux values
        #self.velocity[1].fill(-0.3) #initialize the uy values
        print(self.velocity[0])        
        print(self.velocity[1])
        self.arrowsprites = [] #initialize the arrows drawings. The list becomes a 2D array later
        for i in range(self.FIELDSIZE):
            column = []
            for j in range(self.FIELDSIZE):
                x,y = i*50,j*50
                column.append(pyglet.sprite.Sprite(pyglet.image.load("arrow.png"), x, y, batch=passedbatch))
            self.arrowsprites.append(column)
    def updateArrows(self):
        for i in range(self.FIELDSIZE):
            for j in range(self.FIELDSIZE):
                ux,uy = self.velocity[0][i][j],self.velocity[1][i][j]
                angle = math.degrees(math.atan(ux/uy))
                abs = math.sqrt(math.pow(ux,2)+math.pow(uy,2))
                self.arrowsprites[i][j].update(50*i,50*j,angle,abs)#adapt arrow size, orientation related to values 
    