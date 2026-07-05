**Derivation of Precession Rate:**

The torque acting on the top due to gravity is given by $\tau = mgl \sin\theta$, where $\theta$ is the angle between the symmetry axis and the vertical. In the fast-top approximation, $\sin\theta \approx \theta$ since the axis is nearly horizontal.

The rate of change of angular momentum is given by $\frac{dL}{dt} = \tau$. The angular momentum $L = I_3\omega_3$ since the top is spinning fast around its symmetry axis. Thus, $\frac{dL}{dt} = I_3\frac{d\omega_3}{dt} \approx 0$ in the fast-top approximation, as the spin rate is nearly constant.

So, $\tau = mgl \sin\theta \approx mgl\theta = I_3\omega_3\frac{d\theta}{dt}$, which gives $\frac{d\theta}{dt} = \frac{mgl}{I_3\omega_3}$. This is the precession rate $\Omega$.

**Calculation of Precession Rate and Period:**

Given $m = 0.500$ kg, $l = 0.0500$ m, $I_3 = 2.00\times 10^{-4}$ kg m$^2$, $\omega_3 = 300$ rad/s, and $g = 9.81$ m/s$^2$, we have:

\[
\Omega = \frac{mgl}{I_3\omega_3} = \frac{0.500 \times 0.0500 \times 9.81}{2.00\times 10^{-4} \times 300} \approx 0.817 \text{ rad/s}
\]

The precession period $T = \frac{2\pi}{\Omega} \approx \frac{2\pi}{0.817} \approx 7.64$ s.

**Effect of Doubling the Spin:**

If the spin $\omega_3$ doubles to $600$ rad/s, the new precession rate $\Omega'$ is:

\[
\Omega' = \frac{mgl}{I_3\omega_3'} = \frac{0.500 \times 0.0500 \times 9.81}{2.00\times 10^{-4} \times 600} \approx 0.408 \text{ rad/s}
\]

So, the precession rate scales inversely with the spin rate, and the new value is $0.408$ rad/s.

**Why the Top Precesses and Nutates:**

The top precesses instead of falling because the torque due to gravity causes the angular momentum to change, leading to a change in the direction of the spin axis. The small nutation superimposed on steady precession is due to the fact that the top is not a perfect top (i.e., it has a small moment of inertia about the other two axes), leading to a small oscillation in the nutation angle.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 0.817 \text{ rad/s} \\
\mathrm{precession\_period\_s} &= 7.64 \text{ s} \\
\mathrm{precession\_double\_spin} &= 0.408 \text{ rad/s}
\end{aligned}
\]