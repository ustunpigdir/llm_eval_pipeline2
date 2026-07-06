# Worked gold solutions — Batch 1 (5 of 32)

Step-by-step derivations that land **exactly** on Fable's now-locked keys (every number
re-verified programmatically against the generator constants). Each solution is
structured for cheap deterministic autograding:

- **Steps + intermediate values** — the grader can check named checkpoints, not just the final block.
- **FINAL ANSWER block** — matches the scenario's `expected_values` field names for numeric compare.
- **Reasoning checkpoints** — the `required_concepts`, phrased as pass/fail checks.
- **Wrong-answer fingerprints** — the specific distractor values a common misconception produces, each tied to a `failure_tag`. These are what let the grader mark a wrong answer *and its cause* without an LLM call; the LLM second-opinion is reserved for genuinely ambiguous runs.

Status: **LOCKED 2026-07-04** — matches the arithmetically-verified keys (human-locked).

---

## QI_WERNER_001 — Werner state: entanglement without nonlocality

**Given:** ρ = p |Ψ⁻⟩⟨Ψ⁻| + (1−p) 𝟙/4. Concurrence C = max(0, (3p−1)/2). Maximal CHSH value S = 2√2·p.

**Derivation**
1. **Entanglement threshold.** For two qubits PPT is exact; the singlet-Werner state is non-separable iff its concurrence is positive: C = max(0, (3p−1)/2) > 0 ⟺ 3p−1 > 0 ⟺ **p > 1/3 = 0.333333**.
2. **CHSH threshold.** The optimal CHSH value for this family is S = 2√2·p (Horodecki criterion). Violation requires S > 2 ⟺ **p > 1/√2 = 0.707107**.
3. **At p = 0.500.** C = max(0, (3·0.5 − 1)/2) = max(0, 0.25) = **0.25** (positive → entangled). S = 2√2·0.5 = √2 = **1.414214** (< 2 → no CHSH violation).
4. **Interpretation.** Because 1/3 < 0.5 ≤ 1/√2, the state is entangled yet admits a local hidden-variable model for projective measurements. Entanglement does **not** imply Bell nonlocality — Werner's 1989 result.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= 0.333333 \\
\mathrm{chsh\_threshold}         &= 0.707107 \\
\mathrm{concurrence\_at\_p05}    &= 0.25 \\
\mathrm{chsh\_S\_at\_p05}        &= 1.414214
\end{aligned}
\]
```

**Reasoning checkpoints:** entanglement threshold 1/3 (PPT); CHSH threshold 1/√2; at p=0.5 C=0.25 and S=√2<2; identifies the 1/3<p≤1/√2 "entangled-but-local" window; does not claim every entangled state violates Bell.

**Wrong-answer fingerprints:** reports one threshold for both (e.g. both 1/3 or both 1/√2) → `C_ENT_NONLOCALITY_CONFLATED`; threshold values swapped/other → `N_THRESHOLD_CONFUSION`; C ≠ 0.25 at p=0.5 → `N_CONCURRENCE_ERROR`.

---

## QI_CLONE_001 — Optimal universal cloning: 5/6, not 1, not 1/2

**Given:** 1→2 symmetric universal cloner, F = ⟨ψ|ρ_out|ψ⟩ independent of |ψ⟩.

**Derivation**
1. **Why not F = 1.** A perfect cloner would need a unitary mapping |ψ⟩|0⟩ → |ψ⟩|ψ⟩ for all |ψ⟩; that map is quadratic in |ψ⟩, hence not linear, so no unitary implements it (Wootters–Zurek 1982). No-cloning forbids **only** F = 1.
2. **Optimal universal fidelity.** The Bužek–Hillery machine (optimality proven by Gisin–Massar 1997) achieves **F = 5/6 = 0.833333** per copy.
3. **Classical bound.** Measure the unknown qubit in a random basis and prepare copies of the outcome; averaged over uniform inputs the fidelity is **F = 2/3 = 0.666667**.
4. **Quantum advantage.** 5/6 − 2/3 = **1/6 = 0.166667**. Beating measure-and-prepare is allowed precisely because 5/6 < 1 — no-cloning is not violated.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{optimal\_fidelity}   &= 0.833333 \\
\mathrm{classical\_fidelity} &= 0.666667 \\
\mathrm{quantum\_advantage}  &= 0.166667
\end{aligned}
\]
```

**Reasoning checkpoints:** no-cloning from linearity forbids only F=1; optimal F=5/6; classical F=2/3; advantage 1/6; does not claim cloning is simply impossible or stuck at trivial fidelity.

**Wrong-answer fingerprints:** "cloning impossible" / F=1 or F=1/2 → `C_NO_CLONING_MISAPPLIED`; any F ≠ 5/6, 2/3 → `N_FIDELITY_VALUE_ERROR`.

---

## QI_TELEPORT_001 — Teleportation with a noisy resource

**Given:** singlet fidelity f = ⟨Ψ⁻|χ|Ψ⁻⟩ = 0.900 (isotropic). Average teleportation fidelity F = (2f+1)/3.

**Derivation**
1. **Output fidelity.** F = (2·0.900 + 1)/3 = 2.800/3 = **0.933333**.
2. **Classical limit.** Best measure-and-send strategy with no shared entanglement: **F_cl = 2/3 = 0.666667** (Massar–Popescu).
3. **Threshold to beat it.** (2f+1)/3 > 2/3 ⟹ 2f+1 > 2 ⟹ **f > 1/2 = 0.5**.
4. **Interpretation.** f > 1/2 is exactly the entanglement threshold of the isotropic resource; since no classical strategy exceeds 2/3, any F > 2/3 certifies a genuinely quantum (entanglement-assisted) channel. Note the bookkeeping: the resource quality f = 0.900 is **not** the teleportation fidelity F = 0.9333.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{teleport\_fidelity} &= 0.933333 \\
\mathrm{classical\_limit}   &= 0.666667 \\
\mathrm{f\_threshold}       &= 0.5
\end{aligned}
\]
```

**Reasoning checkpoints:** F=(2f+1)/3=0.9333; classical limit 2/3; beats classical iff f>1/2; f>1/2 is the isotropic-state entanglement threshold; does not report f itself as F.

**Wrong-answer fingerprints:** reports F = 0.900 (= f) → `C_RESOURCE_OUTPUT_CONFLATED`; classical limit ≠ 2/3 → `N_CLASSICAL_LIMIT_WRONG`.

---

## QI_HOLEVO_001 — Holevo bound: one qubit, less than one bit

**Given:** x=0 → |0⟩, x=1 → |+⟩, uniform prior. χ = S(ρ̄) − Σ pₓ S(ρₓ), entropies in **bits** (log₂).

**Derivation**
1. **Average state and eigenvalues.** ρ̄ = ½|0⟩⟨0| + ½|+⟩⟨+| = ½·[[1,0],[0,0]] + ½·[[½,½],[½,½]] = [[¾, ¼],[¼, ¼]]. With Tr = 1 and det = 3/16 − 1/16 = 1/8, the eigenvalues are (1 ± √(1−4·⅛))/2 = (1 ± 1/√2)/2 → **λ₊ = 0.853553**, λ₋ = 0.146447.
2. **Holevo quantity.** Both signal states are pure, so S(ρₓ) = 0 and χ = S(ρ̄) = −λ₊ log₂ λ₊ − λ₋ log₂ λ₋ = **0.600876 bits**.
3. **Purity.** Tr ρ̄² = λ₊² + λ₋² = **0.75**.
4. **Interpretation.** (a) χ < 1 bit because |0⟩ and |+⟩ are non-orthogonal (overlap ⟨0|+⟩ = 1/√2), so they are not perfectly distinguishable. (b) Accessible information I_acc ≤ χ (Holevo 1973): no measurement extracts more than 0.6009 bits. Using natural log gives 0.4165 **nats**, not bits.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{eigenvalue\_large} &= 0.853553 \\
\mathrm{holevo\_chi\_bits}  &= 0.600876 \\
\mathrm{avg\_state\_purity} &= 0.75
\end{aligned}
\]
```

**Reasoning checkpoints:** eigenvalues (1±1/√2)/2 ≈ 0.854/0.146; pure ensemble ⟹ χ = S(ρ̄) ≈ 0.601 bits; χ<1 from non-orthogonality (overlap 1/√2); I_acc ≤ χ; uses log₂.

**Wrong-answer fingerprints:** χ = 1 bit / assumes distinguishable states → `C_ORTHOGONALITY_ASSUMED`; χ = 0.4165 (nats) → `N_LOG_BASE_ERROR`.

---

## GR_PERI_001 — Mercury perihelion precession: the 43″/century

**Given:** a = 5.7909×10¹⁰ m, e = 0.2056, period T = 87.969 d, GM_⊙ = 1.32712×10²⁰ m³/s², c = 2.99792458×10⁸ m/s, 1 century = 36525 d.

**Derivation**
1. **Closed form.** First-order Schwarzschild result: Δφ = 6πGM_⊙ / (a(1−e²)c²) per orbit.
2. **Per orbit.** 1 − e² = 1 − 0.042271 = 0.957729; a(1−e²)c² = 5.7909×10¹⁰ · 0.957729 · 8.98755×10¹⁶. Δφ = 6π·1.32712×10²⁰ / (that) = 5.0186×10⁻⁷ rad. Convert: ×(180/π)×3600 = **0.103516 arcsec/orbit**.
3. **Per century.** Orbits per century = 36525 / 87.969 = **415.203083**. Δφ_century = 0.103516 × 415.203 = **42.980208 arcsec/century** (≈ 43″).
4. **The remainder.** The observed ~574″/century is dominated (~532″) by Newtonian planetary perturbations (Venus, Jupiter, Earth) plus a tiny solar-oblateness term; only the ~43″ residual, unexplained by Newtonian gravity, is the GR test.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit}   &= 0.103516 \\
\mathrm{advance\_arcsec\_century} &= 42.980208 \\
\mathrm{orbits\_per\_century}     &= 415.203083
\end{aligned}
\]
```

**Reasoning checkpoints:** uses Δφ = 6πGM/(a(1−e²)c²); keeps the 1/(1−e²) factor; ~0.1035″/orbit and ~43″/century; distinguishes GR 43″ from planetary perturbations (~532″); identifies 6π (not 4π/2π) as the GR coefficient.

**Wrong-answer fingerprints:** drops (1−e²) → **41.2″**/century → `N_ECCENTRICITY_FACTOR_DROPPED`; uses 4π instead of 6π → **28.7″**/century → `N_COEFFICIENT_4PI`; attributes the whole 574″ (or the perturbation part) to GR → `C_PERTURBATION_CONFUSION`.

---

*Batch 1 of 32. Verified against generator constants (`_generator_part1.py`). LOCKED 2026-07-04.*
