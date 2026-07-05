**1. Expressions for constant proper acceleration:**

In special relativity, for constant proper acceleration $a$, the expressions for lab time $t(\tau)$, lab distance $x(\tau)$, and velocity $\beta(\tau)$ are given by the Rindler relations:

- $t(\tau) = \frac{1}{a} \sinh(a\tau)$
- $x(\tau) = \frac{1}{a^2} \left( \sinh(a\tau) - a\tau \right)$
- $\beta(\tau) = \tanh(a\tau)$

**2. Elapsed lab time after $\tau = 1.00$ proper year:**

Given $a = 9.8$ m/s$^2$, we first find $a\tau$:

$a\tau = 9.8 \times 1.00 = 9.8$

Now, calculate $t(\tau)$:

$t(\tau) = \frac{1}{9.8} \sinh(9.8) \approx 1.013$ years

**3. Distance covered in light-years:**

First, convert $a$ to units of $c$:

$a = 9.8 \text{ m/s}^2 = 9.8 \times \frac{1}{c} \text{ c/s}^2$

Now, find $x(\tau)$:

$x(\tau) = \frac{1}{9.8^2} \left( \sinh(9.8) - 9.8 \right) \approx 0.0104 \text{ ly}$

**4. Final speed $\beta$:**

$\beta(\tau) = \tanh(9.8) \approx 0.9999$

**5. Error in using $v = a\tau$:**

The error in using $v = a\tau$ is that it does not account for time dilation. In special relativity, the velocity is given by $\beta = \tanh(a\tau)$, which ensures that $\beta < 1$ for all proper times $\tau$. Using $v = a\tau$ would lead to $\beta = a\tau/c$, which can exceed 1, violating the principle of relativity.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 1.013 \\
\mathrm{distance\_ly} &= 0.0104 \\
\mathrm{final\_beta} &= 0.9999
\end{aligned}
\]