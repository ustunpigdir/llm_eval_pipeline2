To analyze the stability and apsidal angles for a particle in a central force field $F(r) = -k r^n$, we use the provided formula for the apsidal angle $\Phi$ for nearly circular orbits:
$$ \Phi = \frac{\pi}{\sqrt{3+n}} $$
We convert this to degrees using $\pi \text{ rad} = 180^\circ$:
$$ \Phi = \frac{180^\circ}{\sqrt{3+n}} $$

### 1. Verification for Closed-Orbit Cases ($n = -2$ and $n = +1$)

**Case $n = -2$ (Kepler Problem):**
Substitute $n = -2$ into the formula:
$$ \Phi = \frac{180^\circ}{\sqrt{3 + (-2)}} = \frac{180^\circ}{\sqrt{1}} = 180^\circ $$
For a closed orbit, the particle must return to the perihelion after a full radial period. The angle swept in one radial period is $2\Phi$.
$$ 2\Phi = 2 \times 180^\circ = 360^\circ $$
Since $2\Phi$ is a rational multiple of $360^\circ$ (specifically $1$), the orbit is closed (elliptical).

**Case $n = +1$ (Harmonic Oscillator):**
Substitute $n = +1$ into the formula:
$$ \Phi = \frac{180^\circ}{\sqrt{3 + 1}} = \frac{180^\circ}{\sqrt{4}} = \frac{180^\circ}{2} = 90^\circ $$
The angle swept in one radial period is:
$$ 2\Phi = 2 \times 90^\circ = 180^\circ $$
Since $2\Phi$ is a rational multiple of $360^\circ$ (specifically $1/2$), the orbit is closed (elliptical, centered at the origin).

### 2. Evaluation for $n = -1$

Substitute $n = -1$ into the formula:
$$ \Phi = \frac{180^\circ}{\sqrt{3 + (-1)}} = \frac{180^\circ}{\sqrt{2}} $$
Calculating the numerical value:
$$ \Phi \approx \frac{180^\circ}{1.41421356} \approx 127.28^\circ $$
Exact form: $90\sqrt{2}^\circ$.

### 3. Orbit Closure and Precession for $n = -1$

**Is the orbit closed?**
An orbit is closed if the ratio of the apsidal angle to $\pi$ (or the radial period angle to $2\pi$) is rational.
$$ \frac{2\Phi}{360^\circ} = \frac{2 \times 127.28^\circ}{360^\circ} = \frac{180\sqrt{2}^\circ}{360^\circ} = \frac{1}{\sqrt{2}} $$
Since $\frac{1}{\sqrt{2}}$ is irrational, the orbit is **not closed**. The particle will not return to the exact same position in phase space after a finite number of radial periods.

**Apsidal Precession per Radial Period:**
The precession is defined in the prompt as $2\Phi - 360^\circ$.
$$ 2\Phi = 2 \times 127.28^\circ = 254.56^\circ $$
$$ \text{Precession} = 254.56^\circ - 360^\circ = -105.44^\circ $$
The negative sign indicates a retrograde precession (the perihelion lags behind).

### 4. Bertrand's Theorem and $n \le -3$

**Bertrand's Theorem:**
Bertrand's theorem states that the only central force laws $F(r)$ for which **all** bounded orbits are closed are the inverse-square law ($F \propto -1/r^2$, i.e., $n = -2$) and the isotropic harmonic oscillator ($F \propto -r$, i.e., $n = +1$).

**Illustration:**
Our results confirm this theorem. For $n = -2$ and $n = +1$, the apsidal angle $\Phi$ is a rational multiple of $\pi$ ($\pi$ and $\pi/2$), ensuring that $2\Phi$ is a rational multiple of $2\pi$, which guarantees closed orbits. For $n = -1$, $\Phi = \pi/\sqrt{2}$, which is not a rational multiple of $\pi$, resulting in a non-closed, precessing orbit.

**What goes wrong for $n \le -3$?**
The formula for the apsidal angle involves the term $\sqrt{3+n}$.
- If $n = -3$, the denominator becomes $\sqrt{0} = 0$, making $\Phi$ undefined (infinite).
- If $n < -3$, the term $3+n$ is negative, making $\Phi$ imaginary.
Physically, this corresponds to the effective potential $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} + \frac{k}{n+1}r^{n+1}$. For $n \le -3$, the centrifugal barrier ($\propto 1/r^2$) cannot balance the attractive force ($\propto 1/r^{|n|}$ or stronger) to form a stable minimum in the effective potential. Consequently, stable circular orbits do not exist for $n \le -3$, and the concept of an apsidal angle for a stable circular orbit is invalid.

### Final Values
- $n = -2$: $\Phi = 180^\circ$
- $n = +1$: $\Phi = 90^\circ$
- $n = -1$: $\Phi \approx 127.28^\circ$
- Precession ($n = -1$): $\approx -105.44^\circ$

FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180^\circ \\
\mathrm{apsidal\_harmonic\_deg} &= 90^\circ \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28^\circ \\
\mathrm{precession\_per\_period\_deg} &= -105.44^\circ
\end{aligned}
\]