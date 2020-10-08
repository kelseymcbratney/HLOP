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
                if states[0][1] < best_state[1]:
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

    # def simulatedAnnealing(self):
        
    #     t = 10000 # tempature
    #     a = .05
    #     prob = lambda a : exp(a/t)
    #     choice = ["true", "false"]
    #     temp_delta = -2 #best state dist - the worse off state dist
        
    #     alpha = prob(temp_delta)
        
    #     distro = [alpha, 1-alpha]
    #     random.seed(datetime.now())
    #     selection = random.choices(choice, distro)

    #     # decrease tempature




    #     restarts = 0
    #     best_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
    #     current_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
    #     while t > 0:
    #         possible_states = current_state[0].move()
    #         states = []
    #         for state in possible_states:
    #             states.append((cpy.copy(state), state.calc_manhatten()))
    #         states.sort(key = lambda x:x[1]) # can be used for finding the lowest manhatten distance, index 0 will be new state to move into
    #         if states[0][1] < best_state[1]:
    #             best_state = cpy.deepcopy(states[0])
    #             current_state = cpy.deepcopy(states[0])
    #             states = []
    #             continue
    #         else:
    #             t = t * a
    #             current_state = states[random] #TODO implement random state selection
    #             temp_delta = current_state[1] - best_state[1]
    #             states = []
    #             break

    #     self.beststate = best_state[0]
    #     return best_state[0]




        """
        randomly select new state
        if new state is better than current, current state becomes new state. Save this state as global optimum
        if new state is worse, has probability of still replacing current state, depending on current temperature, and delta E
        """
        
    def simulatedAnnealing(self):
        t = 10000 # tempature
        a = .05
        prob_f = lambda x : round(exp(round(x, 3)/round(t,3)), 5)
        choice = ["true", "false"]
        best_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        current_state = (cpy.deepcopy(self.startState), self.startState.calc_manhatten())
        while t > 1:
            possible_states = current_state[0].move()
            states = []
            for state in possible_states:
                states.append((cpy.copy(state), state.calc_manhatten()))
            random_state = states[random.randrange(0,len(states))] # Probably needs fixing
            delta = best_state[1] - random_state[1]
            prob = prob_f(delta)
            distro = [prob, 1-prob]
            random.seed(datetime.now())
            selection = random.choices(choice, distro)
            if delta > 0 or selection == ["true"]:
                if delta < 0:
                    t = float(t * a)
                elif random_state[1] < best_state[1]:
                    best_state = cpy.deepcopy(random_state)
                current_state = cpy.deepcopy(random_state)
                states = []
                continue 
        self.beststate = best_state[0]
        return best_state[0]    

        
b = Board(10,10,20)
b.launch()
print(b.calc_manhatten())
s = Solver(b,1)
s2 = Solver(b,2)

print()
s.beststate.printArray()
print(s.beststate.calc_manhatten())

print()
s2.beststate.printArray()
print(s2.beststate.calc_manhatten())