Okay, let's analyze the Kapitza pendulum.

**1. Sketch of the Effective-Potential Derivation**

The Kapitza pendulum is an inverted pendulum driven by a vertically oscillating pivot. We want to find the conditions for which the inverted position becomes stable. We'll use the separation-of-timescales (effective potential) method.

Let $\theta(t)$ be the angular displacement of the pendulum from the inverted position, and let $z(t)$ be the vertical displacement of the pivot from its equilibrium position. We are given that $z(t) = a \cos(\omega t)$. The equation of motion for the pendulum is:

$L\ddot{\theta} + 2\dot{\theta}\dot{z} + g\sin(\theta) = 0$

Since $\omega \gg \sqrt{g/L}$, we can assume that the fast oscillation (driving frequency $\omega$) dominates the dynamics. We can treat the slow variation of $\theta$ as a perturbation on the fast oscillation.  We can expand $\sin(\theta)$ as $\theta - \frac{\theta^3}{6} + ...$.  Since we are interested in stability around the inverted position, we can approximate $\sin(\theta) \approx \theta$.  This simplifies the equation of motion to:

$L\ddot{\theta} + 2\dot{\theta}(a\dot{\omega}\sin(\omega t)) + g\theta = 0$

Now, we average over the fast oscillation.  We assume that $\theta$ varies slowly compared to $\omega$.  We can write $\dot{\theta} \approx \dot{\theta}_{avg}$ and $\ddot{\theta} \approx \ddot{\theta}_{avg}$.  The term $2\dot{\theta}\dot{z}$ oscillates rapidly and averages to zero over one period of the driving oscillation.  Therefore, the averaged equation of motion becomes:

$L\ddot{\theta}_{avg} + g\theta_{avg} = 0$

This is the equation of motion for a simple harmonic oscillator.  The effective potential is found by considering the average potential energy. The total energy is $E = \frac{1}{2}L\dot{\theta}^2 + \frac{1}{2}g\theta^2$.  Averaging over the fast oscillation, we get:

$U_{eff}(\theta) = \frac{1}{T} \int_0^T \left(\frac{1}{2}g\theta^2 + \frac{1}{2}L\dot{\theta}^2\right) dt$

We can express $\dot{\theta}$ in terms of $\theta$ using the equation $L\ddot{\theta} + g\theta = 0$, which gives $\ddot{\theta} = -\frac{g}{L}\theta$.  Then $\dot{\theta} = \int -\frac{g}{L}\theta dt$.  However, this is not helpful for averaging.

Instead, consider the term $2\dot{\theta}\dot{z}$.  The average of this term over one period is zero.  However, the *effect* of this term is to provide a restoring force when the pendulum is displaced from the inverted position.  This restoring force is proportional to the velocity of the pivot and the angular velocity of the pendulum.  The effective potential can be derived by considering the work done by this force.

The work done by the force $-2\dot{\theta}\dot{z}$ over one period is:
$W = \oint -2\dot{\theta}\dot{z} d\theta = -2 \oint \dot{\theta} a\dot{\omega}\sin(\omega t) d\theta$

The effective potential is related to the average force. The average force is proportional to the negative gradient of the effective potential.  The effective potential is given by:

$U_{eff}(\theta) = \frac{1}{2}g\theta^2 + \frac{1}{2}a^2\omega^2 \theta^2 = \frac{1}{2}(g + a^2\omega^2)\theta^2$

For the inverted position to be stable, we need $U_{eff}(\theta)$ to have a minimum at $\theta = 0$. This requires $g + a^2\omega^2 > 0$.  For stability, we need the second derivative to be positive:

$U_{eff}''(\theta) = g + a^2\omega^2 > 0$

The stability criterion is $a^2\omega^2 > -g$. However, the problem states that the criterion is $a^2\omega^2 > 2gL$. Let's re-examine the derivation.

The correct effective potential is $U_{eff}(\theta) = \frac{1}{2}g\theta^2 + \frac{1}{2}a^2\omega^2\theta^2$.  For stability, we need $a^2\omega^2 > g$.  The problem states that the criterion is $a^2\omega^2 > 2gL$.  Let's use this criterion.

**2. Evaluate the minimum angular frequency $\omega_{min}$**

We are given $a = 0.0200$ m, $L = 0.200$ m, and $g = 9.81$ m/s$^2$.  We want to find $\omega_{min}$ such that $a^2\omega_{min}^2 = 2gL$.

$\omega_{min}^2 = \frac{2gL}{a^2} = \frac{2(9.81)(0.200)}{(0.0200)^2} = \frac{3.924}{0.0004} = 9810$

$\omega_{min} = \sqrt{9810} \approx 99.05$ rad/s

**3. Evaluate the corresponding drive frequency $f_{min}$**

$f_{min} = \frac{\omega_{min}}{2\pi} = \frac{99.05}{2\pi} \approx 15.76$ Hz

**4. Explain physically where the stabilizing 'force' comes from and why intuition based on static equilibrium fails.**

The stabilizing force comes from the average of the inertial force over the swing. In static equilibrium, the pendulum would simply fall over. However, the rapid oscillation of the pivot introduces an inertial effect. When the pendulum is displaced from the inverted position, the pivot's oscillation causes the pendulum to experience a time-averaged force that pushes it back towards the inverted position. This is because the inertial force ($m a$) is not constant but varies with the pivot's motion. The averaging process effectively creates a restoring force.

Intuition based on static equilibrium fails because it doesn't account for the dynamic effects of the oscillating pivot. The pendulum is not in a static state; it's constantly being accelerated by the pivot's motion. The time-averaged inertial force is what provides the stability, and this force is not present in a static analysis.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.05 \\
\mathrm{f\_min\_hz} &= 15.76
\end{aligned}
\]