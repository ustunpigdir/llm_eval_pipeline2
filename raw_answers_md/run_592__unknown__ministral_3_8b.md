### Solution

We solve the problem using the exact Rindler relations for constant proper acceleration \(a\). The proper acceleration \(a\) is the acceleration measured by an accelerometer on the rocket, which is the four-acceleration's magnitude in the instantaneous rest frame of the rocket.

---

#### 1. Exact expressions for lab time \(t(\tau)\), lab distance \(x(\tau)\), and velocity \(\beta(\tau)\)

For constant proper acceleration \(a\), the exact solutions for hyperbolic motion are:

\[
t(\tau) = \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right),
\]
\[
x(\tau) = \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right],
\]
\[
\beta(\tau) = \frac{v(\tau)}{c} = \tanh\left(\frac{a\tau}{c}\right).
\]

Here:
- \(\tau\) is the proper time on the rocket,
- \(c\) is the speed of light,
- \(a\) is the proper acceleration,
- \(t(\tau)\) is the lab-frame time elapsed,
- \(x(\tau)\) is the lab-frame distance covered,
- \(\beta(\tau)\) is the velocity as a fraction of \(c\).

---

#### 2. Elapsed lab time after \(\tau = 1.00\) proper year

Given:
- \(a = 9.8 \, \text{m/s}^2\),
- \(\tau = 1.00 \, \text{yr} = 3.15576 \times 10^7 \, \text{s}\),
- \(c = 2.99792 \times 10^8 \, \text{m/s}\).

Compute the argument of the hyperbolic functions:

\[
\frac{a\tau}{c} = \frac{9.8 \times 3.15576 \times 10^7}{2.99792 \times 10^8} \approx 0.1039.
\]

Now compute \(t(\tau)\):

\[
t(\tau) = \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right) = \frac{2.99792 \times 10^8}{9.8} \sinh(0.1039).
\]

Calculate \(\sinh(0.1039)\):

\[
\sinh(0.1039) \approx 0.1040.
\]

Thus:

\[
t(\tau) \approx \frac{2.99792 \times 10^8}{9.8} \times 0.1040 \approx 3.155 \times 10^7 \, \text{s}.
\]

Convert to years:

\[
t(\tau) \approx \frac{3.155 \times 10^7}{3.15576 \times 10^7} \approx 0.9996 \, \text{yr}.
\]

---

#### 3. Distance covered in light-years

Using the exact expression for \(x(\tau)\):

\[
x(\tau) = \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right].
\]

Calculate \(\cosh(0.1039)\):

\[
\cosh(0.1039) \approx 1 + \frac{(0.1039)^2}{2} \approx 1.0054.
\]

Thus:

\[
x(\tau) \approx \frac{(2.99792 \times 10^8)^2}{9.8} \times (1.0054 - 1) = \frac{8.9875 \times 10^{16}}{9.8} \times 0.0054 \approx 4.87 \times 10^{13} \, \text{m}.
\]

Convert to light-years:

\[
1 \, \text{ly} = c \times 1 \, \text{yr} = 2.99792 \times 10^8 \times 3.15576 \times 10^7 \approx 9.461 \times 10^{15} \, \text{m}.
\]

Thus:

\[
x(\tau) \approx \frac{4.87 \times 10^{13}}{9.461 \times 10^{15}} \approx 0.00515 \, \text{ly}.
\]

---

#### 4. Final speed \(\beta = v/c\)

Using the exact expression:

\[
\beta(\tau) = \tanh\left(\frac{a\tau}{c}\right) = \tanh(0.1039).
\]

Calculate \(\tanh(0.1039)\):

\[
\tanh(0.1039) \approx 0.1034.
\]

---

#### 5. Error in the student's calculation

The student uses \(v = a\tau\), which is the Newtonian approximation for small velocities. However, in relativity, the velocity cannot exceed \(c\), and the correct relation for constant proper acceleration is:

\[
v(\tau) = c \tanh\left(\frac{a\tau}{c}\right).
\]

For \(\tau = 1 \, \text{yr}\), the student's calculation would give:

\[
v = a\tau = 9.8 \times 3.15576 \times 10^7 \approx 3.09 \times 10^8 \, \text{m/s}.
\]

This exceeds \(c\) (since \(c \approx 3.00 \times 10^8 \, \text{m/s}\)), which is impossible. The error arises because the student ignores relativistic effects, which limit the velocity to approach \(c\) asymptotically. The exact hyperbolic motion ensures \(\beta < 1\) for all finite \(\tau\).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 0.9996 \\
\mathrm{distance\_ly} &= 0.00515 \\
\mathrm{final\_beta} &= 0.1034
\end{aligned}
\]