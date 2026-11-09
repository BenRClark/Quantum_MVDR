This code performs Minimum variance distortionless response (MVDR) using block encoding and Quantum Singular Value Decomposition (QSVT) on a quantum computer. The code can by ran by running and modifying main.py. There are a few key parameters. 



M - number of antennas on antenna array

JAMMER\_DEG - angle relative to 0 where jammer is

JNR\_DB - noise of jammer

T - number of signals (snapshots) received



The code by default runs the process multiple times with different jammer strengths since a more powerful jammer produces a matrix with a larger condition number. This tests the limits of QSVT for inverting matrices. The jupyter notebook explains the approach and the problem in detail. However, to summarize results, we find that matrices although this method does work, it is far outclassed by the classical method. Computing matrix inversions for higher condition numbers require solving a O(N^3) problem of solving a nonlinear system of equations looking for Chebyschev angles. 



However, even if the problem of finding angles could be worked around, reading out the result of QMVDR would require quantum state tomography or extra qubits to store M phases. Therefore, we have concluded that this problem is not ideal for a quantum computer. As it stands now, the space complexity is 



$S = 2\\log2{M} + \\log2{2\*T} + 2$



and the depth required is 



$D \\approx 20\*k$



where k is the condition number. As we can see, even for a moderate condition number, the gate depth is already quite large. 

