# Normalized-body merge — sample for review

Math regions merged in place: `⟦ … ⟧` = display/environment, `⟨ … ⟩` = inline.


---
## run 496  (display=14, inline=15, residual=0, len 3643→2564)

**Derivation of the resonance condition**

For a 1‑D square well of depth ⟨-V_0⟩ (with ⟨V_0>0⟩ ) and width ⟨L⟩ , the interior wave number is 

 ⟦k' = √(2m (E+V_0)/ħ^2) .⟧ 

Perfect transmission ( ⟨T=1⟩ ) occurs when the phase accumulated inside the well satisfies 

 ⟦k' L = nπ, n = 1,2,3,…⟧ 

Solving for the energy ⟨E⟩ :

 ⟦√(2m (E+V_0)/ħ^2) L = nπ⟹2m (E+V_0)/ħ^2 = n^2π^2/L^2 ⟹E+V_0 = n^2π^2ħ^2/2mL^2 .⟧ 

Hence 

 ⟦E_n = n^2π^2ħ^2/2mL^2 - V_0 .⟧ 

This is the resonance (or “bound‑state‑like”) condition for a positive‑energy scattering state.

---

**Evaluation of the energy unit ⟨π^2ħ^2/2mL^2⟩ in eV**

Given constants (electron rest mass ⟨m = 9.10938356×10^-31 kg⟩ , reduced Planck constant ⟨ħ= 1.0545718×10^-34 J·s⟩ , and ⟨1 eV=1.602176634×10^-19 J⟩ ):

 ⟦π^2ħ^2/2mL^2 = π^2/2 (1.0545718×10^-34)^2/9.10938356×10^-31 (0.400×10^-9)^2 J [4pt] = 9.8696044/2 1.112121×10^-68/9.10938356×10^-31×1.6×10^-19 J [4pt] = 4.9348022 ×1.112121×10^-68/1.4542989×10^-49 J [4pt] = 4.9348022 ×7.645 ×10^-20 J [4pt] ≈3.773 ×10^-19 J.⟧ 

Convert to electron‑volts:

 ⟦3.773 ×10^-19 J/1.602176634×10^-19 J/eV ≈2.35 eV.⟧ 

Thus 

 ⟦energy_unit_ev ≈2.35 eV.⟧ 

---

**Finding the smallest integer ⟨n⟩ giving ⟨E_n > 0⟩ ** 

The resonance condition is 

 ⟦E_n = n^2π^2ħ^2/2mL^2 - V_0 .⟧ 

We need ⟨E_n > 0⟩ :

 ⟦n^2π^2ħ^2/2mL^2 > V_0 = 10.0 eV.⟧ 

Using the energy unit in eV ( ⟨≈2.35 eV⟩ ):

 ⟦n^2 ×2.35 eV > 10.0 eV ⟹n^2 > 10.0/2.35 ≈4.255.⟧ 

The smallest integer satisfying this is 

 ⟦n_lowest = 3.⟧ 

---

**Evaluating the first positive resonance energy**

Insert ⟨n=3⟩ into the resonance formula:

 ⟦E_3 = 3^2π^2ħ^2/2mL^2 - V_0 = 9 ×π^2ħ^2/2mL^2 - 10.0 eV ≈9 ×2.35 eV - 10.0 eV ≈21.15 eV - 10.0 eV ≈11.15 eV.⟧ 

Thus 

 ⟦first_resonance_ev ≈11.2 eV.⟧ 

---

**Relation to the Ramsauer–Townsend minimum**

The Ramsauer–Townsend effect describes a pronounced peak in electron–noble‑gas scattering cross‑section (i.e., near‑perfect transmission) at certain energies. This occurs because the incident electron can form a standing wave inside the effective potential barrier, satisfying the resonance condition ⟨k'L = nπ⟩ . At these energies, the phase shifts of partial waves cancel destructive interference, leading to constructive interference and maximal transmission—exactly the situation derived above for the square well. Hence, the electron transmits perfectly at special energies due to constructive interference of the wave inside the well, analogous to the Ramsauer–Townsend resonance.

---

FINAL ANSWER
 ⟦energy_unit_ev ≈2.35 n_lowest = 3 first_resonance_ev ≈11.2⟧ 

---
## run 120  (display=9, inline=14, residual=0, len 2751→2089)

**Derivation Steps**

1. **Photon temperature scaling with redshift** 
 For an adiabatically expanding blackbody photon gas, the temperature scales inversely with the scale factor ⟨a⟩ : 
 ⟦T ∝1/a ⇒T(z) = T_0/1+z,⟧ 
 where ⟨T_0 = 2.725 K⟩ is the present‑day CMB temperature.

 At recombination, ⟨z_rec = 1100⟩ : 
 ⟦T_rec = 2.725 K/1+1100 = 2.725/1101 K ≈0.002475 K.⟧ 

2. **Photon number density scaling** 
 The number density of photons follows the volume expansion as ⟨n ∝a^-3⟩ . Hence: 
 ⟦n(z)/n_0 = (a_0/a(z) )^3 = (1+z)^3.⟧ 

 Taking the base‑10 logarithm: 
 ⟦log_10 (n(z)/n_0 ) = log_10[(1+z)^3] = 3log_10(1+z).⟧ 

 For ⟨z = 1100⟩ : 
 ⟦log_10 (n(z_rec)/n_0 ) = 3log_10(1101) ≈3 ×3.0414 ≈9.124.⟧ 

3. **Photon energy density scaling** 
 The energy density of a blackbody photon gas scales as ⟨ρ∝a^-4⟩ (since each photon's energy scales as ⟨1/a⟩ and the number density scales as ⟨a^-3⟩ ): 
 ⟦ρ(z)/ρ_0 = (a_0/a(z) )^4 = (1+z)^4.⟧ 

 Taking the base‑10 logarithm: 
 ⟦log_10 (ρ(z)/ρ_0 ) = log_10[(1+z)^4] = 4log_10(1+z).⟧ 

 For ⟨z = 1100⟩ : 
 ⟦log_10 (ρ(z_rec)/ρ_0 ) = 4log_10(1101) ≈4 ×3.0414 ≈12.166.⟧ 

 **Explanation of the extra factor ⟨(1+z)⟩ :** 
 The number density scales as ⟨a^-3⟩ because the photon count per comoving volume is conserved. Energy per photon scales as ⟨1/a⟩ due to redshift, and multiplying by the number density gives an overall scaling of ⟨a^-4⟩ . Thus, the energy density acquires one additional factor of ⟨(1+z)⟩ compared to the number density.

4. **Why the CMB remains a perfect blackbody** 
 The CMB photons decouple from matter at recombination and subsequently undergo only adiabatic expansion. In an adiabatic process, the phase space distribution of photons remains unchanged; there is no scattering, absorption, or emission that would redistribute photon energies. Consequently, the Planck spectrum is preserved, and the CMB stays a perfect blackbody without any need for rethermalization.

---

**FINAL ANSWER**

 ⟦T_rec_K = 2.725/1101 ≈0.002475 K, [4pt] log10_number_ratio = 3log_10(1101) ≈9.124, [4pt] log10_energy_ratio = 4log_10(1101) ≈12.166.⟧ 

---
## run 411  (display=10, inline=15, residual=0, len 2246→1996)

To compute the teleportation fidelity with an imperfect entangled resource, we follow the provided definitions and the physics of quantum teleportation.

### 1. Evaluation of Average Teleportation Fidelity ⟨F⟩ 
The problem states that the shared resource is an isotropic state with singlet fidelity ⟨f = 0.900⟩ . The average teleportation fidelity ⟨F⟩ for such a resource is given by the formula:
 ⟦F = 2f + 1/3⟧ 
Substituting ⟨f = 0.900⟩ :
 ⟦F = 2(0.900) + 1/3 = 1.800 + 1/3 = 2.800/3⟧ 
 ⟦F ≈0.9333...⟧ 

### 2. The Classical Limit
The classical limit is the maximum average fidelity achievable using a "measure-and-prepare" strategy (where Alice measures the state and sends the result to Bob) without using any shared entanglement. For a uniformly random pure qubit input, the optimal classical strategy yields an average fidelity of:
 ⟦F_classical = 2/3 ≈0.6667⟧ 

### 3. Minimum Singlet Fidelity ⟨f⟩ to Beat the Classical Limit
To beat the classical limit, we require the teleportation fidelity ⟨F⟩ to be strictly greater than the classical limit ⟨F_classical⟩ :
 ⟦F > 2/3⟧ 
Using the relation ⟨F = 2f + 1/3⟩ :
 ⟦2f + 1/3 > 2/3⟧ 
Multiplying both sides by 3:
 ⟦2f + 1 > 2⟧ 
 ⟦2f > 1⟧ 
 ⟦f > 1/2 = 0.500⟧ 
Thus, the threshold singlet fidelity is ⟨f_threshold = 0.500⟩ .

### 4. Physical Interpretation
- **Entanglement and ⟨f > 1/2⟩ **: For an isotropic state (Werner state), the state is represented as ⟨χ= f |Ψ^-⟩⟨Ψ^-| + 1-f/3(I - |Ψ^-⟩⟨Ψ^-|)⟩ . Such a state is entangled if and only if ⟨f > 1/2⟩ . If ⟨f ≤1/2⟩ , the state is separable and can be described by a local hidden variable model.
- **Certifying a Quantum Channel**: Since the best classical strategy cannot exceed ⟨F = 2/3⟩ , any experimental result where ⟨F > 2/3⟩ proves that the process cannot be simulated by a classical measure-and-prepare scheme. This certifies that the resource used was entangled and the channel is truly quantum.

FINAL ANSWER

 ⟦teleport_fidelity = 0.9333 classical_limit = 0.6667 f_threshold = 0.500⟧ 