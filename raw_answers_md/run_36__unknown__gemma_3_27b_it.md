## Foucault Pendulum Precession Analysis

**1. Derivation of the $\sin\lambda$ factor**

The Foucault pendulum's precession is a consequence of the Coriolis effect acting on the pendulum's motion. The Coriolis effect is proportional to the cross product of the Earth's angular velocity vector $\vec{\Omega}_E$ and the pendulum's velocity vector $\vec{v}$.  We are interested in the component of $\vec{\Omega}_E$ that causes the *plane* of the pendulum's swing to rotate.

Let's define a coordinate system where the z-axis points towards the North Pole. The Earth's angular velocity vector is then $\vec{\Omega}_E = \omega (\cos\lambda \hat{i} + \sin\lambda \hat{k})$, where $\omega$ is the Earth's angular velocity (in radians per unit time), $\lambda$ is the latitude, $\hat{i}$ is the unit vector in the east direction, and $\hat{k}$ is the unit vector in the north direction.

The pendulum swings in a plane.  The Coriolis force acts perpendicular to the pendulum's velocity.  The component of $\vec{\Omega}_E$ that is *perpendicular* to the swing plane is the vertical component, $\Omega_z = \omega \sin\lambda$. This component causes a torque on the pendulum, leading to the precession of the swing plane.  The precession rate is proportional to this vertical component.

To see this more clearly, consider the pendulum's motion in the plane perpendicular to the pendulum's suspension point. The Coriolis force is given by $\vec{F}_C = -2\vec{\Omega}_E \times \vec{v}$. The torque $\vec{\tau}$ on the pendulum due to the Coriolis force is $\vec{\tau} = \vec{r} \times \vec{F}_C$, where $\vec{r}$ is the position vector from the pivot to the pendulum bob. The precession rate is proportional to the torque and inversely proportional to the pendulum's moment of inertia. The relevant component of the torque is proportional to $\Omega_z = \omega \sin\lambda$.

**2. Evaluation of the precession rate**

Given $\lambda = 48.85^\circ$ and Earth's rotation rate is $360^\circ$ per 24 hours, we have $\omega = \frac{360^\circ}{24 \text{ h}} = 15^\circ/\text{h}$.

The precession rate in degrees per hour is:
$\mathrm{rate\_deg\_per\_hour} = \omega \sin\lambda = 15^\circ/\text{h} \times \sin(48.85^\circ) \approx 15^\circ/\text{h} \times 0.7543 \approx 11.31^\circ/\text{h}$.

The precession rate in degrees per day is:
$\mathrm{rate\_deg\_per\_day} = \mathrm{rate\_deg\_per\_hour} \times 24 \text{ h} \approx 11.31^\circ/\text{h} \times 24 \text{ h} \approx 271.44^\circ/\text{day}$.

**3. Evaluation of the full-turn period**

The full-turn period is the time it takes for the swing plane to complete a full rotation ($360^\circ$).
$\mathrm{period\_hours} = \frac{360^\circ}{\mathrm{rate\_deg\_per\_hour}} = \frac{360^\circ}{11.31^\circ/\text{h}} \approx 31.83 \text{ h}$.

**4. Behavior at the Equator and the Pole**

*   **Equator ($\lambda = 0^\circ$):** At the equator, $\sin(0^\circ) = 0$, so the precession rate is zero. The pendulum's plane of oscillation does not rotate.
*   **Pole ($\lambda = 90^\circ$):** At the pole, $\sin(90^\circ) = 1$, so the precession rate is maximum. The pendulum's plane of oscillation completes a full rotation in approximately 24 hours.

**Student's Error**

A student using $\cos\lambda$ has taken the component of $\vec{\Omega}_E$ in the east-west direction. This component is responsible for the apparent deflection of moving objects (the Coriolis deflection), but it does *not* cause the precession of the swing plane. The precession is caused by the component of $\vec{\Omega}_E$ that is perpendicular to the swing plane, which is the vertical component $\omega \sin\lambda$. The east-west component causes a deflection of the pendulum's path, but not a rotation of the plane of oscillation.

\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day} &= 271.44 \\
\mathrm{rate\_deg\_per\_hour} &= 11.31 \\
\mathrm{period\_hours} &= 31.83
\end{aligned}
\]