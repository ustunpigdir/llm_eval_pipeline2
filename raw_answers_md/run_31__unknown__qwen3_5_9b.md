To analyze the stability and apsidal angles for a particle in a central force field $F(r) = -k r^n$, we begin by deriving the apsidal angle formula for nearly circular orbits.

### Derivation of the Apsidal Angle Formula

1.  **Effective Potential:**
    The motion of a particle of mass $m$ with angular momentum $L$ in a central potential $V(r)$ is governed by the effective potential:
    $$ V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + V(r) $$
    Given the force $F(r) = -k r^n$, the potential is $V(r) = \frac{k}{n+1} r^{n+1}$ (assuming $n \neq -1$).
    $$ V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + \frac{k}{n+1} r^{n+1} $$

2.  **Circular Orbit Condition:**
    A circular orbit exists at radius $r_0$ where the effective force is zero:
    $$ \frac{dV_{\text{eff}}}{dr}\bigg|_{r_0} = -\frac{L^2}{mr_0^3} + k r_0^n = 0 \implies \frac{L^2}{m} = k r_0^{n+3} $$

3.  **Stability and Frequencies:**
    For a nearly circular orbit, we consider small radial oscillations around $r_0$. The frequency of radial oscillation $\omega_r$ is determined by the curvature of the effective potential:
    $$ \omega_r^2 = \frac{1}{m} \frac{d^2V_{\text{eff}}}{dr^2}\bigg|_{r_0} $$
    Calculating the second derivative:
    $$ \frac{d^2V_{\text{eff}}}{dr^2} = \frac{3L^2}{mr^4} + k n r^{n-1} $$
    Substituting $L^2/m = k r_0^{n+3}$:
    $$ \frac{d^2V_{\text{eff}}}{dr^2}\bigg|_{r_0} = \frac{3 k r_0^{n+3}}{r_0^4} + k n r_0^{n-1} = k r_0^{n-1} (3 + n) $$
    Thus, $\omega_r^2 = \frac{k}{m} r_0^{n-1} (3 + n)$.

    The angular frequency $\omega_\theta$ for the circular orbit is:
    $$ \omega_\theta = \frac{L}{m r_0^2} = \sqrt{\frac{k r_0^{n+3}}{m r_0^4}} = \sqrt{\frac{k}{m} r_0^{n-1}} $$
    Thus, $\omega_\theta^2 = \frac{k}{m} r_0^{n-1}$.

4.  **Apsidal Angle:**
    The ratio of the frequencies is:
    $$ \frac{\omega_r^2}{\omega_\theta^2} = 3 + n \implies \frac{\omega_r}{\omega_\theta} = \sqrt{3 + n} $$
    The angle swept during one full radial period (from perihelion to perihelion) is $\Delta \theta = 2\pi \frac{\omega_\theta}{\omega_r}$.
    The apsidal angle $\Phi$ is defined in the problem as the angle between successive perihelion and aphelion, which is half the radial period:
    $$ \Phi = \pi \frac{\omega_\theta}{\omega_r} = \frac{\pi}{\sqrt{3 + n}} $$

---

### Task 1: Verify for Closed-Orbit Cases

**Case 1: Kepler Problem ($n = -2$)**
Substitute $n = -2$ into the formula:
$$ \Phi = \frac{\pi}{\sqrt{3 + (-2)}} = \frac{\pi}{\sqrt{1}} = \pi \text{ radians} $$
Convert to degrees:
$$ \Phi = 180^\circ $$
This corresponds to a full orbit ($2\Phi = 360^\circ$), which is closed.

**Case 2: Harmonic Oscillator ($n = +1$)**
Substitute $n = +1$ into the formula:
$$ \Phi = \frac{\pi}{\sqrt{3 + 1}} = \frac{\pi}{\sqrt{4}} = \frac{\pi}{2} \text{ radians} $$
Convert to degrees:
$$ \Phi = 90^\circ $$
This corresponds to a full orbit ($2\Phi = 180^\circ$), which is closed (Lissajous figure with 1:1 ratio in 2D).

---

### Task 2: Evaluate for $n = -1$

Substitute $n = -1$ into the formula:
$$ \Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians} $$
Convert to degrees:
$$ \Phi = \frac{180^\circ}{\sqrt{2}} = 90\sqrt{2}^\circ \approx 127.28^\circ $$

---

### Task 3: Closed Orbit and Precession for $n = -1$

**Is the orbit closed?**
An orbit is closed if the angle swept during one radial period ($2\Phi$) is a rational multiple of $360^\circ$.
$$ 2\Phi = 2 \times 127.28^\circ = 254.56^\circ $$
The ratio is:
$$ \frac{2\Phi}{360^\circ} = \frac{2\pi/\sqrt{2}}{2\pi} = \frac{1}{\sqrt{2}} $$
Since $\sqrt{2}$ is irrational, the ratio is irrational. Therefore, the orbit is **not closed**. The particle will not return to the same position in phase space after a finite number of radial periods.

**Apsidal Precession per Radial Period:**
The precession is defined as the deviation from a full $360^\circ$ circle per radial period.
$$ \text{Precession} = 2\Phi - 360^\circ $$
$$ \text{Precession} = 254.56^\circ - 360^\circ = -105.44^\circ $$
The negative sign indicates a retrograde precession (the perihelion shifts backwards relative to the direction of motion).

---

### Task 4: Bertrand's Theorem and $n \le -3$

**Bertrand