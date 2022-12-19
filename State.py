from Transition import Transition


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def addTransition(self, condition):
        transition = Transition(condition)
        self.transitions.append(transition)

        return transition



    def getByCondition(self, condition):
        transitions = []
        for transition in self.transitions:
            if condition == transition.condition:
                transitions.append(transition)

        return transitions
