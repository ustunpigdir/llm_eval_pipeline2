**Step‑by‑step reasoning**

1. **Entanglement of the Werner state**  
   The Werner state is  
   \[
   \rho = p\,|\Psi^{-}\rangle\langle\Psi^{-}| + \frac{1-p}{4}\,\mathbb{I}_{4},
   \]
   where \(|\Psi^{-}\rangle = \frac{1}{\sqrt2}(|01\rangle - |10\rangle)\).  
   For two‑qubit states the Peres–Horodecki (PPT) criterion is both necessary and sufficient: a state is separable iff its partial transpose has non‑negative eigenvalues.  

   The singlet \(|\Psi^{-}\rangle\langle\Psi^{-}|\) is PPT‑negative (its partial transpose has a negative eigenvalue). Adding a positive operator \(\frac{1-p}{4}\mathbb{I}\) can only increase the eigenvalues of the partial transpose. Therefore the state becomes separable when the negative eigenvalue is completely cancelled, i.e. when the weight of the singlet is below a critical value.  

   For the Werner state this critical weight is known to be \(p_{\text{sep}} = \frac{1}{3}\). Hence the state is **entangled** for  
   \[
   p > \frac{1}{3}.
   \]
   **Entanglement threshold:** \(p_{\text{ent}} = 1/3\).

2. **CHSH violation (Bell non‑locality)**  
   The maximal quantum CHSH value attainable with a given amount of singlet component is \(S_{\max}=2\sqrt{2}\,p\). A local hidden‑variable model can never exceed \(S=2\). Consequently the state violates the CHSH inequality iff  
   \[
   2\sqrt{2}\,p > 2 \;\Longrightarrow\; p > \frac{1}{\sqrt{2}}.
   \]
   **CHSH threshold:** \(p_{\text{CHSH}} = 1/\sqrt{2}\).

3. **Concurrence at \(p = 0.5\)**  
   The concurrence for a two‑qubit state is  
   \[
   C = \max\!\bigl(0,\; \lambda_{1}-\lambda_{2}-\lambda_{3}-\lambda_{4}\bigr),
   \]
   where \(\lambda_i\) are the square roots of the eigenvalues of \(\rho (\sigma_y\otimes\sigma_y)\rho^{\dagger}(\sigma_y\otimes\sigma_y)\).  
   For the Werner state a closed form is known:  
   \[
   C(p) = \max\!\bigl(0,\; 2p-1\bigr).
   \]
   Setting \(p = 0.5\):  
   \[
   C(0.5) = \max\!\bigl(0,\; 2\times0.5-1\bigr) = \max(0,0) = 0.
   \]
   **Concurrence at \(p=0.5\):** \(C_{0.5}=0\).

4. **Maximal CHSH value at \(p = 0.5\)**  
   Using the known maximal CHSH value for the Werner state:  
   \[
   S_{\max}(p) = 2\sqrt{2}\,p.
   \]
   For \(p = 0.5\):  
   \[
   S_{\max}(0.5) = 2\sqrt{2}\times0.5 = \sqrt{2} \approx 1.414.
   \]
   Since \(\sqrt{2} < 2\), the state does **not** violate the CHSH bound, consistent with the threshold found in step 2 (\(p > 1/\sqrt{2}\approx0.707\)).  

   **Why entanglement ≠ Bell non‑locality**  
   The Werner state with \(p=0.5\) is entangled (its PPT is negative, i.e., it lies in the entangled region \(p>1/3\)) but its CHSH value is only \(\sqrt{2}<2\). Thus it cannot demonstrate any Bell‑inequality violation. Werner’s 1989 paper showed that **entanglement** (PPT negativity) is a weaker resource than **Bell non‑locality** (CHSH violation). A state can be genuinely non‑separable yet still be “local” in the sense of not being able to produce correlations that exceed the classical bound \(S\le2\). This distinction is crucial: entanglement is necessary but not sufficient for all quantum tasks, such as device‑independent randomness generation or secure quantum communication, which require CHSH violation.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]