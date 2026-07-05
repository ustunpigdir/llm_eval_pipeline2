**Derivation of the steady precession rate**

For a symmetric top with a fixed point at the tip of the symmetry axis, the gravitational torque about the pivot is  

\[
\boldsymbol{\tau}= \mathbf{r}\times m\mathbf{g}=mgl\,\hat{\mathbf{e}}_{\perp},
\]

where \( \mathbf{r}=l\hat{\mathbf{e}}_{3}\) points along the symmetry axis and \( \hat{\mathbf{e}}_{\perp}\) is perpendicular to it.  
In the fast‑top limit the spin angular momentum is essentially aligned with the symmetry axis:

\[
\mathbf{L}\simeq I_{3}\,\omega_{3}\,\hat{\mathbf{e}}_{3}.
\]

Steady precession means that the direction of \(\mathbf{L}\) changes at a constant rate \(\Omega\) about the vertical (or the direction of the torque). The time derivative of \(\mathbf{L}\) has magnitude  

\[
\left|\frac{d\mathbf{L}}{dt}\right| = \Omega L \sin\theta \approx \Omega L,
\]

because the precession axis is perpendicular to \(\mathbf{L}\) (the tilt angle \(\theta\) is constant).  
Equating the magnitude of torque to the rate of change of angular momentum gives  

\[
mgl = \Omega (I_{3}\omega_{3})\;\;\Longrightarrow\;\;
\boxed{\Omega = \frac{mgl}{I_{3}\omega_{3}} }.
\]

This expression is independent of the tilt angle, as required for the fast‑top approximation.

---

**Numerical evaluation**

Given  

\[
m = 0.500\ \text{kg},\quad 
g = 9.81\ \text{m/s}^{2},\quad 
l = 0.0500\ \text{m},\quad 
I_{3}=2.00\times10^{-4}\ \text{kg·m}^{2},\quad 
\omega_{3}=300\ \text{rad/s},
\]

the numerator is  

\[
mgl = (0.500)(9.81)(0.0500)=0.24525\ \text{kg·m}^{2}\!\!/\!\text{s}^{2}.
\]

The denominator is  

\[
I_{3}\omega_{3}= (2.00\times10^{-4})(300)=0.0600\ \text{kg·m}^{2}\!\!/\!\text{s}.
\]

Hence  

\[
\Omega = \frac{0.24525}{0.0600}=4.0875\ \text{rad/s}\;\approx\;4.09\ \text{rad/s}.
\]

The corresponding precession period is  

\[
T_{\text{prec}}=\frac{2\pi}{\Omega}= \frac{6.2832}{4.0875}=1.537\ \text{s}\;\approx\;1.54\ \text{s}.
\]

---

**Effect of doubling the spin**

If \(\omega_{3}\) is doubled to \(600\ \text{rad/s}\),

\[
\Omega' = \frac{mgl}{I_{3}(2\omega_{3})}= \frac{\Omega}{2}= \frac{4.0875}{2}=2.04375\ \text{rad/s}\;\approx\;2.04\ \text{rad/s}.
\]

Thus the precession rate scales **inversely** with the spin: \(\Omega\propto 1/\omega_{3}\). Doubling the spin halves the precession rate.

---

**Why the top precesses instead of falling, and the role of nutation**

The gravitational torque does not change the magnitude of \(\mathbf{L}\); it only changes its direction. Because the top is spinning rapidly, the angular momentum vector is large and points along the symmetry axis. The torque causes this vector to **rotate** about the vertical axis, producing a steady precession. The top does not simply fall because the gyroscopic effect continuously redirects the angular momentum, maintaining the axis at a fixed tilt while it precesses.

If the actual motion deviates slightly from the ideal steady precession—e.g., due to a small perturbation in the tilt angle—a component of angular momentum appears perpendicular to the steady precession direction. This produces a small oscillatory motion called **nutation**, which superposes on the uniform precessional motion. In the fast‑top limit the nutation frequency is much higher than the precession rate and its amplitude remains small.

---

\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 4.09 \\
\mathrm{precession\_period\_s} &= 1.54 \\
\mathrm{precession\_double\_spin} &= 2.04
\end{aligned}
\]