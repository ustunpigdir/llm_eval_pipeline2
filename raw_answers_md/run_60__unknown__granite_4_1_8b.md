**1. Effective‑potential derivation**

Consider a pendulum of length \(L\) and mass \(m\) whose pivot is driven vertically as  
\[
y_{\text{pivot}}(t)=a\cos(\omega t),\qquad a\ll L,\;\;\omega\gg\sqrt{g/L}.
\]

The generalized coordinate is the angle \(\theta(t)\) measured from the downward vertical.  
The Lagrangian (ignoring the small kinetic energy of the pivot) is  

\[
L = T - V = \frac12 m L^{2}\dot\theta^{2}
      - m g\bigl(L - a\cos(\omega t)\bigr)\cos\theta .
\]

Expanding the potential to first order in the small amplitude \(a\),

\[
V = -m g L\cos\theta + m g a\cos(\omega t)\cos\theta .
\]

The first term \(-m g L\cos\theta\) is the usual pendulum potential (minimum at \(\theta=0\), maximum at \(\theta=\pi\) – the inverted position).  
The second term is a fast, periodic modulation of the potential:

\[
V_{\text{mod}}(t,\theta)= m g a\cos(\omega t)\cos\theta .
\]

**Separation of time scales**

Because \(\omega\gg\dot\theta\) (the slow motion of the pendulum), we write \(\theta(t)=\Theta(t)+\theta'(t)\) with \(\Theta(t)\) slowly varying and \(\theta'(t)\) a rapid oscillation of order \(a/L\).  
Insert into the Lagrangian and keep only terms that vary on the slow time scale. The rapid part \(\theta'\) satisfies the equation of a simple harmonic oscillator and averages to zero over one drive period.  

**Averaging over the fast oscillation**

The average of \(\cos(\omega t)\) over a full period is zero, but the product \(\cos(\omega t)\cos\theta\) averaged over the fast motion yields a contribution that depends on the slow variable \(\Theta\).  Using the identity  

\[
\langle \cos(\omega t)\cos\theta\rangle_{t}
   = \frac{1}{T}\int_{0}^{T}\cos(\omega t)\cos\theta\,dt
   = \frac{1}{2}\cos\theta,
\]

(where the average is taken over the fast oscillation while \(\theta\) is held fixed), the effective potential for the slow coordinate \(\Theta\) becomes  

\[
V_{\text{eff}}(\Theta)= -m g L\cos\Theta
                       + \frac{1}{2} m g a^{2}\cos^{2}\Theta .
\]

**Stability analysis**

Expand \(\cos\Theta\) about the inverted equilibrium \(\Theta=\pi\) (write \(\Granite = \pi-\Theta\), so \(\cos\Theta = -\cos\Granite\)). For small \(\Granite\),

\[
\cos\Theta \approx -\bigl(1-\tfrac{\Granite^{2}}{2}\bigr),\qquad
\cos^{2}\Theta \approx 1-\Granite^{2}+\tfrac{\Granite^{4}}{4}.
\]

Substituting,

\[
V_{\text{eff}} \approx -m g L\bigl(-1+\tfrac{\Granite^{2}}{2}\bigr)
                     + \frac{1}{2} m g a^{2}\bigl(1-\Granite^{2}\bigr)
               = m g L + \frac{1}{2} m g\bigl(a^{2}-L\bigr)\Granite^{2} + \cdots .
\]

The coefficient of \(\Granite^{2}\) determines stability:

\[
\frac{d^{2}V_{\text{eff}}}{d\Granite^{2}}\Big|_{\Granite=0}
   = m g\bigl(a^{2}-L\bigr).
\]

A minimum (stable inverted position) requires this second derivative to be **positive**, i.e.

\[
a^{2} - L > 0 \quad\Longrightarrow\quad a^{2}\omega^{2} > 2 g L .
\]

The factor \(2\) appears because the averaging of the fast inertial term yields an effective “spring constant’’ proportional to \(a^{2}\omega^{2}\) that must overcome the gravitational restoring term \(g L\).  

Thus the **stability criterion** for the inverted pendulum is  

\[
\boxed{a^{2}\omega^{2} > 2 g L } .
\]

---

**2. Minimum angular frequency \(\omega_{\min}\)**  

Set the inequality to equality to find the threshold:

\[
a^{2}\omega_{\min}^{2}=2 g L
\quad\Longrightarrow\quad
\omega_{\min}= \sqrt{\frac{2 g L}{a^{2}}}.
\]

Insert the given numbers:

\[
g = 9.81\;\text{m/s}^{2},\qquad
L = 0.200\;\text{m},\qquad
a = 0.0200\;\text{m}.
\]

\[
\omega_{\min}= \sqrt{\frac{2 \times 9.81 \times 0.200}{(0.0200)^{2}}}
               = \sqrt{\frac{3.924}{0.0004}}
               = \sqrt{9810}
               \approx 99.05\;\text{rad/s}.
\]

---

**3. Corresponding drive frequency \(f_{\min}\)**  

The drive frequency in hertz is related to the angular frequency by \(f = \omega/(2\pi)\):

\[
f_{\min}= \frac{\omega_{\min}}{2\pi}
        = \frac{99.05}{2\pi}
        \approx \frac{99.05}{6.2832}
        \approx 15.77\;\text{Hz}.
\]

---

**4. Physical origin of the stabilizing force**

The stabilizing “force’’ originates from the **average of the fast inertial (centrifugal) force** that the pendulum experiences as the pivot oscillates.  

- As the pivot moves upward (\(y_{\text{pivot}} = a\)), the pendulum bob feels an upward inertial force \(m\omega^{2}a\cos(\omega t)\).  
- When the pivot moves downward (\(y_{\text{pivot}} = -a\)), the bob feels a downward inertial force of equal magnitude.  

Although each instantaneous inertial force is opposite to gravity at the inverted angle, the **time‑averaged** effect of this periodic force is a **static‑like restoring force** that points toward the inverted equilibrium.  

Mathematically, the averaging yields an extra term \(\tfrac{1}{2} m g a^{2}\cos^{2}\theta\) in the effective potential, which acts like a harmonic potential with curvature proportional to \(a^{2}\omega^{2}\).  

**Why static intuition fails:**  
In a static picture, an inverted pendulum is unstable because any small displacement increases the gravitational potential energy. The static picture ignores the **dynamic (parametric) modulation** of the effective potential. The rapid vertical motion of the pivot continuously “pushes” the bob back toward the inverted position, providing a stabilizing influence that cannot be captured by a simple static energy diagram. Hence, intuition based solely on static equilibrium (which would predict instability) is incomplete; the parametric driving supplies the necessary restoring “force” on the slow time scale.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.05 \\
\mathrm{f\_min\_hz} &= 15.77
\end{aligned}
\]