from src import QMVDR
import qiskit as qis
import numpy as np

results = []

# Antennas on antenna array

M = 8
JAMMER_DEG = [22.0]
JNR_DB = [40.0]
RNG = np.random.default_rng(seed=7)
T = 2**3  # snapshots (half the snapshots will be used to produce a head-on signal)

X_train = QMVDR.simulate_snapshots(M, JAMMER_DEG, JNR_DB, T, RNG)

# add more explicit noise
X = np.hstack([X_train, np.sqrt(T * 20) * np.eye(M)])

print("Qubits needed ", int(np.log2(np.shape(X)[1]) + 2 * int(np.log2(M) + 2)))

sign = qis.QuantumRegister(1, "sign")
phase = qis.QuantumRegister(1, "phase")
time = qis.QuantumRegister(int(np.log2(np.shape(X)[1])), "time")
arrays = qis.QuantumRegister(int(np.log2(M)), "arrays")
qsvt = qis.QuantumRegister(int(np.log2(M)), "qsvt")
registers = [sign, phase, time, arrays, qsvt]
qc = qis.QuantumCircuit(*registers)


for pow in [10, 20, 40, 80, 100, 200]:
    results.append(
        QMVDR.compare_methods(
            M, JAMMER_DEG, [pow], T, RNG, registers, TARGET_DEG=0, approx_cond=10
        )
    )

print(results)

QMVDR.plot_results(results, 10)
