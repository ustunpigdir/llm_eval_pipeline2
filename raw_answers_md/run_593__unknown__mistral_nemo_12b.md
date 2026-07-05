**1. Expressions for constant proper acceleration:**

The expressions for constant proper acceleration in special relativity are:

- Lab time: $t(\tau) = \frac{1}{a} \sinh\left(a\tau\right)$
- Lab distance: $x(\tau) = \frac{1}{a^2} \left(\cosh\left(a\tau\right) - 1\right)$
- Velocity: $\beta(\tau) = \tanh\left(a\tau\right)$

**2. Elapsed lab time after 1 proper year:**

Given $a = 9.8$ m/s$^2$ and $\tau = 1.00$ yr, we have:

\[
t(\tau) = \frac{1}{9.8} \sinh\left(9.8 \times 1.00\right) \approx 1.0158 \text{ yr}
\]

**3. Distance covered in light-years:**

First, convert the acceleration to light-years per proper time (yr/proper yr):

\[
a = 9.8 \text{ m/s}^2 \times \frac{1 \text{ ly}}{9.4607 \times 10^{15} \text{ m}} \times \frac{3.15576 \times 10^7 \text{ s}}{1 \text{ yr}} \approx 3.04 \times 10^{-15} \text{ ly/proper yr}
\]

Now, calculate the distance:

\[
x(\tau) = \frac{1}{\left(3.04 \times 10^{-15}\right)^2} \left(\cosh\left(3.04 \times 10^{-15} \times 1.00\right) - 1\right) \approx 3.29 \times 10^{-14} \text{ ly}
\]

**4. Final speed $\beta$:**

\[
\beta(\tau) = \tanh\left(9.8 \times 1.00\right) \approx 0.9999999999999999
\]

**5. Error in using $v = a\tau$:**

The error in using $v = a\tau$ is that it does not account for time dilation. In special relativity, the velocity cannot exceed 1 (c), and using $v = a\tau$ would lead to $\beta > 1$ for large enough $\tau$. The correct expression $\beta(\tau) = \tanh\left(a\tau\right)$ ensures that $\beta \leq 1$ for all $\tau$.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 1.0158 \text{ yr} \\
\mathrm{distance\_ly} &= 3.29 \times 10^{-14} \text{ ly} \\
\mathrm{final\_beta} &= 0.9999999999999999
\end{aligned}
\]