### Derivation of the \(\sin \lambda\) Factor in Foucault Pendulum Precession

The Foucault pendulum precession arises due to the Coriolis effect caused by Earth's rotation. To derive the \(\sin \lambda\) factor, we analyze the vertical component of Earth's angular velocity \(\vec{\Omega}_E\) and its influence on the pendulum's swing plane.

---

#### **Step 1: Earth's Angular Velocity and Its Components**
Earth rotates with an angular velocity \(\vec{\Omega}_E\) of magnitude:
\[
\Omega_E = \frac{360^\circ}{24 \text{ h}} = 15^\circ/\text{h}.
\]
This vector points along Earth's axis of rotation (northward at the North Pole). At latitude \(\lambda\), the vertical direction is tilted relative to \(\vec{\Omega}_E\).

The **vertical component** of \(\vec{\Omega}_E\) (i.e., the component perpendicular to the local vertical) is responsible for the Coriolis force acting on the pendulum. This component is:
\[
\Omega_{\text{vertical}} = \Omega_E \sin \lambda.
\]
Here, \(\sin \lambda\) arises because the local vertical is tilted by \(\lambda\) relative to \(\vec{\Omega}_E\). The vertical component is the projection of \(\vec{\Omega}_E\) onto the plane perpendicular to the local vertical.

---

#### **Step 2: Coriolis Effect on the Pendulum Plane**
The Coriolis acceleration experienced by the pendulum bob is:
\[
\vec{a}_C = -2 \vec{\Omega}_E \times \vec{v},
\]
where \(\vec{v}\) is the velocity of the bob. For a pendulum swinging in a plane, the Coriolis force causes a torque that gradually rotates the plane of oscillation.

The **effective angular velocity** of the precession is determined by the component of \(\vec{\Omega}_E\) perpendicular to the local vertical (i.e., \(\Omega_E \sin \lambda\)), because this is the component that directly influences the horizontal motion of the pendulum. The vertical component (\(\Omega_E \cos \lambda\)) does not contribute to the precession of the swing plane.

---

#### **Step 3: Precession Rate Calculation**
The precession rate \(\Omega_{\text{precession}}\) is equal to the vertical component of Earth's angular velocity:
\[
\Omega_{\text{precession}} = \Omega_E \sin \lambda.
\]

Given:
- \(\Omega_E = 15^\circ/\text{h}\),
- \(\lambda = 48.85^\circ\) (Paris).

Compute \(\sin \lambda\):
\[
\sin(48.85^\circ) \approx 0.7536.
\]

Thus:
\[
\Omega_{\text{precession}} = 15^\circ/\text{h} \times 0.7536 = 11.304^\circ/\text{h}.
\]

---

#### **Step 4: Convert to Degrees per Day**
Multiply by 24 hours:
\[
\Omega_{\text{precession}} = 11.304^\circ/\text{h} \times 24 \text{ h} = 271.29^\circ/\text{day}.
\]

---

#### **Step 5: Full-Turn Period**
A full precession cycle corresponds to \(360^\circ\). The time for one full turn is:
\[
T = \frac{360^\circ}{\Omega_{\text{precession}}} = \frac{360^\circ}{11.304^\circ/\text{h}} \approx 31.84 \text{ h}.
\]

---

#### **Step 6: Behavior at the Equator and Pole**
- **At the equator (\(\lambda = 0^\circ\)):**
  \(\sin \lambda = 0\), so \(\Omega_{\text{precession}} = 0\). The pendulum plane does not precess; it remains fixed in space.

- **At the pole (\(\lambda = 90^\circ\)):**
  \(\sin \lambda = 1\), so \(\Omega_{\text{precession}} = \Omega_E = 15^\circ/\text{h}\). The pendulum completes a full precession in \(24 \text{ h}\).

---

#### **Step 7: Student's Mistake with \(\cos \lambda\)**
A student using \(\cos \lambda\) would be incorrectly considering the **horizontal component** of \(\vec{\Omega}_E\) (the component parallel to the local horizontal plane). This is the wrong component for plane precession because:
- The Coriolis force that causes the pendulum plane to rotate depends on the **vertical component** of Earth's angular velocity (the component perpendicular to the local vertical).
- The horizontal component (\(\Omega_E \cos \lambda\)) does not contribute to the rotation of the swing plane; it only affects the apparent motion of the pendulum's bob in the horizontal plane (e.g., causing a drift in the direction of motion).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day} &= 271.29 \\
\mathrm{rate\_deg\_per\_hour} &= 11.304 \\
\mathrm{period\_hours} &= 31.84
\end{aligned}
\]