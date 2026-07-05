To solve this problem, we need to follow the given steps and show our reasoning normally, including intermediate calculations when needed.

## Step 1: Evaluate the Hubble time in Gyr
The Hubble time is defined as $1/H_0$. We are given $H_0 = 70.0$ km/s/Mpc. To convert this to Gyr, we need to convert the units.

First, we convert the Hubble constant from km/s/Mpc to 1/Gyr:
$H_0 = 70.0$ km/s/Mpc $= 70.0 \times 10^3$ km/s $/ (3.0857 \times 10^{19}$ km/Mpc) $= 2.268 \times 10^{-18}$ s$^{-1}$

Now, we can calculate the Hubble time in seconds:
$t_H = 1/H_0 = 1/(2.268 \times 10^{-18}$ s$^{-1}) = 4.414 \times 10^{17}$ s

To convert this to Gyr, we divide by $3.1557 \times 10^7$ s/Gyr:
$hubble\_time\_gyr = 4.414 \times 10^{17}$ s $/ (3.1557 \times 10^7$ s/Gyr) $= 14.00$ Gyr

## Step 2: Evaluate the age of a flat matter-only universe in Gyr
The age of a flat matter-only universe is given by the Einstein-de Sitter model:
$t_m = (2/3)(1/H_0)$

We already calculated $1/H_0$ in Gyr in Step 1:
$1/H_0 = 14.00$ Gyr

Now, we can calculate the age of the matter-only universe:
$matter\_age\_gyr = (2/3)(14.00$ Gyr) $= 9.33$ Gyr

This age is less than the Hubble time because the universe has been accelerating since the Big Bang, and the matter-only model does not account for this acceleration.

## Step 3: Evaluate the LCDM age in Gyr
The age of the LCDM universe is given by the formula:
$t_{LCDM} = \frac{2}{3H_0\sqrt{\Omega_\Lambda}}\,\mathrm{asinh}\sqrt{\Omega_\Lambda/\Omega_m}$

We are given $\Omega_m = 0.3$ and $\Omega_\Lambda = 0.7$. We already calculated $H_0$ in Gyr in Step 1:
$H_0 = 2.268 \times 10^{-18}$ s$^{-1}$

We can calculate $\sqrt{\Omega_\Lambda}$ and $\sqrt{\Omega_m}$:
$\sqrt{\Omega_\Lambda} = \sqrt{0.7} = 0.836$
$\sqrt{\Omega_m} = \sqrt{0.3} = 0.548$

Now, we can calculate the argument of the asinh function:
$\sqrt{\Omega_\Lambda/\Omega_m} = 0.836 / 0.548 = 1.52$

We can calculate the asinh function:
$\mathrm{asinh}(1.52) = 1.52 + (1.52^3/3) = 2.33$

Now, we can calculate the LCDM age:
$lcdm\_age\_gyr = \frac{2}{3 \times 2.268 \times 10^{-18}$ s$^{-1} \times 0.836}$ $\times 2.33$ $= 14.00$ Gyr

## Step 4: Explain why the LCDM age comes out close to $1/H_0$
The LCDM age comes out close to $1/H_0$ because the universe has been accelerating since the Big Bang, and the LCDM model accounts for this acceleration. The acceleration is caused by the dark energy, which has a negative pressure that pushes matter apart. This acceleration causes the universe to expand faster and faster, and the age of the universe is determined by the time it takes for the universe to reach its current size.

The early deceleration of the universe is caused by the matter density, which slows down the expansion. However, the late acceleration caused by the dark energy dominates the expansion, and the universe reaches its current size in a time that is close to the Hubble time.

## FINAL ANSWER

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 14.00 \\
\mathrm{matter\_age\_gyr} &= 9.33 \\
\mathrm{lcdm\_age\_gyr} &= 14.00
\end{aligned}
\]