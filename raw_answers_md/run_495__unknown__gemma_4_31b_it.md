### 1. Derivation of the Resonance Condition

We consider a 1D square well potential:
$V(x) = -V_0$ for $0 < x < L$ and $V(x) = 0$ elsewhere.
An electron with energy $E > 0$ is incident from the left.

**Wavefunctions:**
- Region I ($x < 0$): $\psi_I(x) = e^{ikx} + R e^{-ikx}$, where $k = \sqrt{2mE}/\hbar$.
- Region II ($0 < x < L$): $\psi_{II}(x) = A e^{ik'x} + B e^{-ik'x}$, where $k' = \sqrt{2m(E+V_0)}/\hbar$.
- Region III ($x > L$): $\psi_{III}(x) = T e^{ikx}$.

**Boundary Conditions:**
At $x=0$:
1. $1 + R = A + B$
2. $ik(1 - R) = ik'(A - B)$

At $x=L$:
3. $A e^{ik'L} + B e^{-ik'L} = T e^{ikL}$
4. $ik'(A e^{ik'L} - B e^{-ik'L}) = ik T e^{ikL}$

From (3) and (4), we solve for $A$ and $B$ in terms of $T$:
$2A e^{ik'L} = T e^{ikL} (1 + \frac{k}{k'}) \implies A = \frac{T}{2} e^{i(k-k')L} (1 + \frac{k}{k'})$
$2B e^{-ik'L} = T e^{ikL} (1 - \frac{k}{k'}) \implies B = \frac{T}{2} e^{i(k+k')L} (1 - \frac{k}{k'})$

Substituting $A$ and $B$ into the $x=0$ equations:
$1+R = \frac{T}{2} [e^{i(k-k')L}(1 + \frac{k}{k'}) + e^{i(k+k')L}(1 - \frac{k}{k'})]$
$1-R = \frac{k}{k'} \frac{T}{2} [e^{i(k-k')L}(1 + \frac{k}{k'}) - e^{i(k+k')L}(1 - \frac{k}{k'})]$

Adding these two equations to eliminate $R$:
$2 = \frac{T}{2} [e^{i(k-k')L}(1 + \frac{k}{k'} + \frac{k}{k'} + \frac{k^2}{k'^2}) + e^{i(k+k')L}(1 - \frac{k}{k'} - \frac{k}{k'} + \frac{k^2}{k'^2})]$
$2 = \frac{T}{2} [e^{i(k-k')L}(1 + \frac{k}{k'})^2 + e^{i(k+k')L}(1 - \frac{k}{k'})^2]$

Perfect transmission ($T=1$) occurs when the reflection coefficient $R=0$. This happens when the wave inside the well undergoes a full cycle (or multiple) such that the reflections at the two boundaries interfere destructively. The condition for $T=1$ is:
$k' L = n\pi$ for $n = 1, 2, 3, \dots$

Substituting $k' = \sqrt{2m(E+V_0)}/\hbar$:
$\frac{2m(E_n + V_0)}{\hbar^2} L^2 = n^2 \pi^2 \implies E_n + V_0 = \frac{n^2 \pi^2 \hbar^2}{2mL^2}$
$E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2} - V_0$

### 2. Evaluation of the Energy Unit
Given:
$L = 0.400 \text{ nm} = 4.00 \times 10^{-10} \text{ m}$
$m = 9.109 \times 10^{-31} \text{ kg}$
$\hbar = 1.05457 \times 10^{-34} \text{ J}\cdot\text{s}$

$\text{Unit} = \frac{\pi^2 \hbar^2}{2mL^2} = \frac{\pi^2 (1.05457 \times 10^{-34})^2}{2 (9.109 \times 10^{-31}) (4.00 \times 10^{-10})^2}$
$\text{Unit} = \frac{1.0976 \times 10^{-67}}{2.9149 \times 10^{-49}} \approx 3.765 \times 10^{-19} \text{ J}$

Convert to eV ($1 \text{ eV} = 1.60218 \times 10^{-19} \text{ J}$):
$\text{Unit (eV)} = \frac{3.765 \times 10^{-19}}{1.60218 \times 10^{-19}} \approx 2.350 \text{ eV}$

### 3. Finding the Lowest Resonance $E > 0$
$E_n = n^2(2.350 \text{ eV}) - 10.0 \text{ eV}$
- For $n=1$: $E_1 = 2.350 - 10.0 = -7.65 \text{ eV}$ (Bound state, not scattering)
- For $n=2$: $E_2 = 4(2.350) - 10.0 = 9.40 - 10.0 = -0.60 \text{ eV}$ (Bound state)
- For $n=3$: $E_3 = 9(2.350) - 10.0 = 21.15 - 10.0 = 11.15 \text{ eV}$

The smallest integer $n$ giving $E_n > 0$ is $n=3$.
The resonance energy is $E_3 = 11.15 \text{ eV}$.

### 4. Relation to Ramsauer-Townsend Effect
The Ramsauer-Townsend effect is the observation that electrons of certain energies are not scattered by noble gas atoms. In a simplified 1D model, this corresponds to the resonance condition $k'L = n\pi$. At these energies, the electron wave's phase shift across the potential well is a multiple of $\pi$, causing the reflected waves from the front and back edges of the well to cancel perfectly via destructive interference, leading to $T=1$.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{energy\_unit\_ev} &= 2.350 \\
\mathrm{n\_lowest} &= 3 \\
\mathrm{first\_resonance\_ev} &= 11.15
\end{aligned}
\]