**Derivation of Precession Rate:**

1. The torque acting on the top due to gravity is given by $\tau = mgl \sin\theta$, where $\theta$ is the angle between the symmetry axis and the vertical.

2. The rate of change of angular momentum is given by $\frac{d\mathbf{L}}{dt} = \mathbf{\tau}$. Since the top is precessing with an angular velocity $\Omega$, the angular momentum can be written as $\mathbf{L} = I_3 \omega_3 \hat{k} + I_1 \Omega \hat{i}$, where $I_1$ is the moment of inertia about an axis perpendicular to the symmetry axis and $\hat{i}$ and $\hat{k}$ are unit vectors along the precession and spin axes, respectively.

3. In the fast-top approximation, the precession is independent of the tilt angle, so we can assume $\sin\theta \approx 1$. Also, since $I_3 \omega_3 \gg I_1 \Omega$, we can neglect the term $I_1 \Omega \hat{i}$. Thus, the torque is approximately $\tau \approx mgl$.

4. Substituting these into the equation $\frac{d\mathbf{L}}{dt} = \mathbf{\tau}$, we get $\frac{d}{dt}(I_3 \omega_3 \hat{k}) = mgl \hat{i}$. Since $\omega_3$ is constant, we have $I_3 \omega_3 \frac{d\Omega}{dt} = mgl$.

5. Solving for $\Omega$, we get $\Omega = \frac{mgl}{I_3 \omega_3}$.

**Calculations:**

1. Substituting the given values, we get $\Omega = \frac{0.500 \times 9.81 \times 0.0500}{2.00 \times 10^{-4} \times 300} = 0.8175$ rad/s.

2. The precession period is $T = \frac{2\pi}{\Omega} = \frac{2\pi}{0.8175} = 7.64$ s.

3. If the spin $\omega_3$ doubles, the new precession rate is $\Omega' = \frac{mgl}{I_3 \omega_3'} = \frac{mgl}{I_3 \frac{\omega_3}{2}} = 2\Omega = 1.635$ rad/s.

**Explanation:**

The top precesses instead of falling because the angular momentum of the spin is conserved. The torque due to gravity causes the top to precess, but the angular momentum of the spin remains constant. The small nutation superimposed on steady precession is due to the fact that the top is not a perfect symmetric top and there are small deviations from the ideal case.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 0.8175 \\
\mathrm{precession\_period\_s} &= 7.64 \\
\mathrm{precession\_double\_spin} &= 1.635
\end{aligned}
\]