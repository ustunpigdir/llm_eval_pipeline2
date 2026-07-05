**1. Average teleportation fidelity $F$ for $f = 0.900$:**

The average teleportation fidelity for an isotropic resource is given by $F = (2f+1)/3$. Plugging in $f = 0.900$, we get:

\[F = \frac{2(0.900) + 1}{3} = \frac{1.800 + 1}{3} = \frac{2.800}{3} = 0.933\]

**2. Classical limit:**

The 'classical limit' is the best average fidelity that can be achieved with measure-and-send and no entanglement. For a uniformly random input, the best fidelity is achieved when the receiver has a perfect copy of the input state. This gives a fidelity of 1. However, since we are considering the average fidelity over all input states, the classical limit is simply the average fidelity of the identity channel, which is 1/2.

**3. Minimum singlet fidelity $f$ to beat the classical limit:**

To beat the classical limit, we need $F > 1/2$. Using the formula for $F$, we have:

\[(2f+1)/3 > 1/2\]

Solving for $f$, we get:

\[2f + 1 > 1.5\]
\[2f > 0.5\]
\[f > 0.25\]

So, the minimum singlet fidelity $f$ to beat the classical limit is $f = 0.25$.

**4. Why $f > 1/2$ relates to entanglement and beating 2/3 certifies a quantum channel:**

- $f > 1/2$ relates to entanglement because the singlet state $|\Psi^-\rangle$ has a fidelity of 1 with itself, and any state with fidelity greater than 1/2 with $|\Psi^-\rangle$ must be entangled with it. This is because the fidelity of a state with $|\Psi^-\rangle$ is maximized when the state is entangled with it.

- Beating the 'classical limit' of 2/3 certifies a quantum channel because the classical limit is the best fidelity that can be achieved with measure-and-send and no entanglement. Therefore, if the teleportation fidelity is greater than 2/3, it must be due to the use of a quantum channel (i.e., entanglement).

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{teleport\_fidelity} &= 0.933 \\
\mathrm{classical\_limit} &= 0.5 \\
\mathrm{f\_threshold} &= 0.25
\end{aligned}
\]