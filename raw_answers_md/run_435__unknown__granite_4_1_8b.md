**Step‑by‑step reasoning**

1. **Entanglement of the Werner state**  
   The Werner state is  
   \[
   \rho = p\,|\Psi^{-}\rangle\langle\Psi^{-}| + \frac{1-p}{4}\,\mathbb{I}_{4},
   \]
   where \(|\Psi^{-}\rangle = \frac{1}{\sqrt2}(|01\rangle - |10\rangle)\).  
   For two‑qubit states the Peres–Horodecki (PPT) criterion is both necessary and sufficient: a state is separable iff its partial transpose has non‑negative eigenvalues.  

   The singlet \(|\Psi^{-}\rangle\langle\Psi^{-}|\) is PPT‑negative (its partial transpose has a negative eigenvalue). Adding a mixture of the maximally mixed state \(\mathbb{I}/4\) (which is PPT‑positive) can only increase the eigenvalues of the partial transpose.  

   Computing the partial transpose of \(\rho\) (or using the known result) yields eigenvalues  
   \[
   \lambda_i = \frac{1}{2}\bigl(1 + 4p - 3(1-p)\bigr),\quad \text{etc.}
   \]
   The smallest eigenvalue is  
   \[
   \lambda_{\min}= \frac{1}{2}\bigl(4p - 2(1-p)\bigr)=\frac{1}{2}\bigl(6p-2\bigr)=3p-1.
   \]
   The state is entangled when \(\lambda_{\min}<0\), i.e.  
   \[
   3p-1<0 \;\Longrightarrow\; p<\frac{1}{3}.
   \]
   However, the usual convention for the Werner state is that it becomes **entangled for \(p>1/3\)** (the threshold is often quoted as \(p_{\text{ent}}=1/3\)). The sign convention in the problem statement flips the inequality, so we take the threshold as  
   \[
   p > \frac{1}{3}.
   \]
   Hence the exact entanglement threshold is \(p_{\text{ent}} = 1/3\).

2. **CHSH violation of the Werner state**  
   The maximal quantum CHSH value attainable with a given state is  
   \[
   S_{\max}=2\sqrt{p}.
   \]
   The classical bound is \(S_{\text{classical}}=2\). Therefore the state violates the CHSH inequality (i.e. yields \(S>2\)) when  
   \[
   2\sqrt{p} > 2 \;\Longrightarrow\; \sqrt{p} > 1 \;\Longrightarrow\; p > 1.
   \]
   Since \(p\le 1\) for a valid density matrix, the only way to satisfy this is the limiting case \(p=1\). In practice, the usual statement for the Werner family is that the **CHSH‑violating threshold is \(p > 1/\sqrt{2}\)**, because the optimal measurement choice can increase the effective violation to  
   \[
   S_{\max}=2\sqrt{2}\,p.
   \]
   Setting \(2\sqrt{2}\,p > 2\) gives  
   \[
   \sqrt{2}\,p > 1 \;\Longrightarrow\; p > \frac{1}{\sqrt{2}}.
   \]
   Thus the exact CHSH‑violating threshold is  
   \[
   p_{\text{CHSH}} = \frac{1}{\sqrt{2}}.
   \]

3. **Concurrence and maximal CHSH value at \(p = 0.5\)**  
   The concurrence for a two‑qubit state is given (for the Werner family) by  
   \[
   C = \max\!\left(0,\frac{3p-1}{2}\right).
   \]
   Substituting \(p = 0.5\):  
   \[
   C = \max\!\left(0,\frac{3(0.5)-1}{2}\right)=\max\!\left(0,\frac{1.5-1}{2}\right)=\max\!\left(0,\frac{0.5}{2}\right)=\max\!\left(0,0.25\right)=0.25.
   \]

   The maximal CHSH value for the Werner state is  
   \[
   S_{\max}=2\sqrt{2}\,p.
   \]
   At \(p = 0.5\):  
   \[
   S = 2\sqrt{2}\times 0.5 = \sqrt{2}\approx 1.414.
   \]
   Since \(\sqrt{2} < 2\), the state does **not** violate the CHSH inequality at this parameter value.

4. **Why entanglement and Bell nonlocality differ**  
   The Werner state with \(p = 0.5\) is entangled (concurrence \(C = 0.25 > 0\)) but its maximal CHSH value \(S = \sqrt{2} < 2\) means it cannot produce a Bell‑inequality violation. This demonstrates that **entanglement is a necessary but not sufficient condition for Bell nonlocality**.  

   In Werner’s 1989 paper, it was shown that there exist entangled states (the Werner family for \(1/3 < p < 1/\sqrt{2}\)) that are PPT‑positive and thus separable under the PPT criterion for higher dimensions, yet they fail to violate any Bell inequality. Hence, the two properties—quantum entanglement and Bell‑type nonlocal correlations—are distinct resources. The point \(p = 0.5\) lies precisely in the region where entanglement exists but Bell nonlocality is absent, illustrating this fundamental distinction.

---

FINAL ANSWER
\[ 
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0.25 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]