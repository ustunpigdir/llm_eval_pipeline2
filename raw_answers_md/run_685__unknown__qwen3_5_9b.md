### 1. Landauer Bound and Origin

The Landauer principle establishes a fundamental thermodynamic limit on information processing. It states that any logically irreversible manipulation of information, such as the erasure of a bit, must be accompanied by a corresponding increase in the physical entropy of the environment.

**Derivation:**
Consider a single bit of information that can exist in one of two states, 0 or 1. If the bit is in a random state with equal probability ($p_0 = p_1 = 0.5$), its Shannon entropy (in bits) is 1. In thermodynamic terms, the entropy of the bit is:
$$ S_{\text{bit}} = -k_B \sum_{i} p_i \ln p_i = -k_B (0.5 \ln 0.5 + 0.5 \ln 0.5) = k_B \ln 2 $$
Erasing the bit means forcing it into a specific state (e.g., 0), regardless of its initial state. The final entropy of the bit is $S_{\text{final}} = 0$.
The change in the entropy of the information system is:
$$ \Delta S_{\text{sys}} = S_{\text{final}} - S_{\text{initial}} = 0 - k_B \ln 2 = -k_B \ln 2 $$
According to the Second Law of Thermodynamics, the total entropy change of the universe (system + environment) must be non-negative:
$$ \Delta S_{\text{total}} = \Delta S_{\text{sys}} + \Delta S_{\text{env}} \ge 0 $$
Substituting $\Delta S_{\text{sys}}$:
$$ -k_B \ln 2 + \Delta S_{\text{env}} \ge 0 \implies \Delta S_{\text{env}} \ge k_B \ln 2 $$
The heat $Q$ dissipated into the environment at temperature $T$ is related to the entropy change by $Q = T \Delta S_{\text{env}}$. Therefore, the minimum heat dissipated is:
$$ Q_{\min} = T (k_B \ln 2) = k_B T \ln 2 $$
This cost arises specifically from the **erasure** (logical irreversibility), not from the computation itself. Computation that is logically reversible does not require this entropy increase.

### 2. Evaluation of $Q_{\min}$ at 300 K

We calculate the value using the standard physical constants:
-   Boltzmann constant: $k_B \approx 1.380649 \times 10^{-23} \, \text{J/K}$
-   Temperature: $T = 300 \, \text{K}$
-   Natural log of 2: $\ln 2 \approx 0.693147$

**Calculation in Joules:**
$$ Q_{\min} = (1.380649 \times 10^{-23} \, \text{J/K}) \times (300 \, \text{K}) \times (0.693147) $$
$$ Q_{\min} = 414.1947 \times 10^{-23} \times 0.693147 \, \text{J} $$
$$ Q_{\min} \approx 287.096 \times 10^{-23} \, \text{J} $$
$$ Q_{\min} \approx 2.87096 \times 10^{-21} \, \text{J} $$

**Conversion to Zeptojoules (zJ):**
Given $1 \, \text{zJ} = 10^{-21} \, \text{J}$:
$$ Q_{\min} \approx 2.87 \, \text{zJ} $$

**Conversion to Millielectronvolts (meV):**
Given $1 \, \text{eV} = 1.602176634 \times 10^{-19} \, \text{J}$:
$$ Q_{\min} (\text{eV}) = \frac{2.87096 \times 10^{-21} \, \text{J}}{1.602176634 \times 10^{-19} \, \text{J/eV}} $$
$$ Q_{\min} (\text{eV}) \approx 0.017919 \, \text{eV} $$
$$ Q_{\min} (\text{meV}) = 0.017919