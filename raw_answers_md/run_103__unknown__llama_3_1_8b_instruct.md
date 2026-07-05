To solve this problem, we need to follow the given steps and show our reasoning normally, including intermediate calculations when needed.

## Step 1: Evaluate the Hubble time in Gyr
The Hubble time is given by $1/H_0$. We need to convert the Hubble constant from km/s/Mpc to Gyr. We know that $1 \text{ Gyr} = 3.1557 \times 10^{16} \text{ s}$ and $1 \text{ Mpc} = 3.0857 \times 10^{19} \text{ km}$.

First, we need to convert the Hubble constant from km/s/Mpc to s$^{-1}$:
\[H_0 = 70.0 \text{ km/s/Mpc} = \frac{70.0 \text{ km/s}}{3.0857 \times 10^{19} \text{ km}} = 2.268 \times 10^{-18} \text{ s}^{-1}\]

Now, we can calculate the Hubble time in seconds:
\[t_H = \frac{1}{H_0} = \frac{1}{2.268 \times 10^{-18} \text{ s}^{-1}} = 4.41 \times 10^{17} \text{ s}\]

Finally, we can convert the Hubble time from seconds to Gyr:
\[t_H = \frac{4.41 \times 10^{17} \text{ s}}{3.1557 \times 10^{16} \text{ s/Gyr}} = 13.96 \text{ Gyr}\]

## Step 2: Evaluate the age of a flat matter-only universe in Gyr
The age of a flat matter-only universe is given by the Einstein-de Sitter model:
\[t_{\text{matter}} = \frac{2}{3H_0}\]

We already calculated the Hubble time in Gyr in Step 1:
\[t_H = 13.96 \text{ Gyr}\]

Now, we can calculate the age of a flat matter-only universe:
\[t_{\text{matter}} = \frac{2}{3}t_H = \frac{2}{3} \times 13.96 \text{ Gyr} = 9.31 \text{ Gyr}\]

## Step 3: Evaluate the LCDM age in Gyr with the given formula
The LCDM age is given by the formula:
\[t_{\text{LCDM}} = \frac{2}{3H_0\sqrt{\Omega_\Lambda}}\,\mathrm{asinh}\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\]

We are given $\Omega_m = 0.3$ and $\Omega_\Lambda = 0.7$. We already calculated the Hubble time in Gyr in Step 1:
\[t_H = 13.96 \text{ Gyr}\]

Now, we can calculate the LCDM age:
\[t_{\text{LCDM}} = \frac{2}{3 \times 2.268 \times 10^{-18} \text{ s}^{-1} \sqrt{0.7}} \times \mathrm{asinh}\sqrt{\frac{0.7}{0.3}}\]

First, we need to calculate the argument of the asinh function:
\[\sqrt{\frac{0.7}{0.3}} = \sqrt{2.333} = 1.53\]

Now, we can calculate the asinh function:
\[\mathrm{asinh}(1.53) = \ln(1.53 + \sqrt{1.53^2 + 1}) = 1.16\]

Now, we can calculate the LCDM age:
\[t_{\text{LCDM}} = \frac{2}{3 \times 2.268 \times 10^{-18} \text{ s}^{-1} \sqrt{0.7}} \times 1.16 = 13.85 \text{ Gyr}\]

## Step 4: Explain why the LCDM age comes out close to $1/H_0$
The LCDM age comes out close to $1/H_0$ because the universe underwent a period of deceleration in the past, which caused the age of the universe to be less than $1/H_0$. However, in the distant future, the universe will undergo a period of acceleration, which will cause the age of the universe to be greater than $1/H_0$. The LCDM age is a compromise between these two periods, and it comes out close to $1/H_0$.

## FINAL ANSWER

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 13.96 \\
\mathrm{matter\_age\_gyr} &= 9.31 \\
\mathrm{lcdm\_age\_gyr} &= 13.85
\end{aligned}
\]