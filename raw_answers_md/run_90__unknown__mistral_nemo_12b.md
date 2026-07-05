**1. Derivation of the precession rate:**

The torque acting on the top is given by the weight of the top times the moment arm, which is $mg \times l$. The rate of change of angular momentum is given by the torque, so we have:

\[
\tau = \frac{dL}{dt} = mg \times l
\]

The angular momentum of the top is the sum of the spin angular momentum and the precession angular momentum:

\[
L = I_3 \omega_3 + I_1 \Omega
\]

where $I_1$ is the moment of inertia about the axis perpendicular to the spin axis, and $\Omega$ is the precession rate. In the fast-top approximation, $I_1 \approx I_3$, so we can write:

\[
L \approx I_3 \omega_3 + I_3 \Omega
\]

Differentiating this with respect to time and equating it to the torque, we get:

\[
I_3 \frac{d\omega_3}{dt} + I_3 \frac{d\Omega}{dt} = mg \times l
\]

Since the spin rate is constant, $\frac{d\omega_3}{dt} = 0$, and we can solve for the precession rate:

\[
I_3 \frac{d\Omega}{dt} = mg \times l \implies \Omega = \frac{mg \times l}{I_3 \omega_3}
\]

**2. Evaluation of the precession rate and period:**

Plugging in the given values:

\[
\Omega = \frac{(0.500 \text{ kg})(9.81 \text{ m/s}^2)(0.0500 \text{ m})}{(2.00 \times 10^{-4} \text{ kg m}^2)(300 \text{ rad/s})} = 0.0327 \text{ rad/s}
\]

The precession period is the reciprocal of the precession rate:

\[
T = \frac{2\pi}{\Omega} = \frac{2\pi}{0.0327 \text{ rad/s}} \approx 192.3 \text{ s}
\]

**3. Effect of doubling the spin rate:**

If the spin rate doubles, $\omega_3$ becomes $600$ rad/s. The new precession rate is:

\[
\Omega_{\text{new}} = \frac{mg \times l}{I_3 \omega_3} = \frac{mg \times l}{I_3 (2\omega_3)} = \frac{1}{2} \Omega
\]

So, the precession rate halves when the spin rate doubles.

**4. Explanation of precession and nutation:**

The top precesses instead of falling because the spin angular momentum is much larger than the precession angular momentum. The weight of the top causes a torque that tries to align the spin axis with the vertical, but the large spin angular momentum resists this, causing the top to precess around the vertical axis.

The small nutation superimposed on steady precession is due to the fact that the top is not a perfect top, and there are small deviations from the ideal behavior. These deviations cause the spin axis to nutate (wobble) around the mean precession cone.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 0.0327 \text{ rad/s} \\
\mathrm{precession\_period\_s} &= 192.3 \text{ s} \\
\mathrm{precession\_double\_spin} &= 0.01635 \text{ rad/s}
\end{aligned}
\]