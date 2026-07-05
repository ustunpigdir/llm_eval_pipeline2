**Step‑by‑step reasoning**

1. **Yukawa potential**  
   In the Yukawa picture the nucleon–nucleon interaction mediated by a scalar meson (the pion) is  
   \[
   V(r) = -\frac{g^{2}}{4\pi}\,\frac{e^{-m_{\pi} r/\hbar c}}{r},
   \]
   where \(g\) is the coupling constant, \(m_{\pi}\) the mediator mass, and \(\hbar c\) the reduced Planck constant in energy–length units.  
   The exponential contains the **reduced Compton wavelength** \(\lambda = \hbar/(m_{\pi}c)\); thus the range of the force is set by \(\lambda\).

2. **Evaluate the reduced Compton wavelength**  
   Given:  
   \[
   m_{\pi}c^{2}=139.57\ \text{MeV},\qquad \hbar c = 197.327\ \text{MeV·fm}.
   \]  
   The reduced Compton wavelength in femtometers is  
   \[
   \lambda_{\text{reduced}} = \frac{\hbar}{m_{\pi}c}
   = \frac{197.327\ \text{MeV·fm}}{139.57\ \text{MeV}}
   \approx 1.413\ \text{fm}.
   \]  
   Hence  
   \[
   \boxed{\text{range\_fm}=1.413\ \text{fm}}.
   \]

3. **Non‑reduced Compton wavelength**  
   The non‑reduced Compton wavelength uses the full Planck constant \(h\) instead of \(\hbar\):  
   \[
   \lambda_{\text{non‑reduced}} = \frac{h}{m_{\pi}c}
   = \frac{2\pi\hbar}{m_{\pi}c}
   = 2\pi\,\lambda_{\text{reduced}}
   \approx 2\pi \times 1.413\ \text{fm}
   \approx 8.86\ \text{fm}.
   \]  
   Therefore  
   \[
   \boxed{\text{nonreduced\_fm}=8.86\ \text{fm}}.
   \]  
   **Why the reduced wavelength belongs in the Yukawa exponential:**  
   The Yukawa potential was derived from a relativistic field theory where the propagator of a massive scalar particle contains the factor \(\exp(-m r/\hbar c)\). This factor naturally arises from the **reduced** Compton wavelength \(\hbar/(m c)\). Using the full \(h/(m c)\) would introduce an extra factor of \(2\pi\), which is not present in the original derivation and would incorrectly lengthen the range by a factor of \(2\pi\).

4. **Historical inversion (Yukawa, 1935)**  
   Yukawa observed that the nuclear force had a finite range of roughly \(R \approx 2\ \text{fm}\). He inverted the relation  
   \[
   R \sim \frac{\hbar}{m_{\pi}c}
   \]
   to predict the mass of the mediating particle:  
   \[
   m_{\pi}c^{2} \approx \frac{\hbar c}{R}
   = \frac{197.327\ \text{MeV·fm}}{2\ \text{fm}}
   \approx 98.66\ \text{MeV}.
   \]  
   This value is close to the experimentally measured pion mass (≈139 MeV), but the historical estimate from a 2 fm range gives a **mass scale** of about **99 MeV**. Hence  
   \[
   \boxed{\text{mass\_for\_2fm\_mev}=99\ \text{MeV}}.
   \]

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{range\_fm} &= 1.413 \\
\mathrm{nonreduced\_fm} &= 8.86 \\
\mathrm{mass\_for\_2fm\_mev} &= 99
\end{aligned}
\]