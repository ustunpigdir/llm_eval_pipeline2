# Worked gold solutions — Batch 6 (scenarios 25–28 of 32): Statistical Mechanics

STAT_ISING, STAT_BEC, STAT_LANDAUER, STAT_NEGT. Same structure. Verified against generator constants.
Status: **LOCKED 2026-07-04** (human-locked).

> **Reviewer flag:** STAT_NEGT `temperature_K = −1.318567` is genuinely **negative** (a negative-temperature
> system). The sign is the physics — do not grade it as a magnitude.

---

## STAT_ISING_001 — 2D Ising: Onsager's exact Tc vs mean field

**Given:** ferromagnetic Ising on the square lattice (coordination z = 4), J > 0, zero field. Report k_B T_c/J.

**Derivation**
1. **Mean field.** k_B T_c^{MF}/J = z = **4**.
2. **Onsager exact.** k_B T_c/J = 2/ln(1+√2) = 2/0.88137 = **2.269**.
3. **Ratio.** T_c^{exact}/T_c^{MF} = 2.269/4 = **0.567**. Mean field **overestimates** T_c because it replaces each spin's neighbors by their average and ignores fluctuations; thermal fluctuations destroy long-range order at a lower temperature than the mean-field estimate.
4. **One dimension.** T_c = 0 — no finite-temperature transition. A single domain wall costs energy 2J but gains entropy k ln N; for any T > 0 the free-energy term −TΔS wins for large N, so order is always destroyed (Peierls / domain-wall argument).

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{tc\_exact}      &= 2.269185 \\
\mathrm{tc\_meanfield}  &= 4.0 \\
\mathrm{ratio\_exact\_mf} &= 0.567296
\end{aligned}
\]
```

**Reasoning checkpoints:** MF k_B T_c/J = z = 4; Onsager 2/ln(1+√2) = 2.269; ratio ≈ 0.567 (MF neglects fluctuations); 1D T_c = 0 (domain-wall entropy); does not present the mean-field value as exact.

**Wrong-answer fingerprints:** presents mean-field as exact → `C_MEANFIELD_AS_EXACT`; claims a 1D finite-T transition → `C_1D_TRANSITION_CLAIMED`; wrong Onsager value → `N_ONSAGER_VALUE_ERROR`.

---

## STAT_BEC_001 — BEC critical temperature: where the zeta function bites

**Given:** ideal uniform Bose gas of ⁸⁷Rb (m = 1.443×10⁻²⁵ kg), n = 1.00×10¹⁹ m⁻³. Degeneracy condition nλ_T³ = ζ(3/2) = 2.612 at T_c, λ_T = √(2πℏ²/(m k_B T)). Report nK.

**Derivation**
1. **Derive T_c.** At T_c, nλ_T³ = ζ(3/2). With λ_T³ = (2πℏ²/(m k_B T_c))^{3/2}: n(2πℏ²/(m k_B T_c))^{3/2} = ζ ⟹ (m k_B T_c/(2πℏ²))^{3/2} = n/ζ ⟹ **k_B T_c = (2πℏ²/m)(n/ζ)^{2/3}**.
2. **Evaluate.** T_c = (2πℏ²/(m k_B))(n/ζ)^{2/3} = **85.82 nK**.
3. **Phase-space density.** At T_c it is ζ(3/2) = **2.612** by definition. Since nλ_T³ ∝ T^{−3/2}, at 2T_c it is 2.612/2^{3/2} = 2.612/2.828 = **0.924**.
4. **Dropping ζ.** Setting nλ³ = 1 gives T_c' = (2πℏ²/(m k_B))·n^{2/3} = T_c·ζ^{2/3} = 85.82·1.897 = **162.8 nK** — an overestimate by ζ^{2/3} ≈ 1.90×. ζ(3/2) sums the Bose occupation over all excited states; ignoring it overstates the degeneracy required.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{tc\_nK}                 &= 85.817924 \\
\mathrm{phase\_space\_density\_tc} &= 2.612375 \\
\mathrm{psd\_at\_2tc}            &= 0.923614 \\
\mathrm{tc\_no\_zeta\_nK}         &= 162.780255
\end{aligned}
\]
```

**Reasoning checkpoints:** degeneracy nλ_T³ = ζ(3/2) = 2.612 at T_c; T_c ≈ 86 nK; nλ³ ∝ T^{−3/2} → ≈ 0.924 at 2T_c; dropping ζ overestimates by ζ^{2/3} ≈ 1.90 (→ 163 nK); ζ(3/2) sums Bose occupation.

**Wrong-answer fingerprints:** drops ζ(3/2) → `N_ZETA_DROPPED`; wrong 2/3 power → `N_POWER_23_ERROR`; conflates uniform gas with a harmonic trap → `C_TRAP_UNIFORM_CONFLATED`.

---

## STAT_LANDAUER_001 — Landauer limit: the thermodynamic cost of erasure

**Given:** erase one bit at T = 300 K. Landauer bound Q_min = k_B T ln 2. Report zJ and meV.

**Derivation**
1. **Origin.** Erasing one bit maps two logical states to one, reducing the memory's entropy by k ln 2; that entropy must be expelled to the bath as heat, Q ≥ k_B T ln 2. The cost lives in **erasure** (irreversible logical compression), not in computation per se.
2. **Evaluate.** Q_min = k_B T ln 2 = 1.3806×10⁻²³·300·0.6931 = 2.871×10⁻²¹ J = **2.871 zJ = 17.92 meV**.
3. **Maxwell's demon.** The demon's measurement record must eventually be reset (erased); Bennett showed this reset costs at least the work the Szilard engine extracted — no net gain, so the demon is exorcised.
4. **Reversible computation.** Logically invertible computation avoids erasure and so evades the bound: nothing is destroyed, so no entropy need be dumped.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{landauer\_zJ}  &= 2.870979 \\
\mathrm{landauer\_meV} &= 17.919241
\end{aligned}
\]
```

**Reasoning checkpoints:** Q_min = k_B T ln 2 (erasure maps 2→1, k ln 2 to bath); ≈ 2.87 zJ = 17.9 meV; demon exorcised via memory reset (Bennett); reversible computation avoids erasure; ln 2 not log₁₀ 2; erasure not "any gate."

**Wrong-answer fingerprints:** drops ln 2 → `N_LN2_DROPPED`; uses log₁₀ 2 → `N_LOG_BASE_ERROR`; conflates erasure with computation → `C_ERASURE_COMPUTATION_CONFLATED`.

---

## STAT_NEGT_001 — Negative temperature: population inversion done right

**Given:** isolated two-level systems, ΔE = 2.00×10⁻²³ J, N_up/N_down = 3.00 (inverted). Boltzmann ratio N_up/N_down = e^{−ΔE/k_B T}. Report T with sign.

**Derivation**
1. **Sign.** e^{−ΔE/k_B T} = 3 > 1 ⟹ −ΔE/(k_B T) = ln 3 > 0; since ΔE > 0, this forces **T < 0**. T = −ΔE/(k_B ln 3).
2. **Evaluate.** T = −2×10⁻²³ / (1.3806×10⁻²³·1.0986) = −2×10⁻²³ / 1.5168×10⁻²³ = **−1.319 K**.
3. **Hotter, not colder.** A negative-T system is **hotter** than any positive-T system: on contact, heat flows **from** T < 0 **to** T > 0 (ordering by −1/T). Adding energy to the inverted system lowers its entropy (dS/dE < 0 ⟹ T < 0), so it readily gives energy up.
4. **Requirements.** Negative T needs a **bounded** energy spectrum (an upper energy bound), or the partition function diverges. Realized in nuclear-spin systems (Purcell & Pound 1951). It is "beyond +∞" on the 1/T scale — not "below absolute zero" in the colder sense.

**FINAL ANSWER** *(temperature is genuinely negative — sign is physical)*
```
\[
\begin{aligned}
\mathrm{temperature\_K}     &= -1.318567 \\
\mathrm{abs\_temperature\_K} &= 1.318567
\end{aligned}
\]
```

**Reasoning checkpoints:** inversion ⟹ e^{−ΔE/kT} > 1 ⟹ T < 0; T = −ΔE/(k ln 3) ≈ −1.32 K; negative T is hotter (heat flows T<0 → T>0, 1/T ordering); requires bounded spectrum (nuclear spins); not "colder than 0."

**Wrong-answer fingerprints:** drops the sign (reports +1.32) → `N_SIGN_DROPPED`; claims negative T is colder → `C_NEGATIVE_T_COLDER_CLAIMED`; ignores the bounded-spectrum requirement → `C_UNBOUNDED_SPECTRUM_IGNORED`.

---

*Batch 6 of 32 (cumulative 28/32). Statistical mechanics complete. Verified against the generators. LOCKED 2026-07-04.*
