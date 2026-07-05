### 1. Evaluation of the Hubble Time
The Hubble constant is given as $H_0 = 70.0 \text{ km/s/Mpc}$.
The Hubble time is defined as $t_H = 1/H_0$.

First, we convert $H_0$ to inverse seconds ($\text{s}^{-1}$):
$$H_0 = \frac{70.0 \text{ km/s}}{3.0857 \times 10^{19} \text{ km}} = 2.2685 \times 10^{-18} \text{ s}^{-1}$$

Now, calculate $t_H$ in seconds:
$$t_H = \frac{1}{2.2685 \times 10^{-18} \text{ s}^{-1}} = 4.4083 \times 10^{17} \text{ s}$$

Convert seconds to Gigayears (Gyr). 
$1 \text{ year} \approx 31,557,600 \text{ s}$ (using the Julian year $365.25$ days).
$1 \text{ Gyr} = 10^9 \times 31,557,600 \text{ s} = 3.15576 \times 10^{16} \text{ s}$.

$$t_H = \frac{4.4083 \times 10^{17} \text{ s}}{3.15576 \times 10^{16} \text{ s/Gyr}} \approx 13.969 \text{ Gyr}$$

### 2. Age of a Flat Matter-Only Universe
For a flat, matter-dominated universe (Einstein-de Sitter), the Friedmann equation leads to the scale factor $a(t) \propto t^{2/3}$. The age is:
$$t_0 = \frac{2}{3} \frac{1}{H_0} = \frac{2}{3} t_H$$

Calculation:
$$t_{matter} = \frac{2}{3} \times 13.969 \text{ Gyr} \approx 9.313 \text{ Gyr}$$

**Reasoning:** The age is less than $1/H_0$ because gravity from matter causes the expansion rate to decelerate over time. Since the universe was expanding faster in the past than it is now, it reached its current size in less time than a coasting universe (where $H$ is constant) would have.

### 3. Age of the $\Lambda$CDM Universe
Given $\Omega_m = 0.3$ and $\Omega_\Lambda = 0.7$, the age is:
$$t_0 = \frac{2}{3H_0\sqrt{\Omega_\Lambda}} \mathrm{asinh}\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}$$

Substitute the values:
$$\sqrt{\frac{\Omega_\Lambda}{\Omega_m}} = \sqrt{\frac{0.7}{0.3}} = \sqrt{2.3333} \approx 1.5275$$
$$\mathrm{asinh}(1.5275) = \ln(1.5275 + \sqrt{1.5275^2 + 1}) = \ln(1.5275 + 1.8257) = \ln(3.3532) \approx 1.2099$$

Now calculate the pre-factor:
$$\frac{2}{3 H_0 \sqrt{0.7}} = \frac{2 t_H}{3 \sqrt{0.7}} = \frac{2 \times 13.969}{3 \times 0.83666} = \frac{27.938}{2.510} \approx 11.131 \text{ Gyr}$$

Total age:
$$t_{LCDM} = 11.131 \text{ Gyr} \times 1.2099 \approx 13.467 \text{ Gyr}$$

### 4. Comparison and Physical Reasoning
The $\Lambda$CDM age ($\approx 13.47$ Gyr) is very close to the Hubble time ($\approx 13.97$ Gyr). This is a result of two competing effects:
1. **Early Deceleration:** In the early universe, matter dominated, causing the expansion to slow down (which tends to make the age smaller than $1/H_0$, as seen in the EdS case).
2. **Late Acceleration:** In the recent epoch, dark energy ($\Lambda$) dominates, causing the expansion to accelerate. This means the universe was expanding more slowly in the recent past than a linear extrapolation would suggest, which increases the time required to reach the current scale factor (making the age larger than the matter-only case).

In the specific case of $\Omega_m=0.3, \Omega_\Lambda=0.7$, these two effects nearly cancel each other out, making $t_0 \approx t_H$.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 13.969 \\
\mathrm{matter\_age\_gyr} &= 9.313 \\
\mathrm{lcdm\_age\_gyr} &= 13.467
\end{aligned}
\]