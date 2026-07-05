**Step‑by‑step derivation**

For constant proper acceleration \(a\) in special relativity the Rindler (hyperbolic) world‑line is obtained from the standard solution of the relativistic equation of motion.  
Starting from the relation between proper time \(\tau\) and the lab (inertial) time \(t\),

\[
\frac{d\tau}{dt}= \sqrt{1-\frac{v^{2}}{c^{2}}}\;,
\]

and using \(a = \dfrac{d\gamma v}{dt}\) with \(\gamma = 1/\sqrt{1-\beta^{2}}\) (\(\beta = v/c\)), one integrates to obtain the exact Rindler formulas (see any textbook on relativistic kinematics):

\[
\boxed{t(\tau)=\frac{c}{a}\,\sinh\!\left(\frac{a\tau}{c}\right)} ,
\qquad
\boxed{x(\tau)=\frac{c^{2}}{a}\,\cosh\!\left(\frac{a\tau}{c}\right)} ,
\qquad
\boxed{\beta(\tau)=\tanh\!\left(\frac{a\tau}{c}\right)} .
\]

These satisfy the initial conditions \(t(0)=0,\;x(0)=0,\;v(0)=0\) and the proper acceleration \(a\) is constant.

---

### 1. Exact expressions (already given above)

\[
t(\tau)=\frac{c}{a}\sinh\!\left(\frac{a\tau}{c}\right),\qquad
x(\tau)=\frac{c^{2}}{a}\cosh\!\left(\frac{a\tau}{c}\right),\qquad
\beta(\tau)=\tanh\!\left(\frac{a\tau}{c}\right).
\]

---

### 2. Lab time after \(\tau = 1\) proper year  

Proper time \(\tau = 1\) yr = \(1 \times 3.15576\times10^{7}\,\text{s}\).

Define the dimensionless parameter  

\[
\alpha \equiv \frac{a\tau}{c}.
\]

Given \(a = 9.8\;\text{m/s}^{2}\) and \(c = 2.99792458\times10^{8}\;\text{m/s}\),

\[
\alpha = \frac{9.8\;\text{m/s}^{2}\times 3.15576\times10^{7}\,\text{s}}
               {2.99792458\times10^{8}\;\text{m/s}}
        \approx \frac{3.091 \times 10^{8}\;\text{m/s}}
                     {3.0 \times 10^{8}\;\text{m/s}}
        \approx 1.03 .
\]

Now compute the lab time:

\[
t(1\;\text{yr}) = \frac{c}{a}\,\sinh(\alpha)
                = \frac{c}{a}\,\sinh(1.03).
\]

\[
\sinh(1.03) \approx \frac{e^{1.03}-e^{-1.03}}{2}
               \approx \frac{2.803 - 0.3568}{2}
               \approx 1.223 .
\]

Thus

\[
t(1\;\text{yr}) \approx \frac{2.9979\times10^{8}}{9.8}\times1.223
                 \approx 3.058\times10^{7}\times1.223
                 \approx 3.744\times10^{7}\,\text{s}.
\]

Convert to years:

\[
\text{lab\_time\_yr} = \frac{3.744\times10^{7}\,\text{s}}
                           {3.15576\times10^{7}\,\text{s/yr}}
                     \approx 1.187\;\text{yr}.
\]

---

### 3. Distance covered in light‑years  

\[
x(1\;\text{yr}) = \frac{c^{2}}{a}\,\cosh(\alpha).
\]

\[
\cosh(1.03) \approx \frac{e^{1.03}+e^{-1.03}}{2}
               \approx \frac{2.803 + 0.3568}{2}
               \approx 1.580 .
\]

Hence

\[
x(1\;\text{yr}) \approx \frac{(2.9979\times10^{8})^{2}}{9.8}\times1.580
                 \approx \frac{8.9876\times10^{16}}{9.8}\times1.580
                 \approx 9.176\times10^{15}\times1.580
                 \approx 1.449\times10^{16}\,\text{m}.
\]

One light‑year (ly) is \(c \times 1\;\text{yr}\):

\[
1\;\text{ly} = c \times 3.15576\times10^{7}\,\text{s}
            \approx 2.9979\times10^{8}\times3.15576\times10^{7}
            \approx 9.4607\times10^{15}\,\text{m}.
\]

Thus

\[
\text{distance\_ly} = \frac{1.449\times10^{16}}{9.4607\times10^{15}}
                    \approx 1.532\;\text{ly}.
\]

---

### 4. Final speed \(\beta = v/c\)

\[
\beta(1\;\text{yr}) = \tanh(\alpha) = \tanh(1.03).
\]

\[
\tanh(1.03) \approx \frac{\sinh(1.03)}{\cosh(1.03)}
              \approx \frac{1.223}{1.580}
              \approx 0.774.
\]

So

\[
\text{final\_beta} \approx 0.774.
\]

---

### 5. Explanation of the student’s error  

The student used the Newtonian relation \(v = a\tau\).  
In special relativity, velocities do **not** add linearly with proper time because the speed of light is a hard limit. The correct relation for a body undergoing constant proper acceleration is

\[
v(\tau) = c \tanh\!\left(\frac{a\tau}{c}\right),
\]

which asymptotically approaches \(c\) as \(\tau \to \infty\) but never exceeds it.  

The error arises because \(a\tau\) grows without bound, whereas the relativistic velocity addition law forces the speed to saturate at \(c\). The hyperbolic tangent ensures \(\beta < 1\) for all finite \(\tau\). Hence the student’s linear approximation \(v = a\tau\) would predict \(\beta > 1\) for sufficiently large \(\tau\), violating causality and the principle of relativity.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 1.187,\\
\mathrm{distance\_ly} &= 1.532,\\
\mathrm{final\_beta} &= 0.774.
\end{aligned}
\]