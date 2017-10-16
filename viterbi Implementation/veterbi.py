from collections import defaultdict as ddict

class Viterbi(object):
    START = "start"
   
    def __init__(self):
        self.states = []
        self.transitions = ddict(lambda: ddict(lambda: 0.0))
        self.observations = ddict(lambda: ddict(lambda: 0.0))
        
    #Building the model
    def addState(self, state, transitions={}, observations={}):
        self.states.append(state)
        for targetState, probability in transitions.items():
            self.transitions[state][targetState] = probability
            
        for observation, probability in observations.items():
            self.observations[state][observation] = probability
            
    # Predict the path for given observations      
    def predictPath(self, observations):
        trellis = ddict(lambda: ddict(lambda: 0.0))
        backPointers = ddict(lambda: {}) 
        trellis[-1][self.START] = 1.0
             
        i = -1
        for i, observation in enumerate(observations):
            for state in self.states:               
                pathProbalilities = {}
                for previousState in self.states:
                    pathProbalilities[previousState] = trellis[i - 1][previousState] * self.transitions[previousState][state] *self.observations[state][observation]

                bestState = max(pathProbalilities, key=pathProbalilities.get)
                trellis[i][state] = pathProbalilities[bestState]
                backPointers[i][state] = bestState
                
        currentState = max(trellis[i], key=trellis[i].get)    
        beststates = []
        for i in range(i, -1, -1):
            beststates.append(currentState)
            currentState = backPointers[i][currentState]
            
        beststates.reverse()
        return beststates

def main():
    viterbi = Viterbi()
    viterbi.addState(Viterbi.START, dict(H=0.8, C=0.2))
    viterbi.addState('H', dict(H=0.7, C=0.3), {1:.2, 2:.4, 3:.4})
    viterbi.addState('C', dict(H=0.4, C=0.6), {1:.5, 2:.4, 3:.1})
    states = viterbi.predictPath([3, 3, 1, 1, 2, 2, 3, 1, 3])
    
    print("Trace for observation 3 3 1 1 2 2 3 1 3")
    print(states)    
    print("Enter the observation to be predicted")
    
    observations = [int(x) for x in input().split()]
    statesEntered = viterbi.predictPath(observations)
    
    print(statesEntered)
    
 


if __name__ == "__main__":
    main()
    
    
