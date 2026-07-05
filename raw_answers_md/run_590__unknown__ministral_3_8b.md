### Solution to the Problem of Hyperbolic Motion with Constant Proper Acceleration

We solve the problem using the exact Rindler relations for constant proper acceleration \(a\). The key relations for hyperbolic motion are derived from the 4-acceleration and the hyperbolic trajectory in special relativity.

---

#### **1. Exact Expressions for \(t(\tau)\), \(x(\tau)\), and \(\beta(\tau)\)**

For constant proper acceleration \(a\), the exact solutions for a rocket starting from rest are:

- **Proper time \(\tau\)** is the time measured by the rocket's clock.
- **Lab-frame time \(t(\tau)\)** is given by:
  \[
  t(\tau) = \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right)
  \]

- **Lab-frame position \(x(\tau)\)** is given by:
  \[
  x(\tau) = \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right]
  \]

- **Velocity \(\beta(\tau) = v/c\)** is given by:
  \[
  \beta(\tau) = \tanh\left(\frac{a\tau}{c}\right)
  \]

---

#### **2. Evaluation of Elapsed Lab Time After \(\tau = 1.00\) Proper Year**

Given:
- \(a = 9.8 \, \text{m/s}^2\)
- \(c = 3.00 \times 10^8 \, \text{m/s}\)
- \(\tau = 1.00 \, \text{yr} = 3.15576 \times 10^7 \, \text{s}\)

Compute the argument of the hyperbolic functions:
\[
\frac{a\tau}{c} = \frac{9.8 \times 3.15576 \times 10^7}{3.00 \times 10^8} = 0.10278
\]

Now compute \(t(\tau)\):
\[
t(\tau) = \frac{c}{a} \sinh\left(\frac{a\tau}{c}\right) = \frac{3.00 \times 10^8}{9.8} \sinh(0.10278)
\]
\[
\sinh(0.10278) \approx 0.10281
\]
\[
t(\tau) = \frac{3.00 \times 10^8}{9.8} \times 0.10281 \approx 3.155 \times 10^7 \, \text{s}
\]

Convert to years:
\[
t(\tau) = \frac{3.155 \times 10^7}{3.15576 \times 10^7} \approx 0.9996 \, \text{yr}
\]

---

#### **3. Evaluation of Distance Covered in Light-Years**

Using the exact expression for \(x(\tau)\):
\[
x(\tau) = \frac{c^2}{a} \left[\cosh\left(\frac{a\tau}{c}\right) - 1\right]
\]
\[
\cosh(0.10278) \approx 1 + \frac{(0.10278)^2}{2} = 1.00528
\]
\[
x(\tau) = \frac{(3.00 \times 10^8)^2}{9.8} \times (1.00528 - 1) = \frac{9.00 \times 10^{16}}{9.8} \times 0.00528
\]
\[
x(\tau) \approx 4.77 \times 10^{13} \, \text{m}
\]

Convert to light-years:
\[
1 \, \text{ly} = c \times 1 \, \text{yr} = 3.00 \times 10^8 \times 3.15576 \times 10^7 \, \text{m} = 9.46732 \times 10^{15} \, \text{m}
\]
\[
x(\tau) = \frac{4.77 \times 10^{13}}{9.46732 \times 10^{15}} \approx 0.00504 \, \text{ly}
\]

---

#### **4. Evaluation of Final Speed \(\beta = v/c\)**

Using the exact expression for \(\beta(\tau)\):
\[
\beta(\tau) = \tanh\left(\frac{a\tau}{c}\right) = \tanh(0.10278)
\]
\[
\tanh(0.10278) \approx 0.1023
\]

---

#### **5. Error in the Student's Calculation**

The student uses the Newtonian approximation \(v = a\tau\), which is incorrect for relativistic motion. This approximation ignores the relativistic effects that limit the velocity to \(c\). For \(\tau = 1.00 \, \text{yr}\), the Newtonian estimate would be:
\[
v = a\tau = 9.8 \times 3.15576 \times 10^7 = 3.0926 \times 10^8 \, \text{m/s}
\]
This exceeds \(c = 3.00 \times 10^8 \, \text{m/s}\), which is impossible. The correct relativistic expression \(\beta = \tanh(a\tau/c)\) ensures \(\beta < 1\) for all finite \(\tau\).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 0.9996 \\
\mathrm{distance\_ly} &= 0.00504 \\
\mathrm{final\_beta} &= 0.1023
\end{aligned}
\]