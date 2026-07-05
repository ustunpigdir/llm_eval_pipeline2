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
        = \frac{3.091 \times 10^{8}\;\text{m/s}}
               {2.9979\times10^{8}\;\text{m/s}}
        \approx 1.031.
\]

Now compute the lab time:

\[
t(1\;\text{yr}) = \frac{c}{a}\,\sinh(\alpha)
                = \frac{c}{a}\,\sinh(1.031).
\]

\[
\sinh(1.031) = \frac{e^{1.031} - e^{-1.031}}{2}
             \approx \frac{2.807 - 0.356}{2}
             \approx 1.225.
\]

\[
\frac{c}{a} = \frac{2.9979\times10^{8}\;\text{m/s}}{9.8\;\text{m/s}^{2}}
            \approx 3.058 \times 10^{7}\;\text{s}.
\]

Thus  

\[
t(1\;\text{yr}) \approx 3.058 \times 10^{7}\;\text{s}\times 1.225
                 \approx 3.747 \times 10^{7}\;\text{s}.
\]

Convert to years using \(1\;\text{yr}=3.15576\times10^{7}\;\text{s}\):

\[
\text{lab\_time\_yr} = \frac{3.747\times10^{7}\;\text{s}}{3.15576\times10^{7}\;\text{s/yr}}
                     \approx 1.188\;\text{yr}.
\]

---

### 3. Distance covered in light‑years  

\[
x(1\;\text{yr}) = \frac{c^{2}}{a}\,\cosh(\alpha).
\]

\[
\cosh(1.031) = \frac{e^{1.031}+e^{-1.031}}{2}
             \approx \frac{2.807 + 0.356}{2}
             \approx 1.581.
\]

\[
\frac{c^{2}}{a} = \frac{(2.9979\times10^{8}\;\text{m/s})^{2}}{9.8\;\text{m/s}^{2}}
                \approx \frac{8.9876\times10^{16}\;\text{m}^{2}\!/\!\text{s}^{2}}{9.8\;\text{m/s}^{2}}
                \approx 9.176 \times 10^{15}\;\text{m}.
\]

Hence  

\[
x(1\;\text{yr}) \approx 9.176 \times 10^{15}\;\text{m}\times 1.581
                 \approx 1.450 \times 10^{16}\;\text{m}.
\]

One light‑year (ly) is  

\[
1\;\text{ly}=c\times 1\;\text{yr}=2.9979\times10^{8}\;\text{m/s}\times 3.15576\times10^{7}\;\text{s}
            \approx 9.4607\times10^{15}\;\text{m}.
\]

Thus  

\[
\text{distance\_ly}= \frac{1.450\times10^{16}\;\text{m}}{9.4607\times10^{15}\;\text{m/ly}}
                   \approx 1.533\;\text{ly}.
\]

---

### 4. Final speed \(\beta = v/c\)

\[
\beta(1\;\text{yr}) = \tanh(\alpha) = \tanh(1.031).
\]

\[
\tanh(1.031)=\frac{\sinh(1.031)}{\cosh(1.031)}
            \approx \frac{1.225}{1.581}
            \approx 0.775.
\]

So  

\[
\text{final\_beta} \approx 0.775.
\]

---

### 5. Error in the student’s approximation \(v = a\tau\)

The student used the Newtonian relation \(v = a\tau\).  
In the relativistic regime this neglects the factor \(\gamma = 1/\sqrt{1-\beta^{2}}\) that appears in the correct relation \(a = \dfrac{d\gamma v}{dt}\).  

Consequences:

* **Missing \(\gamma\) factor:** The true velocity grows more slowly than the linear prediction because as \(v\) approaches \(c\), \(\gamma\) increases, reducing the rate of change of \(v\) for a given proper acceleration.
* **Resulting \(\beta > 1\):** If one naively substitutes \(v = a\tau\) into \(\beta = v/c\), one obtains \(\beta = (a\tau)/c\). For \(\tau = 1\) yr, this gives \(\beta \approx 1.031 > 1\), which is impossible because speeds cannot exceed \(c\).
* **Correct behavior:** The exact \(\beta(\tau)=\tanh(a\tau/c)\) always satisfies \(0 \le \beta < 1\) for any finite \(\tau\). The hyperbolic tangent saturates at 1 as \(\tau \to \infty\), reflecting the fact that an object with constant proper acceleration asymptotically approaches the speed of light but never reaches or exceed it.

Thus the student’s error is the omission of relativistic time dilation and the resulting over‑estimate of velocity, leading to an unphysical \(\beta>1\).

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 1.188,\\
\mathrm{distance\_ly} &= 1.533,\\
\mathrm{final\_beta} &= 0.775.
\end{aligned}
\]