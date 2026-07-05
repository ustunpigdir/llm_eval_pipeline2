Let's solve the problem step by step using the exact Rindler relations for hyperbolic motion.

1. **Exact expressions for lab time, lab distance, and velocity:**

For an object undergoing constant proper acceleration \( a \), the exact relations are given by:

\[
t(\tau) = \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right)
\]

\[
x(\tau) = \frac{c^2}{a} \left( \cosh\left(\frac{a\tau}{c}\right) - 1 \right)
\]

\[
\beta(\tau) = \tanh\left(\frac{a\tau}{c}\right)
\]

where:
- \( \tau \) is the proper time on the rocket,
- \( c \) is the speed of light,
- \( a \) is the constant proper acceleration,
- \( t(\tau) \) is the lab time,
- \( x(\tau) \) is the lab distance,
- \( \beta(\tau) \) is the velocity in units of \( c \).

2. **Evaluate the elapsed lab time in years after \( \tau = 1.00 \) proper year:**

Given:
- \( a = 9.8 \, \text{m/s}^2 \),
- \( \tau = 1.00 \, \text{yr} = 3.15576 \times 10^7 \, \text{s} \),
- \( c = 2.99792 \times 10^8 \, \text{m/s} \).

First, calculate \( \frac{a\tau}{c} \):

\[
\frac{a\tau}{c} = \frac{9.8 \times 3.15576 \times 10^7}{2.99792 \times 10^8} \approx 1.042
\]

Now, calculate \( \sinh\left(\frac{a\tau}{c}\right) \):

\[
\sinh(1.042) \approx 1.373
\]

Now, calculate \( t(\tau) \):

\[
t(\tau) = \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right) = \frac{2.99792 \times 10^8}{9.8} \times 1.373 \approx 3.92 \times 10^7 \, \text{s}
\]

Convert \( t(\tau) \) to years:

\[
t(\tau) = \frac{3.92 \times 10^7}{3.15576 \times 10^7} \approx 1.24 \, \text{yr}
\]

3. **Evaluate the distance covered in light-years:**

Calculate \( \cosh\left(\frac{a\tau}{c}\right) \):

\[
\cosh(1.042) \approx 1.561
\]

Now, calculate \( x(\tau) \):

\[
x(\tau) = \frac{c^2}{a} \left( \cosh\left(\frac{a\tau}{c}\right) - 1 \right) = \frac{(2.99792 \times 10^8)^2}{9.8} \times (1.561 - 1) \approx 1.19 \times 10^{16} \, \text{m}
\]

Convert \( x(\tau) \) to light-years:

\[
x(\tau) = \frac{1.19 \times 10^{16}}{2.99792 \times 10^8 \times 3.15576 \times 10^7} \approx 1.22 \, \text{ly}
\]

4. **Evaluate the final speed \( \beta = v/c \):**

\[
\beta(\tau) = \tanh\left(\frac{a\tau}{c}\right) = \tanh(1.042) \approx 0.801
\]

5. **Explanation of the student's error:**

The student used the Newtonian approximation \( v = a\tau \), which is valid only for low velocities and small time intervals. In the context of special relativity, the velocity cannot exceed the speed of light \( c \). The correct expression for velocity is \( \beta(\tau) = \tanh\left(\frac{a\tau}{c}\right) \), which asymptotically approaches 1 as \( \tau \) increases, ensuring that the speed never exceeds \( c \).

FINAL ANSWER

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 1.24 \\
\mathrm{distance\_ly} &= 1.22 \\
\mathrm{final\_beta} &= 0.801
\end{aligned}
\]