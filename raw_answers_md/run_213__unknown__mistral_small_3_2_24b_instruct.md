To solve this problem, we need to compute the relativistic effects on the GPS satellite clocks compared to a ground clock. We will consider both the gravitational (blueshift) effect and the velocity (time-dilation) effect separately, then combine them to find the net effect.

### 1. Gravitational (Blueshift) Rate Difference

The gravitational time dilation effect is given by the general relativistic formula:

\[
\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{2GM_E}{rc^2}}
\]

where:
- \( \Delta t_s \) is the time interval measured by the satellite clock,
- \( \Delta t_g \) is the time interval measured by the ground clock,
- \( G \) is the gravitational constant,
- \( M_E \) is the mass of the Earth,
- \( r \) is the distance from the center of the Earth to the satellite,
- \( c \) is the speed of light.

The rate difference due to the gravitational effect is:

\[
\frac{\Delta t_s}{\Delta t_g} - 1 \approx \frac{GM_E}{rc^2}
\]

Given:
- \( GM_E = 3.986 \times 10^{14} \, \text{m}^3/\text{s}^2 \),
- \( r = 26,562 \, \text{km} = 26,562,000 \, \text{m} \),
- \( c = 3 \times 10^8 \, \text{m/s} \).

First, compute \( \frac{GM_E}{rc^2} \):

\[
\frac{GM_E}{rc^2} = \frac{3.986 \times 10^{14}}{26,562,000 \times (3 \times 10^8)^2} = \frac{3.986 \times 10^{14}}{26,562,000 \times 9 \times 10^{16}} = \frac{3.986 \times 10^{14}}{2.39058 \times 10^{23}} \approx 1.667 \times 10^{-9}
\]

This is the fractional rate difference per second. To convert this to microseconds per day:

\[
1.667 \times 10^{-9} \, \text{per second} \times 86,400 \, \text{seconds/day} \times 10^6 \, \mu\text{s/s} = 144 \, \mu\text{s/day}
\]

Since the satellite is at a higher gravitational potential (further from the Earth), it runs faster than the ground clock.

### 2. Velocity (Time-Dilation) Rate Difference

The special relativistic time dilation effect is given by:

\[
\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{v^2}{c^2}}
\]

where \( v \) is the orbital speed of the satellite.

Given:
- \( v^2 = \frac{GM_E}{r} \).

First, compute \( v^2 \):

\[
v^2 = \frac{3.986 \times 10^{14}}{26,562,000} \approx 14,630 \, \text{m}^2/\text{s}^2
\]

Now, compute \( \frac{v^2}{c^2} \):

\[
\frac{v^2}{c^2} = \frac{14,630}{(3 \times 10^8)^2} = \frac{14,630}{9 \times 10^{16}} \approx 1.626 \times 10^{-12}
\]

The rate difference due to the velocity effect is:

\[
\frac{\Delta t_s}{\Delta t_g} - 1 \approx -\frac{v^2}{2c^2}
\]

This is the fractional rate difference per second. To convert this to microseconds per day:

\[
1.626 \times 10^{-12} \, \text{per second} \times 86,400 \, \text{seconds/day} \times 10^6 \, \mu\text{s/s} \approx 140.5 \, \mu\text{s/day}
\]

Since the satellite is moving, its clock runs slower than the ground clock.

### 3. Net Rate Difference

The net rate difference is the sum of the gravitational and velocity effects:

\[
\text{Net rate difference} = 144 \, \mu\text{s/day} - 140.5 \, \mu\text{s/day} = 3.5 \, \mu\text{s/day}
\]

### 4. Ranging Error

If uncorrected, the ranging error accumulates as the net rate difference over one day. Since the satellite clock runs faster by 3.5 microseconds per day, the ranging error would be:

\[
3.5 \, \mu\text{s/day} \times c = 3.5 \times 10^{-6} \, \text{s/day} \times 3 \times 10^8 \, \text{m/s} = 1,050 \, \text{m/day}
\]

The two effects have opposite signs because the gravitational effect causes the satellite clock to run faster (blueshift), while the velocity effect causes it to run slower (time dilation).

FINAL ANSWER

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 144 \\
\mathrm{velocity\_shift\_us\_day} &= 140.5 \\
\mathrm{net\_shift\_us\_day} &= 3.5
\end{aligned}
\]