
Let's break down the calculation of luminosity distances using the provided formula and parameters.

1. **Evaluate the Hubble distance $c/H_0$ in Mpc and the linear term $cz/H_0$ at $z = 0.200$.**

First, we need to convert $H_0$ from km/s/Mpc to $s^{-1}$.
$H_0 = 70.0 \text{ km/s/Mpc} = 70.0 \times \frac{1000 \text{ m/s}}{1 \text{ Mpc}} = 70.0 \times \frac{10^3 \text{ m/s}}{1 \text{ Mpc}}$.
Since 1 Mpc = $3.086 \times 10^{19}$ m, we have
$H_0 = 70.0 \times \frac{10^3}{3.086 \times 10^{19}} \text{ s}^{-1} \approx 2.27 \times 10^{-18} \text{ s}^{-1}$.
The speed of light, $c = 3.00 \times 10^8 \text{ m/s}$.
Therefore, the Hubble distance is:
$d_H = \frac{c}{H_0} = \frac{3.00 \times 10^8 \text{ m/s}}{2.27 \times 10^{-18} \text{ s}^{-1}} \approx 1.32 \times 10^{26} \text{ m}$.
Converting to Mpc:
$d_H = \frac{1.32 \times 10^{26} \text{ m}}{3.086 \times 10^{19} \text{ m/Mpc}} \approx 4270 \text{ Mpc}$.

Now, let's calculate the linear term $cz/H_0$ at $z = 0.200$.
$cz = 0.200c = 0.200 \times 3.00 \times 10^8 \text{ m/s} = 6.00 \times 10^7 \text{ m/s}$.
$cz/H_0 = \frac{6.00 \times 10^7 \text{ m/s}}{2.27 \times 10^{-18} \text{ s}^{-1}} \approx 2.64 \times 10^{25} \text{ m}$.
Converting to Mpc:
$cz/H_0 = \frac{2.64 \times 10^{25} \text{ m}}{3.086 \times 10^{19} \text{ m/Mpc}} \approx 8557 \text{ Mpc}$.

2. **Evaluate $d_L$ at $z = 0.2$ for LCDM ($q_0 = -0.55$).**

$d_L = \frac{cz}{H_0}\left[1 + \frac{(1-q_0)z}{2}\right] = 8557 \left[1 + \frac{(1 - (-0.55)) \times 0.2}{2}\right] = 8557 \left[1 + \frac{1.55 \times 0.2}{2}\right] = 8557 \left[1 + 0.155\right] = 8557 \times 1.155 \approx 9883 \text{ Mpc}$.

3. **Evaluate $d_L$ at $z = 0.2$ for Einstein-de Sitter ($q_0 = +0.5$).**

$d_L = \frac{cz}{H_0}\left[1 + \frac{(1-q_0)z}{2}\right] = 8557 \left[1 + \frac{(1 - 0.5) \times 0.2}{2}\right] = 8557 \left[1 + \frac{0.5 \times 0.2}{2}\right] = 8557 \left[1 + 0.05\right] = 8557 \times 1.05 \approx 8985 \text{ Mpc}$.

4. **A supernova at $z = 0.2$ appears FAINTER than the EdS prediction. Which model does that favor, and why? Relate to the 1998 discovery.**

The supernova appears fainter than the EdS prediction, meaning the luminosity distance is *larger* than predicted by EdS.  Since $d_L$ is larger for LCDM (9883 Mpc) than for EdS (8985 Mpc) at $z=0.2$, the LCDM model is favored. This is because a larger luminosity distance implies a greater amount of dimming, and thus a fainter apparent brightness.

This result is directly related to the 1998 discovery of the accelerating expansion of the universe. The observation of Type Ia supernovae at high redshifts being fainter than expected (based on EdS cosmology) was the primary evidence for the existence of dark energy and the accelerating expansion. The LCDM model, which includes a cosmological constant (dark energy), predicts larger luminosity distances at high redshifts, consistent with the supernova observations.



\[
\begin{aligned}
\mathrm{hubble\_distance\_mpc} &= 4270 \\
\mathrm{dl\_linear\_mpc} &= 8557 \\
\mathrm{dl\_lcdm\_mpc} &= 9883 \\
\mathrm{dl\_eds\_mpc} &= 8985
\end{aligned}
\]