To compute the relativistic clock corrections for a GPS satellite, we compare the proper time of the satellite clock ($\tau_{sat}$) and the ground clock ($\tau_{ground}$) relative to a coordinate time $t$ (the time measured by an observer at infinity).

The general expression for the rate of a clock in a weak gravitational field is:
$\frac{d\tau}{dt} \approx 1 + \frac{\Phi}{c^2} - \frac{v^2}{2c^2}$
where $\Phi = -GM/r$ is the gravitational potential.

**Constants:**
$GM_E = 3.986 \times 10^{14} \text{ m}^3/\text{s}^2$
$R_E = 6.371 \times 10^6 \text{ m}$
$r = 2.6562 \times 10^7 \text{ m}$
$c = 2.9979 \times 10^8 \text{ m/s}$
$1 \text{ day} = 86,400 \text{ s}$

### 1. Gravitational Rate Difference
The gravitational shift is determined by the difference in potential between the satellite and the ground:
$\Delta f_{grav} = \frac{\Phi_{sat} - \Phi_{ground}}{c^2} = \frac{GM_E}{c^2} \left( \frac{1}{R_E} - \frac{1}{r} \right)$

Calculation:
$\frac{GM_E}{c^2} = \frac{3.986 \times 10^{14}}{(2.9979 \times 10^8)^2} \approx 4.435 \times 10^{-3} \text{ m}$
$\frac{1}{R_E} - \frac{1}{r} = \frac{1}{6.371 \times 10^6} - \frac{1}{2.6562 \times 10^7} \approx 1.5696 \times 10^{-7} - 3.7648 \times 10^{-8} = 1.1931 \times 10^{-7} \text{ m}^{-1}$
$\Delta f_{grav} = (4.435 \times 10^{-3}) \times (1.1931 \times 10^{-7}) \approx 5.291 \times 10^{-10}$

Convert to $\mu\text{s/day}$:
$\text{Shift} = 5.291 \times 10^{-10} \times 86,400 \text{ s/day} \times 10^6 \mu\text{s/s} \approx 45.73 \mu\text{s/day}$
Since $\Phi_{sat} > \Phi_{ground}$ (satellite is higher in the potential well), the satellite clock runs **faster**.

### 2. Velocity Rate Difference
The velocity shift (Special Relativity) is given by:
$\Delta f_{vel} = -\frac{v_{sat}^2 - v_{ground}^2}{2c^2}$
Per instructions, we ignore Earth's rotation ($v_{ground} = 0$) and use $v_{sat}^2 = GM_E/r$.
$\Delta f_{vel} = -\frac{GM_E}{2rc^2}$

Calculation:
$\Delta f_{vel} = -\frac{3.986 \times 10^{14}}{2 \times (2.6562 \times 10^7) \times (2.9979 \times 10^8)^2} \approx -\frac{3.986 \times 10^{14}}{4.774 \times 10^{24}} \approx -8.349 \times 10^{-11}$

Convert to $\mu\text{s/day}$:
$\text{Shift} = -8.349 \times 10^{-11} \times 86,400 \times 10^6 \approx -7.21 \mu\text{s/day}$
The satellite clock runs **slower** due to its orbital velocity.

### 3. Net Rate
$\text{Net Shift} = \text{Gravitational Shift} + \text{Velocity Shift}$
$\text{Net Shift} = 45.73 \mu\text{s/day} - 7.21 \mu\text{s/day} = 38.52 \mu\text{s/day}$

### 4. Ranging Error and Physical Explanation
The ranging error is the distance light travels in the accumulated time offset:
$\text{Error} = c \times \Delta t = (2.9979 \times 10^8 \text{ m/s}) \times (38.52 \times 10^{-6} \text{ s}) \approx 11,548 \text{ km/day}$.

**Explanation of signs:**
The gravitational effect is positive because the satellite is in a region of higher gravitational potential (further from the mass), causing time to pass faster (General Relativity). The velocity effect is negative because the satellite is moving relative to the ground observer, causing time dilation (Special Relativity).

FINAL ANSWER

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 45.73 \\
\mathrm{velocity\_shift\_us\_day} &= -7.21 \\
\mathrm{net\_shift\_us\_day} &= 38.52
\end{aligned}
\]