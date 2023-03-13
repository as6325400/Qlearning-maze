import numpy as np
import time
from environment import Environment
from view import MazeWindow
from agent import Agent

    
def main():    
    initState = (np.where(maze==-1)[0][0], np.where(maze==-1)[1][0])
    # Create an Agent
    agent = Agent(maze, initState)
    for j in range(0, 5000):
        agent.state = initState
        m.target(agent.state)
        time.sleep(0.1)
        i = 0
        while True:
            i += 1
            # Get the next step from the Agent
            action = agent.getAction(0.9)
            # Give the action to the Environment to execute
            reward, nextState, result = environment.doAction(agent.state, action, maze)
            # Update Q Table based on Environmnet's response
            agent.updateQTable(action, nextState, reward)
            # Agent's state changes
            agent.state = nextState
            m.target(agent.state)
            if result:
                print(f' {j+1:2d} : {i} steps to the goal.')
                break
    agent.showQTable()
    agent.showBestAction()

# Create a game Environment
environment = Environment()
maze = environment.create_maze(10, 10)
m = MazeWindow(maze)
m.mainloop(main)