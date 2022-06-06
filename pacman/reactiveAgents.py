# reactiveAgents.py
# ---------------
# Licensing Information: You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC
# Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
import numpy as np

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search

class NaiveAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        sense = state.getPacmanSensor()
        if sense[7]:
            action = Directions.STOP
        else:
            action = Directions.WEST
        return action

class PSAgent(Agent):
    "An agent that follows the boundary using production system."

    def getAction(self, state):
        sense = state.getPacmanSensor()
        x = [sense[1] or sense[2] , sense[3] or sense[4] ,
        sense[5] or sense[6] , sense[7] or sense[0]]
        if x[0] and not x[1]:
            action = Directions.EAST
        elif x[1] and not x[2]:
            action = Directions.SOUTH
        elif x[2] and not x[3]:
            action = Directions.WEST
        elif x[3] and not x[0]:
            action = Directions.NORTH
        else:
            action = Directions.NORTH
        return action

class ECAgent(Agent):
    "An agent that follows the boundary using error-correction."
    def getAction(self, state):
        ''' @TODO: Your code goes here! '''
        sense = state.getPacmanSensor()
        x = [sense[0], sense[1], sense[2], sense[3],
             sense[4], sense[5], sense[6], sense[7], 1]
        result_n = 0
        result_e = 0
        result_s = 0
        result_w = 0

        weight_n = [1, -2, -2, 0, 0, 0, 0, 1, -1]
        weight_e = [0, 1, 1, -2, -2, 0, 0, 0, -1]
        weight_s = [0, 0, 0, 1, 1, -2, -2, 0, -1]
        weight_w = [-2, 0, 0, 0, 0, 1, 1, -2, -1]

        for i in range(9):
            result_n += weight_n[i] * x[i]
            result_e += weight_e[i] * x[i]
            result_s += weight_s[i] * x[i]
            result_w += weight_w[i] * x[i]

        if result_n >= 0:
            result_n = 1
        else:
            result_n = 0
        if result_e >= 0:
            result_e = 1
        else:
            result_e = 0
        if result_s >= 0:
            result_s = 1
        else:
            result_s = 0
        if result_w >= 0:
            result_w = 1
        else:
            result_w = 0


        if result_n == 1 and (result_e == 0 and result_s == 0 and result_w == 0):
            return Directions.NORTH
        if result_e == 1 and (result_n == 0 and result_s == 0 and result_w == 0):
            return Directions.EAST
        if result_s == 1 and (result_e == 0 and result_n == 0 and result_w == 0):
            return Directions.SOUTH
        if result_w == 1 and (result_e == 0 and result_s == 0 and result_n == 0):
            return Directions.WEST

        if result_n == 1:
            return Directions.NORTH
        if result_e == 1:
            return Directions.EAST
        if result_s == 1:
            return Directions.SOUTH
        if result_w == 1:
            return Directions.WEST

        else:
            return Directions.NORTH

class SMAgent(Agent):
    "An sensory-impaired agent that follows the boundary using state machine."
    def registerInitialState(self,state):
        "The agent receives the initial GameState (defined in pacman.py)."
        sense = state.getPacmanImpairedSensor() #north east south west
        self.prevAction = Directions.STOP # previous action
        self.prevSense = sense # previous sense


    def getAction(self, state):
        '''@TODO: Your code goes here! '''
        sense = state.getPacmanImpairedSensor()
        # print(sense, self.prevSense, self.prevAction)
        weight_n = [-10,0,0,5,2,-3,0,0, 0,1,0,0]
        weight_e = [5,-10,0,0,0,2,-3,0, 0,0,1,0]
        weight_s = [0,5,-10,0,0,0,2,-3, 0,0,0,1]
        weight_w = [0,0,5,-10,-3,0,0,2, 1,0,0,0]
        de = np.zeros(4)

        if self.prevAction == Directions.NORTH:
            de[0] = 1
        if self.prevAction == Directions.EAST:
            de[1] = 1
        if self.prevAction == Directions.SOUTH:
            de[2] = 1
        if self.prevAction == Directions.WEST:
            de[3] = 1
        # print(sense,self.prevSense,de)
        x = np.zeros(12)
        for i in range(4):
            x[i] = sense[i]
            x[4+i] = self.prevSense[i]
            x[8+i] = de[i]
        print(x)
        result_n = 0
        result_e = 0
        result_s = 0
        result_w = 0
        for i in range(12):
            result_n += weight_n[i] * x[i]
            result_e += weight_e[i] * x[i]
            result_s += weight_s[i] * x[i]
            result_w += weight_w[i] * x[i]
        print(result_n, result_e, result_s, result_w)
        if result_n >=2:
            self.prevSense = sense
            self.prevAction = Directions.NORTH
            return Directions.NORTH

        if result_e >= 2:
            self.prevSense = sense
            self.prevAction = Directions.EAST
            return Directions.EAST

        if result_s >= 2:
            self.prevSense = sense
            self.prevAction = Directions.SOUTH
            return Directions.SOUTH

        if result_w >= 2:
            self.prevSense = sense
            self.prevAction = Directions.SOUTH
            return Directions.WEST
        # if sense[3] == 1 and sense[0] == 0:
        #     self.prevSense = sense
        #     self.prevAction = Directions.NORTH
        #     return Directions.NORTH
        #
        # if sense[0] == 1 and sense[1] == 0:
        #     self.prevSense = sense
        #     self.prevAction = Directions.EAST
        #     return Directions.EAST
        #
        # if sense[1] == 1 and sense[2] == 0:
        #     self.prevSense = sense
        #     self.prevAction = Directions.SOUTH
        #     return Directions.SOUTH
        #
        # if sense[2] == 1 and sense[3] == 0:
        #     self.prevSense = sense
        #     self.prevAction = Directions.WEST
        #     return Directions.WEST
        #
        # if sense[0] == 0 and sense[1] == 0 and sense[2] == 0 and sense[3] == 0:
        #     if self.prevSense[1] == 1 and self.prevAction == Directions.SOUTH:
        #         self.prevSense = sense
        #         self.prevAction = Directions.EAST
        #         return Directions.EAST
        #
        #     if self.prevSense[2] == 1 and self.prevAction == Directions.WEST:
        #         self.prevSense = sense
        #         self.prevAction = Directions.SOUTH
        #         return Directions.SOUTH
        #
        #     if self.prevSense[3] == 1 and self.prevAction == Directions.NORTH:
        #         self.prevSense = sense
        #         self.prevAction = Directions.WEST
        #         return Directions.WEST
        #
        #     if self.prevSense[0] == 1 and self.prevAction == Directions.EAST:
        #         self.prevSense = sense
        #         self.prevAction = Directions.NORTH
        #         return Directions.NORTH
        print("nooo")
        return Directions.NORTH
