Okay, let's break down this problem step by step.

**1. Derivation of Ω = mgl/(I₃ω₃)**

The torque acting on the top due to gravity is given by:

τ = -mg * l *  $\hat{z}$

where $m$ is the mass, $g$ is the acceleration due to gravity, $l$ is the distance from the pivot to the center of mass, and $\hat{z}$ is the unit vector along the symmetry axis.

The rate of change of angular momentum is given by:

τ = dL/dt

where L is the angular momentum.  In the fast-top approximation, the angular momentum is primarily due to the spin about the symmetry axis, so L ≈ I₃ω₃ * $\hat{z}$.  Therefore:

τ = d(I₃ω₃ * $\hat{z}$)/dt = I₃ dω₃/dt * $\hat{z}$

Since the spin is assumed to be constant in the fast-top approximation, dω₃/dt = 0. However, the axis of the angular momentum vector *does* change direction.  The angular momentum vector is $\vec{L} = I_3 \vec{\omega}_3$. The torque causes a precession, which means the angular momentum vector is changing in direction, but its magnitude remains constant.  The rate of precession is $\Omega$.  Therefore, the change in angular momentum is:

dL/dt = Ω x L

where Ω is the precession angular velocity vector. Since L is along the z-axis, Ω must be in the xy-plane.  The magnitude of the change in angular momentum is:

|dL/dt| = Ω |L| = Ω I₃ω₃

Equating the two expressions for the torque:

-mg l = Ω I₃ω₃

Solving for Ω:

Ω = -mg l / (I₃ω₃)

The negative sign indicates that the precession is opposite to the direction of the torque.  We are interested in the magnitude of the precession rate, so we take the absolute value:

Ω = mgl / (I₃ω₃)

**2. Evaluation of Ω and the Precession Period**

Given:
m = 0.500 kg
l = 0.0500 m
g = 9.81 m/s²
I₃ = 2.00 x 10⁻⁴ kg m²
ω₃ = 300 rad/s

Ω = (0.500 kg * 9.81 m/s² * 0.0500 m) / (2.00 x 10⁻⁴ kg m² * 300 rad/s)
Ω = 0.24525 / 0.06 = 4.0875 rad/s

The precession period, T, is the time it takes for one complete precession:

T = 2π / Ω
T = 2π / 4.0875 rad/s
T ≈ 1.548 s

**3. Precession Rate if Spin Doubles**

If the spin doubles, ω₃' = 2 * ω₃ = 2 * 300 rad/s = 600 rad/s.

Ω' = mgl / (I₃ω₃')
Ω' = (0.500 kg * 9.81 m/s² * 0.0500 m) / (2.00 x 10⁻⁴ kg m² * 600 rad/s)
Ω' = 0.24525 / 0.12 = 2.04375 rad/s

The scaling is: Ω' = Ω / 2.  The new precession rate is 2.04375 rad/s.

**4. Explanation of Precession and Nutation**

The top precesses instead of falling because the angular momentum vector, due to its spin, resists changes in its direction. The gravitational torque tries to pull the top down, but instead of causing the top to fall, it causes the angular momentum vector to sweep out a cone in space. This sweeping motion is precession.

Nutation is a small, superimposed oscillation on the steady precession. It arises from the fact that the fast-top approximation is not perfectly accurate. The tilt angle *does* change slightly, and this change introduces a small oscillatory component to the precession.  The nutation is a "nodding" motion of the top's axis of rotation as it precesses.  It's a consequence of the fact that the torque is not perfectly aligned with the axis of rotation, and the inertia tensor is not perfectly diagonal.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{precession\_rad\_s} &= 4.0875 \\
\mathrm{precession\_period\_s} &= 1.548 \\
\mathrm{precession\_double\_spin} &= 2.04375
\end{aligned}
\]