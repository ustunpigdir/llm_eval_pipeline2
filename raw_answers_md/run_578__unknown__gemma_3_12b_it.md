Okay, let's tackle this special relativity problem with constant proper acceleration.

**1. Rindler Relations for Constant Proper Acceleration**

The Rindler relations connect proper time $\tau$ (on the rocket) to lab time $t$ and lab distance $x$. They are derived from the Lorentz transformations, taking into account the constant acceleration.

*   **Lab Time:**
    $t(\tau) = \frac{\tau}{a} \sinh\left(\frac{a\tau}{c}\right)$

*   **Lab Distance:**
    $x(\tau) = \frac{c^2}{a} \cosh\left(\frac{a\tau}{c}\right) - \frac{c\tau}{a}$

*   **Velocity (as a fraction of c):**
    $\beta(\tau) = \frac{v(\tau)}{c} = \frac{1}{\gamma(\tau)} \tanh\left(\frac{a\tau}{c}\right) = \frac{1}{\sinh\left(\frac{a\tau}{c}\right)} \tanh\left(\frac{a\tau}{c}\right)$
    where $\gamma(\tau) = \frac{\sinh\left(\frac{a\tau}{c}\right)}{\cosh\left(\frac{a\tau}{c}\right)}$

**2. Elapsed Lab Time after $\tau = 1.00$ proper year**

We are given $\tau = 1.00$ year $= 3.15576 \times 10^7$ s and $a = 9.8$ m/s$^2$.  We need to find $t(\tau)$.

$t(\tau) = \frac{\tau}{a} \sinh\left(\frac{a\tau}{c}\right)$

Let's calculate the argument of the hyperbolic sine:
$\frac{a\tau}{c} = \frac{9.8 \text{ m/s}^2 \times 3.15576 \times 10^7 \text{ s}}{3 \times 10^8 \text{ m/s}} = \frac{3.099 \times 10^8}{3 \times 10^8} \approx 1.033$

Now, we can calculate $t(\tau)$:
$t(\tau) = \frac{3.15576 \times 10^7 \text{ s}}{9.8 \text{ m/s}^2} \sinh(1.033) = 3.2196 \times 10^6 \text{ s} \times 1.188 \approx 3.836 \times 10^6 \text{ s}$

Converting to years:
$t(\tau) = \frac{3.836 \times 10^6 \text{ s}}{3.15576 \times 10^7 \text{ s/yr}} \approx 0.1215 \text{ years}$

**3. Distance Covered in Light-Years**

We need to find $x(\tau)$ and convert it to light-years.

$x(\tau) = \frac{c^2}{a} \cosh\left(\frac{a\tau}{c}\right) - \frac{c\tau}{a}$

Using the same value for $\frac{a\tau}{c} \approx 1.033$:
$\cosh(1.033) \approx 1.573$

$x(\tau) = \frac{(3 \times 10^8 \text{ m/s})^2}{9.8 \text{ m/s}^2} \times 1.573 - \frac{3 \times 10^8 \text{ m/s} \times 3.15576 \times 10^7 \text{ s}}{9.8 \text{ m/s}^2}$
$x(\tau) = \frac{9 \times 10^{16}}{9.8} \times 1.573 - \frac{9.467 \times 10^{15}}{9.8} = 1.49 \times 10^{16} - 9.67 \times 10^{14} = 1.393 \times 10^{16} \text{ m}$

Converting to light-years:
$1 \text{ ly} = c \times 1 \text{ yr} = 3 \times 10^8 \text{ m/s} \times 3.15576 \times 10^7 \text{ s} = 9.467 \times 10^{15} \text{ m}$

$x(\tau) = \frac{1.393 \times 10^{16} \text{ m}}{9.467 \times 10^{15} \text{ m/ly}} \approx 1.47 \text{ ly}$

**4. Final Speed $\beta = v/c$**

$\beta(\tau) = \frac{1}{\sinh\left(\frac{a\tau}{c}\right)} \tanh\left(\frac{a\tau}{c}\right)$

Using $\frac{a\tau}{c} \approx 1.033$:
$\sinh(1.033) \approx 1.188$
$\tanh(1.033) \approx 0.826$

$\beta(\tau) = \frac{1}{1.188} \times 0.826 \approx 0.695$

**5. Error in Student's Calculation**

The student's error lies in using $v = a\tau$. This is a Newtonian approximation that neglects relativistic effects. In Newtonian mechanics, acceleration is the rate of change of velocity. However, in special relativity, the velocity is bounded by the speed of light ($c$). As the rocket accelerates, its velocity approaches $c$ but never exceeds it. The Rindler relations account for this relativistic limit, while $v = a\tau$ does not.  The correct Rindler relations incorporate the Lorentz factor and ensure that $\beta$ always remains less than 1.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 0.1215 \\
\mathrm{distance\_ly} &= 1.47 \\
\mathrm{final\_beta} &= 0.695
\end{aligned}
\]