Okay, let's break down this problem step-by-step.

1. **Evaluate the Hubble distance $c/H_0$ in Mpc and the linear term $cz/H_0$ at $z = 0.200$.**

First, we need to convert $H_0$ from km/s/Mpc to Mpc/s.  $H_0 = 70.0 \text{ km/s/Mpc} = 70.0 \times 10^5 \text{ m/s/Mpc} = 70.0 \times 10^5 \times 10^{-3} \text{ Mpc/s} = 70 \text{ Mpc/s}$.
The speed of light, $c$, is approximately $3 \times 10^5 \text{ km/s} = 3 \times 10^5 \times 10^3 \text{ m/s} = 3 \times 10^8 \text{ m/s} = 3 \times 10^8 \times 10^{-3} \text{ Mpc/s} = 3 \times 10^5 \text{ Mpc/s}$.

The Hubble distance is $c/H_0 = (3 \times 10^5 \text{ Mpc/s}) / (70 \text{ Mpc/s}) \approx 4285.71 \text{ Mpc}$.

The linear term $cz/H_0$ at $z = 0.2$ is $(c \times z) / H_0 = (3 \times 10^5 \text{ Mpc/s} \times 0.2) / (70 \text{ Mpc/s}) = (6 \times 10^4) / 70 \approx 857.14 \text{ Mpc}$.

2. **Evaluate $d_L$ at $z = 0.2$ for LCDM ($q_0 = -0.55$).**

The luminosity distance formula is $d_L = \frac{cz}{H_0}\left[1 + \frac{(1-q_0)z}{2}\right]$.
For LCDM, $q_0 = -0.55$.  So,
$d_L = \frac{cz}{H_0}\left[1 + \frac{(1-(-0.55))z}{2}\right] = \frac{cz}{H_0}\left[1 + \frac{1.55z}{2}\right]$.
Plugging in $z = 0.2$, we get
$d_L = 857.14 \left[1 + \frac{1.55(0.2)}{2}\right] = 857.14 \left[1 + \frac{0.31}{2}\right] = 857.14 [1 + 0.155] = 857.14 \times 1.155 \approx 993.14 \text{ Mpc}$.

3. **Evaluate $d_L$ at $z = 0.2$ for Einstein-de Sitter ($q_0 = +0.5$).**

For EdS, $q_0 = 0.5$.  So,
$d_L = \frac{cz}{H_0}\left[1 + \frac{(1-0.5)z}{2}\right] = \frac{cz}{H_0}\left[1 + \frac{0.5z}{2}\right]$.
Plugging in $z = 0.2$, we get
$d_L = 857.14 \left[1 + \frac{0.5(0.2)}{2}\right] = 857.14 \left[1 + \frac{0.1}{2}\right] = 857.14 [1 + 0.05] = 857.14 \times 1.05 \approx 900 \text{ Mpc}$.

4. **A supernova at $z = 0.2$ appears FAINTER than the EdS prediction. Which model does that favor, and why? Relate to the 1998 discovery.**

A supernova appears fainter than predicted by EdS means its distance is *greater* than predicted by EdS.  Since $d_L$ for LCDM is larger than $d_L$ for EdS at $z=0.2$, the LCDM model is favored.

The 1998 discovery of accelerating expansion of the universe was based on observations of Type Ia supernovae. These supernovae were found to be fainter (and thus further away) than expected in a decelerating universe (like EdS). This observation strongly supported the existence of dark energy and favored models like LCDM, which have a negative deceleration parameter ($q_0 < 0$).  A negative $q_0$ implies acceleration, which leads to larger distances at a given redshift than predicted by a decelerating universe.

\[
\begin{aligned}
\mathrm{hubble\_distance\_mpc} &= 4285.71 \\
\mathrm{dl\_linear\_mpc} &= 857.14 \\
\mathrm{dl\_lcdm\_mpc} &= 993.14 \\
\mathrm{dl\_eds\_mpc} &= 900.00
\end{aligned}
\]