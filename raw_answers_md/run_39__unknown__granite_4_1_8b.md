**Derivation of the \(\sin\lambda\) factor**

1. **Earth’s angular velocity vector**  
   The Earth rotates with angular velocity \(\vec{\Omega}_E\) about its axis. Its magnitude is  
   \[
   |\vec{\Omega}_E| = \frac{2\pi}{T_{\text{sidereal}}}\approx\frac{360^\circ}{24\;\text{h}} = 15^\circ/\text{h}.
   \]  
   In a local inertial frame at latitude \(\lambda\), the vertical component of \(\vec{\Omega}_E\) is obtained by projecting \(\vec{\Omega}_E\) onto the local vertical direction \(\hat{z}\):
   \[
   \Omega_{E,z} = \vec{\Omega}_E \cdot \hat{z} = |\vec{\Omega}_E|\cos\lambda .
   \]
   However, the **horizontal** component of \(\vec{\Omega}_E\) that acts perpendicular to the pendulum’s plane is what drives the precession. This horizontal component is obtained by projecting \(\vec{\Omega}_E\) onto the horizontal plane:
   \[
   \Omega_{E,\text{horiz}} = \vec{\Omega}_E \times \hat{z} \quad \Rightarrow \quad |\Omega_{E,\text{horiz}}| = |\vec{\Omega}_E|\sin\lambda .
   \]
   The factor \(\sin\lambda\) appears because the component of \(\vec{\Omega}_E\) that is **parallel to the local horizontal** (and thus perpendicular to the pendulum’s swing plane) is reduced by the cosine of the latitude when viewed from the vertical, leaving \(\sin\lambda\).

2. **Precession rate of the swing plane**  
   The Coriolis force on the pendulum’s motion introduces a torque that causes the plane of oscillation to rotate with angular velocity
   \[
   \Omega_{\text{precession}} = \Omega_{E,\text{horiz}} = \Omega_E \sin\lambda .
   \]
   Substituting \(\Omega_E = 15^\circ/\text{h}\) gives
   \[
   \Omega_{\text{precession}} = 15^\circ/\text{h}\,\sin\lambda .
   \]

**Evaluation for Paris (\(\lambda = 48.85^\circ\))**

- Compute \(\sin(48.85^\circ)\):
  \[
  \sin(48.85^\circ) \approx 0.7547 .
  \]

- **Precession rate in degrees per hour**:
  \[
  \text{rate\_deg\_per\_hour} = 15^\circ/\text{h} \times 0.7547 \approx 11.32^\circ/\text{h}.
  \]

- **Precession rate in degrees per day** (24 h):
  \[
  \text{rate\_deg\_per\_day} = 11.32^\circ/\text{h} \times 24\;\text{h} \approx 271.7^\circ/\text{day}.
  \]

- **Full‑turn period** (time for the plane to complete one full \(360^\circ\) rotation):
  \[
  \text{period\_hours} = \frac{360^\circ}{\text{rate\_deg\_per\_hour}} = \frac{360^\circ}{15^\circ/\text{h}\,\sin\lambda}
  = \frac{24\;\text{h}}{\sin\lambda}
  \approx \frac{24}{0.7547} \approx 31.8\;\text{h}.
  \]

**Behavior at the equator and the pole**

- **At the equator (\(\lambda = 0^\circ\))**:  
  \[
  \sin(0^\circ) = 0 \quad \Rightarrow \quad \Omega_{\text{precession}} = 0.
  \]  
  The pendulum’s swing plane does **not precess**; it remains fixed relative to the Earth’s surface.

- **At the pole (\(\lambda = 90^\circ\))**:  
  \[
  \sin(90^\circ) = 1 \quad \Rightarrow \quad \Omega_{\text{precession}} = \Omega_E = 15^\circ/\text{h}.
  \]  
  The plane precesses **once per sidereal day**, i.e., it completes a full rotation in 24 h.

**Student’s mistake with \(\cos\lambda\)**

A student who uses \(\cos\lambda\) instead of \(\sin\lambda\) is actually taking the **vertical component** of Earth’s angular velocity:
\[
\Omega_{E,z} = \Omega_E \cos\lambda .
\]
This component influences the direction of the Coriolis force **along the vertical axis**, affecting the pendulum’s amplitude or the direction of the force, but **does not produce a horizontal torque** that would cause the plane of oscillation to rotate. The precession of the swing plane arises from the **horizontal component** of the Coriolis effect, which is proportional to \(\sin\lambda\). Hence, \(\cos\lambda\) is the wrong factor for plane precession.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day} &= 271.7 \\
\mathrm{rate\_deg\_per\_hour} &= 11.32 \\
\mathrm{period\_hours} &= 31.8
\end{aligned}
\]