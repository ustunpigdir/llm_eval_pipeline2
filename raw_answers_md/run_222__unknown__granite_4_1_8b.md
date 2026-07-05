**Step‑by‑step derivation**

1. **Constants and mass of the black hole**  

   \[
   M_\odot = 1.989 \times 10^{30}\,\text{kg},\qquad 
   G = 6.674 \times 10^{-11}\,\text{m}^3\text{kg}^{-1}\text{s}^{-2},\qquad 
   c = 2.998 \times 10^{8}\,\text{m s}^{-1}.
   \]

   The black‑hole mass is  

   \[
   M = 10\,M_\odot = 10 \times 1.989 \times 10^{30}\,\text{kg}
     = 1.989 \times 10^{31}\,\text{kg}.
   \]

2. **Schwarzschild radius \(r_s = GM/c^{2}\)**  

   \[
   r_s = \frac{G M}{c^{2}}
        = \frac{6.674 \times 10^{-11}\,\text{m}^3\text{kg}^{-1}\text{s}^{-2}
                \times 1.989 \times 10^{31}\,\text{kg}}
               {(2.998 \times 10^{8}\,\text{m s}^{-1})^{2}}
        \approx 2.953 \times 10^{4}\,\text{m}
        \approx 29.53\;\text{km}.
   \]

   In units of \(GM/c^{2}\),

   \[
   \frac{r_s}{GM/c^{2}} = 1.
   \]

3. **Photon sphere**  

   For a Schwarzschild black hole the photon sphere lies at  

   \[
   r_{\text{ph}} = \frac{3GM}{c^{2}} = 3\,r_s.
   \]

   Hence in units of \(GM/c^{2}\),

   \[
   \frac{r_{\text{ph}}}{GM/c^{2}} = 3.
   \]

4. **Innermost Stable Circular Orbit (ISCO)**  

   The ISCO radius for a Schwarzschild black hole is  

   \[
   r_{\text{ISCO}} = \frac{6GM}{c^{2}} = 6\,r_s.
   \]

   Therefore in units of \(GM/c^{2}\),

   \[
   \frac{r_{\text{ISCO}}}{GM/c^{2}} = 6.
   \]

   Converting to kilometres:

   \[
   r_{\text{ISCO}} = 6 \times 29.53\;\text{km}
                  \approx 177.2\;\text{km}.
   \]

   So  

   \[
   r_{\text{ISCO\_km}} \approx 177.2\;\text{km}.
   \]

5. **Orbital frequency at the ISCO**  

   The exact relation for circular orbits in Schwarzschild coordinates is  

   \[
   \Omega^{2} = \frac{GM}{r^{3}}.
   \]

   At the ISCO (\(r = r_{\text{ISCO}} = 6GM/c^{2}\)),

   \[
   \Omega^{2} = \frac{GM}{(6GM/c^{2})^{3}}
              = \frac{GM}{216\,(GM)^{3}/c^{6}}
              = \frac{c^{6}}{216\,G^{2}M^{2}}.
   \]

   Hence  

   \[
   \Omega = \frac{c^{3}}{6\sqrt{6}\,GM}.
   \]

   The orbital frequency measured at infinity is  

   \[
   f_{\text{orbital}} = \frac{\Omega}{2\pi}
                      = \frac{c^{3}}{12\pi\sqrt{6}\,GM}.
   \]

   Plugging in the numbers:

   \[
   f_{\text{orbital}} = 
   \frac{(2.998 \times 10^{8})^{3}}
        {12\pi\sqrt{6}\,(6.674 \times 10^{-11})\,(1.989 \times 10^{31})}
   \approx 1.24 \times 10^{3}\;\text{Hz}.
   \]

   So  

   \[
   f_{\text{orbital\_hz}} \approx 1.24 \times 10^{3}\;\text{Hz}.
   \]

6. **Gravitational‑wave frequency**  

   The dominant GW signal from a binary is at twice the orbital frequency:

   \[
   f_{\text{GW}} = 2\,f_{\text{orbital}}.
   \]

   Therefore  

   \[
   f_{\text{GW}} \approx 2 \times 1.24 \times 10^{3}\;\text{Hz}
                 \approx 2.48 \times 10^{3}\;\text{Hz}.
   \]

   Hence  

   \[
   f_{\text{gw\_hz}} \approx 2.48 \times 10^{3}\;\text{Hz}.
   \]

7. **Why the GW signal “shuts off” near the ISCO**  

   - **Rapid inspiral:** As the binary loses energy via GW emission, the orbit shrinks. When the innermost stable orbit is reached, the orbit can no longer remain circular; the separation drops below the ISCO.  
   - **Merger onset:** Below the ISCO the orbit becomes unstable, leading to a plunge and merger. The GW waveform therefore peaks at the ISCO frequency and then rapidly evolves into the merger signal.  
   - **Scaling with mass:** The ISCO radius scales linearly with the black‑hole mass (\(r_{\text{ISCO}} \propto M\)), and the orbital frequency scales as \(f_{\text{orbital}} \propto M^{-1}\). Consequently, for more massive black holes the ISCO frequency is lower, while for less massive ones it is higher. This mass dependence explains why the “shut‑off” frequency moves to lower values for larger \(M\).

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 177.2 \\
\mathrm{f\_orbital\_hz} &= 1240 \\
\mathrm{f\_gw\_hz} &= 2480
\end{aligned}
\]