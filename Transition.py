from StackTransition import StackTransition


class Transition:
    def __init__(self, condition):
        self.condition = condition
        self.stackTransitions = []

    def addStackTransition(self, stackCondition, destinationState, insertStack):
        self.stackTransitions.append(StackTransition(stackCondition, destinationState, insertStack))




