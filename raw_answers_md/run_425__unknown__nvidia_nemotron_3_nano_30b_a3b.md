**1. Average teleportation fidelity for \(f = 0.900\)**  

The average teleportation fidelity for an isotropic resource is given by  
\[
F = \frac{2f+1}{3}.
\]  
Substituting \(f = 0.9\):
\[
\begin{aligned}
F &= \frac{2(0.9)+1}{3}
   = \frac{1.8+1}{3}
   = \frac{2.8}{3}
   = \frac{28}{30}
   = \frac{14}{15}
   \approx 0.9333.
\end{aligned}
\]

**2. Classical limit**  

The best average fidelity achievable without quantum entanglement (i.e., by a measure‑and‑prepare strategy) for a uniformly random pure qubit input is known to be  
\[
F_{\text{classical}} = \frac{2}{3}\approx 0.6667.
\]  
Thus the classical limit is \(\frac{2}{3}\).

**3. Minimum singlet fidelity \(f\) that beats the classical limit**  

We require \(F > F_{\text{classical}}\):
\[
\frac{2f+1}{3} > \frac{2}{3}
\;\Longrightarrow\;
2f+1 > 2
\;\Longrightarrow\;
2f > 1
\;\Longrightarrow\;
f > \frac{1}{2}.
\]  
Hence the threshold fidelity is \(f_{\text{threshold}} = \frac{1}{2}\). Any \(f\) strictly larger than \(0.5\) yields an average teleportation fidelity exceeding the classical limit.

**4. Why \(f > \tfrac12\) signals entanglement and beating \(\tfrac23\) certifies a quantum channel**  

- The isotropic state \(\chi\) is a mixture of the maximally entangled singlet \(|\Psi^-\rangle\) and white noise. Its density matrix can be written as  
  \[
  \chi = f\,|\Psi^-\rangle\langle\Psi^-| + \frac{1-f}{3}\,I,
  \]  
  where the coefficient \(f\) is the singlet fidelity. The state is entangled iff its partial transpose has a negative eigenvalue, which occurs precisely when \(f > \tfrac12\). Thus \(f > \tfrac12\) is the entanglement witness for isotropic states.

- In quantum teleportation, the achievable average fidelity is \(F = (2f+1)/3\). When \(f = \tfrac12\), \(F = \tfrac23\). Therefore, any resource with \(f > \tfrac12\) yields \(F > \tfrac23\). Since \(\tfrac23\) is the classical limit, surpassing it demonstrates that the channel uses genuine quantum correlations (entanglement) and cannot be simulated classically. This is the standard certification argument: a teleportation protocol that exceeds the classical bound proves the existence of a quantum channel with entangled resources.

---

\[
\begin{aligned}
\mathrm{teleport\_fidelity} &= \frac{14}{15} \\
\mathrm{classical\_limit} &= \frac{2}{3} \\
\mathrm{f\_threshold} &= \frac{1}{2}
\end{aligned}
\]