from board import Board
import copy as cpy

class Solver:
    def __init__(self, startState, algo):
        self.startState = startState
        self.algo = algo
        self.LIMIT = 100
        self.beststate = None
        if (self.algo == 1):
            self.hillclimb()
        elif(self.algo == 2):
            self.simulatedAnnealing()
    
    def hillclimb(self):
        restarts = 0
        best_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        current_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        while restarts <= self.LIMIT:
            while True:
                possible_states = current_state[0].move()
                states = []
                for state in possible_states:
                    states.append((cpy.copy(state), state.calc_manhatten()))
                states.sort(key = lambda x:x[1]) # can be used for finding the lowest manhatten distance, index 0 will be new state to move into
                if states[0][1] < best_state[1]:
                    best_state = cpy.deepcopy(states[0])
                    current_state = cpy.deepcopy(states[0])
                    states = []
                    continue
                else:
                    states = []
                    break
            restarts += 1
            current_state[0].randomize()
        self.beststate = best_state[0]
        return best_state[0]

    def simulatedAnnealing(self):
        restarts = 0
        best_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        current_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        while restarts <= self.LIMIT:
            while True:
                possible_states = current_state[0].move()
                states = []
                for state in possible_states:
                    states.append((cpy.copy(state), state.calc_manhatten()))
                states.sort(key = lambda x:x[1]) # can be used for finding the lowest manhatten distance, index 0 will be new state to move into
                if states[0][1] < best_state[1]:
                    best_state = cpy.deepcopy(states[0])
                    current_state = cpy.deepcopy(states[0])
                    states = []
                    continue
                else:
                    states = []
                    break
            restarts += 1
            current_state[0].randomize()
        self.beststate = best_state[0]
        return best_state[0]
        
b = Board(10,10,10)
b.launch()
print(b.calc_manhatten())
s = Solver(b,1)

print()
s.beststate.printArray()
print(s.beststate.calc_manhatten())
# s = Solver(b,1)