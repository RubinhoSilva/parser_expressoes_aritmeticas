from Automata import Automata
from automato.states import q0, q1, qM, qf
from constants import ALFABETO_ENTRADA, ALFABETO_PILHA

automato = Automata(ALFABETO_ENTRADA, ALFABETO_PILHA, q0, {qf})

automato.addState(q1)
automato.addState(qM)
automato.addState(qf)
npdaAutomato = automato.getNPDAAutomata()

