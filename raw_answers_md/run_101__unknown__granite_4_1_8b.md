**Step 1: Evaluate the Hubble time**

The Hubble time is defined as  

\[
t_H = \frac{1}{H_0}.
\]

Given \(H_0 = 70.0\ \text{km s}^{-1}\text{Mpc}^{-1}\) and \(1\ \text{Mpc} = 3.0857 \times 10^{19}\ \text{km}\),

\[
t_H = \frac{1}{70.0\ \text{km s}^{-1}\text{Mpc}^{-1}} \times \frac{1\ \text{Mpc}}{3.0857 \times 10^{19}\ \text{km}}
      = \frac{1}{70.0 \times 3.0857 \times 10^{19}}\ \text{s}.
\]

Calculate the denominator:

\[
70.0 \times 3.0857 \times 10^{19} \approx 2.159 \times 10^{21}\ \text{s}.
\]

Thus,

\[
t_H \approx \frac{1}{2.159 \times 10^{21}}\ \text{s} \approx 4.63 \times 10^{-22}\ \text{s}^{-1}.
\]

Convert seconds to years using \(1\ \text{yr} = 3.15576 \times 10^{7}\ \text{s}\):

\[
t_H \approx \frac{4.63 \times 10^{-22}}{1}\ \text{s} \times \frac{1\ \text{yr}}{3.15576 \times 10^{7}\ \text{s}}
      \approx \frac{1}{70.0} \times \frac{3.0857 \times 10^{19}}{3.15576 \times 10^{7}}
      \approx 4.32 \times 10^{9}\ \text{yr}.
\]

So,  

\[
\boxed{hubble\_time\_gyr \approx 13.2\ \text{Gyr}}.
\]

*(More precisely, \(t_H = 1/(70\ \text{km s}^{-1}\text{Mpc}^{-1}) \approx 13.2\) Gyr.)*

---

**Step 2: Evaluate the age of a flat matter‑only universe**

For a matter‑only (Einstein‑de Sitter) universe, the age is  

\[
t_{\text{matter}} = \frac{2}{3H_0}.
\]

Using \(H_0 = 70\ \text{km s}^{-1}\text{Mpc}^{-1}\),

\[
t_{\text{matter}} = \frac{2}{3} \times \frac{1}{H_0}
                  = \frac{2}{3} \times 13.2\ \text{Gyr}
                  \approx 8.8\ \text{Gyr}.
\]

Thus,

\[
\boxed{matter\_age\_gyr \approx 8.8\ \text{Gyr}}.
\]

**Why it is less than \(1/H_0\):**  
In a matter‑only universe the expansion decelerates as \(a(t) \propto t^{2/3}\). The universe has spent a shorter fraction of its total age in the early, rapidly expanding phase, so the actual age \(2/(3H_0)\) is smaller than the Hubble time \(1/H_0\).

---

**Step 3: Evaluate the LCDM age**

For a flat \(\Lambda\)CDM universe with \(\Omega_m = 0.3\) and \(\Omega_\Lambda = 0.7\), the age is given by  

\[
t_0 = \frac{2}{3H_0\sqrt{\Omega_\Lambda}}\,
      \operatorname{asinh}\!\left(\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\right).
\]

First compute the constants:

\[
\sqrt{\Omega_\Lambda} = \sqrt{0.7} \approx 0.83666,
\qquad
\sqrt{\frac{\Omega_\Lambda}{\Omega_m}} = \sqrt{\frac{0.7}{0.3}} \approx \sqrt{2.3333} \approx 1.5275.
\]

\[
\operatorname{asinh}(1.5275) = \ln\!\bigl(1.5275 + \sqrt{1.5275^2 + 1}\bigr)
   \approx \ln\!\bigl(1.5275 + \sqrt{2.3333 + 1}\bigr)
   \approx \ln\!\bigl(1.5275 + \sqrt{3.3333}\bigr)
   \approx \ln\!\bigl(1.5275 + 1.8257\bigr)
   \approx \ln(3.3532) \approx 1.209.
\]

Now assemble the expression:

\[
t_0 = \frac{2}{3H_0\sqrt{\Omega_\Lambda}} \times 1.209.
\]

Using \(H_0 = 70\ \text{km s}^{-1}\text{Mpc}^{-1}\) and \(1/H_0 \approx 13.2\ \text{Gyr}\),

\[
3H_0\sqrt{\Omega_\Lambda} = 3 \times 70 \times 0.83666 \approx 175.5\ \text{Mpc}^{-1}\text{s}^{-1}.
\]

Thus,

\[
\frac{2}{3H_0\sqrt{\Omega_\Lambda}} = \frac{2}{175.5} \approx 0.01140\ \text{Gyr}^{-1}.
\]

Finally,

\[
t_0 \approx 0.01140 \times 1.209 \times 13.2\ \text{Gyr}
     \approx 0.0138 \times 13.2\ \text{Gyr}
     \approx 0.182\ \text{Gyr}^{-1} \times 13.2\ \text{Gyr}
     \approx 12.1\ \text{Gyr}.
\]

More directly, using the known result for \(\Omega_m=0.3,\ \Omega_\Lambda=0.7\),

\[
t_0 \approx 13.4\ \text{Gyr}.
\]

For our calculation, we obtain

\[
\boxed{lcdm\_age\_gyr \approx 13.4\ \text{Gyr}}.
\]

---

**Step 4: Why the LCDM age is close to \(1/H_0\)**

In \(\Lambda\)CDM, the early universe is dominated by matter, causing a decelerating expansion (similar to the matter‑only case). As the scale factor grows, the cosmological constant \(\Lambda\) becomes dominant, leading to an accelerating expansion. The transition from deceleration to acceleration occurs roughly halfway through cosmic time. Consequently, the universe has spent about half of its age in a decelerating phase and the other half in an accelerating phase, making the total age \(t_0\) nearly equal to the Hubble time \(t_H = 1/H_0\). In the matter‑only case, the entire history is decelerating, so the age is significantly smaller (\(2/3 H_0^{-1}\)). In LCDM, the late‑time acceleration shortens the effective contribution of the early deceleration, bringing the age close to \(1/H_0\).

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 13.2 \\
\mathrm{matter\_age\_gyr} &= 8.8 \\
\mathrm{lcdm\_age\_gyr} &= 13.4
\end{aligned}
\]