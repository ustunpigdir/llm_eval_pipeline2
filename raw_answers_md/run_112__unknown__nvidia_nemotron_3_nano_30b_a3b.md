The Hubble constant is given as  

\[
H_0 = 70.0\;\frac{\text{km}}{\text{s·Mpc}} .
\]

1. **Convert \(H_0\) to \(\mathrm{s^{-1}}\).**  
   \[
   1\;\text{Mpc}=3.0857\times10^{19}\;\text{km}
   \]
   \[
   H_0 = \frac{70.0}{3.0857\times10^{19}}\;\text{s}^{-1}
        = 2.2688\times10^{-18}\;\text{s}^{-1}.
   \]

2. **Hubble time \(=1/H_0\).**  
   \[
   t_{\rm H}= \frac{1}{2.2688\times10^{-18}}\;\text{s}
            = 4.4069\times10^{17}\;\text{s}.
   \]

3. **Convert seconds to gigayears.**  
   \[
   1\;\text{yr}=3.15576\times10^{7}\;\text{s},\qquad
   1\;\text{Gyr}=10^{9}\;\text{yr}=3.15576\times10^{16}\;\text{s}.
   \]
   \[
   t_{\rm H\;(Gyr)}=\frac{4.4069\times10^{17}}{3.15576\times10^{16}}
                    = 13.97\;\text{Gyr}.
   \]

   Hence  

   \[
   \mathrm{hubble\_time\_gyr}=13.97 .
   \]

4. **Flat matter‑only (Einstein–de Sitter) age.**  
   For a matter‑dominated flat universe \(\Omega_m=1\) the age is  

   \[
   t_{\rm m}= \frac{2}{3H_0}= \frac{2}{3}\,t_{\rm H}.
   \]
   \[
   t_{\rm m}= \frac{2}{3}\times13.97 = 9.31\;\text{Gyr}.
   \]

   The factor \(2/3<1\) reflects that the expansion decelerates under matter domination, so the universe reaches its present size earlier than the simple constant‑expansion timescale \(1/H_0\).

5. **Flat LCDM age with \(\Omega_m=0.3,\;\Omega_\Lambda=0.7\).**  
   The given formula is  

   \[
   t_0 = \frac{2}{3H_0\sqrt{\Omega_\Lambda}}\,
         \operatorname{asinh}\!\sqrt{\frac{\Omega_\Lambda}{\Omega_m}} .
   \]

   Compute the dimensionless factors:

   \[
   \sqrt{\Omega_\Lambda}= \sqrt{0.7}=0.836660,
   \qquad
   \sqrt{\frac{\Omega_\Lambda}{\Omega_m}}=
   \sqrt{\frac{0.7}{0.3}}=1.527525.
   \]

   \[
   \operatorname{asinh}(1.527525)=
   \ln\!\bigl(1.527525+\sqrt{1.527525^{2}+1}\bigr)
   =\ln(3.353267)=1.209030.
   \]

   \[
   \frac{2}{3\sqrt{\Omega_\Lambda}}=
   \frac{2}{3\times0.836660}=0.796819.
   \]

   Multiply:

   \[
   f = 0.796819 \times 1.209030 = 0.963378.
   \]

   Therefore  

   \[
   t_{\rm LCDM}=f\,t_{\rm H}=0.963378\times13.97
               = 13.46\;\text{Gyr}.
   \]

   The LCDM age is close to the Hubble time because the early matter‑dominated era slows the expansion (reducing the age below \(1/H_0\)), while the later dark‑energy‑dominated era accelerates it (raising the age back up). The two effects partially cancel, leaving a factor \(\approx0.96\) of the Hubble