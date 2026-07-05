**1. Effective Potential Derivation:**

The Lagrangian of the system is given by:

$$L = \frac{1}{2}mL^2\dot{\theta}^2 - mgl\cos\theta - ma\cos(\omega t)\theta$$

where $m$ is the mass of the pendulum, $g$ is the acceleration due to gravity, and $\omega$ is the angular frequency of the pivot.

Using the separation-of-timescales method, we split the motion into slow ($\theta$) and fast ($\omega t$) variables. We average over the fast oscillation to obtain the effective potential:

$$\overline{L} = \frac{1}{2\pi}\int_0^{2\pi}L\,d(\omega t) = \frac{1}{2}mL^2\dot{\theta}^2 - mgl\cos\theta - \frac{1}{2}ma^2\theta^2$$

The effective potential is then:

$$U_{eff}(\theta) = \frac{1}{2}mL^2\dot{\theta}^2 + mgl\cos\theta + \frac{1}{2}ma^2\theta^2$$

The inverted position is stable when the second derivative of the effective potential is positive:

$$\frac{d^2U_{eff}}{d\theta^2} = mL^2\ddot{\theta} + mL^2\dot{\theta}^2 + ma^2\theta > 0$$

At the inverted position, $\theta = 0$, so we have:

$$mL^2\ddot{\theta} + ma^2 > 0$$

Since $\ddot{\theta} = -\omega^2\theta$ (from the equation of motion), we get:

$$mL^2(-\omega^2\theta) + ma^2 > 0$$

Dividing by $mL^2$ and rearranging, we obtain the stability criterion:

$$\omega^2 > \frac{2g}{L}$$

**2. Minimum Angular Frequency:**

From the stability criterion, we have:

$$\omega_{min}^2 = \frac{2g}{L}$$

Substituting the given values:

$$\omega_{min}^2 = \frac{2 \times 9.81}{0.200} = 98.1$$

$$\omega_{min} = \sqrt{98.1} \approx 9.90 \text{ rad/s}$$

**3. Minimum Drive Frequency:**

The minimum drive frequency is:

$$f_{min} = \frac{\omega_{min}}{2\pi} = \frac{9.90}{2\pi} \approx 1.57 \text{ Hz}$$

**4. Physical Explanation:**

The stabilizing 'force' comes from the average of the fast inertial force over the swing. When the pivot oscillates, it imparts a time-varying force on the pendulum. This force has a component that is proportional to the displacement of the pendulum from the inverted position. This component acts as a restoring force, stabilizing the inverted position. Static equilibrium fails because it does not account for the dynamic effects of the oscillating pivot.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 9.90 \\
\mathrm{f\_min\_hz} &= 1.57
\end{aligned}
\]