**1. Solve for \(T\) using the Boltzmann ratio**

The convention is  

\[
\frac{N_{\text{up}}}{N_{\text{down}}}=e^{-\Delta E/(k_B T)} .
\]

Take the natural logarithm:

\[
\ln\!\left(\frac{N_{\text{up}}}{N_{\text{down}}}\right)= -\frac{\Delta E}{k_B T}.
\]

Solve for \(T\):

\[
T = -\frac{\Delta E}{k_B\,\ln\!\left(\frac{N_{\text{up}}}{N_{\text{down}}}\right)} .
\]

**2. Insert the given numbers**

- Energy spacing: \(\Delta E = 2.00\times10^{-23}\,\text{J}\).
- Population ratio: \(\displaystyle \frac{N_{\text{up}}}{N_{\text{down}}}=3.00\).
- Boltzmann constant: \(k_B = 1.380649\times10^{-23}\,\text{J/K}\) (exact value).

Compute the logarithm:

\[
\ln(3.00)=1.0986122886681098 .
\]

Compute the denominator:

\[
k_B\,\ln(3)= (1.380649\times10^{-23}\,\text{J/K})\times(1.0986122886681098)
          = 1.5167979\times10^{-23}\,\text{J/K}.
\]

Now evaluate \(T\):

\[
T = -\frac{2.00\times10^{-23}\,\text{J}}{1.5167979\times10^{-23}\,\text{J/K}}
   = -1.3185\ \text{K}.
\]

Thus the temperature obtained from the inverted Boltzmann ratio is negative.

**3. Is a negative‑temperature system colder or hotter than any positive‑temperature system?**

A system with a negative temperature has a *higher* thermodynamic temperature in the sense of heat flow. When a negative‑temperature system is brought into thermal contact with any positive‑temperature system, heat flows **from the negative‑temperature system to the positive‑temperature system**. This occurs because the negative‑temperature system possesses *lower entropy* at a given energy; adding energy actually *reduces* the number of accessible microstates, making it behave as a hot reservoir. Consequently, a negative‑temperature state is hotter than any state with a positive temperature.

**4. Why do negative temperatures require a bounded energy spectrum, and what is a classic experimental realization?**

A bounded (i.e., finite‑upper‑limit) energy spectrum allows the population of higher energy levels to exceed that of lower levels when the system is driven out of equilibrium, producing an inverted distribution. If the spectrum were unbounded, increasing energy would always increase the number of accessible states, preventing a stable inversion and thus a negative temperature.

A classic experimental realization is a **nuclear spin system in a strong magnetic field** (e.g., hyperpolarized nuclear magnetic resonance of spins such as \(^{13}\)C or \(^{1}\)H in a crystal). In such systems the Zeeman energy levels are discrete and bounded, enabling population inversion and the observation of negative temperatures.

---

\[
\begin{aligned}
\mathrm{temperature\_K} &= -1.32 \\
\mathrm{abs\_temperature\_K} &= 1.32
\end{aligned}
\]