Here's the derivation of the GPS relativistic clock corrections, following the specified requirements.

**1. Gravitational (Blueshift) Rate Difference**

The gravitational time dilation formula relates the time interval $dt_s$ on the satellite to the time interval $dt_g$ on the ground:

$dt_s = dt_g \sqrt{1 - \frac{2GM_E}{rc^2}}$

where $G$ is the gravitational constant, $M_E$ is the Earth's mass, $r$ is the satellite's orbital radius, $c$ is the speed of light.

We want to find the rate difference, which is $\frac{dt_s}{dt_g} - 1$.  From the equation above, $\frac{dt_s}{dt_g} = \sqrt{1 - \frac{2GM_E}{rc^2}}$.  Therefore,

$\frac{dt_s}{dt_g} - 1 = \sqrt{1 - \frac{2GM_E}{rc^2}} - 1$

Now, we plug in the values:
$r = 26562 \times 10^3$ m
$GM_E = 3.986 \times 10^{14}$ m$^3$/s$^2$
$c = 2.998 \times 10^8$ m/s

$\frac{2GM_E}{rc^2} = \frac{2 \times 3.986 \times 10^{14}}{26562 \times 10^3 \times (2.998 \times 10^8)^2} = \frac{7.972 \times 10^{14}}{2.6562 \times 10^9 \times 9.0 \times 10^{16}} \approx \frac{7.972 \times 10^{14}}{2.39 \times 10^{26}} \approx 3.32 \times 10^{-12}$

$\sqrt{1 - 3.32 \times 10^{-12}} \approx 1 - \frac{1}{2} (3.32 \times 10^{-12}) = 1 - 1.66 \times 10^{-12}$

So, $\frac{dt_s}{dt_g} - 1 \approx -1.66 \times 10^{-12}$

This means the satellite clock runs *faster* than the ground clock.  We need to convert this to microseconds per day.

There are $86400$ seconds in a day.
$-1.66 \times 10^{-12} \times 86400 = -1.435 \times 10^{-8}$

Therefore, the gravitational blueshift is approximately $-1.435 \times 10^{-8}$ seconds/day.  To convert to microseconds/day, multiply by $10^6$:

$-1.435 \times 10^{-8} \times 10^6 = -14.35 \times 10^{-6} \approx -14.4 \mu$s/day.

So, $\mathrm{grav\_shift\_us\_day} = -14.4$

**2. Velocity (Time-Dilation) Rate Difference**

The special relativistic time dilation formula is:

$dt_s = dt_g \sqrt{1 - \frac{v^2}{c^2}}$

where $v$ is the satellite's velocity.  We have $v^2 = \frac{GM_E}{r}$.

$\frac{dt_s}{dt_g} = \sqrt{1 - \frac{v^2}{c^2}} = \sqrt{1 - \frac{GM_E}{rc^2}}$

This is the same expression as the gravitational time dilation.  We already calculated $\frac{GM_E}{rc^2} = 3.32 \times 10^{-12}$.

$\frac{dt_s}{dt_g} - 1 = \sqrt{1 - 3.32 \times 10^{-12}} - 1 \approx -1.66 \times 10^{-12}$

The velocity effect is also $-1.66 \times 10^{-12}$.  Converting to microseconds/day:

$-1.66 \times 10^{-12} \times 86400 \times 10^6 = -14.35 \mu$s/day.

So, $\mathrm{velocity\_shift\_us\_day} = -14.4$

**3. Net Rate**

The net rate is the sum of the gravitational and velocity effects:

$\mathrm{net\_shift\_us\_day} = \mathrm{grav\_shift\_us\_day} + \mathrm{velocity\_shift\_us\_day} = -14.4 + (-14.4) = -28.8 \mu$s/day.

**4. Ranging Error**

If uncorrected, the satellite's clock will be off by $-28.8 \mu$s/day.  The GPS system uses two-way ranging, so the error is doubled.  The time it takes for a signal to travel from the satellite to the receiver and back is measured.  If the satellite clock is off, the measured distance will be incorrect.

The speed of light is $c = 3 \times 10^8$ m/s.  The error in distance is:

$\Delta d = 2c \Delta t = 2 \times 3 \times 10^8 \times 28.8 \times 10^{-6} = 6 \times 10^8 \times 28.8 \times 10^{-6} = 172.8$ meters.

So, the ranging error accumulates to 172.8 meters in one day.

The two effects have opposite signs because one is due to the gravitational potential difference (blueshift), and the other is due to the satellite's velocity (time dilation).  The gravitational effect makes the satellite clock run faster, while the velocity effect makes it run slower.  However, in this case, the two effects are identical in magnitude and sign.

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= -14.4 \\
\mathrm{velocity\_shift\_us\_day} &= -14.4 \\
\mathrm{net\_shift\_us\_day} &= -28.8
\end{aligned}
\]