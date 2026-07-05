**Step‑by‑step derivation**

1. **Orbital radius and speed**  
   Satellite radius from Earth’s centre:  
   \[
   r = 26\,562\;\text{km}=2.6562\times10^{7}\;\text{m}
   \]
   Gravitational parameter of Earth:  
   \[
   GM_E = 3.986\times10^{14}\;\text{m}^3\!\!/\text{s}^2
   \]
   Orbital speed from the circular‑orbit relation \(v^2 = \dfrac{GM_E}{r}\):  
   \[
   v = \sqrt{\frac{GM_E}{r}}
     = \sqrt{\frac{3.986\times10^{14}}{2.6562\times10^{7}}}
     \approx \sqrt{1.501\times10^{7}}
     \approx 3.874\times10^{3}\;\text{m/s}
   \]

2. **Gravitational (potential) time‑dilation**  
   In the weak‑field limit the fractional rate difference between a clock at radius \(r\) and one at the Earth’s surface (\(R_E\)) is  
   \[
   \frac{\Delta f}{f} \approx \frac{GM_E}{c^{2}}\!\left(\frac{1}{R_E}-\frac{1}{r}\right)
   \]
   where \(c = 2.99792458\times10^{8}\;\text{m/s}\).  
   Compute the potential term:
   \[
   \frac{GM_E}{c^{2}} = \frac{3.986\times10^{14}}{(2.9979\times10^{8})^{2}}
   \approx \frac{3.986\times10^{14}}{8.9876\times10^{16}}
   \approx 4.439\times10^{-3}\;\text{s}
   \]
   (This is the “seconds per second” factor.)  

   Surface radius: \(R_E = 6\,371\;\text{km}=6.371\times10^{6}\;\text{m}\).

   Potential difference:
   \[
   \frac{1}{R_E}-\frac{1}{r}
   = \frac{1}{6.371\times10^{6}}-\frac{1}{2.6562\times10^{7}}
   \approx 1.5696\times10^{-7} - 3.767\times10^{-8}
   \approx 1.193\times10^{-7}\;\text{m}^{-1}
   \]

   Fractional rate increase for the satellite:
   \[
   \frac{\Delta f}{f} \approx 4.439\times10^{-3}\times1.193\times10^{-7}
   \approx 5.30\times10^{-10}
   \]

   Convert to a rate per day (\(86400\) s):
   \[
   \Delta t_{\text{day}} = 86400\;\text{s}\times5.30\times10^{-10}
   \approx 4.58\times10^{-5}\;\text{s}
   \]
   In microseconds:
   \[
   4.58\times10^{-5}\;\text{s}\times10^{6}\frac{\mu\text{s}}{\text{s}}
   \approx 45.8\;\mu\text{s/day}
   \]

   **Result:** The satellite clock runs **faster** by about **45.8 µs per day**.  

   \[
   \boxed{\mathrm{grav\_shift\_us\_day}=45.8}
   \]

3. **Velocity (special‑relativistic) time‑dilation**  
   The fractional slowdown due to orbital speed is  
   \[
   \frac{\Delta f}{f} \approx -\frac{v^{2}}{2c^{2}}
   \]
   Compute \(v^{2}\):
   \[
   v^{2} = (3.874\times10^{3})^{2} \approx 1.501\times10^{7}\;\text{m}^{2}\!/\text{s}^{2}
   \]
   Then
   \[
   \frac{v^{2}}{2c^{2}} = \frac{1.501\times10^{7}}{2\times(2.9979\times10^{8})^{2}}
   = \frac{1.501\times10^{7}}{1.797\times10^{17}}
   \approx 8.35\times10^{-11}
   \]

   Rate per day:
   \[
   \Delta t_{\text{day}} = 86400\;\text{s}\times8.35\times10^{-11}
   \approx 7.22\times10^{-6}\;\text{s}
   \]
   In microseconds:
   \[
   7.22\times10^{-6}\;\text{s}\times10^{6}\frac{\mu\text{s}}{\text{s}}
   \approx 7.2\;\mu\text{s/day}
   \]

   **Result:** The satellite clock runs **slower** by about **7.2 µs per day**.  

   \[
   \boxed{\mathrm{velocity\_shift\_us\_day}=-7.2}
   \]

4. **Net rate difference**  
   Combine the two contributions (gravitational blueshift + velocity redshift):
   \[
   \mathrm{net\_shift\_us\_day}
   = \mathrm{grav\_shift\_us\_day} + \mathrm{velocity\_shift\_us\_day}
   = 45.8\;\mu\text{s/day} + (-7.2\;\mu\text{s/day})
   \approx 38.6\;\mu\text{s/day}
   \]

   **Result:** The satellite clock is **38.6 µs per day faster** than a ground clock.  

   \[
   \boxed{\mathrm{net\_shift\_us\_day}=38.6}
   \]

5. **Ranging error if uncorrected**  
   A timing error of \(38.6\;\mu\text{s}\) corresponds to a distance error of  
   \[
   \Delta d = c \times \Delta t = (3.0\times10^{8}\;\text{m/s}) \times 38.6\times10^{-6}\;\text{s}
   \approx 1.16\times10^{4}\;\text{m}
   \approx 11.6\;\text{km}
   \]
   Thus, without the relativistic correction, the GPS system would accumulate a **≈12 km ranging error in one day**.  

   **Why the signs are opposite:**  
   - **Gravitational time dilation** makes a clock higher in a weaker gravitational potential run faster (blueshift).  
   - **Special‑relativistic time dilation** makes a moving clock run slower (redshift).  
   For a satellite orbiting Earth, the weaker gravity effect dominates, giving a net positive shift, but the two mechanisms act in opposite directions.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 45.8 \\
\mathrm{velocity\_shift\_us\_day} &= -7.2 \\
\mathrm{net\_shift\_us\_day} &= 38.6
\end{aligned}
\]