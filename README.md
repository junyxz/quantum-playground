# Introduction
This Python script utilizes IBM's quantum computing services to create a Quantum Random Number Generator, which generates a series of "truly" random numbers by executing a quantum circuit that places qubits in a superposition of states and measures their output.

### Prerequisites
- Python 3.8 or above installed.
- [IBM Quantum Experience account](https://quantum-computing.ibm.com/).

Using your terminal or command prompt, navigate to the directory where you'd like to store the project and then clone the repository. Use the following command:
```
git clone https://github.com/junyxz/quantum_random_number_generator.git
```

### Dependencies
To install the dependencies, you need Python 3.6 or later and pip installed on your machine. You can then run:
```
pip install -r requirements.txt
```
This will install the following Python packages:

- qiskit==0.43.1
- qiskit-ibm_provider==0.6.0

### Obtain IBM Quantum Experience API Token
Log in to your IBM Quantum Experience account. If you don't have an account, you can create one for free [here](https://quantum-computing.ibm.com/).

- After logging in, go to your account settings by clicking on your profile on the top-right corner.
- Navigate to the 'Advanced' section, where you will find your API Token.
- Copy this token, you will need it in the next step.

### Configure Your API Token
Replace the placeholder in the script (YOUR_API_TOKEN) with your actual IBM Quantum Experience API token.

### Run the Script

Now, everything is set up. Run the script with the following command:
```
python3 app.py
```

### Understanding the Output

The script prints out a variety of information:
- Number of jobs in queue: This is the number of jobs waiting to be processed on the chosen quantum computer.
- Job ID: This is the unique identifier of your job.
- Generated random numbers: This script measures 5 qubits 50 times to generate a series of random numbers. Each random number is a five-digit binary string converted into decimal.