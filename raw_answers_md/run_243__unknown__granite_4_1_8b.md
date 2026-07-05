**Step‑by‑step derivation**

1. **First‑order GR perihelion advance per orbit**  
   For a test particle in a Schwarzschild spacetime, the relativistic correction to the orbital angular motion gives a perihelion advance per revolution  

   \[
   \Delta\phi_{\text{orbit}} = \frac{6\pi\,GM}{a\,(1-e^{2})\,c^{2}} .
   \]

   Here  
   - \(G\) is the gravitational constant,  
   - \(M\) is the mass of the central body (the Sun, \(M_\odot\)),  
   - \(a\) is the semi‑major axis,  
   - \(e\) is the orbital eccentricity,  
   - \(c\) is the speed of light.  

   This expression already contains the eccentricity factor \((1-e^{2})^{-1}\) as required.

2. **Insert the given data**  

   \[
   GM_\odot = 1.3271244\times10^{20}\ \text{m}^{3}\,\text{s}^{-2},\qquad
   a = 5.7909\times10^{10}\ \text{m},\qquad
   e = 0.2056,\qquad
   c = 2.99792458\times10^{8}\ \text{m s}^{-1}.
   \]

   Compute the denominator:

   \[
   a\,(1-e^{2}) = 5.7909\times10^{10}\,\bigl(1-0.2056^{2}\bigr)
                = 5.7909\times10^{10}\,(1-0.04227)
                = 5.7909\times10^{10}\times0.95773
                \approx 5.548\times10^{10}\ \text{m}.
   \]

   Compute \(c^{2}\):

   \[
   c^{2} = (2.99792458\times10^{8})^{2}
         \approx 8.98755179\times10^{16}\ \text{m}^{2}\,\text{s}^{-2}.
   \]

   Now evaluate the numerator \(6\pi GM_\odot\):

   \[
   6\pi GM_\odot = 6\pi \times 1.3271244\times10^{20}
                \approx 2.502\times10^{21}\ \text{m}^{3}\,\text{s}^{-2}.
   \]

   Assemble the fraction:

   \[
   \Delta\phi_{\text{orbit}} = 
   \frac{2.502\times10^{21}}
        {5.548\times10^{10}\times 8.98755179\times10^{16}}
   = \frac{2.502\times10^{21}}
          {4.985\times10^{27}}
   \approx 5.027\times10^{-7}\ \text{radians}.
   \]

3. **Convert to arcseconds**  

   \(1\ \text{radian} = \dfrac{180\cdot3600}{\pi}\) arcseconds \( \approx 206\,264.806\) arcseconds.

   \[
   \Delta\phi_{\text{orbit}}(\text{arcsec}) 
   = 5.027\times10^{-7}\times 206\,264.806
   \approx 0.1037\ \text{arcseconds}.
   \]

   So the GR perihelion advance per Mercury orbit is about **0.104 arcseconds**.

4. **Number of Mercury orbits per century**  

   Mercury’s orbital period is \(T = 87.969\) days.

   \[
   \text{orbits per century} = \frac{100\ \text{years}\times365.25\ \text{days/yr}}{87.969\ \text{days}}
   = \frac{36525}{87.969}
   \approx 415.2\ \text{orbits/century}.
   \]

5. **Advance per century**  

   \[
   \Delta\phi_{\text{century}} = \Delta\phi_{\text{orbit}} \times \text{orbits per century}
   = 0.1037\ \text{arcsec} \times 415.2
   \approx 43.1\ \text{arcseconds/century}.
   \]

   This matches the classic value of **≈ 43″ per century** attributed to general relativity.

6. **Observed total precession and the remainder**  

   The total observed perihelion precession of Mercury is about **574″ per century**.  
   The excess **\(574'' - 43'' \approx 531''\)** is accounted for by:

   - **Newtonian perturbations** from the gravitational influence of other planets (especially Venus, Earth, and Jupiter).  
   - **Solar oblateness** (the slight equatorial bulge of the Sun).  
   - **Precession of the equinoxes** (a coordinate effect due to Earth’s axial precession).  

   The ≈ 43″ contribution from general relativity is the distinctive signature of spacetime curvature around the Sun and is the part that tests Einstein’s theory.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.104 \ \text{arcseconds} \\
\mathrm{advance\_arcsec\_century} &= 43.1 \ \text{arcseconds} \\
\mathrm{orbits\_per\_century} &= 415.2
\end{aligned}
\]