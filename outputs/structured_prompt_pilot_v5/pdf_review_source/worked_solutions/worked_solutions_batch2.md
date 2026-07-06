# Worked gold solutions — Batch 2 (scenarios 6–10 of 32)

Finishes General Relativity (ISCO, GPS, chirp) and starts Special Relativity (Bell, Fizeau).
Same structure as Batch 1: steps + values, FINAL ANSWER block matching field names, reasoning
checkpoints (= `required_concepts`), and wrong-answer fingerprints (distractor value → `failure_tag`).
Every number re-verified against the generator constants. Status: **LOCKED 2026-07-04** (human-locked).

> **Reviewer flags in this batch:**
> - **GR_GPS sign convention.** The key stores `velocity_shift_us_day = +7.213` (magnitude of the slowdown) and `net = grav − velocity`. A model that reports the velocity term as **−7.21** (signed) is physically correct but will fail a raw numeric compare. Grade that field on `abs(value)`, or store it signed. Decide at lock.
> - **Precise vs prompt constants.** The ISCO and chirp keys were computed with full-precision constants; the prompt's rounded values reproduce them to <0.1% (well inside the 1% tolerance). No action needed, just noted.

---

## GR_ISCO_001 — Schwarzschild ISCO: radius and GW frequency

**Given:** M = 10 M_⊙, M_⊙ = 1.989×10³⁰ kg, G = 6.674×10⁻¹¹, c = 2.998×10⁸ m/s. Exact Schwarzschild identity Ω² = GM/r³.

**Derivation**
1. **Characteristic radii** (units of GM/c²): event horizon 2GM/c², photon sphere 3GM/c², **ISCO 6GM/c²** — three distinct radii. With GM/c² = G·10M_⊙/c² ≈ 14.77 km: horizon 29.54 km, photon sphere 44.31 km, **r_ISCO = 6·14.77 ≈ 88.62 km**.
2. **Orbital frequency.** f = Ω/2π = (1/2π)√(GM/r_ISCO³), GM = 1.3276×10²¹, r_ISCO = 8.862×10⁴ m ⟹ **f_orb = 219.80 Hz**.
3. **GW frequency.** Dominant emission at twice the orbital frequency: **f_GW = 2·219.80 = 439.60 Hz**.
4. **Interpretation.** No stable circular orbit exists inside r_ISCO, so the inspiral transitions to plunge/merger there — the quasi-periodic chirp "shuts off." Since r_ISCO ∝ M and f ∝ M⁻¹, heavier binaries merge at **lower** frequency (f_ISCO ∝ 1/M).

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{r\_isco\_km}    &= 88.620232 \\
\mathrm{f\_orbital\_hz} &= 219.802347 \\
\mathrm{f\_gw\_hz}      &= 439.604695
\end{aligned}
\]
```

**Reasoning checkpoints:** horizon 2 / photon sphere 3 / ISCO 6 GM/c² all distinguished; r_ISCO ≈ 88.6 km; uses the exact Ω² = GM/r³ (no ad-hoc correction); f_orb ≈ 220, f_GW ≈ 440; states f_ISCO ∝ 1/M.

**Wrong-answer fingerprints:** ISCO given as 2 or 3 GM/c² → `N_RADIUS_CONFUSION`; f_GW = f_orb (factor-2 dropped) → `N_GW_FACTOR2_DROPPED`; adds a "relativistic correction" to Ω² = GM/r³ → `C_SPURIOUS_CORRECTION`.

---

## GR_GPS_001 — GPS clock rates: gravitational vs velocity

**Given:** r = 26 562 km, GM_E = 3.986×10¹⁴ m³/s², R_E = 6371 km, ignore rotation. Report μs/day of satellite clock relative to ground.

**Derivation**
1. **Gravitational.** Δrate_grav = GM_E(1/R_E − 1/r)/c². The satellite sits at higher (less negative) potential, so its clock runs **faster**: GM_E(1/6.371×10⁶ − 1/2.6562×10⁷)/c² = 5.292×10⁻¹⁰ → ×86400×10⁶ = **+45.719 μs/day (faster)**.
2. **Velocity.** Δrate_vel = −v²/(2c²) with v² = GM_E/r. = −(GM_E/r)/(2c²) = −8.35×10⁻¹¹ → ×86400×10⁶ = **−7.213 μs/day (slower)** — magnitude 7.213.
3. **Net.** +45.719 + (−7.213) = **+38.506 μs/day** (satellite fast). The two effects have **opposite sign**.
4. **Consequence.** Uncorrected, the timing error maps to a ranging error ≈ c·38.5 μs ≈ **11.5 km/day**. Adding the two with the same sign gives 52.9 μs/day — the classic mistake.

**FINAL ANSWER** *(velocity stored as positive magnitude — see reviewer flag)*
```
\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day}     &= 45.719299 \\
\mathrm{velocity\_shift\_us\_day} &= 7.213057 \\
\mathrm{net\_shift\_us\_day}      &= 38.506242
\end{aligned}
\]
```

**Reasoning checkpoints:** gravitational term ⟹ satellite faster ~45.7; velocity term ⟹ slower ~7.2; net ~+38.5 with opposite signs explained; ranging error ~11.5 km/day; does **not** add the two with the same sign.

**Wrong-answer fingerprints:** net = 52.9 (same-sign addition) → `N_SIGN_ERROR_NET` / `C_EFFECTS_CONFLATED`; wrong potential term → `N_POTENTIAL_TERM_ERROR`.

---

## GR_CHIRP_001 — GW chirp: chirp mass from f and ḟ

**Given:** f_GW = 35.0 Hz, ḟ_GW = 68.678 Hz/s, GM_⊙/c³ = 4.925×10⁻⁶ s. 𝓜 = (m₁m₂)^{3/5}/(m₁+m₂)^{1/5}.

**Derivation**
1. **Leading-order relation.** ḟ = (96/5) π^{8/3} (G𝓜/c³)^{5/3} f^{11/3}.
2. **Invert for 𝓜.** G𝓜/c³ = [ ḟ / ((96/5) π^{8/3} f^{11/3}) ]^{3/5} ≈ 1.379×10⁻⁴ s ⟹ 𝓜 = (G𝓜/c³)/(GM_⊙/c³) = 1.379×10⁻⁴ / 4.925×10⁻⁶ ≈ **28.0 M_⊙**.
3. **Equal masses.** With m₁ = m₂ = m, 𝓜 = m/2^{1/5}, so m = 𝓜·2^{1/5} = 28·1.1487 = **32.16 M_⊙ each**, total **64.33 M_⊙**.
4. **Why chirp mass.** The leading-order (quadrupole) inspiral phasing depends only on the combination 𝓜; the individual masses / mass ratio enter only at higher post-Newtonian order. So a leading-order chirp measures **𝓜**, not the total mass.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{chirp\_mass\_msun} &= 28.0 \\
\mathrm{each\_mass\_msun}   &= 32.163554 \\
\mathrm{total\_mass\_msun}  &= 64.327108
\end{aligned}
\]
```

**Reasoning checkpoints:** uses ḟ = (96/5)π^{8/3}(G𝓜/c³)^{5/3}f^{11/3}; inverts to 𝓜 ≈ 28; equal-mass m ≈ 32.2 each, total ≈ 64.3; leading-order phasing depends only on chirp mass; uses GW frequency (not orbital) consistently.

**Wrong-answer fingerprints:** reports 𝓜 as the total mass → `C_CHIRP_AS_TOTAL_MASS`; orbital/GW frequency mixed (factor 2) → `N_FREQUENCY_FACTOR2`; exponent slip → `N_EXPONENT_ERROR`.

---

## SR_BELL_001 — Bell spaceship paradox: proper distance and the string

**Given:** lab separation L₀ = 100 m; both rockets run identical acceleration programs (equal velocities at every lab instant) up to v = 0.8c; connecting string has rest length 100 m.

**Derivation**
1. **Lorentz factor.** γ = 1/√(1 − 0.8²) = 1/√0.36 = 1/0.6 = **1.6667**.
2. **Lab separation.** Identical velocity-vs-lab-time programs ⟹ the rockets' lab positions differ by a constant, so the lab-frame separation stays **100 m** (unchanged).
3. **Proper separation.** In the rockets' common final rest frame the separation is γ·L₀ = 1.6667·100 = **166.667 m**. The fixed 100 m lab gap is the length-contracted image of this larger proper gap (proper = γ × lab).
4. **The string.** Its rest length is 100 m but it must now span a proper distance of 166.67 m — it is stretched past its rest length and **breaks**. The "60 m" answer wrongly applies contraction L₀/γ to the separation; contraction applies to an object's rest length, not to the coordinate gap between two independently accelerated worldlines.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{gamma\_factor}      &= 1.666667 \\
\mathrm{lab\_separation\_m}  &= 100.0 \\
\mathrm{proper\_separation\_m} &= 166.666667
\end{aligned}
\]
```

**Reasoning checkpoints:** identical lab programs keep lab separation fixed at 100 m; proper separation = γL₀ = 166.67 m (grows, not contracts); string rest length 100 m must span 166.67 m ⟹ breaks; rejects L₀/γ = 60 m; distinguishes object rest length from coordinate separation of two worldlines.

**Wrong-answer fingerprints:** claims the string survives / separation contracts → `C_STRING_BREAK_DENIED` / `C_CONTRACTION_MISAPPLIED`; γ ≠ 5/3 → `N_GAMMA_ERROR`.

---

## SR_FIZEAU_001 — Fizeau drag: light in moving water

**Given:** n = 1.333, water flows at V = 5.00 m/s co-directional with the light; work to first order in V/c; rest-frame phase velocity c/n.

**Derivation**
1. **Velocity addition + expansion.** v = (c/n + V)/(1 + (c/n)V/c²) = (c/n + V)/(1 + V/(nc)). To first order in V/c: v ≈ (c/n + V)(1 − V/(nc)) ≈ c/n + V(1 − 1/n²). So the Fresnel drag coefficient is **f = 1 − 1/n²**.
2. **Evaluate.** f = 1 − 1/1.333² = 1 − 1/1.776889 = 1 − 0.562781 = **0.437219**.
3. **Speed increase.** Δv = f·V = 0.437219·5 = **2.186093 m/s**.
4. **Why not Galilean.** Galilean addition predicts Δv = V = 5 m/s (full drag). The relativistic result gives partial drag, f < 1 — the medium only partially carries the light. This f = 1 − 1/n² is Fresnel's 1818 coefficient, measured by Fizeau in 1851, and special relativity reproduces it exactly via velocity addition.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{drag\_coefficient} &= 0.437219 \\
\mathrm{delta\_v\_ms}       &= 2.186093
\end{aligned}
\]
```

**Reasoning checkpoints:** applies relativistic velocity addition (c/n + V)/(1 + V/(nc)); first-order expansion v = c/n + V(1 − 1/n²); f = 1 − 1/n² = 0.4372 (not 1, not 1 − 1/n = 0.25); Δv = 2.186 m/s (not the Galilean 5); notes Fresnel/Fizeau.

**Wrong-answer fingerprints:** Δv = 5 m/s (Galilean) → `C_GALILEAN_ADDITION_USED`; f = 1 or f = 1 − 1/n → `N_DRAG_COEFFICIENT_ERROR`.

---

*Batch 2 of 32 (cumulative 10/32). Verified against `_generator_part1.py`. LOCKED 2026-07-04.*
