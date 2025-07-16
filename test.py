import pytest
from qiskit import Aer, execute
from algorithm import build_grover_circuit

@pytest.mark.parametrize("marked_state", ["00", "01", "10", "11"])
def test_grover_finds_marked_state(marked_state):
    n_qubits = 2
    qc = build_grover_circuit(n_qubits, marked_state)
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=500).result()
    counts = result.get_counts()
    assert max(counts, key=counts.get) == marked_state
    assert counts[marked_state] / 500 > 0.4