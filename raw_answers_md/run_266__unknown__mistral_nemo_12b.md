**1. PBC Spectrum**

The PBC Hamiltonian in momentum space is given by:

$$
H = \sum_k \left( t_R\, e^{ik} + t_L\, e^{-ik} \right) c_k^\dagger c_k
$$

The PBC spectrum is obtained by solving the equation:

$$
E(k) = t_R\, e^{ik} + t_L\, e^{-ik}
$$

This can be rewritten as:

$$
E(k) = (t_R + t_L) \cos(k) + i (t_R - t_L) \sin(k)
$$

The curve traced by $E(k)$ in the complex energy plane is an ellipse with semi-axes $(t_R + t_L)$ and $(t_R - t_L)$.

**2. Characteristic Equation**

The characteristic equation for $\beta$ at energy $E$ is:

$$
E = t_R \beta + t_L \beta^{-1}
$$

This can be rewritten as:

$$
E \beta^2 - t_R \beta - t_L = 0
$$

The product of the roots of this quadratic equation is:

$$
\beta_1 \beta_2 = -\frac{t_L}{E}
$$

**3. GBZ Radius**

The GBZ radius $|\beta|$ is the common modulus of the two solutions of the characteristic equation. From the quadratic formula, we have:

$$
\beta = \frac{t_R \pm \sqrt{t_R^2 + 4t_L E}}{2E}
$$

The common modulus is:

$$
|\beta| = \sqrt{\frac{t_R^2 + 4t_L E}{4E^2}} = \sqrt{\frac{t_R}{t_L}}
$$

Evaluating this gives:

$$
|\beta| = \sqrt{\frac{1.4}{0.6}} \approx 1.26
$$

**4. OBC Spectrum**

The OBC spectrum is obtained by solving the characteristic equation with the ansatz $\psi_j = \beta^j$. This gives:

$$
E = t_R \beta + t_L \beta^{-1}
$$

Substituting $\beta = \sqrt{\frac{t_R}{t_L}}$ gives:

$$
E = t_R \sqrt{\frac{t_R}{t_L}} + t_L \sqrt{\frac{t_L}{t_R}}
$$

This is real, so the OBC spectrum is real. The maximum $|E|$ of the OBC spectrum in the large-$N$ limit is:

$$
|E| = t_R \sqrt{\frac{t_R}{t_L}} + t_L \sqrt{\frac{t_L}{t_R}} \approx 2 \sqrt{t_R t_L} \approx 2 \sqrt{1.4 \times 0.6} \approx 1.6
$$

**5. Skin Effect**

A skin effect occurs when the OBC spectrum differs from the PBC spectrum. This occurs when $t_R \neq t_L$, which is the case here. The eigenstates are localized at the right edge (site $N$) because $t_R > t_L$.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{pbc\_real\_semiaxis} &= 2.0 \\
\mathrm{pbc\_imag\_semiaxis} &= 0.8 \\
\mathrm{beta\_GBZ} &= 1.26 \\
\mathrm{obc\_E\_max} &= 1.6
\end{aligned}
\]