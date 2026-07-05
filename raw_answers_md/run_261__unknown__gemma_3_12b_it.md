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

Now, we can write the eigenvalue equation:

$$
E \psi_j = \sum_j \left( t_R\, e^{ik} \beta \psi_{j+1} c_j^\dagger c_{j+1} + t_L\, \beta \psi_j c_j^\dagger c_{j+1} \right)
$$

Since $c_j^\dagger c_{j+1}$ creates a particle at $j+1$ and destroys it at $j$, we can write the equation as:

$$
E e^{-ikj} \beta^j = t_R e^{ik} \beta \psi_{j+1} + t_L \beta \psi_j
$$

Substituting $\psi_{j+1} = e^{ik(j+1)} \beta^{j+1} = e^{ik} \beta \psi_j$:

$$
E e^{-ikj} \beta^j = t_R e^{ik} \beta (e^{ik} \beta \psi_j) + t_L \beta \psi_j
$$
$$
E e^{-ikj} \beta^j = t_R e^{2ik} \beta^2 \psi_j + t_L \beta \psi_j
$$
$$
E e^{-ikj} \beta^j = (t_R e^{2ik} \beta^2 + t_L \beta) \psi_j
$$

For this to hold for all $j$, we must have:

$$
E = t_R e^{2ik} \beta + t_L
$$
$$
\beta = \frac{E - t_L}{t_R e^{2ik}}
$$

Let $k = \frac{K}{2}$, where $K$ is the Bloch wavevector in the first Brillouin zone. Then $e^{2ik} = e^{K}$.  We can rewrite the equation as:

$$
E(K) = t_R e^K \beta + t_L
$$

To find the spectrum, we need to solve for $\beta$ in terms of $E$.  We can rewrite this as:

$$
\frac{E - t_L}{t_R} = e^K \beta
$$
$$
\beta = \frac{E - t_L}{t_R e^K}
$$

The equation $E(K) = t_R e^K \beta + t_L$ describes an ellipse in the complex $E$-$K$ plane. The real semi-axis is $t_R + t_L$ and the imaginary semi-axis is $t_R - t_L$.

**2. Characteristic Equation and Product of Roots**

From the PBC analysis, we have:

$$
E = t_R e^{2ik} \beta + t_L
$$

For the open boundary case, we use the ansatz $\psi_j = \beta^j$.  Substituting this into the Hamiltonian:

$$
H \beta^j = \sum_j \left( t_R \beta^{j+1} + t_L \beta^{j-1} \right) \psi_j
$$
$$
E \beta^j = t_R \beta^{j+1} + t_L \beta^{j-1}
$$
$$
E \beta^j = t_R \beta \beta^j + \frac{t_L}{\beta} \beta^j
$$
$$
E = t_R \beta + \frac{t_L}{\beta}
$$
$$
E \beta = t_R \beta^2 + t_L
$$
$$
t_R \beta^2 - E \beta + t_L = 0
$$

This is the characteristic equation. The product of the roots $\beta_1, \beta_2$ is given by $\beta_1 \beta_2 = \frac{t_L}{t_R}$.

**3. GBZ Radius $|\beta|$**

The GBZ radius is the common modulus of the two solutions of the characteristic equation. The solutions are:

$$
\beta = \frac{E \pm \sqrt{E^2 - 4t_R t_L}}{2t_R}
$$

The GBZ radius is the modulus of the solution with the smallest modulus.  We want to find $|\beta|$ such that $t_R \beta^2 - E \beta + t_L = 0$.  The product of the roots is $\frac{t_L}{t_R}$.  Let $\beta_1$ and $\beta_2$ be the roots. Then $\beta_1 \beta_2 = \frac{t_L}{t_R}$.  The GBZ radius is the common modulus of the two roots.  We can find the roots by solving the quadratic equation.  However, we can also use the fact that the product of the roots is $\frac{t_L}{t_R}$.  The GBZ radius is given by $|\beta| = \sqrt{\frac{t_L}{t_R}}$.

$$
|\beta| = \sqrt{\frac{t_L}{t_R}} = \sqrt{\frac{0.6}{1.4}} = \sqrt{\frac{3}{7}} \approx 0.65465
$$

**4. OBC Spectrum and E_max**

The OBC spectrum is complex. The OBC spectrum is given by the solutions to $t_R \beta^2 - E \beta + t_L = 0$.  The solutions are $\beta = \frac{E \pm \sqrt{E^2 - 4t_R t_L}}{2t_R}$.  For the OBC spectrum to exist, we need $E^2 \ge 4t_R t_L$.  The maximum $|E|$ of the OBC spectrum occurs when $E^2 = 4t_R t_L$, so $|E| = 2\sqrt{t_R t_L}$.

$$
|E| = 2\sqrt{t_R t_L} = 2\sqrt{1.4 \times 0.6} = 2\sqrt{0.84} \approx 2 \times 0.9165 = 1.833
$$

**5. Skin Effect**

A skin effect occurs when the OBC spectrum is not real. This happens when $E^2 < 4t_R t_L$.  In our case, $4t_R t_L = 4(1.4)(0.6) = 3.36$.  Since $t_R > t_L$, the eigenstates are localized at the left edge (where $j=1$). This is because $t_R$ is larger, so the exponential decay is slower on the right side.

In general, a skin effect occurs when $t_R \neq t_L$. The localization edge is at the edge where the larger hopping amplitude is located.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{pbc\_real\_semiaxis} &= t_R + t_L = 2 \\
\mathrm{pbc\_imag\_semiaxis} &= t_R - t_L = 0.2 \\
\mathrm{beta\_GBZ} &= \sqrt{\frac{t_R}{t_L}} = \sqrt{\frac{1.4}{0.6}} = \sqrt{\frac{7}{3}} \approx 1.5275 \\
\mathrm{obc\_E\_max} &= 2\sqrt{t_R \cdot t_L} = 2\sqrt{1.4 \cdot 0.6} = 2\sqrt{0.84} \approx 1.833
\end{aligned}
\]