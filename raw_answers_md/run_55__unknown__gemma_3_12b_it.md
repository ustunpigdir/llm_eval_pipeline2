Okay, let's analyze the Kapitza pendulum.

**1. Sketch of the Effective-Potential Derivation**

The Kapitza pendulum is an inverted pendulum driven by a vertically oscillating pivot. We want to find the conditions for which the inverted position becomes stable. We'll use the separation-of-timescales (effective potential) method.

Let $\theta(t)$ be the angular displacement of the pendulum from the inverted position, and let $\phi(t) = a \cos(\omega t)$ be the vertical displacement of the pivot, where $a$ is the amplitude and $\omega$ is the driving frequency. The equation of motion is:

$L\ddot{\theta} + 2\dot{\phi}\dot{\theta} + g\sin(\theta) = 0$

Since $\omega \gg \sqrt{g/L}$, we can use the separation-of-timescales approach. We assume that $\theta$ varies slowly compared to $\phi$. We can expand $\sin(\theta)$ as $\theta - \frac{\theta^3}{6} + ...$ around $\theta = 0$.  We'll keep the $\theta$ and $\theta^3$ terms for now.

$L\ddot{\theta} + 2\dot{\phi}\dot{\theta} + g\theta - \frac{g\theta^3}{6} = 0$

Now, we average over the fast oscillation of $\phi$.  We have $\dot{\phi} = -a\omega \sin(\omega t)$.  The average of $\dot{\phi}\dot{\theta}$ over a period is zero, since it is an odd function of $\omega t$.  Therefore, averaging the equation of motion over a period gives:

$L\langle \ddot{\theta} \rangle + g\langle \theta \rangle - \frac{g}{6}\langle \theta^3 \rangle = 0$

Since $\theta$ varies slowly, we can approximate $\langle \ddot{\theta} \rangle \approx 0$.  This gives us the effective potential equation:

$g\theta - \frac{g\theta^3}{6} = 0$

However, this is not quite correct. We need to consider the effect of the fast oscillation on the pendulum's motion. The term $2\dot{\phi}\dot{\theta}$ is crucial.  Averaging this term over a period gives a force.  We can write the equation of motion as:

$L\ddot{\theta} = -2\dot{\phi}\dot{\theta} - g\sin(\theta)$

Averaging over the fast oscillation, we get:

$L\langle \ddot{\theta} \rangle = - \langle 2\dot{\phi}\dot{\theta} \rangle - g\langle \sin(\theta) \rangle$

Since $\langle \ddot{\theta} \rangle = 0$, we have:

$0 = - \langle 2\dot{\phi}\dot{\theta} \rangle - g\langle \sin(\theta) \rangle$

The term $\langle \sin(\theta) \rangle$ is approximately $\langle \theta \rangle$ for small $\theta$.  So,

$0 = - \langle 2\dot{\phi}\dot{\theta} \rangle - g\langle \theta \rangle$

Now, we need to evaluate $\langle 2\dot{\phi}\dot{\theta} \rangle$.  We have $\dot{\phi} = -a\omega \sin(\omega t)$.  We need to find an expression for $\dot{\theta}$.  From the original equation of motion, we have:

$L\ddot{\theta} = -2\dot{\phi}\dot{\theta} - g\sin(\theta)$

We can write $\ddot{\theta} = -\frac{2\dot{\phi}\dot{\theta} + g\sin(\theta)}{L}$.  Substituting this into the averaged equation:

$0 = - \langle 2\dot{\phi}\dot{\theta} \rangle - g\langle \theta \rangle$

The stability criterion is obtained when the effective potential has a minimum at $\theta = 0$. This requires a positive second derivative of the effective potential. The effective potential is $U(\theta) = g\theta + \frac{g}{6}\theta^3$. The second derivative is $U''(\theta) = g + \frac{g}{2}\theta^2$. For stability, we need $U''(\theta) > 0$, which is always true for $\theta = 0$.

The condition for stability is $a^2\omega^2 > 2gL$.

**2. Evaluate the minimum angular frequency $\omega_{min}$**

We are given $a = 0.0200$ m, $L = 0.200$ m, and $g = 9.81$ m/s$^2$.  We want to find $\omega_{min}$ such that $a^2\omega^2 = 2gL$.

$\omega_{min}^2 = \frac{2gL}{a^2} = \frac{2(9.81)(0.200)}{(0.0200)^2} = \frac{3.924}{0.0004} = 9810$

$\omega_{min} = \sqrt{9810} \approx 99.045$ rad/s

**3. Evaluate the corresponding drive frequency $f_{min}$**

$f_{min} = \frac{\omega_{min}}{2\pi} = \frac{99.045}{2\pi} \approx 15.76$ Hz

**4. Explain physically where the stabilizing 'force' comes from and why intuition based on static equilibrium fails.**

The stabilizing "force" comes from the average of the inertial force due to the fast oscillation of the pivot.  When the pivot moves down, the pendulum gains kinetic energy. When the pivot moves up, the pendulum loses kinetic energy. The *average* of these energy transfers over a cycle results in a net force that opposes the pendulum's tendency to fall. This is a parametric effect – the stability is achieved by modulating the system's energy rather than directly applying a force to counteract gravity.

Intuition based on static equilibrium fails because the pendulum is not in static equilibrium. The pivot's oscillation introduces a time-dependent force that changes the effective potential. In static equilibrium, the pendulum would simply fall. The oscillating pivot creates a situation where the average force over time is sufficient to keep the pendulum upright. The fast oscillation is crucial; if the oscillation were too slow, the pendulum would simply follow the pivot's motion and fall.

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.045 \\
\mathrm{f\_min\_hz} &= 15.76
\end{aligned}
\]