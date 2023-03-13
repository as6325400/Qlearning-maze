import random
import numpy as np

class Agent:
    def __init__(self, maze, initState):
        self.state = initState
        self.maze = maze
        self.initQTable()
        self.actionList = ['up', 'down', 'left', 'right']
        self.actionDict = {element : index for index, element in enumerate(self.actionList)}
    def initQTable(self):
        Q = np.zeros(self.maze.shape).tolist()
        for i, row in enumerate(Q):
            for j, _ in enumerate(row):
                Q[i][j] = [0, 0, 0, 0] # up, down, left, right
        self.QTable = np.array(Q, dtype='f')
    def showQTable(self):
        for i, row in enumerate(self.QTable):
            for j, element in enumerate(row):
                print(f'({i}, {j}){element}')
    def showBestAction(self):
        for i, row in enumerate(self.QTable):
            for j, element in enumerate(row):
                Qa = element.tolist()
                action = self.actionList[Qa.index(max(Qa))] if max(Qa) != 0 else '??'
                print(f'({i}, {j}){action}', end=" ")
            print()
    def getAction(self, eGreddy=0.8):
        if random.random() > eGreddy:
            return random.choice(self.actionList)
        else:
            Qsa = self.QTable[self.state].tolist()
            return self.actionList[Qsa.index(max(Qsa))]
    def getNextMaxQ(self, state):
        return max(np.array(self.QTable[state]))
    def updateQTable(self, action, nextState, reward, lr=0.7, gamma=0.9):
        Qs = self.QTable[self.state]
        Qsa = Qs[self.actionDict[action]]
        Qs[self.actionDict[action]] = (1 - lr) * Qsa + lr * (reward + gamma *(self.getNextMaxQ(nextState)))