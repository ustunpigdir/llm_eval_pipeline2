### 1. Derivation of the Effective Potential

**System Setup and Lagrangian**
Consider a pendulum of length $L$ with a bob of mass $m$. The pivot oscillates vertically with position $y_p(t) = a \cos(\omega t)$. Let $\theta$ be the angle of the pendulum measured from the downward vertical. The coordinates of the bob are:
$$ x = L \sin\theta $$
$$ y = a \cos(\omega t) - L \cos\theta $$

The kinetic energy $T$ is:
$$ T = \frac{1}{2} m (\dot{x}^2 + \dot{y}^2) $$
$$ \dot{x} = L \dot{\theta} \cos\theta $$
$$ \dot{y} = -a \omega \sin(\omega t) + L \dot{\theta} \sin\theta $$
$$ T = \frac{1}{2} m \left[ L^2 \dot{\theta}^2 + a^2 \omega^2 \sin^2(\omega t) + 2 a \omega L \dot{\theta} \sin\theta \sin(\omega t) \right] $$

The potential energy $V$ (gravitational) is:
$$ V = m g y = m g (a \cos(\omega t) - L \cos\theta) $$

The Lagrangian is $L_{ag} = T - V$.

**Equation of Motion**
Applying the Euler-Lagrange equation $\frac{d}{dt} \frac{\partial L_{ag}}{\partial \dot{\theta}} - \frac{\partial L_{ag}}{\partial \theta} = 0$, we obtain the equation of motion. Neglecting the term proportional to $\dot{\theta}$ (which averages to zero over the fast cycle and is smaller than the inertial term by a factor of $\omega/\sqrt{g/L}$), the dominant terms are:
$$ L \ddot{\theta} + g \sin\theta = - a \omega^2 \cos\theta \cos(\omega t) $$

**Separation of Timescales**
We assume the motion can be separated into a slow component $\phi(t)$ and a fast component $\xi(t)$:
$$ \theta(t) = \phi(t) + \xi(t) $$
where $\dot{\phi} \sim \sqrt{g/L}$ and $\dot{\xi} \sim \omega$. Given $\omega \gg \sqrt{g/L}$, $\xi$ is driven by the fast forcing term.
Substituting into the equation of motion and keeping only the fast terms for $\xi$ (treating $\phi$ as constant over one period):
$$ \ddot{\xi} \approx - \frac{a \omega^2}{L} \cos\phi \cos(\omega t) $$
Integrating twice with respect to time (ignoring secular terms):
$$ \xi(t) \approx \frac{a}{L} \cos\phi \cos(\omega t) $$

**Effective Lagrangian**
We now average the Lagrangian over the fast period $T = 2\pi/\omega$ to find the effective Lagrangian $\bar{L}(\phi, \dot{\phi})$.
$$ \bar{L} = \langle T \rangle - \langle V \rangle $$
The potential energy average is:
$$ \langle V \rangle = - m g L \cos\phi + m g a \langle \cos(\omega t) \rangle = - m g L \cos\phi $$
The kinetic energy average involves the fast oscillation $\xi$:
$$ \langle T \rangle = \frac{1}{2} m L^2 \dot{\phi}^2 + \frac{1}{2} m L^2 \langle \dot{\xi}^2 \rangle + \dots $$
$$ \dot{\xi} \approx - \frac{a \omega}{L} \cos\phi \sin(\omega t) $$
$$ \langle \dot{\xi}^2 \rangle = \frac{a^2 \omega^2}{L^2} \cos^2\phi \langle \sin^2(\omega t) \rangle = \frac{a^2 \omega^2}{2 L^2} \cos^2\phi $$
Thus,