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

4. **Convert to the requested unit**  
   \[
   a_e \times 10^{3} = 0.0011614098 \times 10^{3}
                    \approx 1.1614098.
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
   - **Tree‑level Dirac prediction**: For a point‑like spin‑½ particle obeying the Dirac equation, the gyromagnetic ratio is \(g = 2\). This corresponds to a perfectly circularly polarized magnetic moment aligned with the spin.  
   - **Loop (QED) correction**: Quantum electrodynamics allows the electron to emit and re‑absorb a virtual photon. This radiative process modifies the magnetic moment, producing an *anomaly* \(a_e = (g-2)/2\). The leading term is proportional to the fine‑structure constant \(\alpha\) and inversely proportional to \(\pi\).  
   - **Why the same coefficient applies to the muon**: Both the electron and the muon are leptons with the same spin‑½ Dirac structure and experience the same QED interaction with the electromagnetic field. At one‑loop order, the only difference is the muon’s larger mass, which enters higher‑order (two‑loop, three‑loop) corrections, but the *leading* Schwinger term \(\alpha/(2\pi)\) is universal for any point‑like spin‑½ charged particle. Hence the same coefficient appears in the muon’s anomalous magnetic moment.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.161410,\\
\mathrm{g\_factor} &= 2.002323.
\end{aligned}
\]