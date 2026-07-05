To solve this problem, we need to use the leading-order relation between the gravitational-wave frequency \( f_{GW} \), its time derivative \( \dot{f}_{GW} \), and the chirp mass \( \mathcal{M} \).

### Step 1: Leading-Order Relation

At the leading (quadrupole) order, the relation between \( \dot{f}_{GW} \), \( f_{GW} \), and the chirp mass \( \mathcal{M} \) is given by:

\[
\dot{f}_{GW} = \frac{96}{5} \pi^{8/3} \frac{\mathcal{M}^{5/3}}{c^3} f_{GW}^{11/3}
\]

Here, \( c \) is the speed of light, and \( \mathcal{M} \) is the chirp mass defined as:

\[
\mathcal{M} = \frac{(m_1 m_2)^{3/5}}{(m_1 + m_2)^{1/5}}
\]

### Step 2: Solve for Chirp Mass

We can rearrange the above equation to solve for the chirp mass \( \mathcal{M} \):

\[
\mathcal{M}^{5/3} = \frac{5}{96} \pi^{-8/3} \frac{c^3 \dot{f}_{GW}}{f_{GW}^{11/3}}
\]

Taking both sides to the power of \( 3/5 \):

\[
\mathcal{M} = \left( \frac{5}{96} \pi^{-8/3} \frac{c^3 \dot{f}_{GW}}{f_{GW}^{11/3}} \right)^{3/5}
\]

Given:
- \( f_{GW} = 35.0 \) Hz
- \( \dot{f}_{GW} = 68.678 \) Hz/s
- \( G M_\odot/c^3 = 4.925 \times 10^{-6} \) s

First, we need to express \( c^3 \) in terms of \( G M_\odot \):

\[
c^3 = \frac{G M_\odot}{(G M_\odot/c^3)}
\]

But since \( G M_\odot/c^3 \) is given, we can directly use it in our calculations.

Substituting the given values:

\[
\mathcal{M} = \left( \frac{5}{96} \pi^{-8/3} \frac{(4.925 \times 10^{-6} \text{ s}) \cdot 68.678 \text{ Hz/s}}{35.0^{11/3} \text{ Hz}^{11/3}} \right)^{3/5}
\]

Calculating the numerical value:

\[
\mathcal{M} \approx \left( \frac{5}{96} \pi^{-8/3} \frac{4.925 \times 10^{-6} \times 68.678}{35.0^{11/3}} \right)^{3/5}
\]

\[
\mathcal{M} \approx \left( \frac{5}{96} \pi^{-8/3} \frac{0.0003376}{558.456} \right)^{3/5}
\]

\[
\mathcal{M} \approx \left( \frac{5}{96} \pi^{-8/3} \times 6.046 \times 10^{-7} \right)^{3/5}
\]

\[
\mathcal{M} \approx \left( 5.29 \times 10^{-9} \right)^{3/5}
\]

\[
\mathcal{M} \approx 1.0 \text{ solar masses}
\]

### Step 3: Equal Masses

Assuming equal masses, \( m_1 = m_2 = m \), the chirp mass \( \mathcal{M} \) can be written as:

\[
\mathcal{M} = \frac{(m \cdot m)^{3/5}}{(m + m)^{1/5}} = \frac{m^{6/5}}{(2m)^{1/5}} = \frac{m^{6/5}}{2^{1/5} m^{1/5}} = \frac{m}{2^{1/5}}
\]

Solving for \( m \):

\[
m = \mathcal{M} \cdot 2^{1/5}
\]

Given \( \mathcal{M} \approx 1.0 \text{ solar masses} \):

\[
m \approx 1.0 \cdot 2^{1/5} \approx 1.1487 \text{ solar masses}
\]

Thus, the total mass \( M \) is:

\[
M = m_1 + m_2 = 2m \approx 2.2974 \text{ solar masses}
\]

### Step 4: Why Leading-Order Waveform Measures Chirp Mass

The leading-order gravitational-wave waveform depends on the chirp mass \( \mathcal{M} \) rather than the total mass \( M \) because the waveform's phase evolution is primarily determined by the combination of masses that appears in the energy loss due to gravitational radiation. This combination is the chirp mass, which is a specific function of the individual masses \( m_1 \) and \( m_2 \). The total mass \( M \) does not appear directly in the leading-order phase evolution of the waveform.

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{chirp\_mass\_msun} &= 1.0 \\
\mathrm{each\_mass\_msun} &= 1.1487 \\
\mathrm{total\_mass\_msun} &= 2.2974
\end{aligned}
\]