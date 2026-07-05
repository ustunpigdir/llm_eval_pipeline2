To compute the relativistic clock corrections for GPS satellites, we must evaluate the effects of General Relativity (gravitational time dilation) and Special Relativity (velocity time dilation) separately, then combine them.

**Constants and Parameters:**
*   Gravitational parameter of Earth: $GM_E = 3.986 \times 10^{14} \text{ m}^3/\text{s}^2$.
*   Earth's surface radius: $R_E = 6371 \text{ km} = 6.371 \times 10^6 \text{ m}$.
*   Satellite orbital radius: $r = 26\,562 \text{ km} = 2.6562 \times 10^7 \text{ m}$.
*   Speed of light: $c \approx 2.99792458 \times 10^8 \text{ m/s}$.
*   Seconds per day: $T_{\text{day}} = 86\,400 \text{ s}$.

### 1. Gravitational Time Dilation (General Relativity)

According to General Relativity, a clock at a higher gravitational potential runs faster than a clock at a lower potential. The fractional frequency shift $\frac{\Delta f}{f}$ due to the difference in gravitational potential $\Delta \Phi$ is given by:
$$ \frac{\Delta f}{f} = \frac{\Delta \Phi}{c^2} $$
The gravitational potential $\Phi$ at a distance $r$ from Earth's center is $\Phi = -\frac{GM_E}{r}$.
The potential difference between the satellite ($r$) and the ground ($R_E$) is:
$$ \Delta \Phi = \Phi_{\text{sat}} - \Phi_{\text{ground}} = \left( -\frac{GM_E}{r} \right) - \left( -\frac{GM_E}{R_E} \right) = GM_E \left( \frac{1}{R_E} - \frac{1}{r} \right) $$
Since $r > R_E$, the term $\left( \frac{1}{R_E} - \frac{1}{r} \right)$ is positive, meaning the satellite is at a higher potential. Thus, the satellite clock runs faster.

The fractional rate difference is:
$$ \delta_{\text{grav}} = \frac{GM_E}{c^2} \left( \frac{1}{R_E} - \frac{1}{r} \right) $$

**Calculation:**
1.  Compute $GM_E / c^2$:
    $$ \frac{3.986 \times 10^{14}}{(2.99792458 \times 10^8)^2} \approx \frac{3.986 \times 10^{14}}{8.98755 \times 10^{16}} \approx 4.4350 \times 10^{-3} \text{ m} $$
2.  Compute potential difference term:
    $$ \frac{1}{R_E} = \frac{1}{6.371 \times 10^6} \approx 1.5696 \times 10^{-7} \text{ m}^{-1} $$
    $$ \frac{1}{r} = \frac{1}{2.6562 \times 10^7} \approx 0.3765 \times 10^{-7} \text{ m}^{-1} $$
    $$ \left( \frac{1}{R_E} - \frac{1}{r} \right) \approx (1.5696 - 0.3765) \times 10^{-7} = 1.1931 \times 10^{-7} \text{ m}^{-1} $$
3.  Compute fractional shift:
    $$ \delta_{\text{grav}} \approx (4.4350 \times 10^{-3}) \times (1.1931 \times 10^{-7}) \approx 5.2915 \times 10^{-10} $$
4.  Convert to microseconds per day:
    $$ \text{Rate}_{\text{grav}} = \delta_{\text{grav}} \times T_{\text{day}} \times 10^6 $$
    $$ \text{Rate}_{\text{grav}} \approx 5.2915 \times 10^{-10} \times 86\,400 \times 10^6 \approx 45.72 \text{ } \mu\text{s/day} $$

**Result:** The gravitational effect causes the satellite clock to run faster by approximately **45.72 $\mu$s/day**.

### 2. Velocity Time Dilation (Special Relativity)

According to Special Relativity, a moving clock runs slower than a stationary clock. The fractional frequency shift due to velocity $v$ is:
$$ \frac{\Delta f}{f} = -\frac{v^2}{2c^2} $$
For a circular orbit, the orbital speed squared is $v^2 = \frac{GM_E}{r}$.
Thus, the fractional rate difference is:
$$ \delta_{\text{vel}} = -\frac{GM_E}{2 r c^2} $$

**Calculation:**
1.  Compute $GM_E / (2 r c^2)$:
    $$ \frac{GM_E}{c^2} \approx 4.4350 \times 10^{-3} \text{ m} $$
    $$ \frac{1}{r} \approx 0.3765 \times 10^{-7} \text{ m}^{-1} $$
    $$ \frac{GM_E}{2 r c^2} = \frac{1}{2} \times (4.4350 \times 10^{-3}) \times (0.3765 \times 10^{-7}) \approx 8.3485 \times 10^{-11} $$
2.  Convert to microseconds per day:
    $$ \text{Rate}_{\text{vel}} = \delta_{\text{vel}} \times T_{\text{day}} \times 10^6 $$
    $$ \text{Rate}_{\text{vel}} \approx -8.3485 \times 10^{-11} \times 86\,400 \times 10^6 \approx -7.21 \text{ } \mu\text{s/day} $$

**Result:** The velocity effect causes the satellite clock to run slower by approximately **7.21 $\mu$s/day**.

### 3. Net Rate Difference

The net rate difference is the sum of the gravitational and velocity effects:
$$ \delta_{\text{net}} = \delta_{\text{grav}} + \delta_{\text{vel}} $$
$$ \delta_{\text{net}} \approx 45.72 - 7.21 = 38.51 \text{ } \mu\text{s/day} $$

**Result:** The net effect is that the satellite clock runs faster by approximately **38.51 $\mu$s/day**.

### 4. Ranging Error and Sign Explanation

**Ranging Error:**
If the clock is uncorrected, it accumulates a time error of $38.51 \times 10^{-6}$ seconds per day. Since GPS ranging relies on the speed of light ($c \approx 3 \times 10^8$ m/s), this time error translates to a distance error:
$$ \text{Error} = c \times \Delta t \approx (3 \times 10^8 \text{ m/s}) \times (38.51 \times 10^{-6} \text{ s}) \approx 11\,553 \text{ m} $$
More precisely using $c = 299\,792\,458$ m/s:
$$ \text{Error} \approx 299\,792\,458 \times 38.51 \times 10^{-6} \approx 11\,546 \text{ m} $$
So, the ranging error accumulates to approximately **11.5 km per day**.

**Explanation of Opposite Signs:**
The two effects have opposite signs because they arise from different physical principles acting in opposite directions on the clock rate:
1.  **Gravitational Effect (General Relativity):** The satellite is at a higher altitude than the ground clock, meaning it is in a weaker gravitational potential (less negative). General Relativity dictates that clocks run faster in weaker gravitational fields. This effect makes the satellite clock run **faster** (positive shift).
2.  **Velocity Effect (Special Relativity):** The satellite is moving at high orbital speed relative to the ground. Special Relativity dictates that moving clocks run slower (time dilation). This effect makes the satellite clock run **slower** (negative shift).

Since the satellite is both higher (faster) and moving (slower), the effects oppose each other. In the case of GPS, the gravitational effect dominates, resulting in a net positive shift (satellite clock runs faster).

FINAL ANSWER

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 45.72 \\
\mathrm{velocity\_shift\_us\_day} &= -7.21 \\
\mathrm{net\_shift\_us\_day} &= 38.51
\end{aligned}
\]