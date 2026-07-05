The Hatano–Nelson model describes a one-dimensional chain with asymmetric nearest-neighbor hopping. The Hamiltonian on an open chain of sites \(j=1,\dots,N\) is:
\[
H = \sum_j \left( t_R\, c_{j+1}^\dagger c_j + t_L\, c_j^\dagger c_{j+1} \right),
\]
with \(t_R=1.4\) and \(t_L=0.6\). The exponential ansatz for eigenstates is \(\psi_j = \beta^j\). The analysis proceeds as follows.

### 1. Periodic boundary condition (PBC) spectrum
For PBC, the eigenstates are plane waves \(\psi_j = e^{ikj}\) with real \(k\). The eigenvalue equation from \(E\psi_j = t_R\psi_{j-1}+t_L\psi_{j+1}\) gives
\[
E(k) = t_R e^{-ik}+t_L e^{ik} = (t_R+t_L)\cos k + i(t_L-t_R)\sin k.
\]
As \(k\) runs over \([0,2\pi)\), \(E(k)\) traces an ellipse in the complex plane with:
- real semi-axis: \(t_R+t_L = 1.4+0.6 = 2\),
- imaginary semi-axis: \(|t_R-t_L| = 0.8 = t_R-t_L\) (since \(t_R>t_L\)).

### 2. Characteristic equation for the exponential ansatz
Insert \(\psi_j=\beta^j\) into the bulk eigenvalue equation (ignoring boundaries):
\[
E\beta^j = t_R\beta^{j-1}+t_L\beta^{j+1}.
\]
Dividing by \(\beta^{j-1}\) yields \(E\beta = t_R + t_L\beta^2\), or equivalently
\[
t_L\beta^2 - E\beta + t_R = 0.
\]
The product of the two roots \(\beta_1,\beta_2\) is \(\beta_1\beta_2 = t_R/t_L\).

### 3. Generalized Brillouin zone (GBZ) radius
For open boundaries, the allowed energies correspond to the two roots having equal magnitude (the GBZ condition): \(|\beta_1| = |\beta_2| = r\). Since \(|\beta_1\beta_2| = t_R/t_L\), we have \(r^2 = t_R/t_L\), so the GBZ radius is
\[
r = \sqrt{\frac{t_R}{t_L}} = \sqrt{\frac{1.4}{0.6}} = \sqrt{\frac{7}{3}} \approx 1.5275.
\]

### 4. OBC spectrum: reality and maximum modulus
On the GBZ, set \(\beta = r e^{i\theta}\) with \(r = \sqrt{t_R/t_L}\). Then the energy becomes
\[
E = t_R\beta^{-1}+t_L\beta = t_R\frac{1}{r}e^{-i\theta}+t_L r e^{i\theta}
= \sqrt{t_Rt_L}\,e^{-i\theta}+\sqrt{t_Rt_L}\,e^{i\theta} = 2\sqrt{t_Rt_L}\cos\theta,
\]
which is real. Hence the OBC spectrum is purely real. The maximum \(|E|\) occurs at \(\cos\theta=\pm1\), giving
\[
|E|_{\text{max}} = 2\sqrt{t_Rt_L} = 2\sqrt{1.4\cdot0.6} = 2\sqrt{0.84} = \frac{2\sqrt{21}}{5} \approx 1.833.
\]

### 5. Skin effect
A skin effect occurs whenever \(t_R \neq t_L\). Because \(t_R > t_L\), the stronger hopping is to the right; with the ansatz \(\psi_j = \beta^j\) and \(|\beta| = \sqrt{t_R/t_L} > 1\), the wavefunction amplitude grows with \(j\), so eigenstates are exponentially localized at the right edge \(j=N\).

---

FINAL ANSWER

\[
\begin{aligned}
\mathrm{pbc\_real\_semiaxis} &= 2 \\
\mathrm{pbc\_imag\_semiaxis} &= \frac{4}{5} \\
\mathrm{beta\_GBZ} &= \sqrt{\frac{7}{3}} \\
\mathrm{obc\_E\_max} &= \frac{2\sqrt{21}}{5}
\end{aligned}
\]