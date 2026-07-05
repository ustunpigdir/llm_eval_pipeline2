**Step‑by‑step derivation**

For constant proper acceleration \(a\) in special relativity the Rindler (hyperbolic) world‑line is obtained from the standard solution of the relativistic equation of motion.  
Starting from the relation between proper time \(\tau\) and the lab (inertial) time \(t\),

\[
\frac{d\tau}{dt}= \sqrt{1-\frac{v^{2}}{c^{2}}}\;,
\]

and using \(a = \dfrac{d\gamma v}{dt}\) with \(\gamma = 1/\sqrt{1-\beta^{2}}\) (\(\beta = v/c\)), one integrates to obtain the exact Rindler formulas (see any textbook on relativistic kinematics):

\[
\boxed{t(\tau)=\frac{c}{a}\sinh\!\left(\frac{a\tau}{c}\right)} ,
\qquad
\boxed{x(\tau)=\frac{c^{2}}{a}\Bigl[\cosh\!\left(\frac{a\tau}{c}\right)-1\Bigr]} ,
\qquad
\boxed{\beta(\tau)=\tanh\!\left(\frac{a\tau}{c}\right)} .
\]

These satisfy the initial conditions \(t(0)=0,\;x(0)=0,\;v(0)=0\) and the proper acceleration \(a\) is constant.

---

### 1. Exact expressions (already given above)

\[
t(\tau)=\frac{c}{a}\sinh\!\left(\frac{a\tau}{c}\right),\qquad
x(\tau)=\frac{c^{2}}{a}\Bigl[\cosh\!\left(\frac{a\tau}{c}\right)-1\Bigr],\qquad
\beta(\tau)=\tanh\!\left(\frac{a\tau}{c}\right).
\]

---

### 2. Lab time after \(\tau = 1\) proper year  

Given \(a = 9.8\;\text{m s}^{-2}\) and \(\tau = 1\;\text{yr}\),

\[
\tau_{\text{yr}} = 1\;\text{yr}=3.15576\times10^{7}\;\text{s}.
\]

Compute the dimensionless argument

\[
\frac{a\tau}{c}= \frac{9.8\;\text{m s}^{-2}\times 3.15576\times10^{7}\;\text{s}}{2.99792458\times10^{8}\;\text{m s}^{-1}}
               \approx 0.1035 .
\]

Now

\[
t(1\;\text{yr}) = \frac{c}{a}\sinh(0.1035)
                = \frac{2.9979\times10^{8}}{9.8}\,\sinh(0.1035)
                \approx 3.058\times10^{7}\;\text{s}\times 0.1038
                \approx 3.176\times10^{6}\;\text{s}.
\]

Convert to years:

\[
\text{lab\_time\_yr}= \frac{3.176\times10^{6}\;\text{s}}{3.15576\times10^{7}\;\text{s/yr}}
                    \approx 0.1007\;\text{yr}.
\]

---

### 3. Distance covered in light‑years  

Using the same \(\frac{a\tau}{c}=0.1035\),

\[
x(1\;\text{yr}) = \frac{c^{2}}{a}\Bigl[\cosh(0.1035)-1\Bigr]
                = \frac{(2.9979\times10^{8})^{2}}{9.8}\,\bigl[1.00535-1\bigr]
                \approx \frac{8.9876\times10^{16}}{9.8}\times0.00535
                \approx 4.91\times10^{13}\;\text{m}.
\]

One light‑year (ly) is defined as \(c\times1\;\text{yr}=c\cdot3.15576\times10^{7}\;\text{s}\):

\[
1\;\text{ly}=2.9979\times10^{8}\times3.15576\times10^{7}
            \approx 9.4607\times10^{15}\;\text{m}.
\]

Thus

\[
\text{distance\_ly}= \frac{4.91\times10^{13}\;\text{m}}{9.4607\times10^{15}\;\text{m/ly}}
                   \approx 5.19\times10^{-3}\;\text{ly}
                   \approx 0.0052\;\text{ly}.
\]

---

### 4. Final speed \(\beta = v/c\)

\[
\beta(1\;\text{yr}) = \tanh\!\left(\frac{a\tau}{c}\right)
                    = \tanh(0.1035)
                    \approx 0.1033 .
\]

So the rocket’s speed after one proper year is about \(10.3\%\) of the speed of light.

---

### 5. Error in the student’s approximation \(v = a\tau\)

The student used the Newtonian relation \(v = a\tau\).  
In the relativistic regime this neglects the factor \(\gamma\) that arises from time‑dilation:

\[
v = \frac{a\tau}{\sqrt{1+(a\tau/c)^{2}}}\,\frac{c}{\sqrt{1+(a\tau/c)^{2}}}
   = c\,\tanh\!\left(\frac{a\tau}{c}\right).
\]

Because \(\tanh(x) < x\) for any \(x>0\), the true velocity is **always** smaller than the naïve \(a\tau\) result.  
If one incorrectly set \(v = a\tau\) without converting to the lab frame, one would obtain

\[
\beta_{\text{wrong}} = \frac{a\tau}{c}
                     \approx 0.1035,
\]

which is close to the correct value only for very small \(\tau\).  
For larger \(\tau\) the error grows, and the wrong formula would eventually predict \(\beta>1\) (super‑luminal speeds), which is impossible. The correct \(\beta\) stays below 1 because the hyperbolic tangent saturates at 1 as its argument grows, reflecting the relativistic speed limit \(v<c\).

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{lab\_time\_yr} &= 0.1007 \\
\mathrm{distance\_ly}  &= 0.0052 \\
\mathrm{final\_beta}   &= 0.1033
\end{aligned}
\]