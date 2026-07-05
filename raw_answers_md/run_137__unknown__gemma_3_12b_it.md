Okay, let's break down this de Sitter thermodynamics problem step by step.

**1. Evaluate the horizon radius *c/H* in Gpc.**

We are given $H = 70.0 \text{ km/s/Mpc}$. We need to calculate $r = c/H$ and convert it to Gpc.

*   $c = 299792458 \text{ m/s}$
*   $H = 70.0 \text{ km/s/Mpc} = 70.0 \times 10^3 \text{ m/s} / (3.086 \times 10^{22} \text{ m})$

Therefore,

$r = \frac{c}{H} = \frac{299792458 \text{ m/s}}{70.0 \times 10^3 \text{ m/s} / (3.086 \times 10^{22} \text{ m})} = \frac{299792458 \times 3.086 \times 10^{22}}{70.0 \times 10^3} \text{ m} = 1.304 \times 10^{26} \text{ m}$

Now, convert to Gpc.  1 Gpc = $3.086 \times 10^{22}$ m.

$r \text{ (in Gpc)} = \frac{1.304 \times 10^{26} \text{ m}}{3.086 \times 10^{22} \text{ m/Gpc}} \approx 42.37 \text{ Gpc}$

So, $r \approx 42.37$ Gpc.

**2. Evaluate the Gibbons-Hawking temperature in units of 10<sup>-30</sup> K.**

The Gibbons-Hawking temperature is given by $T = \frac{\hbar H}{2\pi k_B}$.

*   $\hbar = 1.0545718 \times 10^{-34} \text{ J s}$
*   $k_B = 1.380649 \times 10^{-23} \text{ J/K}$
*   $H = 70.0 \times 10^3 \text{ m/s} / (3.086 \times 10^{22} \text{ m}) \approx 2.27 \times 10^{-18} \text{ s}^{-1}$

$T = \frac{\hbar H}{2\pi k_B} = \frac{(1.0545718 \times 10^{-34} \text{ J s}) (2.27 \times 10^{-18} \text{ s}^{-1})}{2\pi (1.380649 \times 10^{-23} \text{ J/K})} = \frac{2.40 \times 10^{-52}}{8.69 \times 10^{-23}} \text{ K} \approx 2.76 \times 10^{-29} \text{ K}$

In units of $10^{-30}$ K, $T \approx 0.276 \times 10^{-30} \text{ K}$.

**3. Compare that to the CMB temperature today; after how many e-folds of expansion would a *T ∝ a<sup>-1</sup> radiation background cool below *T<sub>GH</sub>*?**

The CMB temperature today is $T_{CMB} = 2.725 \text{ K}$. We want to find the number of e-folds, $N$, such that $T(N) = T_{GH}$, where $T(N) = T_{CMB} a(N)^{-1}$ and $a(N) = e^N$.

$T(N) = T_{CMB} e^{-N} = T_{GH}$

$e^{-N} = \frac{T_{GH}}{T_{CMB}} = \frac{2.76 \times 10^{-29} \text{ K}}{2.725 \text{ K}} \approx 1.014 \times 10^{-29}$

$-N = \ln(1.014 \times 10^{-29}) \approx -29.02$

$N = 29.02$ e-folds.

Therefore, $\ln(2.725/T_{GH}) = \ln(2.725/(2.76 \times 10^{-29})) \approx 29.02$.

**4. Explain what an observer in pure de Sitter space would (in principle) detect, and the analogy to the Unruh and Hawking effects.**

An observer in pure de Sitter space would, in principle, detect a thermal bath of particles with a temperature given by the Gibbons-Hawking temperature. This is analogous to the Unruh effect, where an accelerating observer in a vacuum perceives a thermal bath.  The de Sitter space is, in a sense, a cosmological version of the Unruh effect. The cosmological event horizon acts as a boundary, and an observer crossing this horizon would experience the thermal radiation.

The Hawking effect is also relevant.  Hawking radiation arises from the emission of particles from a black hole's event horizon.  The de Sitter horizon is a cosmological horizon, and the Gibbons-Hawking temperature is analogous to the Hawking temperature of a black hole.  Both effects involve the emission of particles due to the presence of a horizon.  The key difference is that de Sitter space is expanding, while a black hole is collapsing.

\[
\begin{aligned}
\mathrm{horizon\_gpc} &= 42.37 \\
\mathrm{gh\_temp\_e30\_K} &= 0.276 \\
\mathrm{efolds\_to\_gh} &= 29.02
\end{aligned}
\]