from State import State

q0 = State('q0')
qM = State('qM')
q1 = State('q1')
qf = State('qf')

transition_q0 = q0.addTransition('')
transition_q0.addStackTransition('Z', qM, 'S')

transition_q1 = q1.addTransition('')
transition_q1.addStackTransition('$', qM, ('$', 'S'))

transition_qM_vazia = qM.addTransition('')
transition_qM_vazia.addStackTransition('S', qM, ('V', '=', 'E'))
transition_qM_vazia.addStackTransition('E', qM, ('E', '+', 'T'))
transition_qM_vazia.addStackTransition('E', qM, ('E', '-', 'T'))
transition_qM_vazia.addStackTransition('E', qM, 'T')
transition_qM_vazia.addStackTransition('T', qM, ('T', '*', 'F'))
transition_qM_vazia.addStackTransition('T', qM, ('T', '/', 'F'))
transition_qM_vazia.addStackTransition('T', qM, 'F')
transition_qM_vazia.addStackTransition('F', qM, ('(', 'E', ')'))
transition_qM_vazia.addStackTransition('F', qM, ('n', 'u', 'm'))
transition_qM_vazia.addStackTransition('F', qM, 'V')
transition_qM_vazia.addStackTransition('V', qM, ('i', 'd'))
transition_qM_vazia.addStackTransition('$', qf, '')

transition_qM_atribuicao = qM.addTransition('=')
transition_qM_atribuicao.addStackTransition('=', qM, '')

transition_qM_mais = qM.addTransition('+')
transition_qM_mais.addStackTransition('+', qM, '')

transition_qM_menos = qM.addTransition('-')
transition_qM_menos.addStackTransition('-', qM, '')

transition_qM_abre = qM.addTransition('(')
transition_qM_abre.addStackTransition('(', qM, '')

transition_qM_fecha = qM.addTransition(')')
transition_qM_fecha.addStackTransition(')', qM, '')

transition_qM_i = qM.addTransition('i')
transition_qM_i.addStackTransition('i', qM, '')

transition_qM_d = qM.addTransition('d')
transition_qM_d.addStackTransition('d', qM, '')

transition_qM_n = qM.addTransition('n')
transition_qM_n.addStackTransition('n', qM, '')

transition_qM_u = qM.addTransition('u')
transition_qM_u.addStackTransition('u', qM, '')

transition_qM_m = qM.addTransition('m')
transition_qM_m.addStackTransition('m', qM, '')

transition_qM_barra = qM.addTransition('/')
transition_qM_barra.addStackTransition('/', qM, '')

transition_qM_multiplicacao = qM.addTransition('*')
transition_qM_multiplicacao.addStackTransition('*', qM, '')