# Worked gold solutions — Batch 4 (scenarios 16–20 of 32)

Finishes Quantum Mechanics (opaque-barrier tunneling) and covers all of Quantum Field Theory
(Casimir, Unruh, g−2, Yukawa). Same structure: steps + values, FINAL ANSWER matching field names,
reasoning checkpoints (= `required_concepts`), wrong-answer fingerprints (distractor → `failure_tag`).
Every number re-verified against generator constants. Status: **LOCKED 2026-07-04** (human-locked).

---

## QM_TUNNEL_001 — Opaque-barrier tunneling: exponent and prefactor

**Given:** electron E = 1.00 eV, rectangular barrier V₀ = 5.00 eV, width L = 1.00 nm. Opaque limit T ≈ 16E(V₀−E)/V₀² · e^{−2κL}, κ = √(2m(V₀−E))/ℏ.

**Derivation**
1. **Decay constant.** κ = √(2m(V₀−E))/ℏ uses **V₀ − E = 4 eV** (the height above the electron's energy, not V₀). κ = √(2·9.109×10⁻³¹·4·1.602×10⁻¹⁹)/1.0546×10⁻³⁴ = 1.0246×10¹⁰ m⁻¹ = **10.246 nm⁻¹**; with L = 1 nm, **κL = 10.246**.
2. **Prefactor.** 16E(V₀−E)/V₀² = 16·1·4/25 = 64/25 = **2.56**.
3. **log₁₀T.** The exponent is **2κL** (not κL): log₁₀T = log₁₀(2.56) − 2κL/ln 10 = 0.408 − 20.493/2.3026 = 0.408 − 8.900 = **−8.492**.
4. **Doubling the width.** L → 2L doubles the exponent: log₁₀T = 0.408 − 4κL/ln 10 = **−17.39**. Halving the width or doubling it changes T by ~8.9 orders of magnitude — the transmission is exponentially sensitive to L.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 10.246334 \\
\mathrm{kappa\_L}       &= 10.246334 \\
\mathrm{prefactor}      &= 2.56 \\
\mathrm{log10\_T}       &= -8.491613
\end{aligned}
\]
```

**Reasoning checkpoints:** κ uses V₀ − E (not V₀) ≈ 10.2 nm⁻¹; exponent is 2κL (not κL); prefactor 16·1·4/25 = 2.56 included; log₁₀T ≈ −8.49; doubling L → ~−17.4; states exponential sensitivity to width.

**Wrong-answer fingerprints:** exponent κL instead of 2κL → `N_EXPONENT_HALVED`; prefactor dropped → `N_PREFACTOR_DROPPED`; κ uses V₀ or E → `N_KAPPA_WRONG_ENERGY`.

---

## QFT_CASIMIR_001 — Casimir pressure: vacuum energy between plates

**Given:** ideal conducting neutral plates, d = 100 nm, T = 0. |P| = π²ℏc/(240 d⁴), |E/A| = π²ℏc/(720 d³); state sign in words.

**Derivation**
1. **Origin.** Between the plates only discrete standing modes (k_z = nπ/d) are allowed; outside, a continuum. The zero-point sum Σ½ℏω diverges and must be **regularized** (zeta-function / cutoff); the finite difference between the constrained (inside) and free (outside) vacuum energies yields a net inward pressure.
2. **Pressure.** |P| = π²ℏc/(240 d⁴), with ℏc = 3.1615×10⁻²⁶ J·m and d⁴ = 10⁻²⁸ m⁴ ⟹ **|P| = 13.00 Pa**, and the force is **ATTRACTIVE** (plates pulled together).
3. **Energy per area.** |E/A| = π²ℏc/(720 d³) = **0.433 μJ/m²**.
4. **Scaling.** P ∝ 1/d⁴, so doubling d divides the pressure by 2⁴ = 16 ⟹ **0.813 Pa**.

**FINAL ANSWER** *(magnitudes; force is attractive — stated in words)*
```
\[
\begin{aligned}
\mathrm{pressure\_pa}            &= 13.001258 \\
\mathrm{energy\_per\_area\_uJ\_m2} &= 0.433375 \\
\mathrm{pressure\_double\_d\_pa}  &= 0.812579
\end{aligned}
\]
```

**Reasoning checkpoints:** mode exclusion between plates + regularization of the divergent zero-point sum; P = π²ℏc/(240 d⁴) ≈ 13 Pa, **attractive**; E/A = π²ℏc/(720 d³) ≈ 0.433 μJ/m²; P ∝ 1/d⁴, ÷16 when d doubles; does not swap the 240/720 coefficients or claim repulsion.

**Wrong-answer fingerprints:** swaps 240 ↔ 720 → `N_COEFFICIENT_240_720`; wrong power law (1/d³ etc.) → `N_POWER_LAW_ERROR`; claims repulsion → `C_REPULSION_CLAIMED`.

---

## QFT_UNRUH_001 — Unruh temperature: acceleration heats the vacuum

**Given:** constant proper acceleration a = 1.00×10²⁰ m/s² through the Minkowski vacuum. T = ℏa/(2π c k_B).

**Derivation**
1. **Formula & meaning.** T = ℏa/(2π c k_B). A uniformly accelerated detector perceives the Minkowski vacuum as a **thermal bath** at temperature T, while an inertial observer sees the same state as empty vacuum. (The 2π is essential.)
2. **Evaluate.** T = 1.0546×10⁻³⁴·10²⁰ / (2π·2.998×10⁸·1.3806×10⁻²³) = 1.0546×10⁻¹⁴ / 2.600×10⁻¹⁴ = **0.4055 K**.
3. **Acceleration for 1 K.** a = 2π c k_B·(1 K)/ℏ = **2.466×10²⁰ m/s²** = 2.466 (in units of 10²⁰) — about 2.5×10¹⁹ g.
4. **Hawking link.** By the equivalence principle the Unruh bath is the local counterpart of Hawking radiation (proper acceleration ↔ surface gravity). Everyday accelerations (~10 m/s²) give T ~ 10⁻¹⁹ K — unobservable; ~10²⁰ m/s² is needed to reach ~1 K. (The black-hole *mass* Hawking formula is not used here.)

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{unruh\_temp\_K}    &= 0.405501 \\
\mathrm{accel\_for\_1K\_e20} &= 2.466083
\end{aligned}
\]
```

**Reasoning checkpoints:** T = ℏa/(2π c k_B) with the 2π present; T ≈ 0.41 K at 10²⁰; a(1 K) ≈ 2.47×10²⁰ (~2.5×10¹⁹ g); accelerated detector sees thermal, inertial sees vacuum; connects to Hawking via surface gravity, does not use the BH-mass formula.

**Wrong-answer fingerprints:** drops the 2π → `N_2PI_DROPPED`; invokes the black-hole mass/Hawking formula → `C_HAWKING_FORMULA_MISUSED`.

---

## QFT_G2_001 — Electron g−2: the Schwinger term

**Given:** α = 1/137.036. Anomaly a_e = (g−2)/2; report a_e×10³ and g.

**Derivation**
1. **Schwinger one-loop.** a_e = α/(2π).
2. **Anomaly.** a_e = (1/137.036)/(2π) = 0.0072974/6.2832 = 1.16141×10⁻³ ⟹ **a_e×10³ = 1.16141**.
3. **g-factor.** g = 2(1 + a_e) = 2·1.00116141 = **2.002323**.
4. **Meaning.** The anomaly is the deviation from the tree-level Dirac value g = 2, produced by the electron emitting and reabsorbing a virtual photon (one loop). The leading coefficient α/(2π) is **mass-independent**, so the muon receives the same α/(2π) at leading order; mass-dependent contributions enter only at higher order.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.16141 \\
\mathrm{g\_factor}           &= 2.002323
\end{aligned}
\]
```

**Reasoning checkpoints:** a_e = α/(2π) (Schwinger); a_e×10³ ≈ 1.1614, g ≈ 2.002323; anomaly = loop correction to Dirac g = 2; leading coefficient mass-independent (same α/2π for the muon); does not report α/π or confuse a_e with g − 2.

**Wrong-answer fingerprints:** uses α/π (factor 2) → `N_2PI_VS_PI`; conflates a_e with g − 2 → `C_ANOMALY_G_CONFLATED`.

---

## QFT_YUKAWA_001 — Yukawa range: pion mass sets the nuclear-force reach

**Given:** m_{π±}c² = 139.57 MeV, ℏc = 197.327 MeV·fm. Range = reduced Compton wavelength λ = ℏ/(m_π c).

**Derivation**
1. **Potential.** V(r) ∝ e^{−r/λ}/r with λ = ℏ/(mc); the mediator mass sets the exponential decay length — the force range.
2. **Range.** λ = ℏ/(m_π c) = ℏc/(m_π c²) = 197.327/139.57 = **1.4138 fm**.
3. **Non-reduced (the trap).** h/(m_π c) = 2π·ℏ/(m_π c) = 2π·1.4138 = **8.883 fm**. The Yukawa exponential uses the **reduced** wavelength ℏ/(mc) (the propagator 1/(q²+m²) Fourier-transforms to e^{−mr}/r, with m = 1/λ_reduced in natural units); the full h/(mc) is 2π too large.
4. **Yukawa's inversion (1935).** A 2.0 fm range implies m c² = ℏc/range = 197.327/2.0 = **98.66 MeV** — his ~100 MeV prediction of the pion. Heavier mediator ⟹ shorter range.

**FINAL ANSWER**
```
\[
\begin{aligned}
\mathrm{range\_fm}        &= 1.413821 \\
\mathrm{nonreduced\_fm}   &= 8.883299 \\
\mathrm{mass\_for\_2fm\_mev} &= 98.66349
\end{aligned}
\]
```

**Reasoning checkpoints:** V ∝ e^{−r/λ}/r with λ = ℏ/(mc); range ≈ 1.414 fm; non-reduced h/(mc) = 2π× larger ≈ 8.88 fm (NOT the range); 2.0 fm ⟹ ~98.7 MeV (Yukawa's ~100); heavier mediator ⟹ shorter range.

**Wrong-answer fingerprints:** uses the non-reduced h/(mc) (2π) as the range → `N_2PI_COMPTON`; flips the inverse mass–range relation → `C_INVERSE_RELATION_FLIPPED`.

---

*Batch 4 of 32 (cumulative 20/32). QM and QFT complete. Verified against the generators. LOCKED 2026-07-04. Note: `log10_T = −8.49` is a genuine negative (log of a small number) — the sign is meaningful, not a magnitude.*
