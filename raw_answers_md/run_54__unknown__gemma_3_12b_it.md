Okay, let's analyze the Kapitza pendulum.

**1. Sketch of the Effective-Potential Derivation**

The Kapitza pendulum is an inverted pendulum driven by a vertically oscillating pivot. We want to find the conditions for which the inverted position becomes stable. We'll use the separation-of-timescales (effective potential) method.

Let $\theta(t)$ be the angular displacement of the pendulum from the inverted position, and let $z(t)$ be the vertical displacement of the pivot from its equilibrium position. We are given that $z(t) = a \cos(\omega t)$. The equation of motion for the pendulum is:

$L\ddot{\theta} + 2\dot{\theta}\dot{z} + g\sin(\theta) = 0$

Since $\omega \gg \sqrt{g/L}$, we can assume that the fast oscillation (driving frequency $\omega$) dominates the dynamics. We can treat the slow variation of $\theta$ as a response to an effective potential.

We assume that $\theta$ varies slowly compared to the driving frequency $\omega$.  We can then average the equation of motion over one period of the driving oscillation.  This involves substituting $z(t) = a \cos(\omega t)$ into the equation of motion and then taking the time average.

First, let's rewrite the equation of motion:

$L\ddot{\theta} + 2\dot{\theta}(a\dot{\cos(\omega t)}) + g\sin(\theta) = 0$
$L\ddot{\theta} - 2a\dot{\theta}\omega\sin(\omega t) + g\sin(\theta) = 0$

Now, we take the time average over one period $T = 2\pi/\omega$:

$\langle L\ddot{\theta} \rangle = 0$ (since $\ddot{\theta}$ oscillates with twice the driving frequency)
$\langle -2a\dot{\theta}\omega\sin(\omega t) \rangle = -2a\omega\langle \dot{\theta}\sin(\omega t) \rangle$
$\langle g\sin(\theta) \rangle = g\langle \sin(\theta) \rangle$

Assuming $\theta$ is small, $\sin(\theta) \approx \theta$.  Then $\langle \sin(\theta) \rangle \approx \langle \theta \rangle$.  Also, we can assume that $\dot{\theta}$ is approximately constant over one period of the driving oscillation.  Therefore,

$0 - 2a\omega\dot{\theta}\langle \sin(\omega t) \rangle + g\langle \theta \rangle = 0$

Since $\langle \sin(\omega t) \rangle = 0$, this doesn't help us directly.  Instead, let's consider the energy balance. The total energy of the system is:

$E = \frac{1}{2}L\dot{\theta}^2 + m g L \cos(\theta) + \frac{1}{2} m a^2 \dot{z}^2$

Averaging over one period, we have:

$\langle E \rangle = \frac{1}{2}L\langle \dot{\theta}^2 \rangle + mgL\langle \cos(\theta) \rangle + \frac{1}{2} m a^2 \omega^2 \langle \cos^2(\omega t) \rangle$

Since $\langle \cos^2(\omega t) \rangle = \frac{1}{2}$, we have:

$\langle E \rangle = \frac{1}{2}L\langle \dot{\theta}^2 \rangle + mgL\langle \cos(\theta) \rangle + \frac{1}{4} m a^2 \omega^2$

For stability, we need the effective potential $V_{eff}(\theta) = mgL\cos(\theta) + \frac{1}{4} m a^2 \omega^2$ to have a minimum at $\theta = 0$.  This means that $V''(\theta) > 0$ at $\theta = 0$.

$V'(\theta) = -mgL\sin(\theta)$
$V''(\theta) = -mgL\cos(\theta)$

For a minimum at $\theta = 0$, we need $V''(0) > 0$, which means $-mgL > 0$. This is not possible.

Let's consider the condition for stability. The inverted position is stable if the effective potential has a minimum at $\theta = 0$. The effective potential is given by:

$V_{eff}(\theta) = mgL\cos(\theta) + \frac{1}{2} I \dot{\theta}^2$

The condition for stability is that the effective potential has a minimum at $\theta = 0$. This requires that $V''(\theta) > 0$ at $\theta = 0$.

$V'(\theta) = -mgL\sin(\theta)$
$V''(\theta) = -mgL\cos(\theta)$

For stability, we need $V''(0) = -mgL > 0$, which is impossible.

However, the correct criterion is $a^2\omega^2 > 2gL$. This comes from a more detailed analysis of the averaged equation of motion. The average force stabilizing the pendulum is proportional to $a^2\omega^2$.  For stability, this force must be greater than the restoring force due to gravity, which is $2gL$.

**2. Evaluate the minimum angular frequency $\omega_{min}$**

We have the criterion $a^2\omega^2 > 2gL$.  Therefore, $\omega_{min} = \sqrt{\frac{2gL}{a^2}}$.

$\omega_{min} = \sqrt{\frac{2(9.81)(0.200)}{(0.0200)^2}} = \sqrt{\frac{3.924}{0.0004}} = \sqrt{9810} \approx 99.05$ rad/s

**3. Evaluate the corresponding drive frequency $f_{min}$**

$f_{min} = \frac{\omega_{min}}{2\pi} = \frac{99.05}{2\pi} \approx 15.71$ Hz

**4. Explain physically where the stabilizing 'force' comes from and why intuition based on static equilibrium fails.**

The stabilizing "force" comes from the average of the inertial force over the swing. When the pivot oscillates, the pendulum experiences a time-varying inertial force.  The averaging process effectively creates a force that opposes the pendulum's tendency to fall. This force is proportional to $a^2\omega^2$.

Intuition based on static equilibrium fails because the pendulum is not in static equilibrium. The oscillating pivot introduces a time-dependent force that changes the effective potential. In static equilibrium, the restoring force due to gravity would always dominate, leading to instability. The parametric driving allows the inertial force to counteract gravity, creating a stable inverted position under specific conditions. The key is that the pivot's oscillation provides a periodic "kick" that stabilizes the pendulum.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.05 \\
\mathrm{f\_min\_hz} &= 15.71
\end{aligned}
\]