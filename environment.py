import numpy as np
import queue

class Environment:
    def __init__(self):
        pass
    # Determine the result of an action in this state.
    def getNextState(self, state, action, maze):
        row = state[0]
        column = state[1]
        if action == 'up':
            row -= 1
        elif action == 'down':
            row += 1
        elif action == 'left':
            column -= 1
        elif action == 'right':
            column += 1
        nextState = (row, column)
        try:
            # Beyond the boundary or hit the wall.
            if row < 0 or column < 0 or maze[row, column] == 1:
                return [state, False]
            # Goal
            elif maze[row, column] == 2:
                return [nextState, True]
            # Forward
            else:
                return [nextState, False]
        except IndexError as e:
            # Beyond the boundary.
            return [state, False]
    # Execute action.
    def doAction(self, state, action, maze):
        nextState, result = self.getNextState(state, action, maze)
        # No move
        if nextState == state:
            reward = -10
        # Goal
        elif result:
            reward = 100
        # Forward
        else:
            reward = -1
        return [reward, nextState, result]
    def check(self, maze):
        initState = (np.where(maze==-1)[0][0], np.where(maze==-1)[1][0])
        endState = (np.where(maze==2)[0][0], np.where(maze==2)[1][0])
        if initState == endState:
            return False
        # bfs
        q = queue.Queue()
        q.put(initState)
        while not q.empty():
            state = q.get()
            for action in ['up', 'down', 'left', 'right']:
                nextState, result = self.getNextState(state, action, maze)
                if nextState == endState:
                    return True
                if not result and maze[nextState[0]][nextState[1]] == 0:
                    q.put(nextState)
        return False
      
    # -1 is origin, 0 is road, 1 is wall, 2 is goal 
    def create_maze(self, row, column):
        while True:
            # 迷宫大小
            maze_size = (column, row)
            # 隨機生成迷宮，其中0代表可以走的道路，1代表牆壁
            maze = np.zeros(maze_size)
            num_walls = int(maze_size[0] * maze_size[1] * 0.3)  # 牆壁數量
            maze[np.random.choice(maze_size[0], num_walls), np.random.choice(maze_size[1], num_walls)] = 1
            # 隨機起點和終點的位置
            start = tuple(np.random.randint(maze_size[0], size=2))
            end = tuple(np.random.randint(maze_size[0], size=2))
            # 將起點和終點的值分別設為-1, 2
            maze[start] = -1
            maze[end] = 2
            if self.check(maze):
                break
        return maze