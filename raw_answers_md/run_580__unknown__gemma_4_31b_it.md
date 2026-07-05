### 1. Derivation of Rindler Motion Expressions

For a rocket with constant proper acceleration $a$, the four-acceleration $A^\mu$ satisfies $A^\mu A_\mu = -a^2$. In the lab frame $(t, x)$, the velocity is $v = dx/dt$ and the Lorentz factor is $\gamma = (1 - v^2/c^2)^{-1/2}$. The proper acceleration is defined as the acceleration in the rocket's instantaneous rest frame:
$$a = \gamma^3 \frac{dv}{dt}$$
Integrating with respect to lab time $t$ (starting from $v=0$ at $t=0$):
$$\int_0^v \gamma^3 dv' = \int_0^t a dt' \implies \frac{v}{\sqrt{1-v^2/c^2}} = at$$
Solving for $v(t)$:
$$v(t) = \frac{at}{\sqrt{1 + (at/c)^2}}$$
To find the relationship with proper time $\tau$, we use $d\tau = dt/\gamma$:
$$d\tau = \sqrt{1 - v^2/c^2} dt = \frac{1}{\sqrt{1 + (at/c)^2}} dt$$
Integrating:
$$\tau = \int_0^t \frac{dt'}{\sqrt{1 + (at'/c)^2}} = \frac{c}{a} \sinh^{-1}\left(\frac{at}{c}\right)$$
Rearranging for **lab time $t(\tau)$**:
$$t(\tau) = \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right)$$
Integrating $v(t)$ to find **lab distance $x(\tau)$** (starting at $x=0$):
$$x(t) = \int_0^t \frac{at'}{\sqrt{1 + (at'/c)^2}} dt' = \frac{c^2}{a} \left( \sqrt{1 + (at/c)^2} - 1 \right)$$
Substituting $at/c = \sinh(a\tau/c)$:
$$x(\tau) = \frac{c^2}{a} \left( \cosh\left(\frac{a\tau}{c}\right) - 1 \right)$$
The **velocity $\beta(\tau)$** is $v/c$:
$$\beta(\tau) = \frac{at/c}{\sqrt{1 + (at/c)^2}} = \frac{\sinh(a\tau/c)}{\cosh(a\tau/c)} = \tanh\left(\frac{a\tau}{c}\right)$$

### 2. Numerical Evaluation for $\tau = 1.00$ year

**Constants:**
$a = 9.8 \text{ m/s}^2$
$1 \text{ yr} = 3.15576 \times 10^7 \text{ s}$
$c = 299,792,458 \text{ m/s}$

First, calculate the dimensionless parameter $\phi = \frac{a\tau}{c}$:
$$\phi = \frac{(9.8 \text{ m/s}^2)(3.15576 \times 10^7 \text{ s})}{299,792,458 \text{ m/s}} \approx \frac{309,264,480}{299,792,458} \approx 1.031595$$

**Lab Time $t$:**
$$t = \frac{c}{a} \sinh(\phi) = \frac{1 \text{ ly}}{1.031595} \sinh(1.031595)$$
Using $\sinh(1.031595) \approx 1.22355$:
$$t \approx \frac{1.22355}{1.031595} \text{ yr} \approx 1.1861 \text{ yr}$$

**Distance $x$:**
$$x = \frac{c^2}{a} (\cosh(\phi) - 1) = \frac{1 \text{ ly}}{1.031595} (\cosh(1.031595) - 1)$$
Using $\cosh(1.031595) \approx 1.58155$:
$$x \approx \frac{1.58155 - 1}{1.031595} \text{ ly} \approx \frac{0.58155}{1.031595} \text{ ly} \approx 0.5637 \text{ ly}$$

**Final Speed $\beta$:**
$$\beta = \tanh(\phi) = \tanh(1.031595) \approx 0.7746$$

### 3. Analysis of the Student's Error

The student used the Newtonian formula $v = a\tau$. For $\tau = 1$ year:
$$v = (9.8)(3.15576 \times 10^7) \approx 3.09 \times 10^8 \text{ m/s}$$
Since $c \approx 2.99 \times 10^8 \text{ m/s}$, the student finds $\beta \approx 1.03$, which is $> 1$.
**Error:** The student ignored the relativistic effect where the inertia of the object increases as its velocity approaches $c$. In relativity, constant proper acceleration does not lead to a linear increase in lab velocity. Instead, the velocity follows a hyperbolic tangent function $\beta = \tanh(a\tau/c)$. Because $\tanh(z) < 1$ for all finite $z$, the speed of light is an asymptotic limit that can never be reached or exceeded.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 1.1861 \\
\mathrm{distance\_ly} &= 0.5637 \\
\mathrm{final\_beta} &= 0.7746
\end{aligned}
\]