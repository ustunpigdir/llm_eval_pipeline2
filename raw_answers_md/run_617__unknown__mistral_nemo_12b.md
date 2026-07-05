**1. Time calculations:**

- The traveler's speed is $v = 0.6c$. The distance to the star is $6.00$ ly. The Earth frame time for the round trip is:
  \[
  t_{\text{Earth}} = \frac{2 \times 6.00 \text{ ly}}{0.6c} = \frac{12.00}{0.6} \approx 20 \text{ years}
  \]

- The traveler's proper time for the round trip is:
  \[
  t_{\text{proper}} = \frac{6.00}{0.6c} \gamma = \frac{6.00}{0.6} \sqrt{\frac{1}{1 - (0.6)^2}} \approx 10.61 \text{ years}
  \]
  where $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$ is the Lorentz factor.

**2. Doppler factor calculations:**

- For approach, the traveler is moving towards the Earth, so $\beta = 0.6$:
  \[
  k_{\text{approach}} = \sqrt{\frac{1 + 0.6}{1 - 0.6}} = \sqrt{\frac{1.6}{0.4}} = \sqrt{4} = 2
  \]

- For recession, the traveler is moving away from the Earth, so $\beta = -0.6$:
  \[
  k_{\text{recede}} = \sqrt{\frac{1 - 0.6}{1 + 0.6}} = \sqrt{\frac{0.4}{1.6}} = \sqrt{0.25} = 0.5
  \]

**3. Pulse counting (k-calculus):**

- On the outbound leg, the traveler receives:
  \[
  n_{\text{out}} = t_{\text{Earth}} \times k_{\text{approach}} = 20 \times 2 = 40 \text{ pulses}
  \]

- On the return leg, the traveler receives:
  \[
  n_{\text{return}} = t_{\text{Earth}} \times k_{\text{recede}} = 20 \times 0.5 = 10 \text{ pulses}
  \]

- Total pulses received by the traveler:
  \[
  n_{\text{total}} = n_{\text{out}} + n_{\text{return}} = 40 + 10 = 50 \text{ pulses}
  \]

**4. Symmetry between the twins:**

The situation is not symmetric because the traveler experiences time dilation, while the Earth observer does not. The traveler's proper time is less than the Earth's time, and the number of pulses received by the traveler is less than the number sent by the Earth.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{earth\_time\_yr} &= 20 \\
\mathrm{traveler\_time\_yr} &= 10.61 \\
\mathrm{doppler\_k\_approach} &= 2 \\
\mathrm{doppler\_k\_recede} &= 0.5
\end{aligned}
\]