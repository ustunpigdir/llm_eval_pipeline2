**1. Gravitational (Blueshift) Rate Difference**

The gravitational blueshift is given by the formula:
\[
\Delta f = -\frac{GM}{rc^2}
\]
where $G$ is the gravitational constant, $M$ is the mass of the Earth, $r$ is the distance from the Earth's center to the GPS satellite, and $c$ is the speed of light. Plugging in the given values:
\[
\Delta f = -\frac{(3.986 \times 10^{14} \text{ m}^3/\text{s}^2)(26562 \text{ km})}{c^2}
\]
Converting $c$ to km/s and $r$ to m:
\[
\Delta f = -\frac{(3.986 \times 10^{14})(26562 \times 10^3)}{(299792.458 \times 10^3)^2} \text{ Hz}
\]
\[
\Delta f \approx -4.47 \times 10^{-10} \text{ Hz}
\]
To find the rate difference in microseconds per day, we convert Hz to microseconds and multiply by the number of seconds in a day:
\[
\Delta t = \frac{\Delta f}{f} \times \frac{1 \text{ day}}{1 \text{ s}} \times 10^6 \text{ \mu s}
\]
\[
\Delta t \approx \frac{-4.47 \times 10^{-10}}{10^9} \times 86400 \times 10^6 \text{ \mu s/day}
\]
\[
\Delta t \approx -3.87 \text{ \mu s/day}
\]
The satellite clock runs faster by about 3.87 microseconds per day.

**2. Velocity (Time-Dilation) Rate Difference**

The special-relativistic time dilation is given by:
\[
\Delta t = -\frac{v^2}{2c^2}t
\]
where $v$ is the orbital speed of the satellite. The orbital speed can be approximated as:
\[
v = \sqrt{\frac{GM}{r}}
\]
Plugging in the values:
\[
v \approx \sqrt{\frac{(3.986 \times 10^{14})(26562 \times 10^3)}{(299792.458 \times 10^3)^2}} \text{ km/s}
\]
\[
v \approx 7.71 \text{ km/s}
\]
Now, calculate the time dilation:
\[
\Delta t = -\frac{(7.71 \times 10^3)^2}{2(299792.458 \times 10^3)^2} \times 86400 \text{ s}
\]
\[
\Delta t \approx -1.54 \text{ \mu s/day}
\]
The satellite clock runs slower by about 1.54 microseconds per day.

**3. Net Rate**

The net rate is the sum of the gravitational and velocity rate differences:
\[
\Delta t_{\text{net}} = \Delta t_{\text{grav}} + \Delta t_{\text{vel}}
\]
\[
\Delta t_{\text{net}} \approx -3.87 + 1.54 \text{ \mu s/day}
\]
\[
\Delta t_{\text{net}} \approx -2.33 \text{ \mu s/day}
\]
The satellite clock runs slower than the ground clock by about 2.33 microseconds per day.

**4. Ranging Error**

The ranging error is the product of the net rate and the time:
\[
\text{Error} = \Delta t_{\text{net}} \times t
\]
\[
\text{Error} \approx -2.33 \times 86400 \text{ \mu s}
\]
\[
\text{Error} \approx -201.44 \text{ \mu s}
\]
The two effects have opposite signs because the gravitational blueshift causes the satellite clock to run faster, while the special-relativistic time dilation causes it to run slower. The net effect is that the satellite clock runs slower than the ground clock.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= -3.87 \\
\mathrm{velocity\_shift\_us\_day} &= -1.54 \\
\mathrm{net\_shift\_us\_day} &= -2.33
\end{aligned}
\]