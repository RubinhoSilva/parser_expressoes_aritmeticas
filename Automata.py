from automata.pda.npda import NPDA

class Automata:
    def __init__(self, inputAlphabet, stackAlphabet, initialState, endsStates):
        self.inputAlphabet = inputAlphabet
        self.stackAlphabet = stackAlphabet
        self.initialState = initialState
        self.endsStates = set()
        self.states = [initialState]

        for state in endsStates:
            self.endsStates.add(state.name)

    def addState(self, state):
        self.states.append(state)

    def getDict(self):
        dic = {}
        for state in self.states:
            transitionsState = {}
            for transition in state.transitions:
                stackTransitionsState = {}
                stackTransitionsStateAtual = set()

                stackCondition = transition.stackTransitions[0].stackCondition
                for stackTransition in transition.stackTransitions:
                    if stackCondition != stackTransition.stackCondition:
                        stackTransitionsState[stackCondition] = stackTransitionsStateAtual
                        stackCondition = stackTransition.stackCondition
                        stackTransitionsStateAtual = set()

                    stackTransitionsStateAtual.add((stackTransition.destinationState.name, stackTransition.insertStack))

                stackTransitionsState[stackTransition.stackCondition] = stackTransitionsStateAtual
                transitionsState[transition.condition] = stackTransitionsState

            dic[state.name] = transitionsState

        return dic

    def getNPDAAutomata(self):
        statesName = set()
        for state in self.states:
            statesName.add(state.name)

        return NPDA(
            states=statesName,
            input_symbols=self.inputAlphabet,
            stack_symbols=self.stackAlphabet,
            transitions=self.getDict(),
            initial_state=self.initialState.name,
            initial_stack_symbol='Z',
            final_states=self.endsStates
        )
