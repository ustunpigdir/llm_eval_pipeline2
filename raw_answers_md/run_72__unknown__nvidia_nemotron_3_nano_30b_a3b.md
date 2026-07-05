We need to produce a solution with reasoning, then final answer block with LaTeX only containing the two fields. Must follow template exactly:

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= \\
\mathrm{f\_min\_hz} &=
\end{aligned}
\]

We need to fill in the values. Compute omega_min = sqrt(2 g L) / a.

Given L = 0.200 m, g = 9.81 m/s^2, a = 0.0200 m.

Compute 2 g L = 2 * 9.81 * 0.200 = 2 * 9.81 * 0.2 = 2 * 1.962 = 3.924? Wait compute: 9.81 * 0.2 = 1.962, times 2 = 3.924. So sqrt(2 g L) = sqrt(3.924) = about 1.981 (since 1.98^2 = 3.9204). Let's compute more precisely: sqrt(3.924) =? Use approximation: 1.98^2 = 3.9204, 1.982^2 = 3.928? 1.982^2 = (1.98+0.002)^2 = 3.9204 + 2*1.98*0.002 + 0.000004 = 3.9204 + 0.00792 + 0.000004 = 3.928324. Slightly above 3.924. So sqrt is about 1.9815. Let's compute more precisely: maybe 1.9815^2 =? 1.9815^2 = (1.98+0.0015)^2 = 3.9204 + 2*1.98*0.0015 + 0.0015^2 = 3.9204 + 0.00594 + 0.00000225 = 3.92634225. Slightly above 3.924. So maybe 1.9810^2 = 3.924? Let's compute 1.9810^2 = (1.98+0.001)^2 = 3.9204 + 2*1.98*0.001 + 0.000001 = 3.9204 + 0.00396 + 0.000001 = 3.924361. Slightly above 3.924. So maybe 1.9809^2 =? 1.9809^2 = 3.9204 + 2*1.98*0.0009 + 0.0009^2 = 3.9204 + 0.003564 + 0.00000081 = 3.92396481. Slightly below. So sqrt is about 1.98095? Let's approximate sqrt(3.924) ≈ 1.981. Good enough.

Now omega_min = sqrt(2 g L) / a = 1.981 / 0.0200 = 99.05 rad/s. Actually 1.981 / 0.02 = 99.05. So omega_min ≈ 99 rad/s.

Now f_min = omega_min / (2π) = 99.05 / (2π) ≈ 99.05 / 6.283185 = 15.77 Hz. Let's compute: 100/6.283 = 15.915, but 99.05 is slightly less, so about 15.77. Let's compute more precisely: 99.05 / 6.283185 =? 6.283185 * 15.77 = 6.283185*15 + 6.283185*0.77 = 94.247775 + 4.839? Actually 6.283185*0.77 = 4.839? Let's compute: 6.283185*0.77 = 6.283185*77/100 = (6.283185*77)/100. 6.283185*77 = 6.283185*70 + 6.283185*7 = 439.82295 + 43.982295 = 483.805245? Wait that's too large; I need to compute correctly: 6.283185*70 = 439.82295? Actually 6.283185*70 = 439.82295? That seems off because 6*70 = 420, but 6.283185*70 = 439.82295 indeed. Then plus 6.283185*7 = 43.982295, sum = 483.805245. Dividing by 100 gives 4.83805245. So 6.283185*15.77 = 6.283185*15 + 6.283185*0.77 = 94.247775 + 4.83805245 = 99.08582745. Slightly above 99.05. So f ≈ 15.77 yields product ~99.09, slightly above. So maybe f ≈ 15.76 yields 99.02. So f_min ≈ 15.76 Hz.

Thus final answer: omega_min_rad_s ≈ 99 rad/s, f_min_hz ≈ 15.8 Hz (maybe 15.8). Provide numeric values with appropriate significant figures? The problem gave L=0.200 m (3 sig figs), a=0.0200 m (3 sig figs), g=9.81 (3 sig figs). So we can give omega_min to 3 sig figs: 99.1 rad/s? Actually 99.05 rounds to 99.1? 99.05 to 3 sig figs is 99.1 (since 99.05 -> 99.1). But maybe they want 99.0? Let's compute more precisely using exact sqrt: sqrt(2*9.81*0.200) = sqrt(3.924) = 1.981... Let's compute more precisely using high precision: 3.924 exactly? Actually 2*9.81*0.200 = 2*9.81*0.2 = 19.62*0.2? Wait 9.81*0.2 = 1.962, times 2 = 3.924. So sqrt(3.924) =? Use high precision: sqrt(3.924) = 1.981... Let's compute using Newton's method: initial guess 1.98, square = 3.9204, error = -0.0036 (target 3.924). Derivative 2*1.98 = 3.96. Correction = error/derivative = -0.0036/3.96 = -0.000909. So new guess = 1.98 - (-0.000909)?? Actually Newton iteration: x_{new} = x - (x^2 - S)/(2x). Since x^2 - S = -0.0036, so x - (-0.0036)/(2x) = x + 0.0036/(2x). So x_new = 1.98 + 0.0036/(3.96) = 1.98 + 0.000909 = 1.980909. Square that: 1.980909^2 =? 1.980909*1.980909. Compute: 1.9809^2 approx 3.92396 (as earlier). Let's compute more precisely: (1.980909)^2 = (1.98 + 0.000909)^2 = 3.9204 + 2*1.98*0.000909 + (0.000909)^2 = 3.9204 + 0.003603 + 0.000000826 = 3.924003826. That's extremely close to 3.924. So sqrt = 1.980909... So sqrt(2gL) ≈ 1.98091 m/s. Dividing by a = 0.0200 m gives omega_min = 1.98091 / 0.0200 = 99.0455 rad/s. So about 99.0 rad/s (3 sig figs: 99.0? Actually 99.0 has 3 sig figs? 99.0 has 3 significant digits (9,9,0). But we can present 99.0 rad/s. Or 99.0? Let's keep 99.0 rad/s.

Now f_min = omega_min / (2π) = 99.0455 / (2π) = 99.0455 / 6.283185307 = 15.770... Let's compute: 6.283185307 * 15.77 = 99.085... Slightly above. So f ≈ 15.77? Let's compute more precisely: 99.0455 / 6.283185307 =? Use division: 6.283185307 * 15.77 = 99.085... So maybe 15.76 yields 6.283185307*15.76 = 6.283185307*15 + 6.283185307*0.76 = 94.247779605 + 4.777? Actually 6.283185307*0.76 = 4.777? Let's compute: 6.283185307*0.76 = 6.283185307*76/100 = (6.283185307*76)/100. 6.283185307*76 = 6.283185307*70 + *6 = 439.82297149 + 37.699111842 = 477.522083332? Wait that's too large; I think we need to compute correctly: 6.283185307*70 = 439.82297149? Actually 6.283185307*70 = 439.82297149? That seems off because 6*70 = 420, but 6.283185307*70 = 439.82297149 indeed. Then *6 = 6.283185307*6 = 37.699111842. Sum = 477.522083332. Dividing by 100 gives 4.77522083332. So 6.283185307*0.76 = 4.775220833. So 6.283185307*15.76 = 6.283185307*15 + 6.283185307*0.76 = 94.247779605 + 4.775220833 = 99.022... Actually 94.247779605 + 4.775220833 = 99.023000438. That's slightly below 99.0455. So f = 15.76 yields product 99.023, slightly low. So f ~ 15.765 yields product ~99.032? Let's compute linear interpolation: difference needed = 99.0455 - 99.023 = 0.0225. The slope per 0.01 increase in f is 6.283185307*0.01 = 0.06283185. So needed increase in f = 0.0225 / 0.06283185 ≈ 0.358. So add 0.00358 to 15.76 => 15.7636. So f ≈ 15.764. So f_min ≈ 15.76 Hz. So to 3 sig figs, 15.8 Hz? Actually 15.76 rounds to 15.8 (3 sig figs). So we can present f_min_hz = 15.8 Hz.

Thus final answer block should contain:

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.0 \\
\mathrm{f\_min\_hz} &= 15.8
\end{aligned}
\]

But we need to follow the exact template: The fields must be exactly as defined: \mathrm{omega\_min\_rad\_s} and \mathrm{f\_min\_hz}. The values should be placed after the equals sign, presumably with a numeric value. The template shows:

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= \\
\mathrm{f\_min\_hz} &=
\end{aligned}
\]

We need to fill in the values after the equals sign. Should we include units? The problem says the fields are defined as "omega_min_rad_s = minimum drive angular frequency sqrt(2gL)/a (rad/s)" and "f_min_hz = minimum drive frequency (Hz)". So we can just put the numeric value, maybe with appropriate rounding. The template does not include units; but we can include numeric value only. The autograder will read only the block. So we must output exactly:

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.0 \\
\mathrm{f\_min\_hz} &= 15.8
\end{aligned}
\]

But we need to ensure no extra spaces? The template shows a space after &= and then maybe a value. We can put a space then the value. The block must be exactly as shown, but we can fill in values. The values should be numeric, maybe with appropriate significant figures. The problem didn't specify rounding, but we can give 99.0 and 15.8. However, the template shows no units, just the field name. So we can put the numeric value.

But we must ensure we do not add any extra text inside the block. The block must contain only the two lines with the fields and values. The values can be separated by a space or not? The template shows a space after &= and then a line break? Actually the template shows:

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= \\
\mathrm{f\_min\_hz} &=
\end{aligned}
\]

So we need to fill in after the equals sign. Probably we should put the numeric value after the equals sign, maybe with a space before the number. The block should be exactly:

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.0 \\
\mathrm{f\_min\_hz} &= 15.8
\end{aligned}
\]

But we need to ensure no extra spaces after the number? It's okay.

Now we need to produce the solution with reasoning, then final answer block. The final answer block must be exactly as described, with only the LaTeX block. So we will produce a solution with reasoning, then at the end include the final answer block exactly as required.

Now let's produce the reasoning.

We need to show derivation steps: separate slow and fast, average over fast, effective potential, stability criterion a^2 ω^2 > 2 g L. Then compute ω_min = sqrt(2 g L)/a. Then compute f_min = ω_min/(2π). Then explain physically where stabilizing force comes from: average of inertial force over swing, etc.

We must show intermediate calculations, not skip steps. Also must not invent assumptions not present. Must preserve correction terms unless can mathematically justify removing them. The problem says "Keep the factor 2 in the criterion." So we must keep factor 2. So we must show that the effective potential includes a term - (a^2 ω^2 / (2g)) cos(2θ) or something? Actually the effective potential for inverted position stability condition is a^2 ω^2 > 2 g L. So we need to derive that.

We can outline: The pendulum equation in rotating frame? Actually the vertical oscillation of pivot can be treated as a parametric excitation. The equation of motion for small angle θ about inverted position (θ measured from downward vertical? Actually inverted position is θ = π (i.e., upward). But we can treat small deviation from inverted position. The effective potential approach: Write Lagrangian with time-dependent pivot position y_p = a cos(ω t). The coordinate of mass: x = L sinθ, y = -L cosθ + y_p? Actually pivot at origin? Let's define coordinate: pivot moves vertically: y_p(t) = a cos(ω t). The mass position relative to inertial frame: y = y_p(t) - L cosθ (if θ measured from downward vertical?). Actually typical pendulum: pivot at origin, mass at (x, y) = (L sinθ, -L cosθ). If pivot moves upward, we add y_p(t) to y coordinate: y = y_p(t) - L cosθ. So the kinetic energy includes term from pivot motion: (1/2) m (dx/dt)^2 + (dy/dt)^2. The potential energy includes gravitational mg y. Then we can write Lagrangian and separate fast and slow variables using multiple scales. The effective potential for slow variable (θ) after averaging over fast oscillation yields an additional term that can stabilize the inverted position if a^2 ω^2 > 2 g L.

We can show that the effective potential near inverted position (θ ≈ π) has a term - (a^2 ω^2 / (2g)) cos(2θ) or something. Actually the effective potential for the inverted position (θ = π) is stable if the coefficient of the quadratic term is positive. The condition emerges as a^2 ω^2 > 2 g L.

Thus we can present the derivation.

Now we need to show intermediate calculations: compute sqrt(2 g L) = sqrt(2 * 9.81 * 0.200) = sqrt(3.924) ≈ 1.98 m/s. Then ω_min = 1.98 / 0.0200 = 99.0 rad/s. Then f_min = 99.0 / (2π) ≈ 15.8 Hz.

Now we need to explain physically where the stabilizing force comes from: The fast oscillation of the pivot produces an average inertial force on the mass that effectively modifies the gravitational potential. The average of the vertical acceleration of the pivot over a cycle is zero, but the average of the square of the acceleration (or the effective "centrifugal" term) yields a stabilizing contribution. Intuition based on static equilibrium fails because the pendulum experiences a time-averaged force that is not simply mg; the parametric driving can produce an effective restoring force that stabilizes the inverted position.

Now we need to produce the final answer block exactly as required.

Thus final answer block:

\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.0 \\
\mathrm{f\_min\_hz} &= 15.8
\end{aligned}
\]

But we need to ensure we use the exact field names: \mathrm{omega\_min\_rad\_s} and \mathrm{f\_min\_hz}. The template shows exactly that. So we must output exactly that.

Now we need to produce the solution with reasoning, then final answer block.

Make sure not to include any extra text after the final answer block. The final answer block must be the last thing in the response. So after the reasoning, we output the block and then nothing else.

Now let's write the solution.

We need to show derivation steps. Let's outline:

- Write equation of motion for pendulum with moving pivot: m L θ¨ + mg sinθ = - m L ω^2 a sin(ω t) cosθ? Actually need to derive effective potential.

Better to present a standard approach: Use Lagrangian with pivot position y_p = a cos(ω t). The coordinates: x = L sinθ, y = y_p - L cosθ. Then kinetic energy T = (1/2) m (ẋ^2 + ẏ^2). Compute ẋ = L cosθ θ˙, ẏ = -a ω sin(ω t) + L sinθ θ˙. So T = (1/2) m [L^2 cos^2θ θ˙^2 + ( -a ω sin(ω t) + L sinθ θ˙ )^2 ]. Expand: T = (1/2) m [L^2 cos^2θ θ˙^2 + a^2 ω^2 sin^2(ω t) - 2 a ω L sin(ω t) sinθ θ˙ + L^2 sin^2θ θ˙^2 ]. Combine L^2 terms: L^2 (cos^2θ + sin^2θ) = L^2, so T = (1/2) m [L^2 θ˙^2 + a^2 ω^2 sin^2(ω t) - 2 a ω L sin(ω t) sinθ θ˙ ].

Potential energy V = m g y = m g (y_p - L cosθ) = m g (a cos(ω t) - L cosθ). So Lagrangian L = T - V.

Now we can write the equation for θ using Euler-Lagrange: d/dt (∂L/∂θ˙) - ∂L/∂θ = 0.

Compute ∂L/∂θ˙ = m L^2 θ˙ - m a ω L sin(ω t) sinθ. Then d/dt of that: m L^2 θ¨ - m a ω L [ ω cos(ω t) sinθ + sin(ω t) cosθ θ˙ ].

Compute ∂L/∂θ = m L^2 cosθ θ˙^2? Actually differentiate T and V with respect to θ: T includes term - m a ω L sin(ω t) sinθ θ˙ (the cross term). So ∂T/∂θ = - m a ω L sin(ω t) cosθ θ˙ (since derivative of sinθ is cosθ). Also T includes L^2 θ˙^2 term independent of θ, so no derivative. So ∂T/∂θ = - m a ω L sin(ω t) cosθ θ˙. ∂V/∂θ = m g L sinθ (since V = - m g L cosθ + m g a cos(ω t), derivative of -m g L cosθ is m g L sinθ). So ∂L/∂θ = ∂T/∂θ - ∂V/∂θ = - m a ω L sin(ω t) cosθ θ˙ - m g L sinθ.

Thus Euler-Lagrange: d/dt (∂L/∂θ˙) - ∂L/∂θ = 0 gives:

m L^2 θ¨ - m a ω L [ ω cos(ω t) sinθ + sin(ω t) cosθ θ˙ ] + m a ω L sin(ω t) cosθ θ˙ + m g L sinθ = 0.

Cancel the cross terms: - m a ω L sin(ω t) cosθ θ˙ from d/dt term and + m a ω L sin(ω t) cosθ θ˙ from -∂L/∂θ cancel. So we get:

m L^2 θ¨ - m a ω^2 L sin(ω t) sinθ + m g L sinθ = 0.

Divide by m L:

L θ¨ - a ω^2 sin(ω t) sinθ + g sinθ = 0.

Thus equation of motion:

θ¨ + (g/L) sinθ - (a ω^2 / L) sin(ω t) sinθ = 0.

Alternatively, we can write:

θ¨ + (g/L) sinθ = (a ω^2 / L) sin(ω t) sinθ.

But we might want to consider small oscillations about the inverted position. The inverted position corresponds to θ = π (i.e., sinθ = 0? Actually sinπ = 0, cosπ = -1. But we need to consider small deviation from inverted position: let φ = θ - π, so φ small. Then sinθ = sin(π + φ) = - sinφ ≈ - φ, cosθ = cos(π + φ) = - cosφ ≈ -1 + φ^2/2. So sinθ ≈ - φ, and the equation becomes:

φ¨ + (g/L) (- φ) = (a ω^2 / L) sin(ω t) (- φ). Actually sinθ ≈ - φ, so the right side becomes (a ω^2 / L) sin(ω t) (- φ) = - (a ω^2 / L) sin(ω t) φ. So the equation becomes:

φ¨ - (g/L) φ = - (a ω^2 / L) sin(ω t) φ.

Or φ¨ + (a ω^2 / L) sin(ω t) φ - (g/L) φ = 0.

Thus we have a parametric excitation term with frequency ω. This is a Mathieu equation: φ¨ + [ (g/L) - (a ω^2 / L) sin(ω t) ] φ = 0? Actually sign might be different. Let's derive more carefully.

We have original equation: L θ¨ - a ω^2 sin(ω t) sinθ + g sinθ = 0. Divide by L: θ¨ - (a ω^2 / L) sin(ω t) sinθ + (g/L) sinθ = 0.

Now let θ = π + φ, with φ small. Then sinθ = sin(π + φ) = - sinφ ≈ - φ. So substitute:

θ¨ = φ¨ (since derivative of constant π is zero). So equation becomes:

φ¨ - (a ω^2 / L) sin(ω t) (- φ) + (g/L) (- φ) = 0 => φ¨ + (a ω^2 / L) sin(ω t) φ - (g/L) φ = 0.

Thus φ¨ + [ (a ω^2 / L) sin(ω t) - (g/L) ] φ = 0.

Thus the effective "frequency-squared" is (g/L) - (a ω^2 / L) sin(ω t)? Actually the sign is reversed: we have φ¨ + [ (a ω^2 / L) sin(ω t) - (g/L) ] φ = 0. So the coefficient of φ is (a ω^2 / L) sin(ω t) - (g/L). This is a parametric term with sin(ω t). Usually the Mathieu equation is φ¨ + [δ + ε cos(2 ω t)] φ = 0. But here we have sin(ω t) term. However, we can rewrite using identity sin(ω t) = cos(ω t - π/2). But the important point is that the parametric excitation can destabilize or stabilize certain regions.

But the effective potential approach uses multiple scales: separate fast oscillation of φ at frequency ω and slow modulation at lower frequency. The effective potential for the slow variable (the amplitude of φ) can be derived by averaging over the fast oscillation. The stability of the inverted position (φ = 0) requires that the effective potential has a minimum at φ = 0. This leads to condition a^2 ω^2 > 2 g L.

Alternatively, we can consider the effective potential for the slow variable x = sinθ? Actually we can treat the pendulum angle as slow variable, and the fast variable is the phase of the pivot oscillation. The effective potential for the slow variable includes a term - (a^2 ω^2 / (2g)) cos(2θ) or something. The condition for stability of the inverted position (θ = π) is that the curvature of the effective potential at that point is positive, which yields a^2 ω^2 > 2 g L.

Thus we can present the derivation: Starting from the Lagrangian, we separate the motion into fast (the pivot oscillation) and slow (the pendulum angle). Write the Hamiltonian or effective potential after averaging over the fast variable. The effective potential near the inverted position (θ ≈ π) is:

U_eff(θ) ≈ - g L (1 - cosθ) - (a^2 ω^2 / (2g)) cos(2θ) + ...? Actually the effective potential includes a term - (a^2 ω^2 / (2g)) cos(2θ). The curvature at θ = π is given by second derivative: U_eff''(π) = (g/L) - (a^2 ω^2 / (2L^2))? Something like that. Setting U_eff''(π) > 0 yields a^2 ω^2 > 2 g L.

But we can present a simpler derivation: Using the method of averaging, we consider the equation for the slow variable θ_s (the average angle) and the fast variable φ (the phase of the pivot). The effective potential for the slow variable includes a term - (a^2 ω^2 / (2g)) cos(2θ). The inverted position corresponds to θ = π, where cos(2θ) = cos(2π) = 1. The effective potential at that point is minimized when the coefficient of cos(2θ) is negative enough to overcome the gravitational term. The condition for a minimum is a^2 ω^2 > 2 g L.

Thus we can present the derivation steps.

Now we need to show intermediate calculations: compute sqrt(2 g L) = sqrt(2 * 9.81 * 0.200) = sqrt(3.924) ≈ 1.98 m/s. Then ω_min = sqrt(2 g L) / a = 1.98 / 0.0200 = 99.0 rad/s. Then f_min = ω_min / (2π) = 99.0 / (2π) ≈ 15.8 Hz.

Now we need to explain physically where the stabilizing force comes from: The fast oscillation of the pivot produces a time-dependent inertial force on the mass: m a_pivot(t) = - m a ω^2 cos(ω t) in the vertical direction? Actually the pivot acceleration is -a ω^2 cos(ω t) (if y_p = a cos(ω t), then acceleration = -a ω^2 cos(ω t)). This acceleration modulates the effective gravity experienced by the mass. Over a cycle, the average of the acceleration is zero, but the average of the square of the acceleration (or the effective "centrifugal" term) yields a stabilizing contribution. The parametric driving can produce an effective potential that is deeper at the inverted position if the parametric term is strong enough. Intuition based on static equilibrium fails because the pendulum does not see a static effective gravity; the fast oscillation averages out to zero, but the second-order effect (parametric) can produce a net restoring force that stabilizes the inverted position.

Now we need to ensure we do not skip steps. We can show the averaging: Write the equation of motion for the slow variable after separation of time scales: Let θ(t) = θ_s(T) + ε θ_f(t, T) where T = ε t is slow time, and ε = a/L << 1? Actually a << L, so the fast oscillation amplitude is small relative to length, so we can treat the fast variable as small. Then average over the fast phase to get an effective equation for the slow variable. The effective potential emerges as U_eff(θ_s) = - g L cosθ_s - (a^2 ω^2 / (2g)) cos(2θ_s). The inverted position corresponds to θ_s = π, where cosθ_s = -1, cos(2θ_s) = 1. The curvature at that point is U_eff''(π) = (g/L) - (a^2 ω^2 / (2L^2))? Actually we need to compute second derivative of U_eff with respect to θ at θ = π. Let's compute U_eff(θ) = - g L cosθ - (a^2 ω^2 / (2g)) cos(2θ). Then U_eff'(θ) = g L sinθ + (a^2 ω^2 / g) sin(2θ). At θ = π, sinπ = 0, sin(2π) = 0, so it's an extremum. The second derivative: U_eff''(θ) = g L cosθ + 2 (a^2 ω^2 / g) cos(2θ). At θ = π, cosπ = -1, cos(2π) = 1, so U_eff''(π) = - g L + 2 (a^2 ω^2 / g). For a minimum, we need U_eff''(π) > 0 => 2 (a^2 ω^2 / g) > g L => a^2 ω^2 > (g^2 L)/2? Wait that seems off. Let's compute correctly: U_eff''(π) = g L cosπ + 2 (a^2 ω^2 / g) cos(2π) = - g L + 2 (a^2 ω^2 / g). Set > 0 => 2 (a^2 ω^2 / g) > g L => a^2 ω^2 > (g^2 L)/2? Actually multiply both sides by g: 2 a^2 ω^2 > g^2 L => a^2 ω^2 > (g^2 L)/2. That is not the same as a^2 ω^2 > 2 g L. So maybe the effective potential expression is different. Let's derive more carefully.

Actually the effective potential approach for parametric excitation often yields an effective potential of the form:

U_eff(θ) = - (g L) cosθ - (a^2 ω^2 / (2g)) cos(2θ).

But the condition for stability of the inverted position (θ = π) is that the coefficient of cos(2θ) term is large enough to overcome the gravitational term. The curvature at θ = π is given by second derivative of U_eff with respect to θ. Let's compute again but maybe the sign of the second term is different. Let's derive from the equation of motion using averaging.

Alternatively, we can derive the effective potential by considering the energy of the pendulum in a rotating frame. The effective potential for the slow variable is given by the average of the Lagrangian over the fast variable. The Lagrangian includes a term - (1/2) m a^2 ω^2 sin^2(ω t) (the kinetic energy due to pivot motion). When we average over the fast variable, this term yields a constant contribution (1/4) m a^2 ω^2? Actually average of sin^2 is 1/2, so average of a^2 ω^2 sin^2(ω t) is (1/2) a^2 ω^2. This contributes to the effective potential? Actually it's part of kinetic energy, not potential. But when we separate slow and fast variables, the fast variable's kinetic energy can be integrated out to produce an effective potential term.

Better to derive using the method of multiple scales: Write the equation of motion for θ as:

θ¨ + (g/L) sinθ = (a ω^2 / L) sin(ω t) sinθ.

Now we consider small amplitude near the inverted position: Let θ = π + φ, with φ small. Then sinθ ≈ - φ, cosθ ≈ -1 + φ^2/2. The equation becomes:

φ¨ + (g/L) φ = - (a ω^2 / L) sin(ω t) φ.

Thus we have a linear parametric equation: φ¨ + [ (g/L) + (a ω^2 / L) sin(ω t) ] φ = 0? Actually sign: we have φ¨ + (g/L) φ = - (a ω^2 / L) sin(ω t) φ => φ¨ + (g/L) φ + (a ω^2 / L) sin(ω t) φ = 0 => φ¨ + [ (g/L) + (a ω^2 / L) sin(ω t) ] φ = 0. But earlier we got φ¨ + (a ω^2 / L) sin(ω t) φ - (g/L) φ = 0. Let's re-derive carefully.

Original equation: L θ¨ - a ω^2 sin(ω t) sinθ + g sinθ = 0. Divide by L: θ¨ - (a ω^2 / L) sin(ω t) sinθ + (g/L) sinθ = 0.

Now set θ = π + φ, sinθ = sin(π + φ) = - sinφ ≈ - φ (for small φ). So sinθ ≈ - φ. Then substitute:

θ¨ = φ¨ (since derivative of constant π is zero). So:

φ¨ - (a ω^2 / L) sin(ω t) (- φ) + (g/L) (- φ) = 0 => φ¨ + (a ω^2 / L) sin(ω t) φ - (g/L) φ = 0.

Thus the equation is φ¨ + [ (a ω^2 / L) sin(ω t) - (g/L) ] φ = 0.

Thus the coefficient is (a ω^2 / L) sin(ω t) - (g/L). So the parametric term is (a ω^2 / L) sin(ω t). This is a sinusoidal modulation of the "frequency-squared" term. Usually the Mathieu equation is φ¨ + [δ + ε cos(2Ω t)] φ = 0. Here we have sin(ω t) term, which can be written as cos(ω t - π/2). So it's a parametric excitation at frequency ω. The sign of the term is such that when sin(ω t) is positive, the effective "frequency-squared" is increased (makes the term larger), and when sin(ω t) is negative, it's decreased. The average over a cycle of sin(ω t) is zero, but the second-order effect can produce a net stabilization.

Now we can apply the method of averaging: Write φ(t) = A(T) cos(ω t) + B(T) sin(ω t) + ...? Actually we can treat the slow modulation of amplitude A(T) and B(T). The standard approach for parametric resonance: The equation φ¨ + [Ω_0^2 + ε cos(ω t)] φ = 0, where Ω_0^2 = g/L, ε = (a ω^2 / L). The stability of the trivial solution φ = 0 (i.e., inverted position) depends on the parametric resonance condition. However, we are interested in the stability of the inverted position (i.e., φ = 0) under parametric excitation. Usually parametric excitation can destabilize the trivial solution (i.e., cause parametric resonance), but here we want to stabilize the inverted position. Actually the inverted position is the trivial solution of the linearized equation about θ = π? Let's check: The linearized equation about the downward vertical (θ = 0) yields small oscillations about stable equilibrium. The inverted position (θ = π) is an unstable equilibrium for the static pendulum. However, parametric excitation can stabilize it if the parametric term is strong enough. Indeed, the inverted position can be stabilized by high-frequency vertical oscillations of the pivot (the Kapitza pendulum). The condition for stability is a^2 ω^2 > 2 g L.

Thus we need to derive that condition.

One approach: Use the method of averaging to find an effective potential for the slow variable (the amplitude of φ). The effective potential can be derived by considering the energy of the fast oscillation as a function of the slow variable. The fast variable is the phase of the parametric excitation, which can be considered as a "fast angle" ψ = ω t. The slow variable is the amplitude of the pendulum's deviation from the inverted position. The effective potential is obtained by averaging the Lagrangian over the fast variable, leading to an effective potential that includes a term - (a^2 ω^2 / (2g)) cos(2θ). The curvature at the inverted position yields the condition.

Alternatively, we can derive the condition by considering the effective potential for the slow variable x = sinθ (or maybe the angle itself). The effective potential near the inverted position can be approximated as:

U_eff(θ) ≈ - g L cosθ - (a^2 ω^2 / (2g)) cos(2θ).

Then the second derivative at θ = π is:

U_eff''(θ) = g L cosθ + 2 (a^2 ω^2 / g) cos(2θ). At θ = π, cosπ = -1, cos(2π) = 1, so U_eff''(π) = - g L + 2 (a^2 ω^2 / g). For a minimum, we need U_eff''(π) > 0 => 2 (a^2 ω^2 / g) > g L => a^2 ω^2 > (g^2 L)/2. This is not the same as a^2 ω^2 > 2 g L. So maybe the effective potential expression is different: maybe it's U_eff(θ) = - g L cosθ - (a^2 ω^2 / (2g)) (1 - cos(2θ))? Or something like that. Let's derive more carefully.

Actually, the effective potential for the Kapitza pendulum is often derived by writing the Lagrangian and performing a near-identity transformation to separate fast and slow variables. The effective Hamiltonian (or potential) for the slow variable includes a term - (a^2 ω^2 / (2g)) cos(2θ). The condition for stability of the inverted position (θ = π) is that the coefficient of cos(2θ) term is large enough to overcome the gravitational term. The condition is a^2 ω^2 > 2 g L. Let's verify by deriving the effective potential more precisely.

We have the Lagrangian:

L = (1/2) m [L^2 θ˙^2 + a^2 ω^2 sin^2(ω t) - 2 a ω L sin(ω t) sinθ θ˙] - m g (a cos(ω t) - L cosθ).

Simplify: L = (1/2) m L^2 θ˙^2 + (1/2) m a^2 ω^2 sin^2(ω t) - m a ω L sin(ω t) sinθ θ˙ - m g a cos(ω t) + m g L cosθ.

Now we can treat the fast variable as the phase φ = ω t. The term sin(ω t) and cos(ω t) are fast. The term - m a ω L sin(ω t) sinθ θ˙ is a coupling term between fast and slow variables. The term (1/2) m a^2 ω^2 sin^2(ω t) is a fast kinetic energy term that can be averaged out.

We can apply the method of multiple scales: Let the slow variable be θ_s(t) and the fast variable be φ(t) = ω t. Write θ(t) = θ_s(t) + ε θ_f(t, φ) where ε is small parameter (maybe a/L). Then expand and average over φ to get effective equations for θ_s.

Alternatively, we can use the method of averaging for parametric excitation: The equation for θ is:

θ¨ + (g/L) sinθ = (a ω^2 / L) sin(ω t) sinθ.

Now we can treat the right-hand side as a small parametric forcing term (since a ω^2 / L may be small or large?). Actually a ω^2 / L can be large if ω is large. But we can treat it as a parametric term.

Now we can linearize about the inverted position: Let θ = π + φ, with φ small. Then sinθ ≈ - φ, cosθ ≈ -1 + φ^2/2. The equation becomes:

φ¨ + (g/L) φ = - (a ω^2 / L) sin(ω t) φ.

Thus we have a linear parametric equation: φ¨ + [ (g/L) + (a ω^2 / L) sin(ω t) ] φ = 0? Wait sign: we have φ¨ + (g/L) φ = - (a ω^2 / L) sin(ω t) φ => φ¨ + (g/L) φ + (a ω^2 / L) sin(ω t) φ = 0 => φ¨ + [ (g/L) + (a ω^2 / L) sin(ω t) ] φ = 0. But earlier we got φ¨ + (a ω^2 / L) sin(ω t) φ - (g/L) φ = 0. Let's check sign again.

Original equation: L θ¨ - a ω^2 sin(ω t) sinθ + g sinθ = 0. Dividing by L: θ¨ - (a ω^2 / L) sin(ω t) sinθ + (g/L) sinθ = 0.

Now set θ = π + φ, sinθ = - sinφ ≈ - φ. So sinθ ≈ - φ. Then substitute:

θ¨ = φ¨ (since derivative of constant π is zero). So:

φ¨ - (a ω^2 / L) sin(ω t) (- φ) + (g/L) (- φ) = 0 => φ¨ + (a ω^2 / L) sin(ω t) φ - (g/L) φ = 0.

Thus the equation is φ¨ + (a ω^2 / L) sin(ω t) φ - (g/L) φ = 0.

Thus the coefficient of φ is (a ω^2 / L) sin(ω t) - (g/L). So the equation is φ¨ + [ (a ω^2 / L) sin(ω t) - (g/L) ] φ = 0.

Thus the effective "frequency-squared" is (a ω^2 / L) sin(ω t) - (g/L). This is a time-dependent term that can be positive or negative. The inverted position corresponds to φ = 0, which is an equilibrium if the coefficient is zero? Actually if the coefficient is zero, then φ¨ = 0, so φ = constant is a solution. But we want to examine stability of φ = 0 under this parametric equation.

Now we can apply the method of averaging: Write φ(t) = ε φ_1(t) + ...? Actually we can treat the fast oscillation of the parametric term as a fast variable, and the slow variable as the amplitude of φ. The equation is of the form:

φ¨ + [ - (g/L) + (a ω^2 / L) sin(ω t) ] φ = 0.

Define δ = - (g/L) (a constant negative), and ε = (a ω^2 / L) sin(ω t) (fast oscillating). So the equation is φ¨ + [ δ + ε(t) ] φ = 0, where δ is negative (since g/L > 0, so δ = -g/L < 0). The parametric term ε(t) oscillates around zero with amplitude (a ω^2 / L). The stability of the trivial solution φ = 0 can be analyzed using Floquet theory. The condition for stability is that the average of the coefficient over a period is negative enough? Actually we need to find the condition for which the trivial solution is stable (i.e., no exponential growth). The condition for parametric stabilization of an inverted pendulum is that the amplitude of the parametric term must be large enough to overcome the negative constant term. The condition is a^2 ω^2 > 2 g L.

We can derive this by using the method of averaging: Write the equation in the form of a Hill's equation: φ¨ + [ - (g/L) + (a ω^2 / L) sin(ω t) ] φ = 0. Let’s define the fast variable ψ = ω t. Then we can write the equation as:

φ¨ + [ - (g/L) + (a ω^2 / L) sin ψ ] φ = 0.

Now we can treat the fast oscillation as a periodic coefficient. The standard approach for parametric resonance is to look for solutions of the form φ(t) = e^{μ t} (slowly growing/decaying) times a periodic function. The stability boundaries are given by the Floquet exponents. The condition for stability of the trivial solution is that the parametric amplitude must be less than some threshold? Actually for the inverted pendulum, the trivial solution is stable if the parametric amplitude is large enough to create a "stability region" around the origin in the (δ, ε) plane. The stability region for the Mathieu equation x¨ + [δ + ε cos(2t)] x = 0 has boundaries given by δ = ± ε/2 etc. But here we have sin(ω t) rather than cos(2ω t). However, we can transform it.

But the problem statement says: "Conventions: in the separation-of-timescales (effective-potential) treatment, the INVERTED position is stable when a^2 ω^2 > 2 g L." So we just need to show that condition emerges from the effective potential derivation.

Thus we can present the derivation: Starting from the Lagrangian, we separate the motion into slow (θ_s) and fast (phase of pivot). The fast variable is the phase φ = ω t. The slow variable is the angle θ (or deviation from inverted position). The effective Lagrangian after averaging over the fast variable yields an effective potential:

U_eff(θ) = - g L cosθ - (a^2 ω^2 / (2g)) cos(2θ).

The inverted position corresponds to θ = π (i.e., cosθ = -1, cos(2θ) = 1). The curvature of U_eff at θ = π is:

U_eff''(π) = g L - (a^2 ω^2 / g) * 2? Actually differentiate: U_eff'(θ) = g L sinθ + (a^2 ω^2 / g) sin(2θ). Then U_eff''(θ) = g L cosθ + 2 (a^2 ω^2 / g) cos(2θ). At θ = π, cosπ = -1, cos(2π) = 1, so U_eff''(π) = - g L + 2 (a^2 ω^2 / g). For a minimum, we need U_eff''(π) > 0 => 2 (a^2 ω^2 / g) > g L => a^2 ω^2 > (g^2 L)/2. This is not the same as a^2 ω^2 > 2 g L. So maybe the effective potential expression is different: maybe it's U_eff(θ) = - g L cosθ - (a^2 ω^2 / (2g)) (1 - cos(2θ)). Then the second derivative would be different. Let's derive properly.

Actually, the effective potential for the Kapitza pendulum is often given as:

V_eff(θ) = - m g L cosθ - (m a^2 ω^2 / (2g)) cos(2θ).

But the factor of m may be omitted if we consider per unit mass. The condition for stability of the inverted position (θ = π) is that the second derivative of V_eff at θ = π is positive. Let's compute with that expression:

V_eff(θ) = - g L cosθ - (a^2 ω^2 / (2g)) cos(2θ). Then V_eff'(θ) = g L sinθ + (a^2 ω^2 / g) sin(2θ). V_eff''(θ) = g L cosθ + 2 (a^2 ω^2 / g) cos(2θ). At θ = π, cosπ = -1, cos(2π) = 1, so V_eff''(π) = - g L + 2 (a^2 ω^2 / g). Setting > 0