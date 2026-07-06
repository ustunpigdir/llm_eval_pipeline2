# Worked gold solutions — Batch 7 (scenarios 29–32 of 32): Classical Mechanics

CM_KAPITZA, CM_FOUCAULT, CM_APSIDAL, CM_TOP. Final batch. Same structure. Verified against generator
constants. Status: **LOCKED 2026-07-04** (human-locked).

> **Reviewer flag:** CM_APSIDAL `precession_per_period_deg = −105.441559` is genuinely **negative**
> (the orbit regresses). The sign is physical — do not grade it as a magnitude.

---

## CM_KAPITZA_001 — Kapitza pendulum: stabilizing the inverted state

**Given:** L = 0.200 m, pivot oscillates vertically with amplitude a = 0.0200 m at ω (a ≪ L, ω ≫ √(g/L)), g = 9.81 m/s². Inverted position stable when a²ω² > 2gL.

**Derivation**
1. **Effective potential.** Split the angle into a slow part θ̄ plus a fast driven part; averaging over one drive period gives U_eff(θ̄) = −mgL cos θ̄ + (m a²ω²/4) sin²θ̄. The inverted point θ̄ = π is a **minimum** of U_eff (hence stable) iff the curvature there is positive ⟹ **a²ω² > 2gL**.
2. **Minimum frequency.** ω_min = √(2gL)/a = √(2·9.81·0.2)/0.02 = √3.924/0.02 = 1.9809/0.02 = **99.045 rad/s**.
3. **In Hz.** f_min = ω_min/2π = 99.045/6.2832 = **15.764 Hz**.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{omega\_min\_rad\_s} &= 99.045444 \\
\mathrm{f\_min\_hz}         &= 15.763572
\end{aligned}
\]
```

**Reasoning checkpoints:** U_eff = −mgL cos θ + (m a²ω²/4) sin²θ (averaged fast motion); inverted stable iff a²ω² > 2gL; ω_min = √(2gL)/a ≈ 99 rad/s, f ≈ 15.8 Hz; stabilization from the averaged inertial force (quadratic in the drive); keeps the factor 2 (criterion is not a²ω² > gL).

**Wrong-answer fingerprints:** drops the factor 2 (uses a²ω² > gL) → `N_FACTOR2_DROPPED`; applies static intuition (inverted must be unstable) → `C_STATIC_INTUITION_APPLIED`.

---

## CM_FOUCAULT_001 — Foucault pendulum: precession at Paris

**Given:** latitude λ = 48.85° N; Earth's rotation 360° per 24 h. Precession rate = Ω_E sin λ, clockwise viewed from above (N hemisphere).

**Derivation**
1. **The sin λ factor.** The Coriolis coupling that rotates the swing plane is the **vertical** component of Earth's angular velocity, Ω_E sin λ. (The horizontal component Ω_E cos λ tilts the local vertical; it does not precess the plane.)
2. **Rate.** Ω_E = 360°/24 h = 15°/h. sin(48.85°) = 0.75299. Rate = 15·0.75299 = **11.29°/h**; ×24 = **271.08°/day**.
3. **Period.** Full turn = 360°/(11.29°/h) = **31.87 h**.
4. **Limits.** Equator (λ = 0): sin λ = 0 → no precession. Pole (λ = 90°): 15°/h → 24 h period. A student using cos λ takes the horizontal component — wrong; it tilts, it does not precess the plane.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{rate\_deg\_per\_day}  &= 271.076197 \\
\mathrm{rate\_deg\_per\_hour} &= 11.294842 \\
\mathrm{period\_hours}       &= 31.872957
\end{aligned}
\]
```

**Reasoning checkpoints:** precession = Ω_E sin λ (vertical component); Paris ≈ 271°/day ≈ 11.3°/h, period ≈ 31.9 h; equator none, pole 24 h; cos λ is the horizontal component (tilts, does not precess); clockwise from above in the N hemisphere.

**Wrong-answer fingerprints:** uses cos λ → `N_SIN_COS_CONFUSED`; misidentifies the rotation component → `C_COMPONENT_MISIDENTIFIED`.

---

## CM_APSIDAL_001 — Apsidal angle: why only two potentials close orbits

**Given:** central force F(r) = −k r^n (attractive), near-circular orbits, apsidal angle Φ = π/√(3+n). n is the **force** exponent (Kepler n = −2, harmonic n = +1).

**Derivation**
1. **Closed cases.** Kepler n = −2: Φ = π/√(3−2) = π/√1 = **180°**. Harmonic n = +1: Φ = π/√(3+1) = π/2 = **90°**. Both are rational fractions of π ⟹ orbits close.
2. **n = −1.** Φ = π/√(3−1) = π/√2 = **127.28°**.
3. **Not closed.** For n = −1, Φ is not a rational multiple of 180° that closes; the precession per radial period is 2Φ − 360° = 2·127.28 − 360 = **−105.44°** (the orbit regresses).
4. **Bertrand's theorem.** Only n = −2 (inverse-square) and n = +1 (Hooke) close **all** bounded orbits. For n ≤ −3 the argument 3+n ≤ 0, √ is non-real ⟹ circular orbits are unstable and no apsidal angle exists.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg}       &= 180.0 \\
\mathrm{apsidal\_harmonic\_deg}     &= 90.0 \\
\mathrm{apsidal\_n\_minus1\_deg}    &= 127.279221 \\
\mathrm{precession\_per\_period\_deg} &= -105.441559
\end{aligned}
\]
```

**Reasoning checkpoints:** Φ = π/√(3+n) with the FORCE exponent n; Kepler 180°, harmonic 90° (closed); n = −1 → 127.3°, not closed; precession 2Φ − 360 ≈ −105.4°; Bertrand (only n = −2, +1); n ≤ −3 unstable.

**Wrong-answer fingerprints:** conflates force vs potential exponent → `N_FORCE_POTENTIAL_EXPONENT_CONFLATED`; claims the n = −1 orbit closes → `C_CLOSURE_CLAIMED`; precession sign error → `N_PRECESSION_SIGN_ERROR`.

---

## CM_TOP_001 — Fast top: gyroscopic precession rate

**Given:** m = 0.500 kg, l = 0.0500 m (pivot to CoM), I₃ = 2.00×10⁻⁴ kg·m², ω₃ = 300 rad/s, g = 9.81 m/s². Fast-top limit Ω = mgl/(I₃ω₃), tilt-independent.

**Derivation**
1. **Derivation of Ω.** Gravity exerts torque τ = mgl sin θ, horizontal and perpendicular to the (nearly axial) spin angular momentum L ≈ I₃ω₃. With τ = dL/dt rotating L horizontally at rate Ω: mgl sin θ = Ω·(I₃ω₃ sin θ) ⟹ **Ω = mgl/(I₃ω₃)**, independent of θ.
2. **Evaluate.** Ω = 0.5·9.81·0.05/(2×10⁻⁴·300) = 0.24525/0.06 = **4.0875 rad/s**; period = 2π/Ω = **1.537 s**.
3. **Spin scaling.** Ω ∝ 1/ω₃, so doubling the spin **halves** the precession: Ω = **2.044 rad/s**.
4. **Physics.** Precession changes the **direction** of L, not its magnitude; a superimposed wobble is nutation. Counterintuitively, faster spin gives **slower** precession.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{precession\_rad\_s}     &= 4.0875 \\
\mathrm{precession\_period\_s}  &= 1.537171 \\
\mathrm{precession\_double\_spin} &= 2.04375
\end{aligned}
\]
```

**Reasoning checkpoints:** τ = mgl sin θ = d(L_horiz)/dt ⟹ Ω = mgl/(I₃ω₃), θ-independent; Ω ≈ 4.09 rad/s, period ≈ 1.54 s; Ω ∝ 1/ω₃ (double spin halves precession); precession changes L's direction not magnitude, nutation superimposed; does not claim faster spin → faster precession.

**Wrong-answer fingerprints:** inverts the spin scaling (faster spin → faster precession) → `C_SPIN_SCALING_INVERTED`; torque-arm error → `N_TORQUE_ARM_ERROR`; conflates nutation and precession → `C_NUTATION_PRECESSION_CONFLATED`.

---

*Batch 7 of 32 (cumulative 32/32 — COMPLETE). Classical mechanics done; all 32 scenarios have step-by-step gold solutions. Verified against the generators. All keys LOCKED 2026-07-04.*
