**Step‑by‑step derivation**

For constant proper acceleration \(a\) in special relativity the Rindler (hyperbolic) world‑line is obtained from the exact solution of the geodesic equation.  
Starting from the relation between proper time \(\tau\) and the lab (inertial) time \(t\),

\[
\frac{d\tau}{dt}= \sqrt{1-\frac{v^{2}}{c^{2}}}\;,
\]

and using the definition of proper acceleration \(a = \dfrac{d\gamma v}{dt}\) with \(\gamma = 1/\sqrt{1-\beta^{2}}\) (\(\beta = v/c\)), one integrates to obtain the standard Rindler formulas (see any SR textbook):

\[
\boxed{t(\tau)=\frac{c}{a}\sinh\!\left(\frac{a\tau}{c}\right)} ,
\qquad
\boxed{x(\tau)=\frac{c^{2}}{a}\Bigl[\cosh\!\left(\frac{a\tau}{c}\right)-1\Bigr]} ,
\qquad
\boxed{\beta(\tau)=\tanh\!\left(\frac{a\tau}{c}\right)} .
\]

These expressions satisfy the initial condition \(x(0)=0,\;t(0)=0\) and the proper acceleration \(a\) is constant.

---

### 1. Exact expressions (already given above)

\[
t(\tau)=\frac{c}{a}\sinh\!\left(\frac{a\tau}{c}\right),\qquad
x(\tau)=\frac{c^{2}}{a}\Bigl[\cosh\!\left(\frac{a\tau}{c}\right)-1\Bigr],\qquad
\beta(\tau)=\tanh\!\left(\frac{a\tau}{c}\right).
\]

---

### 2. Lab time after \(\tau = 1\) proper year  

Given \(a = 9.8\;\text{m/s}^{2}\) and \(\tau = 1\;\text{yr}\),

\[
\frac{a\tau}{c}= \frac{9.8\;\text{m/s}^{2}\times 3.15576\times10^{7}\,\text{s}}{2.99792458\times10^{8}\,\text{m/s}}
               \approx 0.1035\;.
\]

Hence

\[
t(1\;\text{yr}) = \frac{c}{a}\sinh(0.1035)
                = \frac{2.9979\times10^{8}}{9.8}\,\sinh(0.1035)
                \approx 3.058\times10^{7}\,\text{s}\times 0.1038
                \approx 3.176\times10^{6}\,\text{s}.
\]

Convert to years using \(1\;\text{yr}=3.15576\times10^{7}\,\text{s}\):

\[
\text{lab\_time\_yr}= \frac{3.176\times10^{6}}{3.15576\times10^{7}}
                    \approx 0.1007\;\text{yr}.
\]

---

### 3. Distance covered in light‑years  

\[
x(1\;\text{yr}) = \frac{c^{2}}{a}\Bigl[\cosh(0.1035)-1\Bigr]
                = \frac{(2.9979\times10^{8})^{2}}{9.8}\bigl[1.00535-1\bigr]
                \approx \frac{8.9876\times10^{16}}{9.8}\times0.00535
                \approx 4.91\times10^{13}\,\text{m}.
\]

Since \(1\;\text{ly}=c\times1\;\text{yr}=2.9979\times10^{8}\times3.15576\times10^{7}\,\text{m}
               \approx 9.4607\times10^{15}\,\text{m}\),

\[
\text{distance\_ly}= \frac{4.91\times10^{13}}{9.4607\times10^{15}}
                   \approx 5.19\times10^{-3}\;\text{ly}
                   \approx 0.0052\;\text{ly}.
\]

---

### 4. Final speed \(\beta = v/c\)

\[
\beta(1\;\text{yr}) = \tanh(0.1035) \approx 0.1033.
\]

Thus

\[
\text{final\_beta}=0.1033.
\]

---

### 5. Explanation of the student’s error  

The student used the Newtonian relation \(v = a\tau\).  
In special relativity, velocities do **not** add linearly with proper time because the speed of light is a hard limit. The correct relation comes from the hyperbolic motion formulas above, which involve hyperbolic functions.  

- The factor \(\gamma = 1/\sqrt{1-\beta^{2}}\) grows without bound as \(v\) approaches \(c\).  
- Consequently, the simple product \(a\tau\) would predict \(v \to c\) only after an infinite proper time, not after a finite \(\tau\).  

Because \(\beta = \tanh(a\tau/c)\) is always **strictly less than** 1 for any finite \(\tau\), the student’s linear approximation overestimates the speed and yields \(\beta>1\), which is unphysical. The correct \(\beta\) stays below 1, as shown above.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 0.1007 \\
\mathrm{distance\_ly} &= 0.0052 \\
\mathrm{final\_beta} &= 0.1033
\end{aligned}
\]