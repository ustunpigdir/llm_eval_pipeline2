### Solution

We solve this problem using the exact Rindler relations for hyperbolic motion under constant proper acceleration \(a\). The key relations are:

\[
\begin{aligned}
t(\tau) &= \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right), \\
x(\tau) &= \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right], \\
\beta(\tau) &= \tanh\left(\frac{a\tau}{c}\right).
\end{aligned}
\]

Here, \(\tau\) is the proper time on the rocket, \(t\) is the lab-frame time, \(x\) is the lab-frame distance, and \(\beta = v/c\).

---

#### 1. Exact expressions for \(t(\tau)\), \(x(\tau)\), and \(\beta(\tau)\)

The exact Rindler relations for constant proper acceleration \(a\) are:

\[
\begin{aligned}
t(\tau) &= \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right), \\
x(\tau) &= \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right], \\
\beta(\tau) &= \tanh\left(\frac{a\tau}{c}\right).
\end{aligned}
\]

---

#### 2. Elapsed lab time after \(\tau = 1.00\) proper year

Given:
- \(a = 9.8\) m/s\(^2\),
- \(\tau = 1.00\) yr \(= 3.15576 \times 10^7\) s,
- \(c = 2.99792 \times 10^8\) m/s.

First, compute the argument of the hyperbolic functions:

\[
\frac{a\tau}{c} = \frac{9.8 \times 3.15576 \times 10^7}{2.99792 \times 10^8} \approx 0.1029.
\]

Now, evaluate \(t(\tau)\):

\[
t(\tau) = \frac{c}{a} \sinh(0.1029).
\]

We know that \(\sinh(x) \approx x + \frac{x^3}{6}\) for small \(x\), but we compute it directly:

\[
\sinh(0.1029) \approx 0.1030,
\]

so

\[
t(\tau) = \frac{2.99792 \times 10^8}{9.8} \times 0.1030 \approx 3.15576 \times 10^7 \times 0.1030 \approx 3.25 \times 10^6 \text{ s}.
\]

Convert to years:

\[
t(\tau) = \frac{3.25 \times 10^6}{3.15576 \times 10^7} \approx 0.103 \text{ yr}.
\]

---

#### 3. Distance covered in light-years

Using the exact expression for \(x(\tau)\):

\[
x(\tau) = \frac{c^2}{a} \left[\cosh(0.1029) - 1\right].
\]

We compute \(\cosh(0.1029)\):

\[
\cosh(0.1029) \approx 1 + \frac{(0.1029)^2}{2} \approx 1.0053,
\]

so

\[
x(\tau) = \frac{(2.99792 \times 10^8)^2}{9.8} \times (1.0053 - 1) \approx \frac{8.9875 \times 10^{16}}{9.8} \times 0.0053 \approx 4.82 \times 10^{14} \text{ m}.
\]

Convert to light-years:

\[
1 \text{ ly} = c \times 1 \text{ yr} = 2.99792 \times 10^8 \times 3.15576 \times 10^7 \approx 9.461 \times 10^{15} \text{ m},
\]

so

\[
x(\tau) = \frac{4.82 \times 10^{14}}{9.461 \times 10^{15}} \approx 0.051 \text{ ly}.
\]

---

#### 4. Final speed \(\beta = v/c\)

Using the exact expression:

\[
\beta(\tau) = \tanh(0.1029).
\]

For small \(x\), \(\tanh(x) \approx x - \frac{x^3}{3}\), so

\[
\beta(\tau) \approx 0.1029 - \frac{(0.1029)^3}{3} \approx 0.1029.
\]

---

#### 5. Error in the student's calculation

The student uses \(v = a\tau\), which is the Newtonian approximation. This leads to:

\[
\beta = \frac{v}{c} = \frac{a\tau}{c} = 0.1029,
\]

which coincidentally matches the relativistic result for small \(a\tau/c\). However, if the student had used a larger \(\tau\) (e.g., \(\tau = 10\) yr), the Newtonian approximation would have failed because \(\beta\) would exceed 1, which is impossible. The relativistic result \(\beta = \tanh(a\tau/c)\) always satisfies \(\beta < 1\) because \(\tanh(x) < 1\) for all finite \(x\).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 0.103 \\
\mathrm{distance\_ly} &= 0.051 \\
\mathrm{final\_beta} &= 0.103
\end{aligned}
\]