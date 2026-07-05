The apsidal angle for a nearly‑circular orbit under a central force \(F(r)=-k\,r^{n}\) is  

\[
\Phi=\frac{\pi}{\sqrt{3+n}}\qquad\text{(radians)} .
\]

To express \(\Phi\) in degrees we multiply by \(\frac{180}{\pi}\).

---

### 1.  Closed‑orbit cases  

**\(n=-2\) (Kepler, inverse‑square)**  

\[
3+n = 3-2 = 1,\qquad \sqrt{3+n}=1,
\]
\[
\Phi = \frac{\pi}{1}= \pi\ \text{rad}.
\]
\[
\Phi_{\text{deg}} = \pi\cdot\frac{180}{\pi}=180^{\circ}.
\]

**\(n=+1\) (harmonic oscillator)**  

\[
3+n = 4,\qquad \sqrt{3+n}=2,
\]
\[
\Phi = \frac{\pi}{2}\ \text{rad},
\]
\[
\Phi_{\text{deg}} = \frac{\pi}{2}\cdot\frac{180}{\pi}=90^{\circ}.
\]

---

### 2.  Case \(n=-1\) (force \(\propto 1/r\))

\[
3+n = 2,\qquad \sqrt{3+n}= \sqrt{2},
\]
\[
\Phi = \frac{\pi}{\sqrt{2}}\ \text{rad},
\]
\[
\Phi_{\text{deg}} = \frac{\pi}{\sqrt{2}}\cdot\frac{180}{\pi}= \frac{180}{\sqrt{2}} = 90\sqrt{2}\approx127.28^{\circ}.
\]

---

### 3.  Closed‑orbit test and precession for \(n=-1\)

A closed orbit requires \(2\Phi = 360^{\circ}\).  
Here  

\[
2\Phi = 2\left(\frac{\pi}{\sqrt{2}}\right)=\frac{2\pi}{\sqrt{2}}=\sqrt{2}\,\pi\ \text{rad},
\]
\[
2\Phi_{\text{deg}} = 2\cdot\frac{180}{\sqrt{2}} = \frac{360}{\sqrt{2}} = 180\sqrt{2}\approx254.56^{\circ}\neq360^{\circ}.
\]

Thus the orbit is **not closed**.  
The apsidal precession per radial period is defined as  

\[
\Delta = 2\Phi - 360^{\circ}
        = \frac{360}{\sqrt{2}} - 360
        = 180\sqrt{2} - 360
        \approx -105.44^{\circ}.
\]

The negative sign indicates a retrograde precession.

---

### 4.  Relation to Bertrand’s theorem  

**Bertrand’s theorem** states that the only central‑force laws for which *all* bounded orbits are closed are  

* the inverse‑square law (\(F\propto r^{-2}\), i.e. \(n=-2\)), and  
* Hooke’s law (\(F\propto r\), i.e. \(n=+1\)).

Our calculations confirm this:  

* For \(n=-2\) and \(n=+1\) the apsidal angle is a rational multiple of \(\pi\) (\(\pi\) and \(\pi/2\)), giving closed orbits (180° and 90°).  
* For \(n=-1\) the angle \(\pi/\sqrt{2}\) is an irrational multiple of \(\pi\); consequently \(2\Phi\neq360^{\circ}\) and the orbit precesses, with a precession of \(180\sqrt{2}-360^{\circ}\) per radial period.  

For exponents \(n\le -3\) the denominator \(\sqrt{3+n}\) becomes zero or imaginary, so the formula for \(\Phi\) ceases to be real. Physically this means that near‑circular orbits are not stable (the effective potential has no minimum), and the assumptions underlying the apsidal‑angle analysis break down.

---

FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 90\sqrt{2} \\
\mathrm{precession\_per\_period\_deg} &= 180\sqrt{2} - 360
\end{aligned}
\]