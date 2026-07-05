**Step‑by‑step derivation**

1. **Earth‑frame round‑trip time**

   The distance to the star (one way) in the Earth frame is  
   \[
   L = 6.00\ \text{ly}.
   \]
   The traveler’s speed is \(v = 0.6c\).  
   The travel time one way is  
   \[
   t_{\text{one‑way}} = \frac{L}{v} = \frac{6.00\ \text{ly}}{0.6c}
                     = \frac{6.00}{0.6}\ \text{yr}
                     = 10\ \text{yr}.
   \]
   Hence the round‑trip duration in the Earth frame is  
   \[
   \boxed{ \text{earth\_time\_yr} = 2 \times 10\ \text{yr} = 20\ \text{yr} }.
   \]

2. **Traveler’s proper time**

   The Lorentz factor for \(\beta = v/c = 0.6\) is  
   \[
   \gamma = \frac{1}{\sqrt{1-\beta^{2}}}
          = \frac{1}{\sqrt{1-0.36}}
          = \frac{1}{\sqrt{0.64}}
          = \frac{1}{0.8}
          = 1.25.
   \]
   Proper time for one leg is  
   \[
   \tau_{\text{one‑way}} = \frac{t_{\text{one‑way}}}{\gamma}
                         = \frac{10\ \text{yr}}{1.25}
                         = 8\ \text{yr}.
   \]
   For the round trip:  
   \[
   \boxed{ \text{traveler\_time\_yr} = 2 \times 8\ \text{yr} = 16\ \text{yr} }.
   \]

3. **Relativistic Doppler factor \(k\)**  

   The Bondi‑k factor is  
   \[
   k = \sqrt{\frac{1+\beta}{1-\beta}}.
   \]
   Substituting \(\beta = 0.6\):  
   \[
   k_{\text{approach}} = \sqrt{\frac{1+0.6}{1-0.6}}
                       = \sqrt{\frac{1.6}{0.4}}
                       = \sqrt{4}
                       = 2.
   \]
   For recession the sign of \(\beta\) reverses, but the magnitude of \(k\) is the same:  
   \[
   k_{\text{recede}} = \sqrt{\frac{1-0.6}{1+0.6}}
                     = \sqrt{\frac{0.4}{1.6}}
                     = \sqrt{0.25}
                     = 0.5.
   \]
   Thus  
   \[
   \boxed{ \text{doppler\_k\_approach} = 2 },\qquad
   \boxed{ \text{doppler\_k\_recede} = 0.5 }.
   \]

4. **Pulse‑counting (k‑calculus) consistency**

   - **Outbound leg**: Earth sends a pulse every 1 yr of its own proper time.  
     The traveler moving toward Earth sees these pulses blueshifted with factor \(k_{\text{approach}} = 2\).  
     Hence the interval between pulses *as received* by the traveler is  
     \[
     \Delta t_{\text{traveler, out}} = \frac{1\ \text{yr}}{k_{\text{approach}}}
                                      = \frac{1}{2}\ \text{yr}.
     \]
     During the traveler’s proper time of 8 yr outbound, the number of Earth pulses received is  
     \[
     N_{\text{out}} = \frac{8\ \text{yr}}{1/2\ \text{yr}} = 16.
     \]

   - **Return leg**: The traveler now recedes, so the Doppler factor is \(k_{\text{recede}} = 0.5\).  
     The interval between received pulses is  
     \[
     \Delta t_{\text{traveler, ret}} = \frac{1\ \text{yr}}{k_{\text{recede}}}
                                      = \frac{1}{0.5}\ \text{yr}
                                      = 2\ \text{yr}.
     \]
     During the traveler’s proper time of 8 yr inbound, the number of Earth pulses received is  
     \[
     N_{\text{ret}} = \frac{8\ \text{yr}}{2\ \text{yr}} = 4.
     \]

   - **Total Earth elapsed time from pulses**:  
     \[
     N_{\text{total}} = N_{\text{out}} + N_{\text{ret}} = 16 + 4 = 20,
     \]
     which equals the Earth‑frame round‑trip duration of 20 yr.  
     Hence the pulse‑counting bookkeeping is consistent.

5. **Why the situation is not symmetric**

   - In the Earth frame the traveler **accelerates** at the turnaround point, breaking the inertial‑worldline condition.  
   - The Earth twin remains (to an excellent approximation) inertial for the entire journey, while the traveler experiences a non‑inertial segment.  
   - Because the twins have different worldlines, the spacetime intervals (proper times) they accumulate are different: the traveler ages less (16 yr) than the Earth twin (20 yr).  
   - The asymmetry originates from the fact that “who is moving” is not a relative notion when one twin changes inertial frames; the acceleration resolves the apparent paradox.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{earth\_time\_yr} &= 20 \\
\mathrm{traveler\_time\_yr} &= 16 \\
\mathrm{doppler\_k\_approach} &= 2 \\
\mathrm{doppler\_k\_recede} &= 0.5
\end{aligned}
\]