# Worked gold solutions — Batch 3 (scenarios 11–15 of 32)

Finishes Special Relativity (rocket, twin) and starts Quantum Mechanics (Berry, Ramsauer–Townsend,
Aharonov–Bohm). Same structure: steps + values, FINAL ANSWER matching field names, reasoning
checkpoints (= `required_concepts`), wrong-answer fingerprints (distractor → `failure_tag`).
Every number re-verified against generator constants. Status: **LOCKED 2026-07-04** (human-locked).

---

## SR_ROCKET_001 — Relativistic rocket: one proper year at 1 g

**Given:** proper acceleration a = 9.8 m/s², from rest; 1 yr = 3.15576×10⁷ s, 1 ly = c·yr; hyperbolic (Rindler) motion, τ = proper time.

**Derivation**
1. **Exact hyperbolic motion.** t(τ) = (c/a) sinh(aτ/c), x(τ) = (c²/a)(cosh(aτ/c) − 1), β(τ) = tanh(aτ/c). The dimensionless combination aτ/c is the **rapidity**.
2. **Rapidity & lab time.** aτ/c = 9.8·3.15576×10⁷ / 2.99792458×10⁸ = 1.0316. Lab time = (c/a) sinh(1.0316) ⟹ **1.187 yr** (> 1 proper year — the correct dilation direction).
3. **Distance.** x = (c²/a)(cosh 1.0316 − 1) ⟹ **0.563 ly**.
4. **Final speed.** β = tanh(1.0316) = **0.7745**.
5. **The student's error.** v = aτ gives β = aτ/c = 1.03 > 1 (superluminal). The resolution: the **rapidity** aτ/c grows linearly, but velocity β = tanh(rapidity) saturates below 1. Newtonian kinematics wrongly adds velocities instead of rapidities.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{lab\_time\_yr}  &= 1.187045 \\
\mathrm{distance\_ly}   &= 0.563194 \\
\mathrm{final\_beta}    &= 0.774547
\end{aligned}
\]
```

**Reasoning checkpoints:** uses x = (c²/a)(cosh−1), t = (c/a)sinh, β = tanh; aτ/c ≈ 1.03; lab time 1.19 > 1 proper yr; distance 0.56 ly; β 0.77; rejects v = aτ — rapidity grows linearly, not velocity.

**Wrong-answer fingerprints:** v = aτ / β > 1 → `C_NEWTONIAN_KINEMATICS_USED` / `C_SUPERLUMINAL_CLAIM`; rapidity mishandled → `N_RAPIDITY_ERROR`.

---

## SR_TWIN_001 — Twin paradox: Doppler bookkeeping (Bondi k-calculus)

**Given:** traveler at v = 0.6c to a star 6.00 ly away (Earth frame), instant turnaround, returns at 0.6c; both send 1 pulse per proper year.

**Derivation**
1. **Elapsed times.** Earth time = 2D/v = 2·6/0.6 = **20 yr**. γ = 1/√(1 − 0.6²) = 1/0.8 = 1.25, so traveler proper time = 20/γ = **16 yr**.
2. **Doppler factor.** k = √((1+β)/(1−β)). Approach: √(1.6/0.4) = √4 = **2**. Recession: 1/k = **0.5**.
3. **Pulse counting (consistency).** Traveler's 8 proper-yr **outbound** (receding): receives Earth's pulses at rate 1/k = 0.5/yr ⟹ 4 pulses. 8 proper-yr **return** (approaching): rate k = 2/yr ⟹ 16 pulses. Total 4 + 16 = **20** = Earth's elapsed years. ✓ (Traveler's own proper time 8 + 8 = 16 yr.)
4. **Asymmetry.** The traveler **changes inertial frames** at turnaround (its line of simultaneity swings); the Earth twin stays inertial throughout. The age difference is the difference in spacetime **path length** (proper time) between the two worldlines — not a local "effect caused by acceleration."

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{earth\_time\_yr}     &= 20.0 \\
\mathrm{traveler\_time\_yr}  &= 16.0 \\
\mathrm{doppler\_k\_approach} &= 2.0 \\
\mathrm{doppler\_k\_recede}   &= 0.5
\end{aligned}
\]
```

**Reasoning checkpoints:** Earth 2D/v = 20; traveler 20/γ = 16; k_approach = 2, k_recede = 1/2; pulse count outbound 4 + return 16 = 20; asymmetry = traveler switches frames; age difference is path length, not acceleration.

**Wrong-answer fingerprints:** claims the situation is symmetric → `C_SYMMETRY_CLAIMED`; wrong k → `N_DOPPLER_ERROR`; attributes the difference to acceleration locally → `C_ACCELERATION_MYSTIFIED`.

---

## QM_BERRY_001 — Berry phase: spin-½ on a cone

**Given:** spin-½ in the instantaneous aligned state; field direction traces a cone of half-angle θ = 60° once, adiabatically. Report |Berry phase| in radians.

**Derivation**
1. **Solid angle.** Ω = 2π(1 − cos θ) = 2π(1 − cos 60°) = 2π(1 − 0.5) = **π = 3.141593 sr**.
2. **Berry phase (spin-½).** γ = −½ Ω, so |γ| = Ω/2 = π/2 = **1.570796 rad**. The factor ½ is the spin.
3. **Spin-1 (m = 1).** In general |γ| = m·Ω for the aligned |S,m⟩ state, so spin-1 m = 1 gives |γ| = π (scales with m).
4. **Why geometric.** γ depends only on the solid angle Ω enclosed by the field's path — **not** on the traversal speed (as long as adiabatic), the field magnitude, or elapsed time. It is distinct from the dynamical phase (∝ energy × time).

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{solid\_angle\_sr}  &= 3.141593 \\
\mathrm{berry\_phase\_rad} &= 1.570796
\end{aligned}
\]
```

**Reasoning checkpoints:** Ω = 2π(1 − cos 60°) = π; spin-½ |γ| = Ω/2 = π/2 (factor ½ present); spin-1 |γ| = mΩ = π; geometric (independent of speed, distinct from dynamical); does not report Ω itself as the phase.

**Wrong-answer fingerprints:** reports Ω = π as the phase (½ dropped) → `N_FACTOR_HALF_DROPPED`; conflates dynamical and geometric phase → `C_DYNAMICAL_GEOMETRIC_CONFLATED`.

---

## QM_RT_001 — Ramsauer–Townsend: transmission resonance over a well

**Given:** electron E > 0 scatters over a 1D square **well** of depth V₀ = 10.0 eV, width L = 0.400 nm. Perfect transmission when k′L = nπ with k′ = √(2m(E+V₀))/ℏ (inside the well).

**Derivation**
1. **Resonance condition.** T = 1 when an integer number of interior half-wavelengths spans the well: k′L = nπ. With k′ = √(2m(E+V₀))/ℏ ⟹ E + V₀ = n²π²ℏ²/(2mL²), i.e. **Eₙ = n²π²ℏ²/(2mL²) − V₀**.
2. **Energy unit.** π²ℏ²/(2mL²) = π²(1.054572×10⁻³⁴)² / (2·9.109384×10⁻³¹·(0.4×10⁻⁹)²) = 3.766×10⁻¹⁹ J = **2.350189 eV**.
3. **Lowest valid mode.** Eₙ = n²·2.350 − 10. n = 1: −7.65 eV; n = 2: −0.60 eV (both < 0 — bound, not scattering states, discard). n = 3: 9·2.350 − 10 = **+11.152 eV** > 0 ⟹ **n = 3**, E₃ = 11.151697 eV.
4. **Physics.** At these energies the internal reflections interfere destructively and the well is transparent (T = 1) — the Ramsauer–Townsend minimum in electron–noble-gas scattering (Ramsauer 1921). The interior wavevector uses E + V₀ (the well deepens k inside), and the n = 1, 2 solutions with E < 0 are not scattering states.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{energy\_unit\_ev}     &= 2.350189 \\
\mathrm{n\_lowest}            &= 3.0 \\
\mathrm{first\_resonance\_ev} &= 11.151697
\end{aligned}
\]
```

**Reasoning checkpoints:** interior wavevector uses E + V₀ (well, not barrier); resonance k′L = nπ; energy unit ≈ 2.35 eV; n = 1, 2 give E < 0 and are discarded; lowest valid n = 3, E ≈ 11.2 eV; connects to Ramsauer–Townsend transparency.

**Wrong-answer fingerprints:** drops the − V₀ shift → `N_WELL_SHIFT_DROPPED`; wrong interior wavevector (E − V₀ or E) → `C_INTERIOR_WAVEVECTOR_WRONG`; picks n = 1 → `N_MODE_INDEX_ERROR`.

---

## QM_AB_001 — Aharonov–Bohm: phase from an unfelt flux

**Given:** two-path interferometer encloses a solenoid, r = 1.00 μm, internal B = 0.0100 T, B = 0 on the electron paths. Φ₀ = h/e = 4.136×10⁻¹⁵ Wb; Δφ = 2π Φ/Φ₀.

**Derivation**
1. **Enclosed flux.** Φ = B·πr² = 0.0100·π·(1.00×10⁻⁶)² = π×10⁻¹⁴ = **3.1416×10⁻¹⁴ Wb**.
2. **Flux quanta & phase.** Φ/Φ₀ = 3.1416×10⁻¹⁴ / 4.136×10⁻¹⁵ = **7.596** flux quanta. Total AB phase Δφ = 2π·7.596 = **47.729 rad**.
3. **Fringe shift.** Δφ / 2π = Φ/Φ₀ = **7.596 fringes**.
4. **Why a shift with B = 0.** Although B (and the local force) is zero on the paths, the vector potential A is not; the observable is the gauge-invariant loop integral (holonomy) ∮A·dl = Φ. Using Φ₀ = h/2e (the Cooper-pair quantum, charge 2e) would halve the count — wrong here, since the carriers are single electrons (charge e). No local force on the electron is required.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{flux\_quanta}     &= 7.596337 \\
\mathrm{total\_phase\_rad} &= 47.729195 \\
\mathrm{fringe\_shift}     &= 7.596337
\end{aligned}
\]
```
*(Key uses the precise h/e = 4.135668×10⁻¹⁵; the prompt's rounded 4.136×10⁻¹⁵ gives 7.5957 — within tolerance.)*

**Reasoning checkpoints:** Φ = Bπr² ≈ 3.14×10⁻¹⁴ Wb; Φ/Φ₀ ≈ 7.60, phase ≈ 47.7 rad, fringe shift ≈ 7.6; effect exists despite B = 0 via the holonomy ∮A (gauge-invariant); rejects h/2e; no local force required.

**Wrong-answer fingerprints:** uses Φ₀ = h/2e → `N_FLUX_QUANTUM_H2E`; claims no effect because B = 0 → `C_NO_EFFECT_CLAIMED`; area/geometry slip → `N_GEOMETRY_ERROR`.

---

*Batch 3 of 32 (cumulative 15/32). SR complete; QM 3/4 (QM_TUNNEL remains). Verified against `_generator_part1.py`. LOCKED 2026-07-04.*
