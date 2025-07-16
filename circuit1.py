from qiskit import QuantumCircuit

def grover_oracle(n_qubits, marked_state):

    oracle = QuantumCircuit(n_qubits)
    for idx, bit in enumerate(reversed(marked_state)):
        if bit == '0':
            oracle.x(idx)
    if n_qubits == 2:
        oracle.cz(0, 1)
    else:
        oracle.h(n_qubits-1)
        oracle.mcx(list(range(n_qubits-1)), n_qubits-1)
        oracle.h(n_qubits-1)
    for idx, bit in enumerate(reversed(marked_state)):
        if bit == '0':
            oracle.x(idx)
    return oracle

def grover_diffuser(n_qubits):

    diffuser = QuantumCircuit(n_qubits)
    diffuser.h(range(n_qubits))
    diffuser.x(range(n_qubits))
    if n_qubits == 2:
        diffuser.h(1)
        diffuser.cz(0, 1)
        diffuser.h(1)
    else:
        diffuser.h(n_qubits-1)
        diffuser.mcx(list(range(n_qubits-1)), n_qubits-1)
        diffuser.h(n_qubits-1)
    diffuser.x(range(n_qubits))
    diffuser.h(range(n_qubits))
    return diffuser

def build_grover_circuit(n_qubits=2, marked_state='11'):
    from math import floor, pi, sqrt
    num_iterations = floor((pi/4) * sqrt(2 ** n_qubits))
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))
    oracle = grover_oracle(n_qubits, marked_state)
    diffuser = grover_diffuser(n_qubits)
    for _ in range(num_iterations):
        qc.append(oracle.to_gate(), range(n_qubits))
        qc.append(diffuser.to_gate(), range(n_qubits))
    qc.measure(range(n_qubits), range(n_qubits))
    return qc