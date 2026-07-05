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
   Rounded to a sensible number of significant figures: **\(a_e \times 10^3 \approx 1.1614\)**.

5. **Compute the \(g\)-factor**  
   \[
   g = 2\bigl(1 + a_e\bigr)
     = 2\bigl(1 + 0.0011614098\bigr)
     = 2.0023228196.
   \]
   Rounded to six decimal places: **\(g \approx 2.002323\)**.

6. **Physical interpretation**  
   - **Tree‑level Dirac prediction**: For a point‑like spin‑½ particle with no charge‑dependent radiative corrections, the Dirac equation gives \(g = 2\).  
   - **Loop (QED) correction**: Quantum electrodynamics predicts that the electron’s interaction with the electromagnetic field (the one‑loop vacuum polarization) slightly modifies the magnetic moment. This modification is called the *anomaly* \(a_e\).  
   - **Same coefficient for muon**: The leading QED contribution depends only on the coupling constant \(\alpha\) and the spin‑½ nature of the particle, not on the lepton mass (as long as the mass is much larger than the photon mass). Hence the same Schwinger term \(\alpha/(2\pi)\) appears in the muon’s anomalous magnetic moment at leading order, although higher‑order hadronic effects differ.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.1614 \\
\mathrm{g\_factor} &= 2.002323
\end{aligned}
\]