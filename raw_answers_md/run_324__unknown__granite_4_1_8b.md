**1. Unruh temperature formula and physical statement**

The Unruh effect predicts that an observer undergoing constant proper acceleration \(a\) in Minkowski spacetime perceives a thermal bath of particles at a temperature given by  

\[
T = \frac{\hbar a}{2\pi c k_B},
\]

where  
- \(\hbar\) is the reduced Planck constant (\(1.0545718 \times 10^{-34}\,\text{J·s}\)),  
- \(c\) is the speed of light (\(2.99792458 \times 10^8\,\text{m/s}\)),  
- \(k_B\) is Boltzmann’s constant (\(1.380649 \times 10^{-23}\,\text{J/K}\)).  

**Physical statement:** An inertial observer in empty (Minkowski) space sees nothing, but an observer undergoing constant proper acceleration \(a\) detects a thermal distribution of particles with the above temperature, as if they were immersed in a blackbody radiation field.

---

**2. Evaluate \(T\) for \(a = 10^{20}\,\text{m/s}^2\)**  

Insert the given acceleration into the formula:

\[
T = \frac{\hbar a}{2\pi c k_B}
   = \frac{(1.0545718 \times 10^{-34}\,\text{J·s}) \times (1.00 \times 10^{20}\,\text{m/s}^2)}
          {2\pi \times (2.99792458 \times 10^8\,\text{m/s}) \times (1.380649 \times 10^{-23}\,\text{J/K})}.
\]

Compute the numerator:

\[
\hbar a = 1.0545718 \times 10^{-34} \times 10^{20}
        = 1.0545718 \times 10^{-14}\,\text{J·s/m}.
\]

Compute the denominator:

\[
2\pi c k_B = 2\pi \times 2.99792458 \times 10^8 \times 1.380649 \times 10^{-23}
           \approx 2\pi \times (2.99792458 \times 1.380649) \times 10^{8-23}
           \approx 2\pi \times 4.142 \times 10^{-15}
           \approx 2.603 \times 10^{-14}\,\text{J·s/K}.
\]

Now the temperature:

\[
T = \frac{1.0545718 \times 10^{-14}}{2.603 \times 10^{-14}}
  \approx 0.405\,\text{K}.
\]

Thus, for \(a = 10^{20}\,\text{m/s}^2\),

\[
\boxed{T \approx 0.405\ \text{K}}.
\]

---

**3. Proper acceleration giving \(T = 1.00\) K**

Set \(T = 1\ \text{K}\) and solve for \(a\):

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
2\pi c k_B \approx 2\pi \times 4.142 \times 10^{-15}
            \approx 2.603 \times 10^{-14}\,\text{J·s/K}.
\]

Now divide by \(\hbar\):

\[
a \approx \frac{2.603 \times 10^{-14}}{1.0545718 \times 10^{-34}}
    \approx 2.467 \times 10^{20}\,\text{m/s}^2.
\]

Express this acceleration in units of \(10^{20}\,\text{m/s}^2\):

\[
\frac{a}{10^{20}\,\text{m/s}^2} \approx 2.47.
\]

Thus, the acceleration required for a Unruh temperature of 1 K is approximately \(2.47 \times 10^{20}\,\text{m/s}^2\), i.e.

\[
\boxed{\text{accel\_for\_1K\_e20} \approx 2.47}.
\]

---

**4. Relation to Hawking radiation and why everyday accelerations produce negligible \(T\)**  

The Unruh effect and Hawking radiation are both manifestations of quantum field theory in curved spacetime and are linked by the equivalence principle:

- **Hawking radiation:** A static observer near a black hole’s event horizon perceives a thermal flux due to the horizon’s spacetime curvature, analogous to the thermal bath seen by an accelerated observer in flat spacetime.
- **Unruh effect:** An accelerated observer in flat spacetime perceives a thermal bath, mirroring the horizon effect in the black hole case.

Both effects arise because the notion of a vacuum state depends on the observer’s trajectory. For an accelerated observer, the Rindler wedge (the region accessible to the observer) behaves like a horizon, leading to particle excitations that appear thermal.

**Why everyday accelerations are unobservable:**

Everyday accelerations (e.g., \(a \sim 9.8\ \text{m/s}^2\) on Earth) are many orders of magnitude smaller than the acceleration required to achieve a measurable Unruh temperature. Using the formula:

\[
T_{\text{earth}} = \frac{\hbar \times 9.8}{2\pi c k_B}
                 \approx \frac{1.0545718 \times 10^{-34} \times 9.8}
                              {2\pi \times 2.99792458 \times 10^8 \times 1.380649 \times 10^{-23}}
                 \approx 10^{-30}\ \text{K},
\]

which is far below any conceivable detection threshold. Hence, the thermal bath predicted by the Unruh effect is negligible for ordinary accelerations.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{unruh\_temp\_K} &= 0.405 \\
\mathrm{accel\_for\_1K\_e20} &= 2.47
\end{aligned}
\]