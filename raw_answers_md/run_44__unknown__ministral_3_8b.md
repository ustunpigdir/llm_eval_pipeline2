### Derivation of the \(\sin \lambda\) Factor in Foucault Pendulum Precession

The Foucault pendulum precession arises due to the Coriolis effect caused by Earth's rotation. To derive the \(\sin \lambda\) factor, we analyze the vertical component of Earth's angular velocity \(\vec{\Omega}_E\) and its influence on the pendulum's swing plane.

---

#### Step 1: Earth's Angular Velocity and Its Components
Earth rotates with an angular velocity \(\vec{\Omega}_E\) of magnitude:
\[
\Omega_E = \frac{360^\circ}{24 \text{ hours}} = 15^\circ/\text{hour}.
\]
This vector points along the Earth's axis of rotation, which is tilted relative to the local vertical at latitude \(\lambda\).

The components of \(\vec{\Omega}_E\) in a local coordinate system (where the \(z\)-axis is vertical and the \(x\)-axis points north) are:
\[
\vec{\Omega}_E = \Omega_E \begin{pmatrix}
0 \\
\sin \lambda \\
\cos \lambda
\end{pmatrix},
\]
where:
- The \(y\)-component (\(\Omega_E \sin \lambda\)) is the **horizontal component perpendicular to the local vertical** (pointing eastward in the northern hemisphere).
- The \(z\)-component (\(\Omega_E \cos \lambda\)) is the **vertical component** of Earth's rotation.

---

#### Step 2: Coriolis Effect on the Pendulum
The Coriolis acceleration experienced by the pendulum bob is given by:
\[
\vec{a}_C = -2 \vec{v} \times \vec{\Omega}_E,
\]
where \(\vec{v}\) is the velocity of the bob. For a pendulum swinging in a plane, the Coriolis force acts perpendicular to both \(\vec{v}\) and \(\vec{\Omega}_E\), causing the swing plane to precess.

The key observation is that **only the horizontal component of \(\vec{\Omega}_E\) perpendicular to the swing plane contributes to the precession of the swing plane itself**. This is because the vertical component (\(\Omega_E \cos \lambda\)) does not affect the horizontal motion of the pendulum bob in a way that changes the orientation of the swing plane.

The relevant component for plane precession is the **horizontal component of \(\vec{\Omega}_E\) perpendicular to the local vertical**, which is \(\Omega_E \sin \lambda\). This is because:
- At the pole (\(\lambda = 90^\circ\)), \(\vec{\Omega}_E\) is entirely horizontal, and the precession is maximal.
- At the equator (\(\lambda = 0^\circ\)), \(\vec{\Omega}_E\) is entirely vertical, and there is no precession of the swing plane (only the bob's path curves, but the plane does not rotate).

---

#### Step 3: Precession Rate
The precession rate of the swing plane is equal to the horizontal component of Earth's angular velocity perpendicular to the local vertical:
\[
\Omega_{\text{precession}} = \Omega_E \sin \lambda.
\]
This is because the Coriolis force causes the swing plane to rotate at this rate relative to the inertial frame.

---

#### Step 4: Numerical Evaluation
Given:
- \(\lambda = 48.85^\circ\),
- \(\Omega_E = 15^\circ/\text{hour}\).

Compute \(\sin \lambda\):
\[
\sin(48.85^\circ) \approx 0.7547.
\]

Now compute the precession rates:
1. **Degrees per hour**:
   \[
   \text{rate\_deg\_per\_hour} = \Omega_E \sin \lambda = 15^\circ/\text{hour} \times 0.7547 \approx 11.32^\circ/\text{hour}.
   \]
2. **Degrees per day**:
   \[
   \text{rate\_deg\_per\_day} = \text{rate\_deg\_per\_hour} \times 24 \approx 11.32 \times 24 \approx 271.7^\circ/\text{day}.
   \]
3. **Full-turn period (hours)**:
   A full turn is \(360^\circ\), so:
   \[
   \text{period\_hours} = \frac{360^\circ}{\text{rate\_deg\_per\_hour}} = \frac{360}{11.32} \approx 31.8 \text{ hours}.
   \]
   Alternatively, using the relation:
   \[
   \text{period\_hours} = \frac{24 \text{ hours}}{\sin \lambda} = \frac{24}{0.7547} \approx 31.8 \text{ hours}.
   \]

---

#### Step 5: Behavior at the Equator and Pole
- **At the equator (\(\lambda = 0^\circ\))**:
  \(\sin \lambda = 0\), so \(\Omega_{\text{precession}} = 0\). The swing plane does not precess; instead, the pendulum's path curves in a circle due to the Coriolis effect, but the plane of oscillation remains fixed in the local frame.

- **At the pole (\(\lambda = 90^\circ\))**:
  \(\sin \lambda = 1\), so \(\Omega_{\text{precession}} = \Omega_E\). The swing plane completes a full rotation in 24 hours (one sidereal day).

---

#### Step 6: Student's Mistake with \(\cos \lambda\)
A student using \(\cos \lambda\) would be incorrectly considering the **vertical component of \(\vec{\Omega}_E\)** (\(\Omega_E \cos \lambda\)) for the precession of the swing plane. This is wrong because:
- The vertical component does not affect the horizontal motion of the pendulum bob in a way that changes the orientation of the swing plane.
- The precession arises from the **horizontal component perpendicular to the local vertical**, which is \(\Omega_E \sin \lambda\), not \(\Omega_E \cos \lambda\).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day} &= 271.7^\circ/\text{day}, \\
\mathrm{rate\_deg\_per\_hour} &= 11.32^\circ/\text{hour}, \\
\mathrm{period\_hours} &= 31.8 \text{ hours}.
\end{aligned}
\]