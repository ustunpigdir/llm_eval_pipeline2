**1. Average teleportation fidelity $F$ for $f = 0.900$:**

The average teleportation fidelity $F$ for an isotropic resource is given by the formula $F = (2f+1)/3$. Plugging in $f = 0.900$, we get:

\[F = \frac{2(0.900) + 1}{3} = \frac{1.800 + 1}{3} = \frac{2.800}{3} = 0.933\]

**2. Classical limit:**

The classical limit is the best average fidelity that can be achieved with measure-and-send and no entanglement. For an isotropic resource, this is given by the formula $F_{classical} = (1 + \sqrt{2})/4$. Calculating this, we get:

\[F_{classical} = \frac{1 + \sqrt{2}}{4} \approx \frac{1 + 1.414}{4} \approx \frac{2.414}{4} \approx 0.603\]

**3. Minimum singlet fidelity $f$ to beat the classical limit:**

To find the minimum singlet fidelity $f$ that beats the classical limit, we set up the inequality $F > F_{classical}$ and solve for $f$:

\[\frac{2f + 1}{3} > \frac{1 + \sqrt{2}}{4}\]

Multiplying both sides by 12 to clear the denominators, we get:

\[8f + 4 > 3(1 + \sqrt{2})\]

\[8f > 3 + 3\sqrt{2} - 4\]

\[8f > 3\sqrt{2} - 1\]

\[f > \frac{3\sqrt{2} - 1}{8}\]

Calculating the right side, we get:

\[f > \frac{3(1.414) - 1}{8} \approx \frac{4.242 - 1}{8} \approx \frac{3.242}{8} \approx 0.405\]

So, the minimum singlet fidelity $f$ to beat the classical limit is approximately $0.405$.

**4. Why $f > 1/2$ relates to entanglement and beating $2/3$ certifies a quantum channel:**

- If $f > 1/2$, the resource is entangled. This is because the singlet state $|\Psi^-\rangle$ has a fidelity of $1$ with itself, and any state with fidelity greater than $1/2$ with $|\Psi^-\rangle$ must be entangled with it.
- Beating the classical limit of $2/3$ certifies a quantum channel because the classical limit is the best fidelity that can be achieved with measure-and-send and no entanglement. If the teleportation fidelity is greater than $2/3$, it must be due to the use of a quantum resource (entanglement).

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{teleport\_fidelity} &= 0.933 \\
\mathrm{classical\_limit} &= 0.603 \\
\mathrm{f\_threshold} &= 0.405
\end{aligned}
\]