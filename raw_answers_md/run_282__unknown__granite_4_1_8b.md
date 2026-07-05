**1. Physical origin and regularization**

The Casimir effect arises from the alteration of the zero‑point (vacuum) electromagnetic modes between two perfectly conducting parallel plates. In free space, the allowed wavevectors \(\mathbf{k}\) satisfy the dispersion relation \(\omega = c|\mathbf{k}|\). Between the plates, however, the conducting boundary conditions force the electric field to vanish at the surfaces, which **excludes** those normal modes whose electric field has a node at the plate surfaces. Consequently, the spectrum of vacuum modes inside the gap is a discrete set with a reduced density of states compared to the unbounded case.

Mathematically, the Casimir energy per unit area is obtained by summing (integrating) the zero‑point energies of all allowed modes:
\[
E/A = \frac{\hbar c}{2} \sum_{\mathbf{k}} \int_{0}^{\infty} \! \omega \, d\omega .
\]
Direct summation/integration diverges, so a **regularization** is required. Common techniques (zeta‑function regularization, cutoff regularization, or the introduction of a small separation \(\epsilon\) and later taking \(\epsilon \to 0\)) are used to isolate the finite part of the divergent series. The regularized result for ideal parallel plates at zero temperature is:
\[
\frac{E}{A} = -\frac{\pi^{2}\hbar c}{720 d^{3}}, \qquad
P = \frac{\partial (E/A)}{\partial d} = -\frac{\pi^{2}\hbar c}{240 d^{4}} .
\]
The negative sign indicates **attractive** pressure.

---

**2. Casimir pressure magnitude at \(d = 100\) nm**

Given:
- \(d = 100\ \text{nm} = 100 \times 10^{-9}\ \text{m}\)
- \(\pi^{2} \approx 9.8696\)
- \(\hbar = 1.0545718 \times 10^{-34}\ \text{J·s}\)
- \(c = 2.99792458 \times 10^{8}\ \text{m/s}\)

Compute the prefactor:
\[
\pi^{2}\hbar c = 9.8696 \times (1.0545718 \times 10^{-34}) \times (2.99792458 \times 10^{8})
\approx 9.8696 \times 3.161 \times 10^{-26}
\approx 3.119 \times 10^{-25}\ \text{J·m}.
\]

Now evaluate the denominator:
\[
240 d^{4} = 240 \times (100 \times 10^{-9})^{4}
= 240 \times (10^{-4})^{4}
= 240 \times 10^{-16}
= 2.4 \times 10^{-14}\ \text{m}^{4}.
\]

Thus the magnitude of the pressure:
\[
|P| = \frac{\pi^{2}\hbar c}{240 d^{4}}
= \frac{3.119 \times 10^{-25}}{2.4 \times 10^{-14}}
\approx 1.299 \times 10^{-11}\ \text{Pa}.
\]

**Sign:** The pressure is **attractive** (negative), as indicated by the negative sign in the formula.

---

**3. Energy per unit area magnitude at \(d = 100\) nm**

Using the energy formula:
\[
\left|\frac{E}{A}\right| = \frac{\pi^{2}\hbar c}{720 d^{3}}.
\]

Compute the denominator:
\[
720 d^{3} = 720 \times (100 \times 10^{-9})^{3}
= 720 \times (10^{-3})^{3}
= 720 \times 10^{-9}
= 7.20 \times 10^{-7}\ \text{m}^{3}.
\]

Now the magnitude:
\[
\left|\frac{E}{A}\right| = \frac{3.119 \times 10^{-25}}{7.20 \times 10^{-7}}
\approx 4.330 \times 10^{-19}\ \text{J/m}^{2}.
\]

Convert to microjoules per square meter (\(1\ \mu\text{J/m}^{2} = 10^{-6}\ \text{J/m}^{2}\)):
\[
\left|\frac{E}{A}\right|_{\mu\text{J/m}^{2}} = \frac{4.330 \times 10^{-19}}{10^{-6}}
= 4.330 \times 10^{-13}\ \mu\text{J/m}^{2}.
\]

---

**4. Pressure scaling when \(d\) doubles**

The pressure magnitude scales as \(P \propto d^{-4}\). If the separation doubles (\(d \to 2d\)):
\[
P_{\text{new}} = \frac{\pi^{2}\hbar c}{240 (2d)^{4}}
= \frac{\pi^{2}\hbar c}{240 \times 16 d^{4}}
= \frac{1}{16}\,\frac{\pi^{2}\hbar c}{240 d^{4}}
= \frac{1}{16}\,|P|.
\]

Using the previously computed \(|P| \approx 1.299 \times 10^{-11}\ \text{Pa}\):
\[
P_{\text{double}} = \frac{1.299 \times 10^{-11}}{16}
\approx 8.12 \times 10^{-13}\ \text{Pa}.
\]

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{pressure\_pa} &= 1.299 \times 10^{-11}\ \text{Pa} \\
\mathrm{energy\_per\_area\_uJ\_m2} &= 4.33 \times 10^{-13}\ \mu\text{J/m}^{2} \\
\mathrm{pressure\_double\_d\_pa} &= 8.12 \times 10^{-13}\ \text{Pa}
\end{aligned}
\]