The Yukawa potential for a scalar (or pseudoscalar) mediator of mass \(m_\pi\) is  

\[
V(r)= -\frac{g^2}{4\pi}\,\frac{e^{-m_\pi r}}{r}\;,
\]

where the exponential factor \(e^{-m_\pi r}\) sets the spatial decay of the force.  
Writing the exponent as \(e^{-r/\lambda}\) defines a characteristic range  

\[
\lambda \equiv \frac{\hbar}{m_\pi c},
\]

i.e. the **reduced** Compton wavelength.  This \(\lambda\) is the quantity that appears in the exponential and therefore determines the force’s range.

---

### 1. Reduced Compton wavelength (range)

\[
\lambda = \frac{\hbar c}{m_\pi c^2}
        = \frac{197.327\;\text{MeV·fm}}{139.57\;\text{MeV}}
        = 1.4138\;\text{fm}\;\approx\;1.41\;\text{fm}.
\]

Thus  

\[
\boxed{\text{range\_fm}=1.41}.
\]

---

### 2. Non‑reduced Compton wavelength

The non‑reduced wavelength uses \(h\) instead of \(\hbar\):

\[
\frac{h}{m_\pi c}= \frac{2\pi\hbar}{m_\pi c}=2\pi\lambda
                 = 2\pi \times 1.4138\;\text{fm}
                 = 8.883\;\text{fm}\;\approx\;8.88\;\text{fm}.
\]

The factor \(2\pi\) comes from \(h=2\pi\hbar\).  However, the Yukawa exponential contains \(\hbar\) (not \(h\)) because the Fourier transform of the propagator \(\frac{1}{k^2+m_\pi^2}\) yields \(e^{-m_\pi r}/r\) with \(\hbar\) in the exponent.  Consequently the **reduced** wavelength, not the non‑reduced one, belongs in the Yukawa potential.

Hence  

\[
\boxed{\text{nonreduced\_fm}=8.88}.
\]

---

### 3. Mass implied by a 2.0 fm range (Yukawa’s 1935 inference)

If the observed range were \(r_0 = 2.0\) fm, the corresponding mass would satisfy  

\[
r_0 = \frac{\hbar}{m c}
\;\;\Longrightarrow\;\;
m c^2 = \frac{\hbar c}{r_0}
      = \frac{197.327\;\text{MeV·fm}}{2.0\;\text{fm}}
      = 98.6635\;\text{MeV}
      \;\approx\;98.7\;\text{MeV}.
\]

Thus  

\[
\boxed{\text{mass\_for\_2fm\_mev}=98.7}.
\]

---

FINAL ANSWER

\[
\begin{aligned}
\mathrm{range\_fm} &= 1.41 \\
\mathrm{nonreduced\_fm} &= 8.88 \\
\mathrm{mass\_for\_2fm\_mev} &= 98.7
\end{aligned}
\]