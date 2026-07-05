Okay, let's break down this de Sitter thermodynamics problem step by step.

**1. Evaluate the horizon radius *c/H* in Gpc.**

We are given $H = 70.0 \text{ km/s/Mpc}$. We need to calculate $r = c/H$ and convert it to Gpc.

*   $c = 299792458 \text{ m/s}$
*   $H = 70.0 \text{ km/s/Mpc} = 70.0 \times 10^3 \text{ m/s} / (3.086 \times 10^{22} \text{ m})$
*   $r = c/H = \frac{299792458 \text{ m/s}}{70.0 \times 10^3 \text{ m/s} / (3.086 \times 10^{22} \text{ m})} = \frac{299792458 \times 3.086 \times 10^{22}}{70.0 \times 10^3} \text{ m} = 1.303 \times 10^{27} \text{ m}$

Now, convert meters to Gpc.  1 Gpc = $3.086 \times 10^{22}$ m.

*   $r \text{ (in Gpc)} = \frac{1.303 \times 10^{27} \text{ m}}{3.086 \times 10^{22} \text{ m/Gpc}} \approx 42.38 \text{ Gpc}$

So, the horizon radius is approximately 42.38 Gpc.

**2. Evaluate the Gibbons-Hawking temperature in units of 10<sup>-30</sup> K.**

The Gibbons-Hawking temperature is given by $T = \hbar H / (2\pi k_B)$. We need to calculate this and express it in units of $10^{-30}$ K.

*   $\hbar = 1.0545718 \times 10^{-34} \text{ J s}$
*   $k_B = 1.380649 \times 10^{-23} \text{ J/K}$
*   $H = 70.0 \times 10^3 \text{ m/s} / (3.086 \times 10^{22} \text{ m}) = 2.27 \times 10^{-20} \text{ s}^{-1}$

$T = \frac{\hbar H}{2\pi k_B} = \frac{1.0545718 \times 10^{-34} \text{ J s} \times 2.27 \times 10^{-20} \text{ s}^{-1}}{2\pi \times 1.380649 \times 10^{-23} \text{ J/K}} = \frac{2.394 \times 10^{-54}}{8.686 \times 10^{-23}} \text{ K} = 2.76 \times 10^{-31} \text{ K}$

Therefore, $T \approx 2.76 \times 10^{-31} \text{ K}$, which is $2.76 \times 10^{-30} \times 10^{-1} \text{ K}$.  So, in units of $10^{-30}$ K, $T \approx 0.276$.

**3. Compare that to the CMB temperature today; after how many e-folds of expansion would a *T ∝ a<sup>-1</sup>* radiation background cool below *T<sub>GH</sub>*?**

The CMB temperature today is $T_{CMB} = 2.725 \text{ K}$. We want to find the number of e-folds, $N$, such that $T(N) = T_{GH}$.  We assume $T \propto a^{-1}$, where $a$ is the scale factor.  The scale factor evolves as $a(N) = e^N$.

So, $T(N) = T_{CMB} / a(N) = T_{CMB} / e^N$.  We want to find $N$ such that $T(N) = T_{GH}$.

$T_{GH} = \frac{T_{CMB}}{e^N}$
$e^N = \frac{T_{CMB}}{T_{GH}} = \frac{2.725 \text{ K}}{2.76 \times 10^{-31} \text{ K}} = 9.87 \times 10^{30}$
$N = \ln(9.87 \times 10^{30}) \approx 30.00$

Therefore, it would take approximately 30 e-folds for a $T \propto a^{-1}$ radiation background to cool below $T_{GH}$.

**4. Explain what an observer in pure de Sitter space would (in principle) detect, and the analogy to the Unruh and Hawking effects.**

An observer in pure de Sitter space would, in principle, detect a thermal bath of particles with a temperature given by the Gibbons-Hawking temperature. This is analogous to the Unruh effect, where an accelerating observer in a vacuum perceives a thermal bath. The key difference is that in de Sitter space, the "acceleration" is due to the expansion of the universe itself, and the observer is at rest with respect to the cosmological horizon.

The Hawking effect arises from the presence of a black hole horizon, where particles are thermally emitted due to quantum effects near the event horizon. The de Sitter space horizon acts similarly, but instead of a black hole, it's the cosmological horizon of an expanding universe. The Gibbons-Hawking temperature is the temperature of the Hawking radiation emitted from the de Sitter horizon.  The observer would detect this as a constant stream of low-energy particles, effectively a thermal background.  The energy of these particles is related to the expansion rate of the universe.

\[
\begin{aligned}
\mathrm{horizon\_gpc} &= 42.38 \\
\mathrm{gh\_temp\_e30\_K} &= 0.276 \\
\mathrm{efolds\_to\_gh} &= 30.00
\end{aligned}
\]