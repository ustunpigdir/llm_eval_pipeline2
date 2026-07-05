**Step‑by‑step reasoning**

1. **Yukawa potential**  
   In the Yukawa picture the nucleon–nucleon interaction mediated by a scalar meson (the pion) is  
   \[
   V(r) = -\frac{g^{2}}{4\pi}\,\frac{e^{-m_{\pi} r/\hbar c}}{r},
   \]
   where \(g\) is the coupling constant, \(m_{\pi}\) the mediator mass, and \(\hbar c\) the reduced Planck constant times the speed of light.  
   The exponential contains the **reduced Compton wavelength** \(\lambda_{\text{red}} = \hbar/(m_{\pi}c)\); thus the range of the force is set by this quantity.

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
   \lambda_{\text{non}} = \frac{h}{m_{\pi}c} = 2\,\frac{\hbar}{m_{\pi}c}=2\lambda_{\text{red}}.
   \]  
   Therefore  
   \[
   \lambda_{\text{non}} = 2 \times 1.413\ \text{fm} \approx 2.826\ \text{fm}.
   \]  
   The Yukawa potential, however, contains the **reduced** wavelength \(\hbar/(m_{\pi}c)\); using the non‑reduced wavelength would incorrectly double the exponential’s argument and thus double the range, which is not physically correct. Hence the correct quantity in the exponential is the reduced Compton wavelength.

4. **Historical inversion: mass from a 2.0 fm range**  
   If the observed nuclear force range is \(\lambda_{\text{obs}} = 2.0\ \text{fm}\), Yukawa inverted the relation  
   \[
   \lambda_{\text{obs}} = \frac{\hbar}{m_{\pi}c}
   \quad\Longrightarrow\quad
   m_{\pi}c^{2}= \frac{\hbar c}{\lambda_{\text{obs}}}.
   \]  
   Substituting the numbers:  
   \[
   m_{\pi}c^{2}= \frac{197.327\ \text{MeV·fm}}{2.0\ \text{fm}}
   \approx 98.66\ \text{MeV}.
   \]  
   Thus the mass scale implied by a 2.0 fm range is about **99 MeV**.  

   \[
   \boxed{\text{mass\_for\_2fm\_mev}=98.66\ \text{MeV}}.
   \]

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{range\_fm} &= 1.413 \\
\mathrm{nonreduced\_fm} &= 2.826 \\
\mathrm{mass\_for\_2fm\_mev} &= 98.66
\end{aligned}
\]