Here's the derivation of the GPS relativistic clock corrections, following the specified instructions.

**1. Gravitational (Blueshift) Rate Difference**

The gravitational time dilation formula relates the time dilation factor to the gravitational potential. The potential difference between the satellite and the Earth's surface is given by:

$\Delta V = V(r) - V(R_E) = -\frac{GM_E}{r} - \left(-\frac{GM_E}{R_E}\right) = GM_E \left(\frac{1}{R_E} - \frac{1}{r}\right)$

Plugging in the given values:
$r = 26562 \times 10^3$ m
$R_E = 6371 \times 10^3$ m
$GM_E = 3.986 \times 10^{14}$ m$^3$/s$^2$

$\Delta V = (3.986 \times 10^{14}) \left(\frac{1}{6371 \times 10^3} - \frac{1}{26562 \times 10^3}\right)$
$\Delta V = (3.986 \times 10^{14}) \left(1.5696 \times 10^{-7} - 3.7765 \times 10^{-8}\right)$
$\Delta V = (3.986 \times 10^{14}) (1.192 \times 10^{-7})$
$\Delta V = 4.742 \times 10^7$ J/kg

The time dilation factor is given by:
$\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 + \frac{2\Delta V}{mc^2}}$
where $m$ is the mass of the clock and $c$ is the speed of light.  Since we are interested in the *difference* in rates, we can use the approximation $\Delta t_s/\Delta t_g \approx 1 + \frac{\Delta V}{mc^2}$.  The rate difference is then:

$\frac{\Delta t_s}{\Delta t_g} - 1 = \frac{\Delta V}{mc^2}$

We don't know $m$, but we can express the rate difference as a fractional change in time.  The gravitational blueshift means the satellite clock runs *faster*.  We want to find the rate difference in microseconds per day.

The fractional change in time is $\frac{\Delta V}{mc^2}$.  We can express this as a rate difference per second, then convert to microseconds per day.  Let's assume a clock mass of 1 kg (this is an assumption, but it allows us to proceed). Then:

$\frac{\Delta V}{mc^2} = \frac{4.742 \times 10^7}{1 \times (3 \times 10^8)^2} = \frac{4.742 \times 10^7}{9 \times 10^{16}} = 5.269 \times 10^{-10}$

This is the fractional change per second.  To convert to microseconds per day:

$5.269 \times 10^{-10} \frac{\text{s}}{\text{s}} \times \frac{10^6 \text{ } \mu\text{s}}{1 \text{ s}} \times 86400 \frac{\text{s}}{\text{day}} = 5.269 \times 10^{-10} \times 10^6 \times 86400 \frac{\mu\text{s}}{\text{day}} = 454.1 \frac{\mu\text{s}}{\text{day}}$

So, the gravitational blueshift causes the satellite clock to run 454.1 microseconds per day faster than the ground clock.

**2. Velocity (Time-Dilation) Rate Difference**

The special relativistic time dilation formula is:

$\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{v^2}{c^2}}$

where $v$ is the satellite's orbital speed.  We have $v^2 = \frac{GM_E}{r}$.

$v^2 = \frac{3.986 \times 10^{14}}{26562 \times 10^3} = 1.500 \times 10^9$ m$^2$/s$^2$
$v = \sqrt{1.500 \times 10^9} = 38730$ m/s

$\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{1.500 \times 10^9}{(3 \times 10^8)^2}} = \sqrt{1 - \frac{1.500 \times 10^9}{9 \times 10^{16}}} = \sqrt{1 - 1.667 \times 10^{-8}} \approx 0.9999999833$

The fractional change in time is $\frac{\Delta t_s}{\Delta t_g} - 1 \approx -1.667 \times 10^{-8}$.  This is the fractional change per second.  To convert to microseconds per day:

$-1.667 \times 10^{-8} \frac{\text{s}}{\text{s}} \times \frac{10^6 \text{ } \mu\text{s}}{1 \text{ s}} \times 86400 \frac{\text{s}}{\text{day}} = -1.667 \times 10^{-8} \times 10^6 \times 86400 \frac{\mu\text{s}}{\text{day}} = -142.9 \frac{\mu\text{s}}{\text{day}}$

The velocity time dilation causes the satellite clock to run 142.9 microseconds per day *slower* than the ground clock.

**3. Net Rate**

The net rate difference is the sum of the gravitational and velocity effects:

$454.1 \frac{\mu\text{s}}{\text{day}} - 142.9 \frac{\mu\text{s}}{\text{day}} = 311.2 \frac{\mu\text{s}}{\text{day}}$

The net effect is that the satellite clock runs 311.2 microseconds per day faster than the ground clock.

**4. Ranging Error**

If uncorrected, the error in one day would be the net rate difference multiplied by the time it takes for a signal to travel to the satellite and back.  The distance to the satellite is $r = 26562$ km, so the round-trip distance is $2r = 53124$ km.  The time for the signal to travel is:

$t = \frac{2r}{c} = \frac{53124 \times 10^3}{3 \times 10^8} = 0.1771 \text{ s}$

The error in one day is:

$311.2 \frac{\mu\text{s}}{\text{day}} \times 86400 \frac{\text{s}}{\text{day}} \times 0.1771 \text{ s} = 311.2 \times 86400 \times 0.1771 \text{ m} = 48000 \text{ m} \approx 48 \text{ km}$

The two effects have opposite signs because one is due to the difference in gravitational potential (blueshift, satellite clock runs faster), and the other is due to the satellite's velocity (time dilation, satellite clock runs slower).

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 454.1 \\
\mathrm{velocity\_shift\_us\_day} &= -142.9 \\
\mathrm{net\_shift\_us\_day} &= 311.2
\end{aligned}
\]