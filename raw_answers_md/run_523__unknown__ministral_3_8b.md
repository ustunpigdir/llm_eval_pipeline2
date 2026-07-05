Let's proceed step-by-step to solve the problem.

---

### Step 1: Constants and given values
We are given:
- Electron energy \( E = 1.00 \, \text{eV} \)
- Barrier height \( V_0 = 5.00 \, \text{eV} \)
- Barrier width \( L = 1.00 \, \text{nm} = 1.00 \times 10^{-9} \, \text{m} \)

We need the electron mass \( m \) and Planck's constant \( \hbar \). Using standard values:
- Electron mass \( m = 9.10938356 \times 10^{-31} \, \text{kg} \)
- Reduced Planck constant \( \hbar = 1.0545718 \times 10^{-34} \, \text{J s} \)

First, convert energies to Joules:
\[
1 \, \text{eV} = 1.602176634 \times 10^{-19} \, \text{J}
\]
Thus,
\[
E = 1.00 \times 1.602176634 \times 10^{-19} = 1.602176634 \times 10^{-19} \, \text{J}
\]
\[
V_0 = 5.00 \times 1.602176634 \times 10^{-19} = 8.01088317 \times 10^{-19} \, \text{J}
\]

---

### Step 2: Calculate \(\kappa\)
The decay constant \(\kappa\) is given by:
\[
\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}
\]

Calculate \(V_0 - E\):
\[
V_0 - E = 8.01088317 \times 10^{-19} - 1.602176634 \times 10^{-19} = 6.408706536 \times 10^{-19} \, \text{J}
\]

Now calculate \(2m(V_0 - E)\):
\[
2m(V_0 - E) = 2 \times 9.10938356 \times 10^{-31} \times 6.408706536 \times 10^{-19}
\]
\[
= 2 \times 9.10938356 \times 6.408706536 \times 10^{-50}
\]
\[
= 1.166 \times 10^{-48} \, \text{kg J}
\]

Take the square root:
\[
\sqrt{2m(V_0 - E)} = \sqrt{1.166 \times 10^{-48}} = 3.415 \times 10^{-24} \, \text{kg}^{1/2} \, \text{J}^{1/2}
\]

Now divide by \(\hbar\):
\[
\kappa = \frac{3.415 \times 10^{-24}}{1.0545718 \times 10^{-34}} = 3.237 \times 10^{10} \, \text{m}^{-1}
\]

Convert \(\kappa\) to nm\(^{-1}\):
\[
1 \, \text{nm} = 10^{-9} \, \text{m} \implies \kappa = 3.237 \times 10^{10} \times 10^{-9} = 3.237 \times 10^{1} \, \text{nm}^{-1}
\]

---

### Step 3: Calculate \(\kappa L\)
Given \(L = 1.00 \, \text{nm}\):
\[
\kappa L = 3.237 \times 10^{1} \times 1.00 = 32.37
\]

---

### Step 4: Calculate the prefactor \(16 E (V_0 - E) / V_0^2\)

First, calculate \(E (V_0 - E)\):
\[
E (V_0 - E) = 1.602176634 \times 10^{-19} \times 6.408706536 \times 10^{-19}
\]
\[
= 1.026 \times 10^{-37} \, \text{J}^2
\]

Now calculate \(V_0^2\):
\[
V_0^2 = (8.01088317 \times 10^{-19})^2 = 6.417 \times 10^{-37} \, \text{J}^2
\]

Now calculate the prefactor:
\[
\frac{16 E (V_0 - E)}{V_0^2} = \frac{16 \times 1.026 \times 10^{-37}}{6.417 \times 10^{-37}} = \frac{16.416}{6.417} \approx 2.56
\]

---

### Step 5: Calculate \(\log_{10} T\)

The transmission probability \(T\) is given by:
\[
T \approx \frac{16 E (V_0 - E)}{V_0^2} e^{-2 \kappa L}
\]

We already have:
\[
\frac{16 E (V_0 - E)}{V_0^2} = 2.56
\]
\[
e^{-2 \kappa L} = e^{-2 \times 32.37} = e^{-64.74}
\]

Calculate \(\log_{10} T\):
\[
\log_{10} T = \log_{10} (2.56) + \log_{10} (e^{-64.74})
\]

Recall that \(\log_{10} e = 0.4343\):
\[
\log_{10} (e^{-64.74}) = -64.74 \times 0.4343 = -28.06
\]

Calculate \(\log_{10} (2.56)\):
\[
\log_{10} (2.56) \approx 0.408
\]

Thus:
\[
\log_{10} T = 0.408 - 28.06 = -27.65
\]

---

### Step 6: How does \(T\) change if \(L\) doubles?

If \(L\) doubles, \(\kappa L\) doubles:
\[
\kappa L_{\text{new}} = 2 \times 32.37 = 64.74
\]

The new exponent is:
\[
-2 \kappa L_{\text{new}} = -2 \times 64.74 = -129.48
\]

The prefactor remains the same:
\[
\log_{10} T_{\text{new}} = \log_{10} (2.56) + \log_{10} (e^{-129.48})
\]
\[
= 0.408 - 129.48 \times 0.4343
\]
\[
= 0.408 - 56.12 = -55.71
\]

---

### Summary of results:

- \(\kappa\) in nm\(^{-1}\): \(3.237 \times 10^{1}\)
- \(\kappa L\): \(32.37\)
- Prefactor: \(2.56\)
- \(\log_{10} T\): \(-27.65\)
- New \(\log_{10} T\) when \(L\) doubles: \(-55.71\)

---

FINAL ANSWER

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 32.37 \\
\mathrm{kappa\_L} &= 32.37 \\
\mathrm{prefactor} &= 2.56 \\
\mathrm{log10\_T} &= -27.65 \\
\end{aligned}
\]