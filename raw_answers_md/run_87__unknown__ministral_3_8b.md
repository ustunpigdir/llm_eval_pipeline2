### **Derivation of the Precession Rate \(\Omega = \frac{mgl}{I_3 \omega_3}\)**

We analyze the gyroscopic precession of a fast top using the **fast-top approximation**, where the spin angular momentum \(I_3 \omega_3\) dominates over the precession angular momentum. This allows us to neglect nutation and treat the motion as steady precession.

---

#### **Step 1: Define the System and Quantities**
- A symmetric top spins about its symmetry axis with angular velocity \(\omega_3\).
- The top is pivoted at a distance \(l\) from its center of mass, so gravity exerts a torque \(\tau = mgl\) about the pivot.
- The spin moment of inertia about the symmetry axis is \(I_3\).
- The precession angular velocity is \(\Omega\), directed perpendicular to both the spin axis and gravity.

---

#### **Step 2: Angular Momentum and Torque**
The total angular momentum \(\mathbf{L}\) of the top is dominated by its spin component \(I_3 \omega_3 \hat{\mathbf{z}}\), where \(\hat{\mathbf{z}}\) is along the symmetry axis. The precession causes \(\mathbf{L}\) to precess about the vertical axis with angular velocity \(\Omega\).

The torque \(\boldsymbol{\tau}\) due to gravity is:
\[
\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} = \mathbf{l} \times (-mg \hat{\mathbf{y}}) = mgl \hat{\mathbf{x}},
\]
where \(\mathbf{l} = l \hat{\mathbf{x}}\) is the vector from the pivot to the center of mass, and \(\mathbf{F} = -mg \hat{\mathbf{y}}\) is the gravitational force (assuming the top is tilted slightly from the horizontal).

---

#### **Step 3: Rate of Change of Angular Momentum**
The torque is equal to the rate of change of angular momentum:
\[
\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}.
\]

In the fast-top approximation, the angular momentum precesses about the vertical axis with angular velocity \(\Omega\). The change in \(\mathbf{L}\) is:
\[
\frac{d\mathbf{L}}{dt} = \boldsymbol{\Omega} \times \mathbf{L}.
\]

Since \(\mathbf{L}\) is nearly aligned with the symmetry axis, and \(\boldsymbol{\Omega}\) is perpendicular to \(\mathbf{L}\), the magnitude of the torque is:
\[
|\boldsymbol{\tau}| = |\boldsymbol{\Omega} \times \mathbf{L}| = \Omega L \sin(90^\circ) = \Omega L,
\]
where \(L \approx I_3 \omega_3\) (since the precession angular momentum is negligible in the fast-top limit).

Thus:
\[
mgl = \Omega I_3 \omega_3.
\]

---

#### **Step 4: Solve for Precession Rate \(\Omega\)**
Rearranging gives:
\[
\Omega = \frac{mgl}{I_3 \omega_3}.
\]

This is the **steady precession rate** in the fast-top approximation.

---

### **Step 5: Numerical Evaluation**
Given:
- \(m = 0.500 \, \text{kg}\),
- \(g = 9.81 \, \text{m/s}^2\),
- \(l = 0.0500 \, \text{m}\),
- \(I_3 = 2.00 \times 10^{-4} \, \text{kg m}^2\),
- \(\omega_3 = 300 \, \text{rad/s}\).

Compute \(\Omega\):
\[
\Omega = \frac{(0.500)(9.81)(0.0500)}{(2.00 \times 10^{-4})(300)} = \frac{0.24525}{0.06} \approx 4.0875 \, \text{rad/s}.
\]

---

#### **Precession Period \(T\)**
The precession period is the time for one full precession:
\[
T = \frac{2\pi}{\Omega} = \frac{2\pi}{4.0875} \approx 1.53 \, \text{s}.
\]

---

### **Step 6: Effect of Doubling Spin \(\omega_3\)**
If \(\omega_3\) doubles to \(600 \, \text{rad/s}\), the new precession rate \(\Omega'\) is:
\[
\Omega' = \frac{mgl}{I_3 (2 \omega_3)} = \frac{\Omega}{2} = \frac{4.0875}{2} = 2.04375 \, \text{rad/s}.
\]

**Scaling:** The precession rate is **inversely proportional** to the spin rate \(\omega_3\).

---

### **Step 7: Why the Top Precesses Instead of Falling**
The top precesses because its **spin angular momentum** creates a gyroscopic effect that resists changes in the direction of \(\mathbf{L}\). The torque due to gravity tries to align \(\mathbf{L}\) with gravity, but the fast spin causes \(\mathbf{L}\) to precess instead of falling over. This is analogous to a spinning bicycle wheel resisting tilting.

The **nutation** is a small, rapid oscillation of the top's axis superimposed on the steady precession. In the fast-top approximation, nutation is negligible, but in reality, it arises from the coupling between spin and precession.

---

### **FINAL ANSWER**

\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 4.09 \, \mathrm{rad/s} \\
\mathrm{precession\_period\_s} &= 1.53 \, \mathrm{s} \\
\mathrm{precession\_double\_spin} &= 2.04 \, \mathrm{rad/s}
\end{aligned}
\]