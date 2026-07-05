### 1. Derivation of the Precession Rate $\Omega$

We consider a symmetric top spinning rapidly about its symmetry axis.
*   **Angular Momentum:** In the fast-top approximation, the total angular momentum $\mathbf{L}$ is dominated by the spin angular momentum along the symmetry axis: $\mathbf{L} \approx I_3 \omega_3 \mathbf{\hat{s}}$, where $\mathbf{\hat{s}}$ is the unit vector along the axis.
*   **Torque:** The gravitational force acts at the center of mass. The torque $\boldsymbol{\tau}$ about the pivot is:
    $$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}_g = (l \mathbf{\hat{s}}) \times (-mg \mathbf{\hat{k}})$$
    Since the axis is nearly horizontal, the magnitude of the torque is $\tau = mgl \sin\theta \approx mgl$ (for $\theta \approx 90^\circ$). The direction of the torque is perpendicular to both the symmetry axis and the vertical axis.
*   **Equation of Motion:** The fundamental relation is $\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}$.
    For steady precession, the vector $\mathbf{L}$ rotates around the vertical axis $\mathbf{\hat{k}}$ with an angular velocity $\boldsymbol{\Omega} = \Omega \mathbf{\hat{k}}$. The rate of change of $\mathbf{L}$ is:
    $$\frac{d\mathbf{L}}{dt} = \boldsymbol{\Omega} \times \mathbf{L}$$
*   **Magnitude Equivalence:**
    $$\tau = |\boldsymbol{\Omega} \times \mathbf{L}| = \Omega L \sin\theta$$
    Substituting $\tau = mgl \sin\theta$ and $L = I_3 \omega_3$:
    $$mgl \sin\theta = \Omega (I_3 \omega_3) \sin\theta$$
    Dividing by $\sin\theta$ (assuming $\theta \neq 0$):
    $$\Omega = \frac{mgl}{I_3 \omega_3}$$

### 2. Evaluation of $\Omega$ and Period $T$

**Given values:**
$m = 0.500$ kg, $l = 0.0500$ m, $I_3 = 2.00 \times 10^{-4}$ kg m$^2$, $\omega_3 = 300$ rad/s, $g = 9.81$ m/s$^2$.

**Calculation of $\Omega$:**
$$\Omega = \frac{(0.500)(9.81)(0.0500)}{(2.00 \times 10^{-4})(300)} = \frac{0.24525}{0.06} = 4.0875 \text{ rad/s}$$

**Calculation of Period $T$:**
$$T = \frac{2\pi}{\Omega} = \frac{2\pi}{4.0875} \approx 1.537 \text{ s}$$

### 3. Effect of Doubling the Spin $\omega_3$

The formula $\Omega = \frac{mgl}{I_3 \omega_3}$ shows that $\Omega \propto \frac{1}{\omega_3}$.
If $\omega_3 \to 2\omega_3$, then $\Omega \to \frac{1}{2}\Omega$.
$$\Omega_{\text{new}} = \frac{4.0875}{2} = 2.04375 \text{ rad/s}$$

### 4. Physical Explanation

**Why it precesses:** The torque exerted by gravity does not cause the top to fall because the angular momentum $\mathbf{L}$ is large. The torque $\boldsymbol{\tau}$ is always perpendicular to $\mathbf{L}$, meaning it changes the *direction* of $\mathbf{L}$ rather than its magnitude. This forces the axis to move in a circle around the vertical axis.

**Nutation:** Nutation is a small, high-frequency oscillation of the tilt angle $\theta$ superimposed on the steady precession. It occurs because the initial conditions (initial $\dot{\theta}$ and $\Omega$) rarely match the exact requirements for "steady" precession, causing the axis to "nod" up and down as it precesses.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 4.0875 \\
\mathrm{precession\_period\_s} &= 1.537 \\
\mathrm{precession\_double\_spin} &= 2.04375
\end{aligned}
\]