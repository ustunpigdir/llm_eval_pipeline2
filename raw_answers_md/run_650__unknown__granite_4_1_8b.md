**Step‑by‑step reasoning**

1. **Mean‑field estimate**  
   For the Ising model the mean‑field critical temperature is given by  
   \[
   k_B T_c^{MF}/J = z,
   \]  
   where \(z\) is the coordination number (number of nearest neighbours).  
   For the square lattice \(z = 4\). Hence  
   \[
   k_B T_c^{MF}/J = 4.
   \]

2. **Onsager’s exact result**  
   Onsager solved the 2‑D Ising model exactly (1944). The exact critical temperature satisfies  
   \[
   k_B T_c^{exact}/J = \frac{2}{\ln\!\bigl(1+\sqrt{2}\bigr)}.
   \]  
   Evaluating the logarithm:  
   \[
   \sqrt{2} \approx 1.41421356,\qquad
   1+\sqrt{2} \approx 2.41421356,\qquad
   \ln(2.41421356) \approx 0.88137358.
   \]  
   Therefore  
   \[
   k_B T_c^{exact}/J \approx \frac{2}{0.88137358} \approx 2.269.
   \]

3. **Ratio of exact to mean‑field critical temperatures**  
   \[
   \frac{T_c^{exact}}{T_c^{MF}} = \frac{k_B T_c^{exact}/J}{k_B T_c^{MF}/J}
   = \frac{2/\ln(1+\sqrt{2})}{4}
   = \frac{1}{2\,\ln(1+\sqrt{2})}
   \approx \frac{1}{2 \times 0.88137358}
   \approx 0.567.
   \]  
   **Why mean‑field overestimates \(T_c\):**  
   In low dimensions (especially \(d=2\)) thermal fluctuations are strong. Mean‑field theory neglects these fluctuations, treating each spin as if it felt an average field from its neighbours. Consequently it predicts a higher ordering temperature than the true system, where fluctuations lower the critical temperature.

4. **One‑dimensional case**  
   For the 1‑D Ising model with nearest‑neighbour coupling \(J>0\) and zero external field, the exact solution shows **no spontaneous magnetization at any finite temperature**. Hence the critical temperature is  
   \[
   k_B T_c^{1D}/J = 0.
   \]  
   The physical reason is the Mermin–Wagner theorem: in one dimension continuous symmetries cannot be broken at finite temperature, and the decay of correlations in 1‑D prevents long‑range order. Consequently fluctuations dominate completely, suppressing any phase transition.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{tc\_exact} &= \frac{2}{\ln\!\bigl(1+\sqrt{2}\bigr)} \approx 2.269,\\[4pt]
\mathrm{tc\_meanfield} &= 4,\\[4pt]
\mathrm{ratio\_exact\_mf} &= \frac{1}{2\,\ln\!\bigl(1+\sqrt{2}\bigr)} \approx 0.567.
\end{aligned}
\]