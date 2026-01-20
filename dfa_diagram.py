from graphviz import Digraph

# Inisialisasi objek Digraph (graf berarah)
f = Digraph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5') # Mengatur layout horizontal

# 1. Tentukan Final States (lingkaran ganda)
final_states = {'q3', 'q5'}
f.attr('node', shape='doublecircle')
for state in final_states:
    f.node(state)

# 2. Tentukan Non-Final States (lingkaran tunggal)
all_states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
non_final_states = all_states - final_states
f.attr('node', shape='circle')
for state in non_final_states:
    f.node(state)

# 3. Tentukan Transisi
transitions = {
    'q0': {'0': 'q1', '1': 'q0'},
    'q1': {'0': 'q2', '1': 'q3'},
    'q2': {'0': 'q0', '1': 'q3'},
    'q3': {'0': 'q1', '1': 'q4'},
    'q4': {'0': 'q5', '1': 'q4'},
    'q5': {'0': 'q3', '1': 'q5'}
}

for state, inputs in transitions.items():
    for input_symbol, next_state in inputs.items():
        f.edge(state, next_state, label=input_symbol)

# 4. Tentukan Start State (gunakan node "invisible" untuk panah masuk)
f.attr('node', shape='none')
f.node('start', label="")
f.edge('start', 'q0') # Panah dari node tak terlihat ke q0

# Render dan lihat diagramnya (ini akan menghasilkan file fsm.gv.pdf atau fsm.gv.png di folder yang sama)
def new_func(f):
    f.render(view=False)
new_func(f) 
