**1. Derivation of $k_B T_c$:**

The degeneracy condition for an ideal Bose gas is given by $n\lambda_T^3 = \zeta(3/2)$, where $\lambda_T = \sqrt{2\pi\hbar^2/(mk_BT)}$ is the thermal de Broglie wavelength. Solving for $T_c$, we have:

\[
n\left(\frac{2\pi\hbar^2}{mk_BT}\right)^{3/2} = \zeta(3/2)
\]

\[
\left(\frac{2\pi\hbar^2}{mk_BT}\right)^{3/2} = \frac{\zeta(3/2)}{n}
\]

\[
T = \frac{2\pi\hbar^2}{mk_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}
\]

\[
k_B T = \frac{2\pi\hbar^2}{m}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}
\]

**2. Evaluation of $T_c$ in nK:**

Given $n = 1.00\times 10^{19}$ m$^{-3}$ and $\zeta(3/2) = 2.612$, we find:

\[
k_B T_c = \frac{2\pi\hbar^2}{1.443\times 10^{-25}\text{ kg}}\left(\frac{1.00\times 10^{19}\text{ m}^{-3}}{2.612}\right)^{2/3}
\]

\[
T_c = \frac{2\pi\hbar^2}{k_B m}\left(\frac{n}{\zeta(3/2)}\right)^{2/3} = 34.0\text{ nK}
\]

**3. Phase-space density at $T_c$ and $2T_c$:**

At $T_c$, $n\lambda_T^3 = \zeta(3/2) = 2.612$.

At $2T_c$, $\lambda_T$ is halved, so $n\lambda_T^3 = \frac{1}{2^3}\zeta(3/2) = \frac{2.612}{8} = 0.3265$.

**4. Dropping $\zeta(3/2)$:**

If we drop $\zeta(3/2)$ and set $n\lambda^3 = 1$, we get:

\[
k_B T_c = \frac{2\pi\hbar^2}{m}\left(\frac{n}{1}\right)^{2/3} = 17.0\text{ nK}
\]

This would correspond to a gas with a density $n = 2.612$ times higher, as $n\lambda^3 = 1$ is the condition for a gas with no interaction and no degeneracy.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{tc\_nK} &= 34.0\text{ nK} \\
\mathrm{phase\_space\_density\_tc} &= 2.612 \\
\mathrm{psd\_at\_2tc} &= 0.3265 \\
\mathrm{tc\_no\_zeta\_nK} &= 17.0\text{ nK}
\end{aligned}
\]