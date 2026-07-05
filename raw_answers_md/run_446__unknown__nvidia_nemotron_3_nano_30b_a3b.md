**1. Entanglement threshold**

For a two‑qubit Werner state  
\[
\rho(p)=p\,|\Psi^{-}\rangle\langle\Psi^{-}|+(1-p)\frac{\mathbb I}{4},
\]
the state is separable (i.e. not entangled) exactly when \(p\le \frac13\).  
Equivalently, it is entangled iff \(p>\frac13\).  
Hence the entanglement threshold is  

\[
p_{\text{ent}} = \frac13 .
\]

---

**2. CHSH‑violation threshold**

The maximal CHSH value achievable with \(\rho(p)\) is \(S_{\max}=2\sqrt{2}\,p\).  
A violation of the CHSH inequality (\(S>2\)) occurs when  

\[
2\sqrt{2}\,p > 2 \;\Longrightarrow\; p > \frac{1}{\sqrt{2}} .
\]

Thus the CHSH‑violation threshold is  

\[
p_{\text{CHSH}} = \frac{1}{\sqrt{2}} .
\]

---

**3. Concurrence and CHSH value at \(p=0.500\)**  

The concurrence for a Werner state is given by  

\[
C(p)=\max\!\bigl(0,\tfrac{3p-1}{2}\bigr).
\]

At \(p=0.5\),

\[
3p-1 = 3(0.5)-1 = 1.5-1 = 0.5,\qquad 
\frac{3p-1}{2}= \frac{0.5}{2}=0.25,
\]
so  

\[
C(0.5)=0.25 .
\]

The maximal CHSH value at the same parameter is  

\[
S_{\max}(p)=2\sqrt{2}\,p \;\Longrightarrow\;
S_{\max}(0.5)=2\sqrt{2}\times 0.5 = \sqrt{2}\approx 1.4142 .
\]

---

**4. Why entanglement ≠ CHSH nonlocality**

At \(p=0.5\) we have \(p>\frac13\) (so the state is entangled) but \(p=0.5<\frac{1}{\sqrt{2}}\approx0.707\), so the CHSH value satisfies \(S=\sqrt{2}<2\).  
Thus the state is entangled yet does **not** violate any CHSH inequality.  
Entanglement is a necessary condition for Bell‑type nonlocality, but it is not sufficient; a state can be entangled without exhibiting Bell‑inequality violations. This distinction was highlighted by Werner (1989) in his analysis of mixed states.

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