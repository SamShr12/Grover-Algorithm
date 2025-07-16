# Grover's Algorithm Example (Qiskit) (Test)

This project demonstrates Grover’s quantum search algorithm using Qiskit.  
It includes a flexible implementation, test cases, and circuit images.

## Features

- Search for any 2-qubit marked state (e.g., `11`, `01`).
- Generates a quantum circuit image (`grover_circuit.png`).
- Plots results histogram (`grover_results.png`).
- Includes test cases (pytest).

## Usage

1. **Install requirements:**

   ```
   pip install -r requirements.txt
   ```

2. **Run Grover's algorithm:**

   ```
   python main.py
   ```

   This will print the measurement results, show a histogram, and save a circuit image.

3. **Run tests:**
   ```
   pytest
   ```
