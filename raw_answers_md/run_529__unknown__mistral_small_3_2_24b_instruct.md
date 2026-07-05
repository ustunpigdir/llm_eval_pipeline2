To solve the problem of quantum tunneling through a rectangular barrier, we will follow the steps outlined in the task. Let's break down each part of the calculation.

### Given:
- Electron energy, \( E = 1.00 \) eV
- Barrier height, \( V_0 = 5.00 \) eV
- Barrier width, \( L = 1.00 \) nm
- Mass of the electron, \( m = 9.11 \times 10^{-31} \) kg
- Reduced Planck's constant, \( \hbar = 1.054 \times 10^{-34} \) J·s
- 1 eV = \( 1.602 \times 10^{-19} \) J

### Step 1: Evaluate \(\kappa\) in nm\(^{-1}\)

The decay constant \(\kappa\) is given by:
\[
\kappa = \sqrt{\frac{2m(V_0 - E)}{\hbar^2}}
\]

First, convert \(V_0 - E\) to joules:
\[
V_0 - E = 5.00 \, \text{eV} - 1.00 \, \text{eV} = 4.00 \, \text{eV} = 4.00 \times 1.602 \times 10^{-19} \, \text{J} = 6.408 \times 10^{-19} \, \text{J}
\]

Now, plug in the values:
\[
\kappa = \sqrt{\frac{2 \times 9.11 \times 10^{-31} \, \text{kg} \times 6.408 \times 10^{-19} \, \text{J}}{(1.054 \times 10^{-34} \, \text{J·s})^2}}
\]

Calculate the denominator:
\[
(1.054 \times 10^{-34} \, \text{J·s})^2 = 1.111 \times 10^{-68} \, \text{J}^2 \cdot \text{s}^2
\]

Now, calculate the numerator:
\[
2 \times 9.11 \times 10^{-31} \, \text{kg} \times 6.408 \times 10^{-19} \, \text{J} = 1.164 \times 10^{-48} \, \text{kg} \cdot \text{J}
\]

Now, divide the numerator by the denominator:
\[
\frac{1.164 \times 10^{-48} \, \text{kg} \cdot \text{J}}{1.111 \times 10^{-68} \, \text{J}^2 \cdot \text{s}^2} = 1.048 \times 10^{20} \, \text{kg} \cdot \text{s}^2
\]

Take the square root:
\[
\kappa = \sqrt{1.048 \times 10^{20} \, \text{kg} \cdot \text{s}^2} = 1.024 \times 10^{10} \, \text{m}^{-1}
\]

Convert to nm\(^{-1}\):
\[
\kappa = 1.024 \times 10^{10} \, \text{m}^{-1} \times 10^{-9} \, \text{m/nm} = 10.24 \, \text{nm}^{-1}
\]

### Step 2: Evaluate the dimensionless product \(\kappa L\)

\[
\kappa L = 10.24 \, \text{nm}^{-1} \times 1.00 \, \text{nm} = 10.24
\]

### Step 3: Evaluate the prefactor \(16E(V_0-E)/V_0^2\)

First, convert \(E\) and \(V_0\) to eV:
\[
E = 1.00 \, \text{eV}, \quad V_0 = 5.00 \, \text{eV}
\]

Now, calculate the prefactor:
\[
\frac{16E(V_0 - E)}{V_0^2} = \frac{16 \times 1.00 \times (5.00 - 1.00)}{5.00^2} = \frac{16 \times 1.00 \times 4.00}{25.00} = \frac{64.00}{25.00} = 2.56
\]

### Step 4: Evaluate \(\log_{10} T\) including the prefactor

The transmission probability \(T\) is given by:
\[
T \approx \frac{16E(V_0 - E)}{V_0^2} e^{-2\kappa L}
\]

We already have:
\[
\frac{16E(V_0 - E)}{V_0^2} = 2.56
\]
\[
2\kappa L = 2 \times 10.24 = 20.48
\]

Now, calculate \(e^{-2\kappa L}\):
\[
e^{-20.48} \approx 1.24 \times 10^{-9}
\]

Multiply by the prefactor:
\[
T \approx 2.56 \times 1.24 \times 10^{-9} = 3.17 \times 10^{-9}
\]

Now, take the base-10 logarithm:
\[
\log_{10} T = \log_{10} (3.17 \times 10^{-9}) = \log_{10} (3.17) + \log_{10} (10^{-9}) = 0.501 - 9 = -8.499
\]

### Step 5: How does \(T\) change if \(L\) doubles?

If \(L\) doubles, \(L = 2.00\) nm, then:
\[
\kappa L = 10.24 \times 2.00 = 20.48
\]

The transmission probability \(T\) becomes:
\[
T \approx 2.56 \times e^{-20.48}
\]

We already know \(e^{-20.48} \approx 1.24 \times 10^{-9}\), so:
\[
T \approx 2.56 \times 1.24 \times 10^{-9} = 3.17 \times 10^{-9}
\]

Taking the base-10 logarithm:
\[
\log_{10} T = \log_{10} (3.17 \times 10^{-9}) = -8.499
\]

However, if we consider the new \(\kappa L\) for \(L = 2.00\) nm:
\[
2\kappa L = 2 \times 10.24 \times 2.00 = 40.96
\]

Then:
\[
e^{-40.96} \approx 1.24 \times 10^{-18}
\]

Multiply by the prefactor:
\[
T \approx 2.56 \times 1.24 \times 10^{-18} = 3.17 \times 10^{-18}
\]

Taking the base-10 logarithm:
\[
\log_{10} T = \log_{10} (3.17 \times 10^{-18}) = \log_{10} (3.17) + \log_{10} (10^{-18}) = 0.501 - 18 = -17.499
\]

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 10.24 \\
\mathrm{kappa\_L} &= 10.24 \\
\mathrm{prefactor} &= 2.56 \\
\mathrm{log10\_T} &= -8.499
\end{aligned}
\]