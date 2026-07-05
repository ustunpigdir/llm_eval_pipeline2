**1. Write $\bar{\rho}$ and find its eigenvalues.**

The average state $\bar{\rho}$ is given by:
\[
\bar{\rho} = \frac{1}{2}(|0\rangle\langle0| + |+\rangle\langle+|)
\]
where $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$. To find the eigenvalues, we first compute $\bar{\rho}^2$:
\[
\bar{\rho}^2 = \frac{1}{4}(|0\rangle\langle0| + |+\rangle\langle+| + 2\text{Re}(\langle0|+ \rangle\langle+|)) = \frac{1}{4}(|0\rangle\langle0| + |+\rangle\langle+| + 2\text{Re}(\frac{1}{\sqrt{2}}\langle0| + \rangle))
\]
Since $\text{Re}(\frac{1}{\sqrt{2}}\langle0| + \rangle) = \frac{1}{2}$, we have:
\[
\bar{\rho}^2 = \frac{1}{4}(|0\rangle\langle0| + |+\rangle\langle+| + 1) = \frac{1}{4}(|0\rangle\langle0| + |+\rangle\langle+|) + \frac{1}{4}
\]
The eigenvalues of $\bar{\rho}$ are the square roots of the eigenvalues of $\bar{\rho}^2$, which are $\frac{1}{2}$ and $\frac{1}{4}$.

**2. Evaluate $\chi$ in bits.**

The Holevo quantity $\chi$ is given by:
\[
\chi = S(\bar{\rho}) - \sum_x p_x S(\rho_x)
\]
where $S(\rho) = -\text{Tr}(\rho\log_2\rho)$ for a pure state $\rho$. Since $\rho_0 = |0\rangle\langle0|$ and $\rho_1 = |+\rangle\langle+|$, we have:
\[
S(\rho_0) = S(\rho_1) = 0
\]
and
\[
S(\bar{\rho}) = -\left(\frac{1}{2}\log_2\frac{1}{2} + \frac{1}{4}\log_2\frac{1}{4}\right) = \frac{3}{4}
\]
Thus,
\[
\chi = \frac{3}{4} - 0 = \frac{3}{4} \text{ bits}
\]

**3. Evaluate the purity $\text{Tr}\,\bar{\rho}^2$.**

The purity of the average state is given by:
\[
\text{Tr}\,\bar{\rho}^2 = \frac{1}{4}(1 + 1) + \frac{1}{4} = \frac{3}{4}
\]

**4. Explain (a) why $\chi < 1$ bit even though a whole qubit was sent, and (b) whether any measurement lets Bob extract more than $\chi$ bits.**

(a) The Holevo bound $\chi$ is the maximum amount of classical information that can be reliably extracted from the ensemble of states, not the amount of information sent. Even though Alice sends a whole qubit, the non-orthogonality of the states means that Bob cannot perfectly distinguish between them, leading to a Holevo bound less than 1 bit.

(b) No measurement lets Bob extract more than $\chi$ bits. The Holevo bound is an upper bound on the accessible information, meaning that no measurement strategy can achieve more than $\chi$ bits of information. This is because the Holevo bound is derived from the quantum mutual information, which takes into account the optimal measurement strategy for the receiver.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{eigenvalue\_large} &= \frac{1}{2} \\
\mathrm{holevo\_chi\_bits} &= \frac{3}{4} \\
\mathrm{avg\_state\_purity} &= \frac{3}{4}
\end{aligned}
\]