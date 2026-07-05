**1. PBC Spectrum**

The PBC Hamiltonian in momentum space is given by:

$$
H = \sum_k \left( t_R\, e^{-ik} + t_L\, e^{ik} \right) c_k^\dagger c_k
$$

The PBC spectrum is:

$$
E(k) = t_R\, e^{-ik} + t_L\, e^{ik}
$$

The real and imaginary semi-axes of the PBC spectral ellipse are:

$$
pbc\_real\_semiaxis = t_R + t_L = 2.0
$$

$$
pbc\_imag\_semiaxis = t_R - t_L = 0.8
$$

**2. Characteristic Equation**

The characteristic equation for $\beta$ at energy $E$ is:

$$
t_R\, \beta + t_L\, \beta^{-1} = E
$$

The product of the two roots is:

$$
\beta_1\, \beta_2 = \frac{t_L}{t_R}
$$

**3. GBZ Radius**

The GBZ radius $|\beta|$ is given by:

$$
|\beta| = \sqrt{\frac{t_L}{t_R}} = \sqrt{\frac{0.6}{1.4}} \approx 0.745
$$

**4. OBC Spectrum**

The OBC spectrum is complex due to the non-Hermitian nature of the Hamiltonian. The maximum $|E|$ of the OBC spectrum in the large-$N$ limit is:

$$
obc\_E\_max = 2\, \sqrt{t_R\, t_L} = 2\, \sqrt{1.4 \times 0.6} \approx 1.633
$$

**5. Skin Effect**

A skin effect occurs when the product of the two roots of the characteristic equation is less than 1, i.e., $\frac{t_L}{t_R} < 1$. In this case, $\frac{t_L}{t_R} = 0.42857$, so a skin effect occurs. The eigenstates are localized at the right edge (site $N$) because $t_R > t_L$.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{pbc\_real\_semiaxis} &= 2.0 \\
\mathrm{pbc\_imag\_semiaxis} &= 0.8 \\
\mathrm{beta\_GBZ} &= 0.745 \\
\mathrm{obc\_E\_max} &= 1.633
\end{aligned}
\]