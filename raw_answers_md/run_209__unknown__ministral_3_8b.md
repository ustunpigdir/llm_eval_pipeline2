To compute the GPS relativistic clock corrections, we separate the gravitational and velocity effects, compute each with the correct sign, and then combine them. Here is the detailed derivation:

---

### **1. Gravitational (Potential) Time Dilation (Blueshift)**
The gravitational time dilation effect arises from the difference in gravitational potential between the satellite and the Earth's surface. The formula for the relative time dilation due to gravity is:

\[
\frac{\Delta t_{\text{grav}}}{t} = \frac{\Phi(r) - \Phi(R_E)}{c^2}
\]

where \(\Phi(r)\) is the gravitational potential at radius \(r\), \(\Phi(R_E)\) is the gravitational potential at Earth's surface, and \(c\) is the speed of light.

The gravitational potential at a distance \(r\) from Earth's center is:

\[
\Phi(r) = -\frac{GM_E}{r}
\]

Thus, the difference in potential between the satellite and Earth's surface is:

\[
\Phi(r) - \Phi(R_E) = -\frac{GM_E}{r} - \left(-\frac{GM_E}{R_E}\right) = GM_E \left(\frac{1}{R_E} - \frac{1}{r}\right)
\]

Substituting this into the time dilation formula:

\[
\frac{\Delta t_{\text{grav}}}{t} = \frac{GM_E}{c^2} \left(\frac{1}{R_E} - \frac{1}{r}\right)
\]

Since the satellite is at a higher potential (less negative), its clock runs **faster** than a ground clock. The fractional rate difference is positive for the satellite.

#### **Convert to microseconds per day:**
The fractional rate difference corresponds to the satellite clock running faster by:

\[
\Delta t_{\text{grav}} = \frac{GM_E}{c^2} \left(\frac{1}{R_E} - \frac{1}{r}\right) \times t
\]

where \(t\) is the time interval (1 day = 86400 seconds). The rate difference in microseconds per day is:

\[
\text{grav\_shift\_us\_day} = \frac{GM_E}{c^2} \left(\frac{1}{R_E} - \frac{1}{r}\right) \times 86400 \times 10^6
\]

#### **Plug in values:**
- \(GM_E = 3.986 \times 10^{14} \, \text{m}^3/\text{s}^2\)
- \(c = 2.998 \times 10^8 \, \text{m/s}\)
- \(R_E = 6371 \times 10^3 \, \text{m}\)
- \(r = 26562 \times 10^3 \, \text{m}\)

\[
\frac{1}{R_E} - \frac{1}{r} = \frac{1}{6371 \times 10^3} - \frac{1}{26562 \times 10^3}
\]

\[
= 1.5696 \times 10^{-7} - 3.765 \times 10^{-8} = 1.1931 \times 10^{-7} \, \text{m}^{-1}
\]

\[
\frac{GM_E}{c^2} = \frac{3.986 \times 10^{14}}{(2.998 \times 10^8)^2} = 4.448 \times 10^{-10} \, \text{m}
\]

\[
\text{grav\_shift\_us\_day} = 4.448 \times 10^{-10} \times 1.1931 \times 10^{-7} \times 86400 \times 10^6
\]

\[
= 4.448 \times 1.1931 \times 86.4 \approx 44.5 \, \mu\text{s/day}
\]

The satellite clock runs **faster** by approximately **44.5 microseconds per day** due to the gravitational effect.

---

### **2. Velocity (Special Relativistic) Time Dilation**
The velocity time dilation effect arises from the satellite's orbital speed. The formula for the relative time dilation due to velocity is:

\[
\frac{\Delta t_{\text{vel}}}{t} = -\frac{v^2}{2c^2}
\]

where \(v\) is the orbital speed of the satellite. The negative sign indicates that the satellite clock runs **slower** than a ground clock due to its motion.

#### **Compute orbital speed \(v\):**
For a circular orbit, the orbital speed is given by:

\[
v = \sqrt{\frac{GM_E}{r}}
\]

\[
v = \sqrt{\frac{3.986 \times 10^{14}}{26562 \times 10^3}} = \sqrt{1.499 \times 10^3} \approx 38.72 \, \text{m/s}
\]

#### **Compute velocity time dilation:**
\[
\frac{v^2}{2c^2} = \frac{(38.72)^2}{2 \times (2.998 \times 10^8)^2} = \frac{1499.7}{2 \times 8.988 \times 10^{16}} \approx 8.29 \times 10^{-15}
\]

The fractional rate difference corresponds to the satellite clock running slower by:

\[
\Delta t_{\text{vel}} = -\frac{v^2}{2c^2} \times t
\]

The rate difference in microseconds per day is:

\[
\text{velocity\_shift\_us\_day} = -\frac{v^2}{2c^2} \times 86400 \times 10^6
\]

\[
= -8.29 \times 10^{-15} \times 86400 \times 10^6 \approx -71.6 \, \mu\text{s/day}
\]

The satellite clock runs **slower** by approximately **71.6 microseconds per day** due to the velocity effect.

---

### **3. Net Rate Difference**
The net effect is the sum of the gravitational and velocity shifts:

\[
\text{net\_shift\_us\_day} = \text{grav\_shift\_us\_day} + \text{velocity\_shift\_us\_day}
\]

\[
= 44.5 \, \mu\text{s/day} - 71.6 \, \mu\text{s/day} = -27.1 \, \mu\text{s/day}
\]

The satellite clock runs **slower** by approximately **27.1 microseconds per day** relative to a ground clock.

---

### **4. Ranging Error Accumulation**
If uncorrected, the net rate difference of \(-27.1 \, \mu\text{s/day}\) means the satellite clock loses time relative to the ground clock. Over one day, this results in a **27.1 microsecond error** in the time measurement. Over longer periods, this accumulates linearly, leading to significant errors in GPS ranging.

The two effects have opposite signs because:
- Gravitational time dilation causes the satellite clock to run **faster** (blueshift) due to the weaker gravitational field at higher altitude.
- Velocity time dilation causes the satellite clock to run **slower** (redshift) due to its motion relative to the ground.

---

### **FINAL ANSWER**

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 44.5 \\
\mathrm{velocity\_shift\_us\_day} &= -71.6 \\
\mathrm{net\_shift\_us\_day} &= -27.1 \\
\end{aligned}
\]