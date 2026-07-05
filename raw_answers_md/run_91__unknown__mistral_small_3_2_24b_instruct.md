To derive the precession rate \(\Omega\) of a fast top, we start with the torque equation and the rate of change of angular momentum.

1. **Torque and Angular Momentum:**

   The torque \(\tau\) acting on the top due to gravity is given by:
   \[
   \tau = mgl \sin \theta
   \]
   where \(m\) is the mass, \(g\) is the acceleration due to gravity, \(l\) is the distance from the pivot to the center of mass, and \(\theta\) is the tilt angle. For a fast top, the tilt angle \(\theta\) is small, so \(\sin \theta \approx \theta\).

   The angular momentum \(\mathbf{L}\) of the top is given by:
   \[
   \mathbf{L} = I_3 \omega_3 \hat{k}
   \]
   where \(I_3\) is the moment of inertia about the spin axis, and \(\omega_3\) is the spin rate.

2. **Rate of Change of Angular Momentum:**

   The rate of change of angular momentum is:
   \[
   \frac{d\mathbf{L}}{dt} = I_3 \frac{d\omega_3}{dt} \hat{k} + I_3 \omega_3 \frac{d\hat{k}}{dt}
   \]
   For a fast top, the spin rate \(\omega_3\) is much larger than the precession rate \(\Omega\), so we can neglect the first term. The second term is due to the precession of the spin axis:
   \[
   \frac{d\hat{k}}{dt} = \Omega \hat{\phi}
   \]
   where \(\hat{\phi}\) is the unit vector in the direction of precession.

3. **Equating Torque and Rate of Change of Angular Momentum:**

   The torque \(\tau\) is equal to the rate of change of angular momentum:
   \[
   \tau = \frac{d\mathbf{L}}{dt}
   \]
   Substituting the expressions for \(\tau\) and \(\frac{d\mathbf{L}}{dt}\), we get:
   \[
   mgl \theta = I_3 \omega_3 \Omega
   \]
   For a fast top, the tilt angle \(\theta\) is small, so \(\theta \approx \sin \theta\). Therefore, we can write:
   \[
   mgl \sin \theta = I_3 \omega_3 \Omega
   \]
   Solving for \(\Omega\), we get:
   \[
   \Omega = \frac{mgl}{I_3 \omega_3}
   \]

4. **Evaluating \(\Omega\) and the Precession Period:**

   Given:
   \[
   m = 0.500 \, \text{kg}, \quad l = 0.0500 \, \text{m}, \quad g = 9.81 \, \text{m/s}^2, \quad I_3 = 2.00 \times 10^{-4} \, \text{kg m}^2, \quad \omega_3 = 300 \, \text{rad/s}
   \]
   Substituting these values into the equation for \(\Omega\), we get:
   \[
   \Omega = \frac{0.500 \times 9.81 \times 0.0500}{2.00 \times 10^{-4} \times 300} = \frac{0.24525}{0.06} = 4.0875 \, \text{rad/s}
   \]
   The precession period \(T\) is given by:
   \[
   T = \frac{2\pi}{\Omega} = \frac{2\pi}{4.0875} \approx 1.526 \, \text{s}
   \]

5. **Doubling the Spin Rate:**

   If the spin rate \(\omega_3\) doubles, the new spin rate is \(600 \, \text{rad/s}\). The new precession rate \(\Omega'\) is:
   \[
   \Omega' = \frac{mgl}{I_3 \omega_3'} = \frac{0.500 \times 9.81 \times 0.0500}{2.00 \times 10^{-4} \times 600} = \frac{0.24525}{0.12} = 2.04375 \, \text{rad/s}
   \]
   The precession rate scales inversely with the spin rate, so doubling the spin rate halves the precession rate.

6. **Explanation of Precession and Nutation:**

   The top precesses instead of falling because the torque due to gravity causes a change in the direction of the angular momentum vector, resulting in precession. The small nutation superimposed on the steady precession is due to the small oscillations of the tilt angle \(\theta\) around its equilibrium value.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 4.0875 \\
\mathrm{precession\_period\_s} &= 1.526 \\
\mathrm{precession\_double\_spin} &= 2.04375
\end{aligned}
\]