from board import Board

class Solver:
    def __init__(self, startState, algo):
        self.startState = startState
        self.algo = algo
        self.LIMIT = 1000
        if (self.algo == 1):
            self.hillclimb(self.startState)
        elif(self.algo == 2):
            self.simulatedAnnealing(self.startState)
    
    def hillclimb(self, startState):
        restarts = 0
        best_state = (self.startState, self.startState.calc_manhatten())
        while restarts <= self.LIMIT:
            pass
        pass

    def simulatedAnnealing(self, startState):

        pass
        

