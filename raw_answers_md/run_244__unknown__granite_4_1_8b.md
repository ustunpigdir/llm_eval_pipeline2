**Step‑by‑step derivation**

1. **First‑order GR perihelion advance per orbit**  
   For a test particle in the Schwarzschild geometry the relativistic correction to the orbital angular motion is  

   \[
   \Delta\Granite \;=\; \frac{6\pi GM}{a\,(1-e^{2})\,c^{2}}\;,
   \]

   where  
   - \(G\) is the gravitational constant,  
   - \(M\) is the mass of the central body (the Sun, \(M_\odot\)),  
   - \(a\) is the semi‑major axis,  
   - \(e\) is the orbital eccentricity,  
   - \(c\) is the speed of light.  

   This expression already contains the eccentricity factor \((1-e^{2})^{-1}\) as required.

2. **Convert \(\Delta\Granite\) from radians to arcseconds**  
   One radian equals \(\frac{180}{\pi}\) degrees, and one degree equals \(3600\) arcseconds. Hence  

   \[
   1\;\text{rad} = \frac{180}{\pi}\times 3600'' \approx 206\,264.806\;'' .
   \]

   Therefore  

   \[
   \Delta\phi_{\text{arcsec}} = \Delta\Granite \times 206\,264.806'' .
   \]

3. **Insert the given numerical data**  

   \[
   GM_\odot = 1.3271244\times10^{20}\;\text{m}^{3}\!\!/\text{s}^{2},
   \qquad
   a = 5.7909\times10^{10}\;\text{m},
   \qquad
   e = 0.2056,
   \qquad
   c = 2.99792458\times10^{8}\;\text{m/s}.
   \]

   Compute the denominator \(a(1-e^{2})\):

   \[
   e^{2}=0.2056^{2}=0.04227,\qquad
   1-e^{2}=0.95773,
   \]
   \[
   a(1-e^{2}) = 5.7909\times10^{10}\times0.95773
               \approx 5.548\times10^{10}\;\text{m}.
   \]

   Compute the factor \(6\pi GM_\odot\):

   \[
   6\pi GM_\odot = 6\pi \times 1.3271244\times10^{20}
                 \approx 2.502\times10^{21}\;\text{m}^{3}\!\!/\text{s}^{2}.
   \]

   Compute \(c^{2}\):

   \[
   c^{2} = (2.99792458\times10^{8})^{2}
         \approx 8.98755179\times10^{16}\;\text{m}^{2}\!\!/\text{s}^{2}.
   \]

   Now the per‑orbit advance in radians:

   \[
   \Delta\Granite = \frac{2.502\times10^{21}}
                     {5.548\times10^{10}\times 8.98755179\times10^{16}}
               \approx 6.28\times10^{-12}\;\text{rad}.
   \]

   Convert to arcseconds:

   \[
   \Delta\phi_{\text{arcsec}} = 6.28\times10^{-12}\;\text{rad}\times206\,264.806''
                               \approx 1.295\times10^{-6}''.
   \]

   Wait – that is far too small. Let’s recompute more carefully using the standard compact form:

   \[
   \Delta\phi_{\text{arcsec}} = \frac{360}{2\pi}\,\frac{6\pi GM_\odot}{a(1-e^{2})c^{2}}
                              = \frac{180}{\pi}\,\frac{6 GM_\odot}{a(1-e^{2})c^{2}}.
   \]

   Simplify:

   \[
   \Delta\phi_{\text{arcsec}} = \frac{1080\,GM_\odot}{\pi\,a(1-e^{2})c^{2}}.
   \]

   Insert numbers:

   \[
   \pi a(1-e^{2})c^{2}
   = \pi \times 5.548\times10^{10}\times 8.98755179\times10^{16}
   \approx 1.567\times10^{28}.
   \]

   \[
   1080\,GM_\odot = 1080 \times 1.3271244\times10^{20}
                  \approx 1.433\times10^{23}.
   \]

   Hence

   \[
   \Delta\phi_{\text{arcsec}} = \frac{1.433\times10^{23}}{1.567\times10^{28}}
                              \approx 9.15\times10^{-6}\;\text{arcsec}.
   \]

   This still seems off. The classic result for Mercury is about **\(43''\) per century**, i.e. **\(0.043''\) per orbit**. Let’s use the well‑known simplified expression:

   \[
   \Delta\phi_{\text{arcsec per orbit}} = \frac{24\pi^{2}a^{2}}{(1-e^{2})^{2}c^{2}}\,
                                          \frac{GM_\odot}{a^{3}}.
   \]

   Simplifying gives the familiar form:

   \[
   \Delta\phi_{\text{arcsec per orbit}} = \frac{6\pi GM_\odot}{a(1-e^{2})c^{2}}.
   \]

   Using the numbers directly:

   \[
   \frac{6\pi GM_\odot}{a(1-e^{2})c^{2}}
   = \frac{6\pi \times 1.3271244\times10^{20}}
          {5.548\times10^{10}\times 8.98755179\times10^{16}}
   \approx 1.48\times10^{-6}\;\text{rad}.
   \]

   Convert to arcseconds:

   \[
   1.48\times10^{-6}\;\text{rad}\times206\,264.806''
   \approx 0.305''\;\text{per orbit}.
   \]

   Wait, the accepted value is **\(0.103''\) per orbit** (≈ 43'' per century). The discrepancy arises from the factor of 2 in the denominator. The correct first‑order GR formula is:

   \[
   \boxed{\displaystyle \Delta\phi_{\text{arcsec per orbit}} = 
          \frac{24\pi^{2}GM_\odot}{c^{2}\,a\,(1-e^{2})}}.
   \]

   Let’s evaluate this:

   \[
   24\pi^{2} \approx 24 \times 9.8696 = 236.984,
   \]
   \[
   \frac{24\pi^{2}GM_\odot}{c^{2}a(1-e^{2})}
   = \frac{236.984 \times 1.3271244\times10^{20}}
          {8.98755179\times10^{16}\times5.548\times10^{10}\times0.95773}
   \approx \frac{3.146\times10^{22}}
                {4.551\times10^{27}}
   \approx 6.91\times10^{-6}\;\text{rad}.
   \]

   Convert to arcseconds:

   \[
   6.91\times10^{-6}\;\text{rad}\times206\,264.806''
   \approx 1.43''\;\text{per orbit}.
   \]

   This is still too large. The standard textbook result for Mercury is:

   \[
   \Delta\phi_{\text{arcsec per orbit}} \approx 0.103''.
   \]

   The correct expression (derived from the Schwarzschild metric) is:

   \[
   \Delta\phi_{\text{arcsec per orbit}} = 
   \frac{6\pi GM_\odot}{a(1-e^{2})c^{2}}.
   \]

   Plugging the numbers:

   \[
   \frac{6\pi GM_\odot}{a(1-e^{2})c^{2}}
   = \frac{6\pi \times 1.3271244\times10^{20}}
          {5.548\times10^{10}\times8.98755179\times10^{16}}
   \approx \frac{2.502\times10^{21}}
                {4.999\times10^{27}}
   \approx 5.00\times10^{-7}\;\text{rad}.
   \]

   Convert to arcseconds:

   \[
   5.00\times10^{-7}\;\text{rad}\times206\,264.806''
   \approx 0.103''\;\text{per orbit}.
   \]

   This matches the classic value.  

   **Thus**  

   \[
   \boxed{\displaystyle \Delta\phi_{\text{arcsec per orbit}} = 
          \frac{6\pi GM_\odot}{a(1-e^{2})c^{2}} \approx 0.103'' }.
   \]

4. **Advance per century**  

   Number of Mercury orbits in one century:

   \[
   \text{orbits per century} = \frac{100\;\text{yr}}{87.969\;\text{d}}
                              = \frac{100 \times 365.25}{87.969}
                              \approx 415.2.
   \]

   Total GR advance per century:

   \[
   \Delta\phi_{\text{arcsec per century}} = 
   \Delta\phi_{\text{arcsec per orbit}} \times \text{orbits per century}
   \approx 0.103'' \times 415.2
   \approx 42.8''.
   \]

   Rounding gives **≈ 43″ per century**, the celebrated GR contribution.

5. **Observed precession and the remainder**  

   The total observed perihelion precession of Mercury is about **\(574''\) per century**.  
   The excess **\(574'' - 43'' = 531''\) per century** is accounted for by:

   - **Newtonian perturbations** from the gravitational influences of other planets (especially Venus, Earth, and Jupiter).  
   - **Solar oblateness** (the slight equatorial bulge of the Sun).  
   - **Precession of the equinoxes** (a coordinate effect due to Earth’s axial precession).  

   Only the **~43″ per century** attributed to the Schwarzschild term is the hallmark test of General Relativity, because it arises solely from spacetime curvature around the Sun and cannot be explained by any Newtonian or classical planetary perturbation model.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.103 \text{ arcseconds per orbit} \\
\mathrm{advance\_arcsec\_century} &= 43.0 \text{ arcseconds per century} \\
\mathrm{orbits\_per\_century} &= 415.2 \text{ orbits per century}
\end{aligned}
\]