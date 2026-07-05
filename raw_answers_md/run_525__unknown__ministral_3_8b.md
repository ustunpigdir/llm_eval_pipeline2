Let's proceed step-by-step to solve the problem.

---

### Step 1: Constants and given values
We are given:
- Electron energy: \( E = 1.00 \, \text{eV} \)
- Barrier height: \( V_0 = 5.00 \, \text{eV} \)
- Barrier width: \( L = 1.00 \, \text{nm} = 1.00 \times 10^{-9} \, \text{m} \)

We need the electron mass \( m \) and reduced Planck constant \( \hbar \). Using standard values:
- Electron mass: \( m = 9.109 \times 10^{-31} \, \text{kg} \)
- Reduced Planck constant: \( \hbar = 1.0545718 \times 10^{-34} \, \text{J·s} \)

We also need to convert energy to Joules:
- \( 1 \, \text{eV} = 1.602176634 \times 10^{-19} \, \text{J} \)

---

### Step 2: Calculate \(\kappa\) in units of \( \text{nm}^{-1} \)
The decay constant is given by:
\[
\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}
\]

First, compute \( V_0 - E \):
\[
V_0 - E = 5.00 \, \text{eV} - 1.00 \, \text{eV} = 4.00 \, \text{eV}
\]

Convert \( V_0 - E \) to Joules:
\[
4.00 \, \text{eV} \times 1.602176634 \times 10^{-19} \, \text{J/eV} = 6.408706536 \times 10^{-19} \, \text{J}
\]

Now compute the numerator:
\[
2m(V_0 - E) = 2 \times 9.109 \times 10^{-31} \, \text{kg} \times 6.408706536 \times 10^{-19} \, \text{J}
= 1.166 \times 10^{-48} \, \text{kg·J}
\]

Take the square root:
\[
\sqrt{2m(V_0 - E)} = \sqrt{1.166 \times 10^{-48}} = 3.415 \times 10^{-24} \, \text{kg}^{1/2} \cdot \text{J}^{1/2}
\]

Now divide by \(\hbar\):
\[
\kappa = \frac{3.415 \times 10^{-24}}{1.0545718 \times 10^{-34}} = 3.238 \times 10^{10} \, \text{m}^{-1}
\]

Convert \(\kappa\) to \(\text{nm}^{-1}\):
\[
1 \, \text{nm} = 10^{-9} \, \text{m} \implies \kappa = 3.238 \times 10^{10} \times 10^{-9} = 3.238 \times 10^{1} \, \text{nm}^{-1}
\]

---

### Step 3: Compute \(\kappa L\)
\[
\kappa L = 3.238 \times 10^{1} \, \text{nm}^{-1} \times 1.00 \, \text{nm} = 32.38
\]

---

### Step 4: Compute the prefactor \( \frac{16 E (V_0 - E)}{V_0^2} \)
First, compute \( E (V_0 - E) \):
\[
E (V_0 - E) = 1.00 \, \text{eV} \times 4.00 \, \text{eV} = 4.00 \, \text{eV}^2
\]

Now compute \( V_0^2 \):
\[
V_0^2 = (5.00 \, \text{eV})^2 = 25.00 \, \text{eV}^2
\]

Now compute the prefactor:
\[
\frac{16 E (V_0 - E)}{V_0^2} = \frac{16 \times 4.00}{25.00} = \frac{64}{25} = 2.56
\]

---

### Step 5: Compute \(\log_{10} T\)
The transmission probability in the opaque-barrier limit is:
\[
T \approx \frac{16 E (V_0 - E)}{V_0^2} e^{-2 \kappa L}
\]

We already have:
\[
\frac{16 E (V_0 - E)}{V_0^2} = 2.56
\]
\[
2 \kappa L = 2 \times 32.38 = 64.76
\]

Thus:
\[
T \approx 2.56 \times e^{-64.76}
\]

Now compute \(\log_{10} T\):
\[
\log_{10} T = \log_{10}(2.56) + \log_{10}(e^{-64.76})
\]

We know:
\[
\log_{10}(2.56) \approx 0.4082
\]
\[
\log_{10}(e^{-64.76}) = -64.76 \times \log_{10}(e) \approx -64.76 \times 0.4343 = -28.11
\]

So:
\[
\log_{10} T \approx 0.4082 - 28.11 = -27.70
\]

---

### Step 6: How does \(T\) change if \(L\) doubles?
If \(L\) doubles, the exponent \(2 \kappa L\) doubles:
\[
2 \kappa (2L) = 2 \times 2 \times \kappa L = 4 \times 32.38 = 129.52
\]

The prefactor remains the same:
\[
T' \approx 2.56 \times e^{-129.52}
\]

Compute \(\log_{10} T'\):
\[
\log_{10} T' = \log_{10}(2.56) + \log_{10}(e^{-129.52}) = 0.4082 - 129.52 \times 0.4343
\]
\[
= 0.4082 - 56.22 = -55.81
\]

---

### Comment on exponential sensitivity:
The transmission probability \(T\) is extremely sensitive to changes in \(L\) because of the exponential term \(e^{-2 \kappa L}\). Doubling \(L\) increases the exponent by a factor of 2, which causes \(T\) to decrease by a factor of \(e^{-2 \kappa L} = e^{-64.76}\) (originally) and now \(e^{-129.52}\). This results in a dramatic reduction in \(T\), illustrating the exponential sensitivity of quantum tunneling to barrier width.

---

FINAL ANSWER

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 32.38 \\
\mathrm{kappa\_L} &= 32.38 \\
\mathrm{prefactor} &= 2.56 \\
\mathrm{log10\_T} &= -27.70 \\
\end{aligned}
\]