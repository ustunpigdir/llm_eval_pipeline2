## Derivation and Calculation of BEC Transition

**1. Derivation of $k_B T_c = \frac{2\pi\hbar^2}{m}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}$**

The condition for Bose-Einstein condensation in an ideal gas is that the phase-space density, $n\lambda_T^3$, equals $\zeta(3/2)$, where $\lambda_T$ is the thermal de Broglie wavelength.  We have:

$\lambda_T = \sqrt{\frac{2\pi\hbar^2}{mk_BT}}$

Therefore,

$n\lambda_T^3 = n\left(\sqrt{\frac{2\pi\hbar^2}{mk_BT}}\right)^3 = n\left(\frac{2\pi\hbar^2}{mk_BT}\right)^{3/2} = \zeta(3/2)$

We want to solve for $k_BT_c$.  Rearranging the equation:

$\left(\frac{2\pi\hbar^2}{mk_BT_c}\right)^{3/2} = \frac{\zeta(3/2)}{n}$

$\frac{2\pi\hbar^2}{mk_BT_c} = \left(\frac{\zeta(3/2)}{n}\right)^{2/3}$

$k_BT_c = \frac{2\pi\hbar^2}{m}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}$

This is the desired result.

**2. Evaluation of $T_c$ in nK**

Given:
$m = 1.443 \times 10^{-25}$ kg
$n = 1.00 \times 10^{19}$ m$^{-3}$
$\zeta(3/2) = 2.612$
$\hbar = 1.0545718 \times 10^{-34}$ J s
$k_B = 1.380649 \times 10^{-23}$ J/K

$k_BT_c = \frac{2\pi(1.0545718 \times 10^{-34})^2}{1.443 \times 10^{-25}}\left(\frac{1.00 \times 10^{19}}{2.612}\right)^{2/3}$

$k_BT_c = \frac{2\pi(1.11 \times 10^{-68})}{1.443 \times 10^{-25}}\left(3.826 \times 10^{18}\right)^{2/3}$

$k_BT_c = \frac{6.97 \times 10^{-68}}{1.443 \times 10^{-25}} (1.18 \times 10^{12})$

$k_BT_c = 4.83 \times 10^{-43} \times 1.18 \times 10^{12} = 5.70 \times 10^{-31}$ J

$T_c = \frac{5.70 \times 10^{-31}}{1.380649 \times 10^{-23}} = 4.13 \times 10^{-8}$ K

$T_c = 4.13 \times 10^{-8} \times 10^9$ nK $= 41.3$ nK

**3. Phase-Space Density at $T_c$ and $2T_c$**

At $T_c$, by definition, $n\lambda_T^3 = \zeta(3/2) = 2.612$.

At $2T_c$, we have:

$n\lambda_{T,2T_c}^3 = n\left(\sqrt{\frac{2\pi\hbar^2}{m k_B (2T_c)}}\right)^3 = n\left(\frac{2\pi\hbar^2}{m k_B (2T_c)}\right)^{3/2} = \frac{n\left(\frac{2\pi\hbar^2}{m k_B T_c}\right)^{3/2}}{2^{3/2}} = \frac{\zeta(3/2)}{2^{3/2}} = \frac{2.612}{2.828} \approx 0.923$

**4. Student's Incorrect $T_c$**

If the student drops $\zeta(3/2)$ and sets $n\lambda_T^3 = 1$, then:

$n\left(\frac{2\pi\hbar^2}{mk_BT_c}\right)^{3/2} = 1$

$\frac{2\pi\hbar^2}{mk_BT_c} = \left(\frac{1}{n}\right)^{2/3}$

$k_BT_c = \frac{2\pi\hbar^2}{m}\left(\frac{1}{n}\right)^{-2/3} = \frac{2\pi\hbar^2}{m} n^{2/3}$

$k_BT_c = \frac{2\pi(1.0545718 \times 10^{-34})^2}{1.443 \times 10^{-25}} (1.00 \times 10^{19})^{2/3}$

$k_BT_c = \frac{6.97 \times 10^{-68}}{1.443 \times 10^{-25}} (1.00 \times 10^{12.66}) = 4.83 \times 10^{-43} \times 4.0 \times 10^{12} = 1.93 \times 10^{-30}$ J

$T_c = \frac{1.93 \times 10^{-30}}{1.380649 \times 10^{-23}} = 1.40 \times 10^{-7}$ K

$T_c = 1.40 \times 10^{-7} \times 10^9$ nK $= 140$ nK

The factor $\zeta(3/2) = 2.612$ accounts for the Pauli exclusion principle.  It represents the number of ways to distribute identical bosons into the lowest energy state.  Without this factor, the phase-space density would not accurately reflect the true onset of Bose-Einstein condensation, and the calculated $T_c$ would be significantly off.  The student's calculation assumes that only one state is occupied, which is not correct for a Bose gas.



\[
\begin{aligned}
\mathrm{tc\_nK} &= 41.3 \\
\mathrm{phase\_space\_density\_tc} &= 2.612 \\
\mathrm{psd\_at\_2tc} &= 0.923 \\
\mathrm{tc\_no\_zeta\_nK} &= 140
\end{aligned}
\]