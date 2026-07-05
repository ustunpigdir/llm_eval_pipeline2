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
     \approx \sqrt{1.501\times10^{7}}
     \approx 3.874\times10^{3}\;\text{m/s}
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
   \approx \frac{3.986\times10^{14}}{8.9876\times10^{16}}
   \approx 4.439\times10^{-3}\;\text{m}
   \]
   Potential difference:  
   \[
   \frac{1}{R_E}-\frac{1}{r}= \frac{1}{6.371\times10^{6}}-\frac{1}{2.6562\times10^{7}}
   \approx 1.5696\times10^{-7}-3.7659\times10^{-8}
   \approx 1.1930\times10^{-7}\;\text{m}^{-1}
   \]
   Fractional rate increase:  
   \[
   \frac{\Delta f}{f}\approx 4.439\times10^{-3}\times1.1930\times10^{-7}
   \approx 5.30\times10^{-10}
   \]
   Convert to a rate per second relative to a ground clock: the satellite clock runs faster by  
   \[
   \Delta f = f\,\frac{\Delta f}{f}\approx f\,(5.30\times10^{-10})
   \]
   Over one day (\(86400\) s) the absolute time gain is  
   \[
   \Delta t_{\text{grav}} = \Delta f \times 86400
   \approx f\,(5.30\times10^{-10})\times86400
   \]
   Since \(f = 1\;\text{Hz}\) for a clock, the gain in seconds is  
   \[
   \Delta t_{\text{grav}} \approx 5.30\times10^{-10}\times86400
   \approx 4.58\times10^{-5}\;\text{s}
   \]
   Convert to microseconds:  
   \[
   4.58\times10^{-5}\;\text{s}\times10^{6}\frac{\mu\text{s}}{\text{s}}
   \approx 45.8\;\mu\text{s}
   \]
   **Result:** gravitational blueshift ≈ **+45.8 µs/day** (satellite faster).

3. **Velocity (special‑relativistic) time‑dilation**  
   The fractional slowdown due to orbital speed is  
   \[
   \frac{\Delta f}{f} \approx -\frac{v^{2}}{2c^{2}}
   \]
   Compute \(v^{2}\):  
   \[
   v^{2} \approx (3.874\times10^{3})^{2} \approx 1.501\times10^{7}\;\text{m}^2\!\!/\text{s}^2
   \]
   Fractional slowdown:  
   \[
   -\frac{v^{2}}{2c^{2}} = -\frac{1.501\times10^{7}}{2(8.9876\times10^{16})}
   \approx -\frac{1.501\times10^{7}}{1.7975\times10^{17}}
   \approx -8.35\times10^{-11}
   \]
   Over one day:  
   \[
   \Delta t_{\text{vel}} = -8.35\times10^{-11}\times86400
   \approx -7.22\times10^{-6}\;\text{s}
   \]
   Convert to microseconds:  
   \[
   -7.22\times10^{-6}\;\text{s}\times10^{6}\frac{\mu\text{s}}{\text{s}}
   \approx -7.2\;\mu\text{s}
   \]
   **Result:** velocity redshift ≈ **–7.2 µs/day** (satellite slower).

4. **Net rate difference**  
   \[
   \text{net shift} = \text{gravitational} + \text{velocity}
   = 45.8\;\mu\text{s/day} - 7.2\;\mu\text{s/day}
   \approx 38.6\;\mu\text{s/day}
   \]
   **Result:** net satellite‑minus‑ground rate ≈ **+38.6 µs/day** (satellite runs faster).

5. **Ranging error if uncorrected**  
   A timing error of \(38.6\;\mu\text{s}\) corresponds to a distance error of  
   \[
   \Delta d = c \times \Delta t \approx (3.0\times10^{8}\;\text{m/s})\times38.6\times10^{-6}\;\text{s}
   \approx 1.16\times10^{4}\;\text{m}
   \approx 11.6\;\text{km}
   \]
   Thus, without the relativistic correction, the GPS system would accumulate a **≈ 12 km** ranging error in one day.  
   **Why opposite signs?**  
   - Gravitational potential is deeper (more negative) at the satellite’s altitude, so a clock higher up ticks faster → **positive** shift.  
   - The satellite’s orbital speed causes special‑relativistic time dilation, which slows the moving clock → **negative** shift.  

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 45.8 \\
\mathrm{velocity\_shift\_us\_day} &= -7.2 \\
\mathrm{net\_shift\_us\_day} &= 38.6
\end{aligned}
\]