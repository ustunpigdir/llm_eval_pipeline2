**Derivation of the precession rate**

For a symmetric top pivoted at a point, the gravitational torque about the pivot is  

\[
\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}_g = (l\,\hat{\mathbf{e}}_z) \times (m\mathbf{g}) = m g l \,\hat{\boldsymbol{\Omega}},
\]

where \(\hat{\boldsymbol{\Omega}}\) is a unit vector perpendicular to the symmetry axis (the direction of the precession).  

The angular momentum of the spinning top is  

\[
\mathbf{L} = I_3 \boldsymbol{\omega}_3,
\]

with \(\boldsymbol{\omega}_3\) along the symmetry axis.  

In the fast‑top (gyroscopic) limit, the tilt angle \(\theta\) is small, and the component of \(\mathbf{L}\) that changes due to precession is  

\[
\frac{d\mathbf{L}}{dt} = \boldsymbol{\Omega} \times \mathbf{L}.
\]

Setting the torque equal to the rate of change of angular momentum:

\[
\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt} \quad\Longrightarrow\quad
m g l \,\hat{\boldsymbol{\Omega}} = \boldsymbol{\Omega} \times (I_3 \boldsymbol{\omega}_3 \hat{\mathbf{e}}_z).
\]

Since \(\boldsymbol{\Omega}\) is perpendicular to \(\hat{\mathbf{e}}_z\), the magnitude of the cross product is  

\[
|\boldsymbol{\Omega} \times (I_3 \boldsymbol{\omega}_3 \hat{\mathbf{e}}_z)| = I_3 \omega_3 \Omega .
\]

Thus  

\[
m g l = I_3 \omega_3 \Omega \quad\Longrightarrow\quad
\Omega = \frac{m g l}{I_3 \omega_3}.
\]

This shows the precession rate \(\Omega\) is **inversely proportional** to the spin rate \(\omega_3\).

---

**Numerical evaluation**

Given:  

- \(m = 0.500\;\text{kg}\)  
- \(l = 0.500\;\text{m}\)  
- \(g = 9.81\;\text{m/s}^2\)  
- \(I_3 = 2.00 \times 10^{-4}\;\text{kg·m}^2\)  
- \(\omega_3 = 300\;\text{rad/s}\)

Compute the numerator:

\[
m g l = 0.500 \times 9.81 \times 0.500 = 0.500 \times 4.905 = 2.4525\;\text{N·m}.
\]

Compute the denominator:

\[
I_3 \omega_3 = (2.00 \times 10^{-4}) \times 300 = 0.060\;\text{kg·m}^2\!\cdot\!\text{rad/s}.
\]

Thus  

\[
\Omega = \frac{2.4525}{0.060} = 40.875\;\text{rad/s}.
\]

The precession period \(T\) is the time for one full \(2\pi\) rad of precession:

\[
T = \frac{2\pi}{\Omega} = \frac{2\pi}{40.875} \approx \frac{6.2832}{40.875} \approx 0.1537\;\text{s}.
\]

---

**Effect of doubling the spin**

If the spin rate doubles: \(\omega_3' = 2\omega_3 = 600\;\text{rad/s}\).

Using the derived relation \(\Omega \propto 1/\omega_3\),

\[
\Omega' = \frac{m g l}{I_3 \omega_3'} = \frac{m g l}{I_3 (2\omega_3)} = \frac{1}{2}\,\Omega.
\]

Hence the new precession rate is half the original:

\[
\Omega' = \frac{40.875}{2} = 20.4375\;\text{rad/s}.
\]

---

**Physical explanation**

The top precesses rather than falling because the rapid spin creates a large angular momentum \(\mathbf{L}\) along the symmetry axis. Gravity exerts a torque \(\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}_g\) that would tilt the angular momentum vector. However, the gyroscopic effect forces the angular momentum to change direction (precession) instead of magnitude, keeping the top upright.  

A small **nutation** (oscillation of the tilt angle) can superimpose on the steady precession due to slight imbalances in the torque and angular momentum, but in the fast‑top limit this nutation is negligible compared to the dominant precessional motion.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 40.875 \\
\mathrm{precession\_period\_s} &= 0.154 \\
\mathrm{precession\_double\_spin} &= 20.438
\end{aligned}
\]