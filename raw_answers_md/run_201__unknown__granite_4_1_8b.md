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
   Orbital speed from the circular‑orbit relation \(v^2 = GM_E/r\):  
   \[
   v = \sqrt{\frac{GM_E}{r}}
     = \sqrt{\frac{3.986\times10^{14}}{2.6562\times10^{7}}}
     \approx \sqrt{1.500\times10^{7}}
     \approx 3.87\times10^{3}\;\text{m/s}
   \]

2. **Gravitational (potential) time‑dilation**  
   In the weak‑field limit the fractional rate difference between a clock at radius \(r\) and one at the Earth’s surface (\(R_E\)) is  
   \[
   \frac{\Delta f}{f} \approx \frac{GM_E}{c^2}\!\left(\frac{1}{R_E}-\frac{1}{r}\right)
   \]
   where \(c = 2.99792458\times10^{8}\;\text{m/s}\).  
   Compute the potential term:  
   \[
   \frac{GM_E}{c^2}= \frac{3.986\times10^{14}}{(2.9979\times10^{8})^2}
   \approx 4.428\times10^{-3}\;\text{m}
   \]
   \[
   \frac{1}{R_E}= \frac{1}{6.371\times10^{6}} \approx 1.5696\times10^{-7}\;\text{m}^{-1}
   \]
   \[
   \frac{1}{r}= \frac{1}{2.6562\times10^{7}} \approx 3.766\times10^{-8}\;\text{m}^{-1}
   \]
   \[
   \frac{1}{R_E}-\frac{1}{r}\approx 1.193\times10^{-7}\;\text{m}^{-1}
   \]
   Fractional rate increase:  
   \[
   \frac{\Delta f}{f}\approx 4.428\times10^{-3}\times1.193\times10^{-7}
   \approx 5.28\times10^{-10}
   \]
   Over one day (\(86400\) s) the absolute time gain is  
   \[
   \Delta t_{\text{grav}} = 86400\;\text{s}\times5.28\times10^{-10}
   \approx 4.56\times10^{-5}\;\text{s}
   \]
   Convert to microseconds:  
   \[
   4.56\times10^{-5}\;\text{s}\times10^{6}\frac{\mu\text{s}}{\text{s}}
   \approx 45.6\;\mu\text{s}
   \]
   **Result:** gravitational blueshift makes the satellite clock run **~45.6 µs per day faster**.  

   \[
   \boxed{\mathrm{grav\_shift\_us\_day}=45.6}
   \]

3. **Velocity (special‑relativistic) time‑dilation**  
   The fractional slowdown due to speed \(v\) is  
   \[
   \frac{\Delta f}{f}\approx -\frac{v^{2}}{2c^{2}}
   \]
   Using \(v^{2}=GM_E/r\):  
   \[
   \frac{v^{2}}{2c^{2}} = \frac{GM_E}{2r c^{2}}
   \]
   Compute:  
   \[
   \frac{GM_E}{2r}= \frac{3.986\times10^{14}}{2\times2.6562\times10^{7}}
   \approx 7.50\times10^{6}\;\text{m}^2\!\!/\text{s}^2
   \]
   \[
   \frac{GM_E}{2r c^{2}} = \frac{7.50\times10^{6}}{(2.9979\times10^{8})^{2}}
   \approx 7.88\times10^{-11}
   \]
   Over one day:  
   \[
   \Delta t_{\text{vel}} = 86400\;\text{s}\times7.88\times10^{-11}
   \approx 6.80\times10^{-6}\;\text{s}
   \]
   Convert to microseconds:  
   \[
   6.80\times10^{-6}\;\text{s}\times10^{6}\frac{\mu\text{s}}{\text{s}}
   \approx -6.8\;\mu\text{s}
   \]
   **Result:** the satellite clock runs **~6.8 µs per day slower** due to velocity.  

   \[
   \boxed{\mathrm{velocity\_shift\_us\_day}=-6.8}
   \]

4. **Net rate difference**  
   \[
   \mathrm{net\_shift\_us\_day}= \mathrm{grav\_shift\_us\_day} + \mathrm{velocity\_shift\_us\_day}
   = 45.6\;\mu\text{s/day} - 6.8\;\mu\text{s/day}
   \approx 38.8\;\mu\text{s/day}
   \]
   **Result:** the satellite clock is **~38.8 µs per day faster** than a ground clock.  

   \[
   \boxed{\mathrm{net\_shift\_us\_day}=38.8}
   \]

5. **Ranging error if uncorrected**  
   A timing error of \(38.8\;\mu\text{s}\) corresponds to a distance error of  
   \[
   \Delta d = c \times \Delta t = (2.998\times10^{8}\;\text{m/s}) \times 38.8\times10^{-6}\;\text{s}
   \approx 1.16\times10^{4}\;\text{m}
   \approx 11.6\;\text{km}
   \]
   Thus, without the relativistic correction, the GPS system would accumulate a **≈12 km ranging error in one day**.  
   The two effects have opposite signs because the stronger gravitational blueshift (higher altitude, weaker potential) tends to speed the satellite clock, while the special‑relativistic time dilation from its orbital speed tends to slow it.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 45.6 \\
\mathrm{velocity\_shift\_us\_day} &= -6.8 \\
\mathrm{net\_shift\_us\_day} &= 38.8
\end{aligned}
\]