from qiskit import QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider

# Instantiate IBMProvider with your API token
provider = IBMProvider('INSERT_API_HERE')

# For testing and building use simulator such as 'ibmq_qasm_simulator's
# In order to use an actual quantum computer selct 'ibm_nairobi'
# Available backends:  [<IBMBackend('ibm_perth')>, <IBMBackend('ibmq_qasm_simulator')>, <IBMBackend('ibmq_quito')>, <IBMBackend('simulator_extended_stabilizer')>, <IBMBackend('simulator_mps')>, <IBMBackend('simulator_statevector')>, <IBMBackend('ibmq_manila')>, <IBMBackend('ibmq_lima')>, <IBMBackend('ibmq_belem')>, <IBMBackend('simulator_stabilizer')>, <IBMBackend('ibm_nairobi')>, <IBMBackend('ibm_lagos')>, <IBMBackend('ibmq_jakarta')>]
# Alternatively use this command to locate computers/simulators: print("Available backends: ", provider.backends())

backend = provider.get_backend('ibmq_qasm_simulator') 

# Get the backend status
status = backend.status()

print("Starting script...")

# Print the number of jobs in queue
print("Number of jobs in queue: ", status.pending_jobs)

# Create a quantum circuit with 5 qubits and 5 classical bits
qc = QuantumCircuit(5, 5)

# Apply a Hadamard gate to each qubit to put them in a superposition of states
for i in range(5):
    qc.h(i)

# Measure each qubit and store the result in the classical bits
qc.measure(range(5), range(5))

# Execute the circuit on the chosen backend
job = execute(qc, backend, shots=50)

# Print the job ID
print("Job ID: ", job.job_id())

# Get the result of our measurement
result = job.result()
counts = result.get_counts(qc)

# Print the generated random numbers
print("Generated random numbers:")
for key, value in counts.items():
    for _ in range(value):
        print(int(key, 2))  # Convert the binary string to an integer
