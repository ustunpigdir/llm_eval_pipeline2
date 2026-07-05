**Step‑by‑step derivation**

1. **Schwinger’s one‑loop result**  
   The leading QED correction to the electron’s anomalous magnetic moment (the Schwinger term) is  
   \[
   a_e \equiv \frac{g-2}{2} = \frac{\alpha}{2\pi}\,,
   \]
   where \(\alpha\) is the fine‑structure constant.

2. **Insert the numerical value of \(\alpha\)**  
   \[
   \alpha = \frac{1}{137.036}\approx 0.00729927007.
   \]

3. **Compute \(a_e\)**  
   \[
   a_e = \frac{\alpha}{2\pi}
        = \frac{0.00729927007}{2\pi}
        = \frac{0.00729927007}{6.283185307}
        \approx 0.0011614098.
   \]

4. **Convert to units of \(10^{-3}\)** (i.e., multiply by \(10^3\))  
   \[
   a_e \times 10^3 = 0.0011614098 \times 10^3 \approx 1.1614098.
   \]
   Rounded to a sensible number of significant figures: **1.161410** (to 6 dp).

5. **Compute the \(g\)-factor**  
   \[
   g = 2\bigl(1 + a_e\bigr)
     = 2\bigl(1 + 0.0011614098\bigr)
     = 2.0023228196.
   \]
   Rounded to 6 decimal places: **2.002323**.

6. **Physical interpretation**  
   - **Tree‑level Dirac prediction**: For a point‑like spin‑½ particle with no anomalous contributions, the Dirac equation gives \(g = 2\).  
   - **Loop (radiative) correction**: Quantum electrodynamics predicts that the electron emits and re‑absorbs a virtual photon, which modifies its magnetic moment. This modification is called the *anomaly* and appears as the term \(\alpha/(2\pi)\).  
   - **Same coefficient for the muon**: The leading QED correction depends only on the coupling constant \(\alpha\) and the spin‑½ nature of the particle; it does not depend on the lepton mass (to leading order). Hence the muon receives the identical Schwinger term \(\alpha/(2\pi)\) (apart from tiny higher‑order mass‑suppressed effects).  

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.161410,\\
\mathrm{g\_factor} &= 2.002323.
\end{aligned}
\]