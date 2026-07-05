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
      \approx 1.47 \times 10^{10}\ \text{yr}.
\]

So,  

\[
\boxed{hubble\_time\_gyr \approx 14.7\ \text{Gyr}}.
\]

---

**Step 2: Evaluate the age of a flat matter‑only universe**

For a matter‑only (Einstein‑de Sitter) universe, the age is  

\[
t_{\text{matter}} = \frac{2}{3}\,t_H.
\]

Using \(t_H \approx 14.7\ \text{Gyr}\),

\[
t_{\text{matter}} = \frac{2}{3} \times 14.7\ \text{Gyr} \approx 9.8\ \text{Gyr}.
\]

**Why it is less than \(1/H_0\):**  
In a matter‑dominated universe, the scale factor evolves as \(a(t) \propto t^{2/3}\). The expansion is slower than exponential, so the universe has not had as much time to expand as it would in a universe with a constant Hubble rate. Consequently, the actual age \(t_{\text{matter}}\) is a fraction (\(2/3\)) of the Hubble time.

Thus,  

\[
\boxed{matter\_age\_gyr \approx 9.8\ \text{Gyr}}.
\]

---

**Step 3: Evaluate the LCDM age**

For a flat \(\Lambda\)CDM universe with \(\Omega_m = 0.3\) and \(\Omega_\Lambda = 0.7\), the age is given by  

\[
t_0 = \frac{2}{3 H_0 \sqrt{\Omega_\Lambda}} \,
      \operatorname{asinh}\!\left(\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\right).
\]

First compute the constants:

\[
\sqrt{\Omega_\Lambda} = \sqrt{0.7} \approx 0.8367,
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

Now compute the prefactor:

\[
\frac{2}{3 H_0 \sqrt{\Omega_\Lambda}}
   = \frac{2}{3 \times 70.0\ \text{km s}^{-1}\text{Mpc}^{-1} \times 0.8367}
   = \frac{2}{3 \times 58.669\ \text{km s}^{-1}\text{Mpc}^{-1}}
   = \frac{2}{176.007\ \text{km s}^{-1}\text{Mpc}^{-1}}.
\]

Convert this to years using \(1/H_0 \approx 14.4\ \text{Gyr}\) (from Step 1) and the factor \(2/(3\sqrt{\Omega_\Lambda})\):

\[
t_0 = \frac{2}{3\sqrt{\Omega_\Lambda}} \times \frac{1}{H_0}
     \times \operatorname{asinh}\!\left(\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\right).
\]

Using \(1/H_0 \approx 14.4\ \text{Gyr}\),

\[
t_0 \approx \frac{2}{3 \times 0.8367} \times 14.4\ \text{Gyr} \times 1.209.
\]

Calculate the prefactor:

\[
\frac{2}{3 \times 0.8367} \approx \frac{2}{2.5101} \approx 0.796.
\]

Thus,

\[
t_0 \approx 0.796 \times 14.4\ \text{Gyr} \times 1.209
      \approx 11.46\ \text{Gyr} \times 1.209
      \approx 13.86\ \text{Gyr}.
\]

Rounded to two significant figures,

\[
\boxed{lcdm\_age\_gyr \approx 13.9\ \text{Gyr}}.
\]

---

**Step 4: Explain why the LCDM age is close to \(1/H_0\)**

In the early universe, matter domination caused a decelerating expansion (\(a(t) \propto t^{2/3}\)). This slowed the growth of the scale factor, making the universe younger than the Hubble time at early times. As the universe evolved, the cosmological constant \(\Lambda\) became dominant at late times, driving an accelerating expansion (\(a(t) \propto e^{H_\Lambda t}\)). This late‑time acceleration speeds up the growth of the scale factor, effectively “catching up” with the Hubble time.

The combination of a slower early phase and a faster late phase results in an age that is only slightly less than the Hubble time. For the given parameters (\(\Omega_m = 0.3\), \(\Omega_\Lambda = 0.7\)), the late acceleration contributes enough to bring the calculated age (\(\approx 13.9\) Gyr) very close to the Hubble time (\(\approx 14.7\) Gyr).

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 14.7 \\
\mathrm{matter\_age\_gyr} &= 9.8 \\
\mathrm{lcdm\_age\_gyr} &= 13.9
\end{aligned}
\]