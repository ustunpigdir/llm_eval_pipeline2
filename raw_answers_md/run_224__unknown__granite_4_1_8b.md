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
        = 29.53\;\text{km}.
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
   r_{\text{ISCO\_km}} = 177.2\;\text{km}.
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
   \begin{aligned}
   f_{\text{orbital}} 
   &= \frac{(2.998 \times 10^{8}\,\text{m s}^{-1})^{3}}
           {12\pi\sqrt{6}\,(6.674 \times 10^{-11}\,\text{m}^3\text{kg}^{-1}\text{s}^{-2})
            \,(1.989 \times 10^{31}\,\text{kg})} \\[4pt]
   &= \frac{2.697 \times 10^{25}\,\text{m}^{3}\text{s}^{-3}}
           {12\pi\sqrt{6}\,(1.327 \times 10^{21}\,\text{m}^3\text{s}^{-3})} \\[4pt]
   &\approx \frac{2.697 \times 10^{25}}{2.904 \times 10^{22}}\;\text{s}^{-1} \\[4pt]
   &\approx 9.28 \times 10^{2}\;\text{Hz}.
   \end{aligned}
   \]

   Thus  

   \[
   f_{\text{orbital\_hz}} \approx 928\;\text{Hz}.
   \]

6. **Gravitational‑wave frequency**  

   The dominant GW signal from a binary is at twice the orbital frequency:

   \[
   f_{\text{GW}} = 2\,f_{\text{orbital}} \approx 2 \times 928\;\text{Hz}
                \approx 1856\;\text{Hz}.
   \]

   Hence  

   \[
   f_{\text{gw\_hz}} \approx 1856\;\text{Hz}.
   \]

7. **Why the GW signal “shuts off” near the ISCO**  

   As the binary inspirals, the orbital separation shrinks until it reaches the ISCO. Below the ISCO, circular orbits are no longer stable; the innermost stable circular orbit is the last point where a bound, Keplerian orbit can exist. Once the separation falls below the ISCO, the orbit becomes eccentric and plunges rapidly into the black hole, leading to a very short, high‑frequency inspiral phase. The gravitational‑wave emission peaks at twice the orbital frequency, so the signal is strongest just before the plunge and then rapidly decays as the separation approaches the event horizon. Consequently, the observable GW signal effectively “turns off” (or becomes negligible) at frequencies just above the ISCO‑derived frequency.

   **Scaling of the ISCO frequency with mass**  

   From the expression \(f_{\text{orbital}} = \dfrac{c^{3}}{12\pi\sqrt{6}\,GM}\),

   \[
   f_{\text{orbital}} \propto \frac{1}{M}.
   \]

   Therefore, for a black hole of mass \(M\), the ISCO orbital frequency scales inversely with the mass, and the corresponding GW frequency scales as \(f_{\text{GW}} \propto 1/M\). A more massive black hole emits GWs at lower frequencies, while a less massive one emits at higher frequencies.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 177.2 \\
\mathrm{f\_orbital\_hz} &= 928 \\
\mathrm{f\_gw\_hz} &= 1856
\end{aligned}
\]