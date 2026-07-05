**Derivation of the \(\sin\lambda\) factor**

1. **Earth’s angular velocity vector**  
   The Earth rotates about its axis with angular velocity \(\vec{\Omega}_E\). Its magnitude is  
   \[
   |\vec{\Omega}_E| = \frac{2\pi}{T_{\text{sidereal}}}\approx\frac{360^\circ}{23\text{ h }56\text{ min}}\approx\frac{360^\circ}{24\text{ h}}=15^\circ/\text{h}
   \]
   (the problem asks us to use the 24‑h approximation).

2. **Local vertical direction**  
   At a latitude \(\lambda\) the local vertical \(\hat{k}\) makes an angle \(\lambda\) with the Earth’s rotation axis. Hence the component of \(\vec{\Omega}_E\) along the local vertical is  
   \[
   \Omega_{\text{vert}} = \vec{\Omega}_E \cdot \hat{k} = |\vec{\Omega}_E|\cos\lambda .
   \]

3. **Coriolis effect on a swinging pendulum**  
   The pendulum’s plane of oscillation experiences a Coriolis acceleration due to the Earth’s rotation. The effective “tilt” of the inertial frame relative to the pendulum’s plane is proportional to the component of \(\vec{\Omega}_E\) **perpendicular** to the pendulum’s plane. For a pendulum swinging in a plane that is initially horizontal, the relevant component is the projection of \(\vec{\Omega}_E\) onto the horizontal plane, which is  
   \[
   \Omega_{\text{horiz}} = \vec{\Omega}_E \times \hat{k} \quad\Rightarrow\quad |\Omega_{\text{horiz}}| = |\vec{\Omega}_E|\sin\lambda .
   \]
   This \(\sin\lambda\) factor appears because the horizontal component of \(\vec{\Omega}_E\) is the part that tilts the pendulum’s plane.

4. **Precession rate of the swing plane**  
   The rate at which the plane precesses about the vertical axis is therefore  
   \[
   \Omega_{\text{precession}} = \Omega_{\text{horiz}} = |\vec{\Omega}_E|\sin\lambda .
   \]
   Using \(|\vec{\Omega}_E| = 15^\circ/\text{h}\), we have  
   \[
   \Omega_{\text{precession}} = 15^\circ/\text{h}\,\sin\lambda .
   \]

---

**Numerical evaluation for Paris (\(\lambda = 48.85^\circ\))**

1. **Compute \(\sin\lambda\)**  
   \[
   \sin(48.85^\circ) \approx 0.7547 .
   \]

2. **Precession rate in degrees per hour**  
   \[
   \text{rate\_deg\_per\_hour} = 15^\circ/\text{h} \times 0.7547 \approx 11.32^\circ/\text{h}.
   \]

3. **Precession rate in degrees per day**  
   \[
   \text{rate\_deg\_per\_day} = 11.32^\circ/\text{h} \times 24\ \text{h} \approx 271.7^\circ/\text{day}.
   \]

4. **Full‑turn period (time for the plane to complete one full rotation)**  
   The plane rotates at \(11.32^\circ\) per hour, so the time for \(360^\circ\) is  
   \[
   \text{period\_hours} = \frac{360^\circ}{11.32^\circ/\text{h}} \approx 31.8\ \text{h}.
   \]
   Using the exact formula \(\text{period\_hours}= \frac{24}{\sin\lambda}\):  
   \[
   \frac{24}{0.7547} \approx 31.8\ \text{h}.
   \]

---

**Behavior at the equator and the pole**

- **At the equator (\(\lambda = 0^\circ\))**:  
  \[
  \sin(0^\circ) = 0 \quad\Rightarrow\quad \Omega_{\text{precession}} = 0.
  \]
  The pendulum’s swing plane does **not** precess; it remains fixed relative to the local vertical.

- **At the pole (\(\lambda = 90^\circ\))**:  
  \[
  \sin(90^\circ) = 1 \quad\Rightarrow\quad \Omega_{\text{precession}} = |\vec{\Omega}_E| = 15^\circ/\text{h}.
  \]
  The plane precesses once every 24 h, i.e., it rotates exactly with the Earth’s rotation.

---

**Student’s mistake with \(\cos\lambda\)**

A student who uses \(\cos\lambda\) is actually taking the **vertical component** of Earth’s angular velocity:
\[
\Omega_{\text{vert}} = |\vec{\Omega}_E|\cos\lambda .
\]
This component is parallel to the local vertical and does **not** cause a tilt of the pendulum’s plane; it merely describes how fast the Earth’s axis itself rotates relative to the vertical. The precession of the pendulum’s swing plane is driven by the **horizontal component** of \(\vec{\Omega}_E\), which is proportional to \(\sin\lambda\). Hence \(\cos\lambda\) is the wrong factor for plane precession.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day} &= 271.7 \\
\mathrm{rate\_deg\_per\_hour} &= 11.32 \\
\mathrm{period\_hours} &= 31.8
\end{aligned}
\]