from qiskit import Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from algorithm import build_grover_circuit

def run_grover_and_plot(n_qubits=2, marked_state='11', shots=1024, save_img=True):
    qc = build_grover_circuit(n_qubits, marked_state)
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=shots).result()
    counts = result.get_counts()
    print(f"Measurement results: {counts}")

    # Save circuit image
    if save_img:
        fig = qc.draw('mpl')
        fig.savefig("grover_circuit.png")
        print("circuit image as grover_circuit.png")

    plot_histogram(counts)
    plt.title("Results")
    plt.savefig("grover_results.png")
    plt.show()

if __name__ == "__main__":
    run_grover_and_plot(n_qubits=2, marked_state='11')