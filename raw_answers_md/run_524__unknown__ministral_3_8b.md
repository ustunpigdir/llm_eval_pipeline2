Let's proceed step-by-step to solve the problem.

---

### Step 1: Constants and given values
We are given:
- Electron energy \( E = 1.00 \, \text{eV} \)
- Barrier height \( V_0 = 5.00 \, \text{eV} \)
- Barrier width \( L = 1.00 \, \text{nm} \)

We need the electron mass \( m \) and Planck constant \( \hbar \) in appropriate units. Recall:
- Electron mass \( m = 9.10938356 \times 10^{-31} \, \text{kg} \)
- Planck constant \( \hbar = 1.0545718 \times 10^{-34} \, \text{J s} \)

First, convert energies to Joules:
\[
1 \, \text{eV} = 1.602176634 \times 10^{-19} \, \text{J}
\]
Thus,
\[
E = 1.00 \, \text{eV} = 1.602176634 \times 10^{-19} \, \text{J}
\]
\[
V_0 = 5.00 \, \text{eV} = 5 \times 1.602176634 \times 10^{-19} \, \text{J} = 8.01088317 \times 10^{-19} \, \text{J}
\]

---

### Step 2: Calculate \(\kappa\) in units of nm\(^{-1}\)

The decay constant is given by:
\[
\kappa = \frac{\sqrt{2 m (V_0 - E)}}{\hbar}
\]

Calculate \( V_0 - E \):
\[
V_0 - E = (8.01088317 - 1.602176634) \times 10^{-19} = 6.408706536 \times 10^{-19} \, \text{J}
\]

Now calculate \( 2 m (V_0 - E) \):
\[
2 m (V_0 - E) = 2 \times 9.10938356 \times 10^{-31} \times 6.408706536 \times 10^{-19}
\]
\[
= 2 \times 9.10938356 \times 6.408706536 \times 10^{-50}
\]
\[
= 116.34 \times 10^{-50} = 1.1634 \times 10^{-48} \, \text{J kg}
\]

Take the square root:
\[
\sqrt{2 m (V_0 - E)} = \sqrt{1.1634 \times 10^{-48}} = 3.411 \times 10^{-24} \, \text{J}^{1/2} \text{kg}^{1/2}
\]

Now divide by \(\hbar\):
\[
\kappa = \frac{3.411 \times 10^{-24}}{1.0545718 \times 10^{-34}} = 3.233 \times 10^{10} \, \text{s}^{-1}
\]

But we want \(\kappa\) in units of nm\(^{-1}\). Recall that \(1 \, \text{nm} = 10^{-9} \, \text{m}\), so:
\[
\kappa \, \text{in nm}^{-1} = \kappa \times 10^{-9} \, \text{m} = 3.233 \times 10^{10} \times 10^{-9} = 3.233 \times 10^{1} \, \text{nm}^{-1}
\]

So,
\[
\kappa \approx 32.33 \, \text{nm}^{-1}
\]

---

### Step 3: Calculate \(\kappa L\)

Given \( L = 1.00 \, \text{nm} \),
\[
\kappa L = 32.33 \times 1.00 = 32.33
\]

---

### Step 4: Calculate the prefactor \( \frac{16 E (V_0 - E)}{V_0^2} \)

First, calculate \( E (V_0 - E) \):
\[
E (V_0 - E) = 1.602176634 \times 10^{-19} \times 6.408706536 \times 10^{-19}
\]
\[
= 1.026 \times 10^{-37} \, \text{J}^2
\]

Now calculate \( V_0^2 \):
\[
V_0^2 = (8.01088317 \times 10^{-19})^2 = 6.417 \times 10^{-37} \, \text{J}^2
\]

Now calculate the prefactor:
\[
\frac{16 E (V_0 - E)}{V_0^2} = \frac{16 \times 1.026 \times 10^{-37}}{6.417 \times 10^{-37}} = \frac{16.416}{6.417} \approx 2.56
\]

---

### Step 5: Calculate \(\log_{10} T\)

The transmission probability is given by:
\[
T \approx \frac{16 E (V_0 - E)}{V_0^2} e^{-2 \kappa L}
\]

We already have:
\[
\frac{16 E (V_0 - E)}{V_0^2} = 2.56
\]
\[
2 \kappa L = 2 \times 32.33 = 64.66
\]

So,
\[
T \approx 2.56 \times e^{-64.66}
\]

Now take \(\log_{10} T\):
\[
\log_{10} T = \log_{10} (2.56) + \log_{10} (e^{-64.66})
\]

Recall that \(\log_{10} e = \frac{1}{\ln 10} \approx 0.4343\):
\[
\log_{10} (e^{-64.66}) = -64.66 \times 0.4343 = -28.04
\]

And \(\log_{10} (2.56) \approx 0.408\):
\[
\log_{10} T = 0.408 - 28.04 = -27.63
\]

---

### Step 6: How does \(T\) change if \(L\) doubles?

If \(L\) doubles, the exponent becomes:
\[
2 \kappa (2L) = 4 \kappa L = 4 \times 32.33 = 128.32
\]

The prefactor remains the same:
\[
T' \approx 2.56 \times e^{-128.32}
\]

Taking \(\log_{10} T'\):
\[
\log_{10} T' = \log_{10} (2.56) + \log_{10} (e^{-128.32}) = 0.408 - 128.32 \times 0.4343
\]
\[
= 0.408 - 55.72 = -55.31
\]

This shows that doubling \(L\) reduces \(\log_{10} T\) by approximately \(27.68\) (from \(-27.63\) to \(-55.31\)), which corresponds to an exponential sensitivity: \(T\) decreases by a factor of \(e^{2 \kappa L} = e^{64.66}\), a huge suppression.

---

FINAL ANSWER

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 32.33 \\
\mathrm{kappa\_L} &= 32.33 \\
\mathrm{prefactor} &= 2.56 \\
\mathrm{log10\_T} &= -27.63 \\
\end{aligned}
\]