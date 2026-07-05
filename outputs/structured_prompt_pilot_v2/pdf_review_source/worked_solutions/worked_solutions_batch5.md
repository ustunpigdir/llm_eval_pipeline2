# Worked gold solutions — Batch 5 (scenarios 21–24 of 32): Cosmology

COS_AGE, COS_CMB, COS_DESITTER, COS_DL. Same structure: steps + values, FINAL ANSWER matching field
names, reasoning checkpoints (= `required_concepts`), wrong-answer fingerprints (distractor → `failure_tag`).
Verified against generator constants. Status: **LOCKED 2026-07-04** (human-locked).

---

## COS_AGE_001 — Age of the universe: Hubble time vs real ages

**Given:** H₀ = 70.0 km/s/Mpc (1 Mpc = 3.0857×10¹⁹ km). Hubble time = 1/H₀. EdS = flat matter-only. ΛCDM (Ω_m=0.3, Ω_Λ=0.7): t₀ = (2/(3H₀√Ω_Λ))·asinh√(Ω_Λ/Ω_m).

**Derivation**
1. **Hubble time.** 1/H₀ = (3.0857×10¹⁹ km)/(70 km/s) = 4.408×10¹⁷ s = **13.97 Gyr**.
2. **Matter-only (EdS).** a ∝ t^{2/3} ⟹ t₀ = (2/3)/H₀ = (2/3)·13.97 = **9.31 Gyr**. It is **less** than 1/H₀ because matter decelerates the expansion — the universe expanded faster in the past, so it reached today's size in less time.
3. **ΛCDM.** t₀ = (2/(3√0.7))·asinh(√(0.7/0.3))·(1/H₀) = 0.9642·13.97 = **13.47 Gyr**.
4. **Near-coincidence.** Early matter domination decelerates (pulling the age below 1/H₀); late Λ domination accelerates (pushing it back up). At Ω_m ≈ 0.3 these nearly cancel, so t₀ ≈ 1/H₀ — an accident of the present epoch, not a law.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 13.96846 \\
\mathrm{matter\_age\_gyr}  &= 9.312307 \\
\mathrm{lcdm\_age\_gyr}    &= 13.466984
\end{aligned}
\]
```

**Reasoning checkpoints:** 1/H₀ ≈ 13.97 Gyr; EdS (2/3)/H₀ ≈ 9.31 (deceleration ⟹ younger); ΛCDM asinh ≈ 13.47; coincidence with 1/H₀ explained (decel then accel); does not report 1/H₀ as "the age."

**Wrong-answer fingerprints:** reports 1/H₀ as the age → `C_HUBBLE_TIME_AS_AGE`; wrong EdS factor (not 2/3) → `N_EDS_FACTOR_ERROR`; ΛCDM formula error → `N_LCDM_FORMULA_ERROR`.

---

## COS_CMB_001 — CMB scaling: temperature, number, and energy densities

**Given:** T₀ = 2.725 K, recombination at z = 1100. Report log₁₀ of density ratios (recombination / today).

**Derivation**
1. **Temperature.** T ∝ (1+z): T_rec = 2.725·1101 = **3000.2 K**.
2. **Number density.** n ∝ (1+z)³: log₁₀(n_rec/n₀) = 3·log₁₀(1101) = **9.125**.
3. **Energy density.** u ∝ (1+z)⁴: log₁₀(u_rec/u₀) = 4·log₁₀(1101) = **12.167**. The extra factor of (1+z) over the number density is the **per-photon energy redshift** — each photon's energy scales as (1+z).
4. **Blackbody preserved.** T ∝ 1/a keeps the Planck spectrum form-invariant: redshifting a Planck spectrum at T yields a Planck spectrum at T/(1+z). No scattering or rethermalization is required.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{T\_rec\_K}            &= 3000.225 \\
\mathrm{log10\_number\_ratio} &= 9.125362 \\
\mathrm{log10\_energy\_ratio} &= 12.167149
\end{aligned}
\]
```

**Reasoning checkpoints:** T ∝ (1+z) → 3000 K; n ∝ (1+z)³ → log 9.13; u ∝ (1+z)⁴ → log 12.17, extra (1+z) from per-photon redshift; blackbody preserved (no rethermalization); does not use (1+z)³ for energy density.

**Wrong-answer fingerprints:** energy scaled as (1+z)³ / conflated with number → `N_ENERGY_NUMBER_SCALING_CONFLATED`; invokes rethermalization → `C_RETHERMALIZATION_INVOKED`.

---

## COS_DESITTER_001 — de Sitter horizon: size and Gibbons–Hawking temperature

**Given:** H = 70.0 km/s/Mpc, constant. Horizon r = c/H; T = ℏH/(2π k_B). Report T in units of 10⁻³⁰ K.

**Derivation**
1. **Horizon radius.** r = c/H = 2.998×10⁸ / 2.269×10⁻¹⁸ = 1.32×10²⁶ m = **4.28 Gpc**.
2. **Gibbons–Hawking temperature.** T = ℏH/(2π k_B) = 2.758×10⁻³⁰ K ⟹ **2.758** (in 10⁻³⁰ K).
3. **e-folds to cool below T_GH.** For a T ∝ a⁻¹ radiation background, cooling from T₀ = 2.725 K below T_GH takes ln(T₀/T_GH) = ln(2.725 / 2.758×10⁻³⁰) = **69.07 e-folds**.
4. **Interpretation.** An observer in pure de Sitter sees a cosmological event horizon at c/H emitting a thermal Gibbons–Hawking bath at T_GH — analogous to Unruh (acceleration) and Hawking (surface gravity). The 2π is present; no black-hole mass formula is used.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{horizon\_gpc}   &= 4.282749 \\
\mathrm{gh\_temp\_e30\_K} &= 2.757786 \\
\mathrm{efolds\_to\_gh}  &= 69.065593
\end{aligned}
\]
```

**Reasoning checkpoints:** c/H ≈ 4.28 Gpc; T_GH = ℏH/(2π k_B) ≈ 2.7×10⁻³⁰ K; e-folds = ln(T₀/T_GH) ≈ 69; horizon thermal radiation analogous to Unruh/Hawking; 2π present, no BH-mass formula.

**Wrong-answer fingerprints:** drops the 2π → `N_2PI_DROPPED`; horizon confusion (Hubble vs event vs particle) → `C_HORIZON_CONFUSION`.

---

## COS_DL_001 — Luminosity distance: the q₀ correction that revealed dark energy

**Given:** d_L = (cz/H₀)[1 + (1−q₀)z/2], H₀ = 70.0 km/s/Mpc. q₀ = Ω_m/2 − Ω_Λ; ΛCDM (0.3,0.7) → q₀ = −0.55; EdS → q₀ = +0.5. z = 0.200.

**Derivation**
1. **Hubble distance & linear term.** c/H₀ = 2.998×10⁵/70 = **4282.75 Mpc**; cz/H₀ = 4282.75·0.2 = **856.55 Mpc**.
2. **ΛCDM (q₀ = −0.55).** [1 + (1−(−0.55))·0.2/2] = [1 + 1.55·0.1] = 1.155 ⟹ d_L = 856.55·1.155 = **989.32 Mpc**.
3. **EdS (q₀ = +0.5).** [1 + (1−0.5)·0.1] = 1.05 ⟹ d_L = 856.55·1.05 = **899.38 Mpc**.
4. **The 1998 result.** A supernova at z = 0.2 appearing **fainter** than the EdS prediction means a **larger** d_L, i.e. larger (1 − q₀), i.e. **more negative q₀** — an accelerating expansion. This favors ΛCDM / dark energy (Riess & Perlmutter 1998). q₀ < 0 signals acceleration.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{hubble\_distance\_mpc} &= 4282.7494 \\
\mathrm{dl\_linear\_mpc}       &= 856.54988 \\
\mathrm{dl\_lcdm\_mpc}         &= 989.315111 \\
\mathrm{dl\_eds\_mpc}          &= 899.377374
\end{aligned}
\]
```

**Reasoning checkpoints:** c/H₀ ≈ 4283 Mpc, linear term ≈ 857; ΛCDM (1 + 1.55·0.1) → 989; EdS (1 + 0.5·0.1) → 900; fainter = larger d_L = negative q₀ = acceleration; q₀ sign handled correctly.

**Wrong-answer fingerprints:** q₀ sign error → `N_Q0_SIGN_ERROR`; acceleration direction confused → `C_ACCELERATION_DIRECTION_CONFUSED`; keeps only the linear term → `N_LINEAR_ONLY`.

---

*Batch 5 of 32 (cumulative 24/32). Cosmology complete. Verified against `_generator_part2.py`. LOCKED 2026-07-04.*
