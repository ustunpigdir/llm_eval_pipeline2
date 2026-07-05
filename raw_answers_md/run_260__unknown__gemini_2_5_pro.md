Here is a step-by-step derivation for the Hatano–Nelson model as requested.

### 1. Periodic Boundary Conditions (PBC) Spectrum

Under periodic boundary conditions (PBC), the system is translationally invariant, and we can use the Bloch theorem. The eigenstates are plane waves $\psi_j = e^{ikj}$, where $k$ is the crystal momentum. The Hamiltonian in momentum space is a $1 \times 1$ matrix, whose value is the energy dispersion $E(k)$.

We start with the real-space Hamiltonian:
$$
H = \sum_j \left( t_R\, c_{j+1}^\dagger c_j + t_L\, c_j^\dagger c_{j+1} \right)
$$
The corresponding time-independent Schrödinger equation for the wavefunction amplitudes $\psi_j$ is:
$$
t_R \psi_{j-1} + t_L \psi_{j+1} = E \psi_j
$$
Substituting the Bloch ansatz $\psi_j = e^{ikj}$ (we can omit the normalization for finding the dispersion):
$$
t_R e^{ik(j-1)} + t_L e^{ik(j+1)} = E e^{ikj}
$$
Dividing by $e^{ikj}$, we get the energy dispersion $E(k)$:
$$
E(k) = t_R e^{-ik} + t_L e^{ik}
$$
Using Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$, we can separate the real and imaginary parts of the energy:
$$
E(k) = t_R (\cos k - i \sin k) + t_L (\cos k + i \sin k)
$$
$$
E(k) = (t_R + t_L) \cos k - i (t_R - t_L) \sin k
$$
This is the parametric equation of a curve in the complex energy plane, with $k$ as the parameter. Let $E = x + iy$. Then:
$$
x(k) = (t_R + t_L) \cos k
$$
$$
y(k) = -(t_R - t_L) \sin k
$$
We can write this in the standard form of an ellipse:
$$
\left(\frac{x}{t_R + t_L}\right)^2 + \left(\frac{y}{t_R - t_L}\right)^2 = \cos^2 k + \sin^2 k = 1
$$
The PBC spectrum traces an ellipse in the complex plane centered at the origin. The semi-axes are:
- Real semi-axis: $a = t_R + t_L$
- Imaginary semi-axis: $b = |t_R - t_L|$

Given the values $t_R = 1.4$ and $t_L = 0.6$:
- Real semi-axis: $a = 1.4 + 0.6 = 2.0$
- Imaginary semi-axis: $b = |1.4 - 0.6| = 0.8$

### 2. Characteristic Equation and Product of Roots

For open boundary conditions (OBC), we use the generalized Bloch ansatz $\psi_j = \beta^j$, where $\beta$ is a complex number. We substitute this into the Schrödinger equation $t_R \psi_{j-1} + t_L \psi_{j+1} = E \psi_j$:
$$
t_R \beta^{j-1} + t_L \beta^{j+1} = E \beta^j
$$
Assuming $\beta \neq 0$, we can divide the entire equation by $\beta^{j-1}$:
$$
t_R + t_L \beta^2 = E \beta
$$
Rearranging this gives the characteristic equation, which is a quadratic equation for $\beta$:
$$
t_L \beta^2 - E \beta + t_R = 0
$$
For a given energy $E$, this equation has two roots, $\beta_1$ and $\beta_2$. According to Vieta's formulas, the product of the roots of a quadratic equation $ax^2+bx+c=0$ is $c/a$. For our characteristic equation, $a=t_L$, $b=-E$, and $c=t_R$.
Therefore, the product of the roots is:
$$
\beta_1 \beta_2 = \frac{t_R}{t_L}
$$

### 3. Generalized Brillouin Zone (GBZ) Radius

The non-Bloch band theory for OBC states that the bulk spectrum in the thermodynamic limit ($N \to \infty$) is determined by the energies $E$ for which the roots of the characteristic equation have the same modulus. This common modulus defines the radius of the Generalized Brillouin Zone (GBZ) in the complex $\beta$-plane.
Let the two roots be $\beta_1$ and $\beta_2$. The condition is $|\beta_1| = |\beta_2| = |\beta|_{GBZ}$.
From the product of the roots derived in the previous step, we have:
$$
|\beta_1 \beta_2| = \left|\frac{t_R}{t_L}\right|
$$
Substituting the equal modulus condition:
$$
|\beta_1| |\beta_2| = |\beta|_{GBZ}^2 = \left|\frac{t_R}{t_L}\right|
$$
Since $t_R$ and $t_L$ are given as positive real numbers, the GBZ radius is:
$$
|\beta|_{GBZ} = \sqrt{\frac{t_R}{t_L}}
$$
Using the given values $t_R = 1.4$ and $t_L = 0.6$:
$$
|\beta|_{GBZ} = \sqrt{\frac{1.4}{0.6}} = \sqrt{\frac{14}{6}} = \sqrt{\frac{7}{3}}
$$

### 4. Open Boundary Conditions (OBC) Spectrum

The OBC spectrum consists of all energies $E$ that satisfy the GBZ condition $|\beta_1| = |\beta_2|$. We can find the explicit form of this spectrum. Let's solve the characteristic equation for $\beta$:
$$
\beta = \frac{E \pm \sqrt{E^2 - 4t_L t_R}}{2t_L}
$$
The two roots $\beta_1$ and $\beta_2$ have the same modulus if the term under the square root (the discriminant $\Delta = E^2 - 4t_L t_R$) is non-positive, i.e., $\Delta \le 0$. In this case, the roots are complex conjugates of each other (or purely imaginary).
If $\Delta \le 0$, then $\sqrt{\Delta} = i\sqrt{4t_L t_R - E^2}$, and the roots are:
$$
\beta_{1,2} = \frac{E \pm i\sqrt{4t_L t_R - E^2}}{2t_L}
$$
The squared modulus of these roots is:
$$
|\beta|^2 = \left(\frac{E}{2t_L}\right)^2 + \left(\frac{\sqrt{4t_L t_R - E^2}}{2t_L}\right)^2 = \frac{E^2 + (4t_L t_R - E^2)}{4t_L^2} = \frac{4t_L t_R}{4t_L^2} = \frac{t_R}{t_L}
$$
This confirms that the condition $\Delta \le 0$ is equivalent to the GBZ condition $|\beta|^2 = t_R/t_L$. The OBC spectrum is therefore given by the range of (real) energies $E$ for which $E^2 - 4t_L t_R \le 0$.
$$
E^2 \le 4t_L t_R
$$
This implies that the OBC spectrum is purely real and forms a continuous line segment on the real axis:
$$
-2\sqrt{t_L t_R} \le E \le 2\sqrt{t_L t_R}
$$
The maximum absolute value of the energy in the OBC spectrum is:
$$
|E|_{\max} = 2\sqrt{t_L t_R}
$$
Using the given values:
$$
|E|_{\max} = 2\sqrt{0.6 \times 1.4} = 2\sqrt{0.84}
$$

### 5. Skin Effect and Eigenstate Localization

**Skin Effect:** The skin effect is the phenomenon where the OBC spectrum and eigenstates differ significantly from the PBC predictions.
- The PBC spectrum is a complex ellipse with semi-axes $t_R+t_L=2.0$ and $t_R-t_L=0.8$.
- The OBC spectrum is a real line segment from $-2\sqrt{0.84}$ to $+2\sqrt{0.84}$ (approx. $[-1.833, 1.833]$).
Since the PBC and OBC spectra are different, the system exhibits a non-Hermitian skin effect. In general, this occurs whenever $t_R \neq t_L$, which makes the Hamiltonian non-Hermitian.

**Eigenstate Localization:** The localization of the eigenstates under OBC is determined by the GBZ radius, $|\beta|_{GBZ} = \sqrt{t_R/t_L}$. The OBC eigenstates are superpositions of the form $\psi_j \propto \beta_1^j - \beta_2^j$, where $|\beta_1|=|\beta_2|=|\beta|_{GBZ}$. The spatial profile of the probability density $|\psi_j|^2$ is therefore enveloped by $(|\beta|_{GBZ}^2)^j = (t_R/t_L)^j$.

- If $t_R > t_L$, then $|\beta|_{GBZ} > 1$. The envelope $(t_R/t_L)^j$ grows exponentially with the site index $j$. Consequently, all bulk eigenstates are localized at the right edge of the chain (largest $j$).
- If $t_R < t_L$, then $|\beta|_{GBZ} < 1$. The envelope decays with $j$, and all bulk eigenstates are localized at the left edge of the chain (smallest $j$).

For the given values $t_R = 1.4$ and $t_L = 0.6$, we have $t_R > t_L$. Therefore, the eigenstates are localized at the **right edge**.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{pbc\_real\_semiaxis} &= 2.0 \\
\mathrm{pbc\_imag\_semiaxis} &= 0.8 \\
\mathrm{beta\_GBZ} &= \sqrt{7/3} \\
\mathrm{obc\_E\_max} &= 2\sqrt{0.84}
\end{aligned}
\]