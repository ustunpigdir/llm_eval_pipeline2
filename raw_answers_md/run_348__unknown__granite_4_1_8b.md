**Step‑by‑step reasoning**

1. **Yukawa potential**  
   In the Yukawa picture the nucleon–nucleon interaction mediated by a scalar meson (the pion) is  
   \[
   V(r) = -\frac{g^{2}}{4\pi}\,\frac{e^{-m_{\pi} r/\hbar c}}{r},
   \]
   where \(g\) is the coupling constant, \(m_{\pi}\) the mediator mass, and \(\hbar c\) the reduced Planck constant times the speed of light. The exponential contains the **reduced Compton wavelength** \(\lambda_{\text{red}} = \hbar/(m_{\pi}c)\).

2. **Evaluate the reduced Compton wavelength**  
   Given:  
   \[
   m_{\pi}c^{2}=139.57\ \text{MeV},\qquad \hbar c = 197.327\ \text{MeV·fm}.
   \]  
   The reduced Compton wavelength in femtometers is  
   \[
   \lambda_{\text{red}} = \frac{\hbar}{m_{\pi}c}
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
   \lambda_{\text{non}} = \frac{h}{m_{\pi}c} = 2\pi\,\frac{\hbar}{m_{\pi}c}=2\pi\,\lambda_{\text{red}}.
   \]  
   Therefore  
   \[
   \lambda_{\text{non}} = 2\pi \times 1.413\ \text{fm}
   \approx 8.86\ \text{fm}.
   \]  
   So  
   \[
   \boxed{\text{nonreduced\_fm}=8.86\ \text{fm}}.
   \]  
   **Why the reduced wavelength belongs in the Yukawa exponential:**  
   The Yukawa potential was derived from a relativistic scalar field theory where the propagator contains the factor \(\exp(-m r/\hbar c)\). This factor naturally arises from the dispersion relation \(E^{2}=p^{2}c^{2}+m^{2}c^{4}\) and the Fourier transform of the Green’s function, leading to the reduced Compton wavelength \(\hbar/(mc)\). Using the full wavelength would over‑dampen the potential and contradict the original derivation.

4. **Historical inversion (1935)**  
   Yukawa observed that the nuclear force had a finite range of roughly \(R \approx 2\ \text{fm}\). He set this range equal to the reduced Compton wavelength of the exchanged particle:  
   \[
   R \approx \frac{\hbar}{m_{\pi}c} \;\Rightarrow\; m_{\pi}c^{2} \approx \frac{\hbar c}{R}.
   \]  
   Substituting the numbers:  
   \[
   m_{\pi}c^{2} \approx \frac{197.327\ \text{MeV·fm}}{2\ \text{fm}}
   \approx 98.66\ \text{MeV}.
   \]  
   This value is close to the experimentally measured pion mass (≈139 MeV), but the historical estimate gave a **lower bound** of roughly \(100\ \text{MeV}\). Hence the mass scale implied by a 2.0 fm range is about **100 MeV**.  
   Therefore  
   \[
   \boxed{\text{mass\_for\_2fm\_mev}=100\ \text{MeV}}.
   \]

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{range\_fm} &= 1.413 \\
\mathrm{nonreduced\_fm} &= 8.86 \\
\mathrm{mass\_for\_2fm\_mev} &= 100
\end{aligned}
\]