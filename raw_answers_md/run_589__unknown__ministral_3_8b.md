### Solution

We solve the problem using the exact Rindler relations for constant proper acceleration \(a\). The rocket starts from rest at \(x = 0\) at \(\tau = 0\). The exact solutions are:

\[
\begin{aligned}
t(\tau) &= \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right), \\
x(\tau) &= \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right], \\
\beta(\tau) &= \tanh\left(\frac{a\tau}{c}\right).
\end{aligned}
\]

---

#### 1. Exact expressions for \(t(\tau)\), \(x(\tau)\), and \(\beta(\tau)\)

The rocket undergoes hyperbolic motion under constant proper acceleration \(a\). The exact solutions are derived from the Rindler coordinates:

\[
\begin{aligned}
t(\tau) &= \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right), \\
x(\tau) &= \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right], \\
\beta(\tau) &= \frac{v}{c} = \tanh\left(\frac{a\tau}{c}\right).
\end{aligned}
\]

---

#### 2. Elapsed lab time after \(\tau = 1.00\) proper year

Given:
- \(a = 9.8 \, \text{m/s}^2\),
- \(\tau = 1.00 \, \text{yr} = 3.15576 \times 10^7 \, \text{s}\),
- \(c = 2.99792 \times 10^8 \, \text{m/s}\).

Compute the argument of the hyperbolic functions:

\[
\frac{a\tau}{c} = \frac{9.8 \times 3.15576 \times 10^7}{2.99792 \times 10^8} \approx 0.1028.
\]

Now evaluate \(t(\tau)\):

\[
t(\tau) = \frac{c}{a} \sinh\left(0.1028\right) \approx \frac{2.99792 \times 10^8}{9.8} \times 0.1028 \approx 3.11 \times 10^7 \, \text{s}.
\]

Convert to years:

\[
t(\tau) = \frac{3.11 \times 10^7}{3.15576 \times 10^7} \approx 0.985 \, \text{yr}.
\]

---

#### 3. Distance covered in light-years

Using the exact expression for \(x(\tau)\):

\[
x(\tau) = \frac{c^2}{a} \left[\cosh(0.1028) - 1\right].
\]

First compute \(\cosh(0.1028)\):

\[
\cosh(0.1028) \approx 1 + \frac{(0.1028)^2}{2} + \frac{(0.1028)^4}{24} \approx 1.00527.
\]

Then:

\[
x(\tau) = \frac{(2.99792 \times 10^8)^2}{9.8} \times (1.00527 - 1) \approx \frac{8.9875 \times 10^{16}}{9.8} \times 0.00527 \approx 4.72 \times 10^{13} \, \text{m}.
\]

Convert to light-years:

\[
x(\tau) = \frac{4.72 \times 10^{13}}{3.15576 \times 10^{16} \times 2.99792 \times 10^8} \approx 0.052 \, \text{ly}.
\]

---

#### 4. Final speed \(\beta = v/c\)

Using the exact expression:

\[
\beta(\tau) = \tanh(0.1028) \approx 0.1023.
\]

---

#### 5. Error in the student's calculation

The student uses the Newtonian approximation \(v = a\tau\), which gives:

\[
v = 9.8 \times 3.15576 \times 10^7 \approx 3.09 \times 10^8 \, \text{m/s}.
\]

This exceeds \(c\) (\(2.99792 \times 10^8 \, \text{m/s}\)), leading to \(\beta > 1\). The error arises because Newtonian kinematics does not account for relativistic effects (time dilation and length contraction). The correct relativistic velocity never exceeds \(c\), as \(\tanh(x) < 1\) for all finite \(x\).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 0.985 \\
\mathrm{distance\_ly} &= 0.052 \\
\mathrm{final\_beta} &= 0.1023
\end{aligned}
\]