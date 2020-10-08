from board import Board
import copy as cpy
from math import exp
import random
from datetime import datetime

class Solver:
    def __init__(self, startState, algo):
        self.startState = startState
        self.algo = algo
        self.LIMIT = 1000
        self.beststate = None
        if (self.algo == 1):
            self.hillclimb()
        elif(self.algo == 2):
            self.simulatedAnnealing()
    
    def hillclimb(self):
        iterations = -1
        restarts = 0
        newglobal = 0
        best_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        current_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        while restarts <= self.LIMIT:
            while True:
                iterations += 1
                possible_states = current_state[0].move()
                states = []
                for state in possible_states:
                    states.append((cpy.copy(state), state.calc_manhatten()))
                states.sort(key = lambda x:x[1]) # can be used for finding the lowest manhatten distance, index 0 will be new state to move into
                if len(states) == 0:
                    pass
                elif states[0][1] < best_state[1]:
                    best_state = cpy.deepcopy(states[0])
                    current_state = cpy.deepcopy(states[0])
                    newglobal+= 1
                    states = []
                    continue
                else:
                    states = []
                    break
            restarts += 1
            current_state[0].randomize()
        print("Total States Checked:",iterations,",", self.LIMIT, "of which are random restarts and",newglobal,"improved global optimal")
        self.beststate = best_state[0]
        return best_state[0]

        
    def simulatedAnnealing(self):
        t = 1000000  # tempature
        a = .99
        newglobal = 0
        iterations = -1
        prob_f = lambda x: round(exp(round(x, 3) / round(t, 3)), 5)
        choice = ["true", "false"]
        global_best = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        local_best = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        current_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        while t > 1:
            iterations+=1
            possible_states = current_state[0].move()
            states = []
            for state in possible_states:
                states.append((cpy.copy(state), state.calc_manhatten()))
            random_state = states[random.randrange(0, len(states))]  # Probably needs fixing
            delta = current_state[1] - random_state[1]
            if delta > 0:
                current_state = cpy.deepcopy(random_state)
                if current_state[1] < local_best[1]:
                    local_best = cpy.deepcopy(random_state)
                if local_best[1] < global_best[1]:
                    newglobal+=1
                    global_best = cpy.deepcopy(local_best)
            else:
                prob = prob_f(delta)
                distro = [prob, 1 - prob]
                random.seed(datetime.now())
                selection = random.choices(choice, distro)
                if selection == ["true"]:
                    current_state = cpy.deepcopy(random_state)
            t *= a
            states = []
        self.beststate = global_best[0]
        print("Total States Checked:",iterations,",",newglobal,"improved global optimal")
        return global_best[0]    
