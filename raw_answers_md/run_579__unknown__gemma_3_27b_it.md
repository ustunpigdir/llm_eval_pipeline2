Here's the solution to the hyperbolic motion problem, following the specified requirements.

**1. Exact Expressions for Lab Time, Distance, and Velocity**

For constant proper acceleration $a$, the Rindler relations are:

*   $x(\tau) = \frac{c^2}{a} (\cosh(\frac{a\tau}{c}) - 1)$
*   $t(\tau) = \frac{c}{a} \sinh(\frac{a\tau}{c})$
*   $v(\tau) = \beta(\tau)c = c \tanh(\frac{a\tau}{c})$

These equations describe the motion in the lab frame as a function of the proper time $\tau$ experienced by the rocket.

**2. Elapsed Lab Time after 1 Proper Year**

Given $a = 9.8$ m/s$^2$ and $\tau = 1.00$ yr $= 3.15576 \times 10^7$ s, we can calculate the elapsed lab time $t(\tau)$:

$t(\tau) = \frac{c}{a} \sinh(\frac{a\tau}{c})$

First, calculate the argument of the sinh function:

$\frac{a\tau}{c} = \frac{(9.8 \text{ m/s}^2)(3.15576 \times 10^7 \text{ s})}{2.99792 \times 10^8 \text{ m/s}} \approx 1.0288$

Then, calculate the sinh:

$\sinh(1.0288) \approx 1.1805$

Finally, calculate the lab time in seconds:

$t(\tau) = \frac{2.99792 \times 10^8 \text{ m/s}}{9.8 \text{ m/s}^2} (1.1805) \approx 3.538 \times 10^7 \text{ s}$

Convert to years:

$t(\tau) \text{ (in years)} = \frac{3.538 \times 10^7 \text{ s}}{3.15576 \times 10^7 \text{ s/yr}} \approx 1.121 \text{ yr}$

Therefore, the elapsed lab time after 1 proper year is approximately 1.121 years.

**3. Distance Covered in Light-Years**

Using the expression for $x(\tau)$:

$x(\tau) = \frac{c^2}{a} (\cosh(\frac{a\tau}{c}) - 1)$

We already calculated $\frac{a\tau}{c} \approx 1.0288$.  Now calculate the cosh:

$\cosh(1.0288) \approx 1.5645$

Then, calculate the distance in meters:

$x(\tau) = \frac{(2.99792 \times 10^8 \text{ m/s})^2}{9.8 \text{ m/s}^2} (1.5645 - 1) \approx 1.215 \times 10^{16} \text{ m}$

Convert to light-years:

$x(\tau) \text{ (in ly)} = \frac{1.215 \times 10^{16} \text{ m}}{2.99792 \times 10^8 \text{ m/ly}} \approx 405.8 \text{ ly}$

Therefore, the distance covered after 1 proper year is approximately 405.8 light-years.

**4. Final Speed $\beta = v/c$**

Using the expression for $\beta(\tau)$:

$\beta(\tau) = \tanh(\frac{a\tau}{c})$

We already calculated $\frac{a\tau}{c} \approx 1.0288$.  Now calculate the tanh:

$\tanh(1.0288) \approx 0.7576$

Therefore, the final speed is approximately 0.7576c.

**5. Student Error and Why $\beta < 1$**

The student's error is using Newtonian kinematics ($v = a\tau$) in a relativistic scenario.  Newtonian kinematics is a low-speed approximation to special relativity. As the speed approaches the speed of light, the relativistic effects become significant, and the Newtonian formula is no longer accurate.

The correct relativistic formula, $\beta = \tanh(\frac{a\tau}{c})$, ensures that $\beta$ remains less than 1 because the hyperbolic tangent function is always between -1 and 1.  As $\frac{a\tau}{c}$ increases, $\tanh(\frac{a\tau}{c})$ approaches 1 asymptotically, but never reaches or exceeds it. This is consistent with the fundamental principle of special relativity that no object with mass can travel at or faster than the speed of light.  The Newtonian formula does not have this built-in constraint and can easily predict speeds greater than $c$.

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 1.121 \\
\mathrm{distance\_ly} &= 405.8 \\
\mathrm{final\_beta} &= 0.7576
\end{aligned}
\]