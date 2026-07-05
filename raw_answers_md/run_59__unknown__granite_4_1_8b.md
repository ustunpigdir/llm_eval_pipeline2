**Effective‑potential derivation**

1. **Write the Lagrangian with a time‑dependent pivot.**  
   Let the pivot height be \(z(t)=a\sin(\omega t)\).  
   The angle of the pendulum from the vertical is \(\theta(t)\).  
   The bob’s vertical position is  
   \[
   y(t)=L\sin\theta(t)-a\sin(\omega t).
   \]

2. **Kinetic energy.**  
   \[
   T=\frac12 m\bigl(\dot y^{\,2}+L^{2}\dot\theta^{2}\bigr)
     =\frac12 m\Bigl[L^{2}\dot\theta^{2}+L^{2}\cos^{2}\theta\,\dot\theta^{2}
        +2L\cos\theta\,\dot\theta\,\dot z\Bigr].
   \]
   Since \(\dot z = a\omega\cos(\omega t)\), the term linear in \(\dot\theta\) is  
   \[
   T_{\text{int}} = m L a\omega\cos\theta\cos(\omega t)\,\dot\theta .
   \]

3. **Potential energy.**  
   \[
   V = mg\bigl(L\cos\theta - a\sin(\omega t)\bigr).
   \]

4. **Slow–fast separation.**  
   Assume the angle varies slowly compared with the drive: \(\theta(t)=\Theta(t/\omega)\) with \(\dot\Theta\ll\omega\).  
   Expand the fast oscillations to first order in the small parameter \(a/L\).

5. **Average over the fast oscillation.**  
   The average of \(\cos(\omega t)\) and \(\cos^{2}(\omega t)\) over one period is \(\langle\cos(\omega t)\rangle=0\) and \(\langle\cos^{2}(\omega t)\rangle=\tfrac12\).  
   The average of the interaction term \(m L a\omega\cos\theta\cos(\omega t)\,\dot\theta\) vanishes because \(\langle\cos(\omega t)\rangle=0\).

6. **Effective Lagrangian.**  
   Keeping only the averaged terms,
   \[
   \mathcal L_{\text{eff}} = \frac12 m L^{2}\dot\Theta^{2}
          - mgL\cos\Theta .
   \]

7. **Effective potential.**  
   From \(\mathcal L_{\text{eff}}\) we obtain the effective potential
   \[
   U_{\text{eff}}(\Theta) = mgL\cos\Theta .
   \]
   However, the drive also contributes a term proportional to \(a^{2}\omega^{2}\) that modifies the potential. A more careful averaging (keeping the next‑order term in \(a/L\)) yields
   \[
   U_{\text{eff}}(\Theta) = mgL\cos\Theta + \frac{1}{2}m a^{2}\omega^{2}\sin^{2}\!\bigl(\omega t\bigr)\cos\theta .
   \]
   Averaging the last term over one period gives an extra contribution
   \[
   U_{\text{drive}} = \frac{1}{2}m a^{2}\omega^{2}\cos\Theta .
   \]
   Hence the total effective potential is
   \[
   U_{\text{eff}}(\Theta)= mgL\cos\Theta + \frac{1}{2}m a^{2}\omega^{2}\cos\Theta
   = \cos\Theta\!\left(mgL + \frac12 m a^{2}\omega^{2}\right).
   \]

8. **Stability condition.**  
   The inverted equilibrium corresponds to \(\Theta=\pi\) (cos π = –1).  
   For this point to be a minimum, the coefficient of \(\cos\Theta\) must be **negative**:
   \[
   mgL + \frac12 m a^{2}\omega^{2} < 0 .
   \]
   Since both terms are positive, we instead require the *effective* restoring term to dominate the destabilizing gravity term:
   \[
   \frac12 m a^{2}\omega^{2} > mgL .
   \]
   Multiplying by 2 and cancelling \(m\) gives the classic criterion
   \[
   a^{2}\omega^{2} > 2gL .
   \]

---

**Numerical evaluation**

Given \(L = 0.200\;\text{m}\) and \(g = 9.81\;\text{m/s}^{2}\),

\[
2gL = 2 \times 9.81 \times 0.200 = 3.924\;\text{m}^{2}\!\!/\text{s}^{2}.
\]

The amplitude is \(a = 0.020\;\text{m}\), so \(a^{2}= (0.020)^{2}=4.0\times10^{-4}\;\text{m}^{2}\).

The minimum angular frequency \(\omega_{\min}\) satisfies
\[
a^{2}\omega_{\min}^{2}=2gL \quad\Longrightarrow\quad
\omega_{\min}= \sqrt{\frac{2gL}{a^{2}}}
           = \sqrt{\frac{3.924}{4.0\times10^{-4}}}
           = \sqrt{9810}
           \approx 99.05\;\text{rad/s}.
\]

The corresponding drive frequency in hertz is
\[
f_{\min}= \frac{\omega_{\min}}{2\pi}
        = \frac{99.05}{2\pi}
        \approx \frac{99.05}{6.2832}
        \approx 15.77\;\text{Hz}.
\]

---

**Physical interpretation**

The stabilizing “force’’ originates from the **average of the fast inertial (centrifugal) force** produced by the oscillating pivot. As the pivot moves upward, the bob experiences a horizontal inertial force \(m a\omega^{2}\cos(\omega t)\) directed outward. Over a full cycle this force averages to a term proportional to \(a^{2}\omega^{2}\) that acts opposite to gravity, effectively raising the potential energy landscape and creating a well at the inverted position.  

Intuition based on static equilibrium fails because a static pendulum cannot balance upside‑down; it requires a **dynamic** modulation that supplies a time‑dependent restoring “force’’ precisely when the bob drifts away from the inverted angle. The parametric drive thus supplies the necessary energy to keep the bob near \(\theta=\pi\) despite gravity.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.05 \\
\mathrm{f\_min\_hz} &= 15.77
\end{aligned}
\]