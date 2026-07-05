### Derivation of the \(\sin \lambda\) Factor in Foucault Pendulum Precession

#### 1. Derivation of \(\sin \lambda\) from the Vertical Component of Earth's Angular Velocity

The Foucault pendulum precession arises due to the Coriolis effect caused by Earth's rotation. The key idea is that the pendulum's swing plane appears to rotate relative to the Earth's surface because the Earth itself is rotating beneath it.

##### Step 1: Earth's Angular Velocity
Earth's angular velocity vector \(\vec{\Omega}_E\) has a magnitude of:
\[
\Omega_E = \frac{360^\circ}{24 \text{ hours}} = 15^\circ/\text{hour}.
\]
This is the rate at which Earth rotates about its axis. The direction of \(\vec{\Omega}_E\) is along the Earth's rotational axis, pointing northward (by the right-hand rule).

##### Step 2: Components of \(\vec{\Omega}_E\) at Latitude \(\lambda\)
At latitude \(\lambda\), the Earth's angular velocity vector \(\vec{\Omega}_E\) can be decomposed into two components:
- A vertical component (parallel to the local vertical, i.e., the direction of gravity): \(\Omega_E \sin \lambda\).
- A horizontal component (parallel to the Earth's surface): \(\Omega_E \cos \lambda\).

The vertical component is the one that directly affects the precession of the pendulum's swing plane. This is because the Coriolis force depends on the component of Earth's angular velocity that is perpendicular to the local vertical (i.e., the horizontal component would affect the pendulum's motion differently, but it is the vertical component that drives the precession of the swing plane).

##### Step 3: Coriolis Effect on the Pendulum
The Coriolis acceleration experienced by the pendulum bob is given by:
\[
\vec{a}_C = -2 \vec{\Omega}_E \times \vec{v},
\]
where \(\vec{v}\) is the velocity of the pendulum bob. For a pendulum swinging in a plane, the Coriolis force causes a torque that tends to rotate the swing plane.

The precession rate of the swing plane is determined by the component of \(\vec{\Omega}_E\) that is perpendicular to the swing plane's normal. For a pendulum swinging in a vertical plane, the relevant component of \(\vec{\Omega}_E\) is the one perpendicular to the local vertical, which is the horizontal component of \(\vec{\Omega}_E\). However, the precession rate is actually determined by the vertical component of \(\vec{\Omega}_E\) because the swing plane's normal is horizontal (perpendicular to the vertical plane of swing), and the precession is driven by the component of \(\vec{\Omega}_E\) that is parallel to the local vertical (i.e., \(\Omega_E \sin \lambda\)).

This might seem counterintuitive at first, but the correct interpretation is that the precession rate is equal to the vertical component of Earth's angular velocity because the swing plane's rotation is tied to the Earth's rotation about its axis, and the vertical component is what "tilts" the rotation axis relative to the local vertical. The horizontal component affects the direction of the pendulum's motion but does not directly cause the precession of the swing plane.

A more precise derivation involves considering the angular momentum of the pendulum and how it precesses under the influence of Earth's rotation. The precession rate \(\Omega_p\) of the pendulum's swing plane is given by:
\[
\Omega_p = \Omega_E \sin \lambda.
\]
This is because the pendulum's angular momentum vector \(\vec{L}\) is aligned with the swing plane's normal (which is horizontal), and the torque due to Earth's rotation is proportional to \(\vec{\Omega}_E \times \vec{L}\), which results in a precession rate equal to the vertical component of \(\vec{\Omega}_E\).

##### Step 4: Physical Interpretation
The \(\sin \lambda\) factor arises because the effective rotation rate that affects the pendulum's swing plane is the component of Earth's rotation that is perpendicular to the local vertical. At the equator (\(\lambda = 0\)), \(\sin \lambda = 0\), so there is no precession (the swing plane does not rotate). At the pole (\(\lambda = 90^\circ\)), \(\sin \lambda = 1\), so the precession rate is equal to Earth's rotation rate (\(15^\circ/\text{hour}\)).

#### 2. Evaluation of the Precession Rate
Given:
- \(\lambda = 48.85^\circ\) N,
- \(\Omega_E = 15^\circ/\text{hour}\).

The precession rate is:
\[
\Omega_p = \Omega_E \sin \lambda = 15^\circ/\text{hour} \cdot \sin(48.85^\circ).
\]

First, calculate \(\sin(48.85^\circ)\):
\[
\sin(48.85^\circ) \approx 0.7547.
\]

Now compute \(\Omega_p\):
\[
\Omega_p = 15 \cdot 0.7547 \approx 11.32^\circ/\text{hour}.
\]

For the precession rate in degrees per day:
\[
\Omega_p \text{ (deg/day)} = 11.32^\circ/\text{hour} \cdot 24 \text{ hours/day} \approx 271.68^\circ/\text{day}.
\]

#### 3. Evaluation of the Full-Turn Period
The full-turn period \(T\) is the time it takes for the swing plane to complete one full rotation (\(360^\circ\)). This is the inverse of the precession rate:
\[
T = \frac{360^\circ}{\Omega_p} = \frac{360^\circ}{11.32^\circ/\text{hour}} \approx 31.8 \text{ hours}.
\]

Alternatively, using the formula \(T = \frac{24 \text{ hours}}{\sin \lambda}\):
\[
T = \frac{24}{0.7547} \approx 31.8 \text{ hours}.
\]

#### 4. Behavior at the Equator and at the Pole
- **At the equator (\(\lambda = 0^\circ\))**:
  \(\sin \lambda = 0\), so \(\Omega_p = 0\). The swing plane does not precess; it remains fixed relative to the Earth's surface.

- **At the pole (\(\lambda = 90^\circ\))**:
  \(\sin \lambda = 1\), so \(\Omega_p = 15^\circ/\text{hour}\). The swing plane precesses at the same rate as Earth's rotation, completing a full rotation every 24 hours.

#### Student's Mistake: Using \(\cos \lambda\)
A student using \(\cos \lambda\) would be considering the horizontal component of \(\vec{\Omega}_E\) (the component parallel to the Earth's surface). This is incorrect for determining the precession rate of the swing plane because:
- The precession of the swing plane is driven by the component of Earth's angular velocity that is perpendicular to the local vertical (i.e., the vertical component \(\Omega_E \sin \lambda\)).
- The horizontal component \(\Omega_E \cos \lambda\) affects the direction of the pendulum's motion but does not directly cause the precession of the swing plane. The horizontal component would be relevant if considering the deflection of the pendulum's path due to the Coriolis force, but not for the rotation of the swing plane itself.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day} &= 271.68 \\
\mathrm{rate\_deg\_per\_hour} &= 11.32 \\
\mathrm{period\_hours} &= 31.8
\end{aligned}
\]