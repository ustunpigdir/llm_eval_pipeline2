Let's tackle this Hatano-Nelson problem step-by-step.

**1. PBC Spectrum E(k)**

For periodic boundary conditions (PBC), we have $\psi_{j+N} = \psi_j$.  We apply a Bloch ansatz: $\psi_j = e^{ikj} \beta^j$. Substituting this into the Hamiltonian:

$$
H \psi_j = \sum_j \left( t_R\, e^{ik(j+1)} \beta^{j+1} c_j^\dagger c_{j+1} + t_L\, e^{ikj} \beta^j c_j^\dagger c_{j+1} \right)
$$

The Hamiltonian acts on the creation operator, so we can rewrite the sum as:

$$
H \psi_j = \sum_j \left( t_R\, e^{ik} \beta \psi_{j+1} c_j^\dagger c_{j+1} + t_L\, \beta \psi_j c_j^\dagger c_{j+1} \right)
$$

Now, we can write the eigenvalue equation $H \psi = E \psi$:

$$
\sum_j \left( t_R\, e^{ik} \beta \psi_{j+1} c_j^\dagger c_{j+1} + t_L\, \beta \psi_j c_j^\dagger c_{j+1} \right) = E \psi_j
$$

Let's consider the term with $c_j^\dagger c_{j+1}$:
$$
t_R e^{ik} \beta \psi_{j+1} + t_L \beta \psi_j = E \psi_j
$$
Since $\psi_{j+1} = e^{-ik} \psi_j$, we have:
$$
t_R e^{ik} \beta e^{-ik} \psi_j + t_L \beta \psi_j = E \psi_j
$$
$$
(t_R \beta + t_L \beta) \psi_j = E \psi_j
$$
$$
(t_R + t_L) \beta \psi_j = E \psi_j
$$
Therefore, the energy eigenvalues are:

$$
E(k) = (t_R + t_L) \beta
$$

Since $\beta$ is a complex number, this represents a line in the complex energy plane. The real semi-axis is $t_R + t_L$ and the imaginary semi-axis is $t_R - t_L$.

**2. Characteristic Equation and Product of Roots**

The ansatz is $\psi_j = \beta^j$. Substituting this into the eigenvalue equation $H \psi = E \psi$:

$$
\sum_j \left( t_R\, \beta^{j+1} c_j^\dagger c_{j+1} + t_L\, \beta^j c_j^\dagger c_{j+1} \right) = E \beta^j
$$

Consider the term $c_j^\dagger c_{j+1}$:
$$
t_R \beta^{j+1} + t_L \beta^j = E \beta^j
$$
$$
t_R \beta + t_L = E
$$
$$
t_R \beta = E - t_L
$$
$$
\beta = \frac{E - t_L}{t_R}
$$
Substituting this back into the eigenvalue equation:
$$
\sum_j \left( t_R\, \frac{E - t_L}{t_R} \beta^{j+1} + t_L\, \beta^j c_j^\dagger c_{j+1} \right) = E \beta^j
$$
This is not correct. Let's go back to the original equation:
$$
t_R \beta^{j+1} + t_L \beta^j = E \beta^j
$$
$$
t_R \beta = E - t_L
$$
$$
\beta = \frac{E - t_L}{t_R}
$$
The characteristic equation is:
$$
\beta = \frac{E - t_L}{t_R}
$$
$$
t_R \beta - E + t_L = 0
$$
This is a linear equation, so there are two roots, which are identical. The product of the roots is $\beta$.
However, we can also consider the equation $H \psi = E \psi$ as:
$$
t_R \beta^{j+1} + t_L \beta^j = E \beta^j
$$
$$
t_R \beta^{j+1} = (E - t_L) \beta^j
$$
$$
t_R \beta = E - t_L
$$
$$
\beta = \frac{E - t_L}{t_R}
$$
The characteristic equation is $t_R \beta - (E - t_L) = 0$. The product of the roots is $\frac{t_L - E}{t_R}$.

**3. GBZ Radius**

The GBZ radius is the common modulus of the two solutions of the characteristic equation. The characteristic equation is $t_R \beta - (E - t_L) = 0$, so $\beta = \frac{E - t_L}{t_R}$.
For OBC, we have $\psi_0 = \psi_N$. Thus, $\beta^N = \beta^0 = 1$.
The characteristic equation for OBC is $t_R \beta^{N+1} + t_L \beta^N = E \beta^N$.
$t_R \beta = E - t_L$, so $\beta = \frac{E - t_L}{t_R}$.
The GBZ radius is the common modulus of the two solutions of the characteristic equation.
The characteristic equation is $t_R \beta^{N+1} + t_L \beta^N - E \beta^N = 0$.
$\beta^N (t_R \beta + t_L - E) = 0$.
Since $\beta \neq 0$, $t_R \beta + t_L - E = 0$, so $\beta = \frac{E - t_L}{t_R}$.
The GBZ radius is $|\beta| = \left| \frac{E - t_L}{t_R} \right|$.
For PBC, we have $E = (t_R + t_L) \beta$.
The GBZ radius is the common modulus of the two solutions of the characteristic equation.
The characteristic equation is $t_R \beta - (E - t_L) = 0$.
The roots are $\beta_1 = \beta_2 = \frac{E - t_L}{t_R}$.
The GBZ radius is $|\beta| = \sqrt{\frac{t_R}{t_L}}$.

**4. OBC Spectrum and E_max**

The OBC spectrum is complex. The maximum $|E|$ of the OBC spectrum in the large-$N$ limit is $2\sqrt{t_R t_L}$.

**5. Skin Effect**

A skin effect occurs when the OBC spectrum differs from the PBC prediction. This happens when $t_R \neq t_L$. In this case, $t_R = 1.4$ and $t_L = 0.6$, so a skin effect occurs. The eigenstates are localized at the left edge (since $t_L < t_R$).

\[
\begin{aligned}
\mathrm{pbc\_real\_semiaxis} &= t_R + t_L = 1.4 + 0.6 = 2 \\
\mathrm{pbc\_imag\_semiaxis} &= t_R - t_L = 1.4 - 0.6 = 0.8 \\
\mathrm{beta\_GBZ} &= \sqrt{\frac{t_R}{t_L}} = \sqrt{\frac{1.4}{0.6}} = \sqrt{\frac{7}{3}} \approx 1.5275 \\
\mathrm{obc\_E\_max} &= 2\sqrt{t_R t_L} = 2\sqrt{1.4 \times 0.6} = 2\sqrt{0.84} \approx 2 \times 0.9165 = 1.833
\end{aligned}
\]