We consider the one-dimensional non-Hermitian tight-binding model in the symplectic class (AII†) with Bloch Hamiltonian
\[
H(\beta) = (t - i\Delta\sigma_x + g\sigma_z)\,\beta^{-1} + (t + i\Delta\sigma_x - g\sigma_z)\,\beta,\qquad \beta = e^{ik},
\]
with \(t=1.0\) and \(\Delta=0.3\).

### 1. PBC dispersion relation
Writing the matrix explicitly:
\[
H(\beta) = \begin{pmatrix}
t+g & -i\Delta\\
-i\Delta & t-g
\end{pmatrix}\beta^{-1} + \begin{pmatrix}
t-g & i\Delta\\
i\Delta & t+g
\end{pmatrix}\beta.
\]
For \(\beta=e^{ik}\), we obtain
\[
H(k) = \begin{pmatrix}
2t\cos k - 2i g\sin k & -2\Delta\sin k\\
-2\Delta\sin k & 2t\cos k + 2i g\sin k
\end{pmatrix}.
\]
The characteristic equation \(\det(H(k)-E)=0\) gives
\[
(2t\cos k - E)^2 + (2g\sin k)^2 - (2\Delta\sin k)^2 =0,
\]
so
\[
E(k) = 2t\cos k \pm 2\sqrt{\Delta^2-g^2}\,\sin k.
\]

### 2. Condition for real PBC spectrum
The spectrum is real when the square root is real, i.e., \(\Delta^2-g^2 \ge 0\). With \(\Delta=0.3\), the condition is \(|g| \le 0.3\).

### 3. OBC GBZ radius
Treat \(\beta\) as a complex variable. The Hamiltonian can be written as
\[
H(\beta) = t(\beta+\beta^{-1})I + (\beta-\beta^{-1})M,\qquad M = -g\sigma_z + i\Delta\sigma_x.
\]
Diagonalising \(M\): its eigenvalues are \(\pm\lambda\) with \(\lambda = \sqrt{g^2-\Delta^2}\). Thus there exists a constant unitary matrix such that
\[
H(\beta) \sim \begin{pmatrix}
(t+\lambda)\beta + (t-\lambda)\beta^{-1} & 0\\
0 & (t-\lambda)\beta + (t+\lambda)\beta^{-1}
\end{pmatrix}.
\]
Hence the system decouples into two independent single‑band models with nearest‑neighbour hoppings:
- Band 1: right hopping \(t+\lambda\), left hopping \(t-\lambda\).
- Band 2: right hopping \(t-\lambda\), left hopping \(t+\lambda\).

For a generic single‑band model \(E = v_R\beta + v_L\beta^{-1}\), the open‑boundary condition leads to the generalised Brillouin zone (GBZ) radius \(r = \sqrt{|v_L/v_R|}\). Therefore the two bands have GBZ radii
\[
r_1 = \sqrt{\left|\frac{t-\lambda}{t+\lambda}\right|},\qquad r_2 = \sqrt{\left|\frac{t+\lambda}{t-\lambda}\right|} = \frac{1}{r_1}.
\]
The skin effect occurs when \(r\neq1\), i.e., when \(|g|>|\Delta|\) (so \(\lambda\) is real and nonzero). For definiteness we take the radius that is less than 1 (the GBZ inside the unit circle):
\[
r = \sqrt{\left|\frac{t-\sqrt{g^2-\Delta^2}}{t+\sqrt{g^2-\Delta^2}}\right|}\quad (|g|>|\Delta|).
\]

### 4. Evaluation for given parameters
- **(a) \(g=0.4\)**: \(\lambda = \sqrt{0.4^2-0.3^2} = \sqrt{0.07} = \frac{\sqrt{7}}{10} \approx 0.264575\).  
  Then
  \[
  r = \sqrt{\frac{1-\lambda}{1+\lambda}} = \sqrt{\frac{10-\sqrt{7}}{10+\sqrt{7}}} \approx 0.7626.
  \]
  Since \(r\neq1\), a skin effect occurs.
- **(b) \(g=0.2\)**: \(\lambda = \sqrt{0.2^2-0.3^2} = \sqrt{-0.05} = i\sqrt{0.05}\), so \(|t-\lambda|=|t+\lambda|\) and \(r=1\). No skin effect.

### 5. Boundary localisation of Kramers partners
The two decoupled bands are Kramers partners (related by time‑reversal symmetry). Their GBZ radii are reciprocals: one band has \(r<1\) and the other has \(1/r>1\). Consequently, eigenstates of the first band are localised near one edge (say the left boundary) while those of the second band are localised near the opposite edge (right boundary). Each Kramers pair thus exhibits opposite boundary localisation.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{sqrt\_g2\_minus\_D2\_a} &= \frac{\sqrt{7}}{10} \\
\mathrm{beta\_GBZ\_a} &= \sqrt{\frac{10-\sqrt{7}}{10+\sqrt{7}}} \\
\mathrm{beta\_GBZ\_b} &= 1 \\
\mathrm{skin\_threshold} &= 0.3
\end{aligned}
\]