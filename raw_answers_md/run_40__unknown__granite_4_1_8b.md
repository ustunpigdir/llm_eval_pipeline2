**Derivation of the \(\sin\lambda\) factor**

1. **Earth’s angular velocity vector**  
   The Earth rotates about its axis with angular velocity \(\vec{\Omega}_E\). Its magnitude is  
   \[
   |\vec{\Omega}_E| = \frac{2\pi}{T_{\text{sidereal}}}\approx\frac{360^\circ}{24\;\text{h}} = 15^\circ/\text{h}.
   \]  
   In a local inertial frame at latitude \(\lambda\), the vertical component of \(\vec{\Omega}_E\) is obtained by projecting \(\vec{\Omega}_E\) onto the local vertical direction \(\hat{z}\):
   \[
   \Omega_{E,z} = \vec{\Omega}_E \cdot \hat{z} = |\vec{\Omega}_E|\cos\lambda .
   \]
   However, the **horizontal** component of \(\vec{\Omega}_E\) that acts perpendicular to the pendulum’s swing plane is what drives the precession. This horizontal component is obtained by projecting \(\vec{\Omega}_E\) onto the horizontal plane:
   \[
   \Omega_{E,\text{horiz}} = \vec{\Omega}_E \times \hat{z} \quad\text{(magnitude)} = |\vec{\Omega}_E|\sin\lambda .
   \]
   The factor \(\sin\lambda\) appears because the component of \(\vec{\Omega}_E\) that is **parallel to the local horizontal** (and thus perpendicular to the pendulum’s plane) is reduced by the cosine of the latitude when viewed from the vertical, leaving \(\sin\lambda\).

2. **Precession rate of the swing plane**  
   The Coriolis force on the pendulum’s motion introduces a torque that causes the plane of oscillation to rotate with angular velocity
   \[
   \Omega_{\text{precession}} = \Omega_{E,\text{horiz}} = \Omega_E \sin\lambda .
   \]
   Substituting \(\Omega_E = 15^\circ/\text{h}\) gives the precession rate in degrees per hour.

**Evaluation for Paris (\(\lambda = 48.85^\circ\) N)**  

- Compute \(\sin\lambda\):
  \[
  \sin(48.85^\circ) \approx 0.7547 .
  \]

- **Precession rate in degrees per hour**:
  \[
  \text{rate}_{\deg/\text{h}} = 15^\circ/\text{h} \times \sin(48.85^\circ) \approx 15 \times 0.7547 \approx 11.32^\circ/\text{h}.
  \]

- **Precession rate in degrees per day** (24 h):
  \[
  \text{rate}_{\deg/\text{day}} = 11.32^\circ/\text{h} \times 24 \approx 271.7^\circ/\text{day}.
  \]

- **Full‑turn period** (time for the plane to complete one full \(360^\circ\) rotation):
  \[
  \text{period}_{\text{hours}} = \frac{360^\circ}{\text{rate}_{\deg/\text{h}}} = \frac{360}{11.32} \approx 31.8\;\text{h}.
  \]
  Alternatively, using the formula \(\text{period}_{\text{hours}} = \frac{24}{\sin\lambda}\):
  \[
  \frac{24}{0.7547} \approx 31.8\;\text{h}.
  \]

**Behavior at the equator and the pole**

- **At the equator (\(\lambda = 0^\circ\))**:  
  \[
  \sin(0^\circ) = 0 \quad\Rightarrow\quad \Omega_{\text{precession}} = 0.
  \]  
  The pendulum’s swing plane does **not precess**; it remains fixed relative to the Earth’s surface.

- **At the pole (\(\lambda = 90^\circ\))**:  
  \[
  \sin(90^\circ) = 1 \quad\Rightarrow\quad \Omega_{\text{precession}} = \Omega_E = 15^\circ/\text{h}.
  \]  
  The plane precesses **once per sidereal day**, i.e., it completes a full rotation in 24 h.

**Student’s mistake with \(\cos\lambda\)**  

A student who uses \(\cos\lambda\) instead of \(\sin\lambda\) is actually taking the **vertical component** of Earth’s angular velocity:
\[
\Omega_{E,z} = \Omega_E \cos\lambda .
\]
This component is **parallel to the local vertical** and does not affect the horizontal plane of the pendulum; it would incorrectly suggest a reduction of precession that is not present. The correct horizontal component, which drives the precession, is \(\Omega_E \sin\lambda\). Hence, \(\cos\lambda\) corresponds to the wrong physical direction for the precession of the swing plane.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day} &= 271.7 \\
\mathrm{rate\_deg\_per\_hour} &= 11.32 \\
\mathrm{period\_hours} &= 31.8
\end{aligned}
\]