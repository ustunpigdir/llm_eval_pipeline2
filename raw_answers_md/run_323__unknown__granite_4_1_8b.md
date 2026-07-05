**1. Unruh temperature formula and physical statement**

The Unruh effect predicts that an observer undergoing constant proper acceleration \(a\) in the Minkowski vacuum perceives a thermal bath of particles with temperature  

\[
T = \frac{\hbar a}{2\pi c k_B},
\]

where  
- \(\hbar\) is the reduced Planck constant (\(1.0545718 \times 10^{-34}\,\text{J·s}\)),  
- \(c\) is the speed of light (\(2.99792458 \times 10^8\,\text{m/s}\)),  
- \(k_B\) is Boltzmann’s constant (\(1.380649 \times 10^{-23}\,\text{J/K}\)).  

**Physical statement:** An inertial observer sees the Minkowski vacuum as empty, but an observer undergoing constant proper acceleration \(a\) detects a thermal distribution of particles with the above temperature, as if they were immersed in a heat bath at temperature \(T\).

---

**2. Evaluate \(T\) for \(a = 10^{20}\,\text{m/s}^2\)**  

Given \(a = 1.00 \times 10^{20}\,\text{m/s}^2\),

\[
T = \frac{\hbar a}{2\pi c k_B}
   = \frac{(1.0545718 \times 10^{-34}\,\text{J·s}) \times (1.00 \times 10^{20}\,\text{m/s}^2)}
          {2\pi \times (2.99792458 \times 10^8\,\text{m/s}) \times (1.380649 \times 10^{-23}\,\text{J/K})}.
\]

Compute the numerator:

\[
\hbar a = 1.0545718 \times 10^{-34} \times 10^{20}
        = 1.0545718 \times 10^{-14}\,\text{J·m/s}.
\]

Compute the denominator:

\[
2\pi c k_B = 2\pi \times 2.99792458 \times 10^8 \times 1.380649 \times 10^{-23}
           \approx 2\pi \times (2.99792458 \times 1.380649) \times 10^{-15}
           \approx 2\pi \times 4.142 \times 10^{-15}
           \approx 2.603 \times 10^{-14}\,\text{J·m/s}.
\]

Now, the temperature:

\[
T = \frac{1.0545718 \times 10^{-14}}{2.603 \times 10^{-14}}
   \approx 0.405\,\text{K}.
\]

Thus, the Unruh temperature for \(a = 10^{20}\,\text{m/s}^2\) is approximately **0.405 K**.

---

**3. Proper acceleration giving \(T = 1.00\) K**

Set \(T = 1\,\text{K}\) and solve for \(a\):

\[
1 = \frac{\hbar a}{2\pi c k_B}
\quad\Longrightarrow\quad
a = \frac{2\pi c k_B}{\hbar}.
\]

Insert the constants:

\[
a = \frac{2\pi \times (2.99792458 \times 10^8) \times (1.380649 \times 10^{-23})}
          {1.0545718 \times 10^{-34}}.
\]

Calculate the numerator:

\[
2\pi c k_B \approx 2\pi \times 2.99792458 \times 1.380649 \times 10^{-15}
            \approx 2\pi \times 4.142 \times 10^{-15}
            \approx 2.603 \times 10^{-14}\,\text{J·m/s}.
\]

Now, the acceleration:

\[
a \approx \frac{2.603 \times 10^{-14}}{1.0545718 \times 10^{-34}}
    \approx 2.47 \times 10^{20}\,\text{m/s}^2.
\]

Expressed in units of \(10^{20}\,\text{m/s}^2\):

\[
\frac{a}{10^{20}\,\text{m/s}^2} \approx 2.47.
\]

Thus, the acceleration required for a Unruh temperature of 1 K is **approximately \(2.47 \times 10^{20}\,\text{m/s}^2\)**, i.e., **2.47** in units of \(10^{20}\,\text{m/s}^2\).

---

**4. Relation to Hawking radiation and why everyday accelerations produce unobservably small \(T\)**  

- **Equivalence principle:** Near a black hole’s event horizon, an observer experiences a gravitational acceleration equivalent to the surface gravity \(\kappa\) of the black hole. The Unruh effect, which describes thermal radiation perceived by an accelerated observer in flat spacetime, is analogous to the Hawking radiation observed by an observer at infinity. Both phenomena arise because the accelerated (or gravitational) frame mixes vacuum modes, leading to a thermal spectrum. In the limit where the acceleration approaches the horizon’s surface gravity, the Unruh temperature matches the Hawking temperature.

- **Scale of everyday accelerations:** For typical accelerations encountered in daily life (e.g., \(g \approx 9.81\,\text{m/s}^2\)), the Unruh temperature is astronomically small:

\[
T_{\text{everyday}} = \frac{\hbar g}{2\pi c k_B}
   \approx \frac{1.0545718 \times 10^{-34} \times 9.81}{2\pi \times 2.99792458 \times 10^8 \times 1.380649 \times 10^{-23}}
   \approx 6 \times 10^{-29}\,\text{K},
\]

far below any conceivable detection threshold. Hence, the Unruh effect is practically unobservable at ordinary accelerations, but becomes significant only at extremely high accelerations, comparable to those near a black hole’s horizon or the hypothetical \(10^{20}\,\text{m/s}^2\) considered above.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{unruh\_temp\_K} &= 0.405 \\
\mathrm{accel\_for\_1K\_e20} &= 2.47
\end{aligned}
\]