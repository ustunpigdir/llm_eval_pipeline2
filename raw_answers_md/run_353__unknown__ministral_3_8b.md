### Task 1: Yukawa Potential and Mediator Mass in the Exponential

The Yukawa potential describes the interaction between two nucleons mediated by a virtual pion exchange. The potential is given by:

\[
V(r) = -\frac{g^2}{4\pi} \frac{e^{-m_\pi r}}{r}
\]

where:
- \( g \) is the coupling constant,
- \( m_\pi \) is the mass of the pion (mediator),
- \( r \) is the distance between the nucleons.

The exponential term \( e^{-m_\pi r} \) determines the **range** of the force. The mass \( m_\pi \) appears directly in the exponent, meaning the force falls off exponentially with a characteristic length scale set by the inverse of the mediator mass.

---

### Task 2: Reduced Compton Wavelength \( \hbar/(m_\pi c) \)

The **reduced Compton wavelength** is defined as:

\[
\lambda = \frac{\hbar}{m_\pi c}
\]

Given:
- \( m_{\pi^\pm} c^2 = 139.57 \) MeV,
- \( \hbar c = 197.327 \) MeV fm.

First, express \( m_\pi c \) in MeV units:

\[
m_\pi c = \frac{m_{\pi^\pm} c^2}{c} = 139.57 \text{ MeV}
\]

Now, compute \( \hbar/(m_\pi c) \):

\[
\lambda = \frac{\hbar}{m_\pi c} = \frac{\hbar c}{m_\pi c^2} = \frac{197.327 \text{ MeV fm}}{139.57 \text{ MeV}} = 1.413 \text{ fm}
\]

Thus, the **reduced Compton wavelength** is approximately **1.413 fm**.

---

### Task 3: Non-Reduced Compton Wavelength \( h/(m_\pi c) \)

The **non-reduced Compton wavelength** is defined as:

\[
\lambda_{\text{non-reduced}} = \frac{h}{m_\pi c}
\]

Recall that \( h = 2\pi \hbar \), so:

\[
\lambda_{\text{non-reduced}} = \frac{2\pi \hbar}{m_\pi c} = 2\pi \cdot \lambda = 2\pi \cdot 1.413 \text{ fm} = 8.88 \text{ fm}
\]

**Which one belongs in the Yukawa exponential?**
The Yukawa potential uses the **reduced Compton wavelength** (or equivalently, the inverse of the mediator mass \( m_\pi \)) in the exponent. This is because the exponential term is \( e^{-m_\pi r} \), and \( m_\pi \) is the mass of the mediator. The reduced Compton wavelength \( \hbar/(m_\pi c) \) is the natural length scale associated with \( m_\pi \), and it is the correct quantity to use for the range of the force.

The non-reduced Compton wavelength \( h/(m_\pi c) \) is not used in the Yukawa potential because it introduces an unnecessary factor of \( 2\pi \) and is not physically meaningful in this context. The Yukawa potential is derived from quantum field theory where the reduced Planck constant \( \hbar \) appears naturally.

---

### Task 4: Mass Scale Implied by a 2.0 fm Range (Historical Yukawa Prediction)

Historically, Yukawa inferred the existence of the pion by observing that the nuclear force has a range of approximately **2.0 fm**. He then predicted the mass of the mediator using the reduced Compton wavelength:

\[
\lambda = \frac{\hbar}{m_\pi c} \approx 2.0 \text{ fm}
\]

We can rearrange this to solve for \( m_\pi c^2 \):

\[
m_\pi c^2 = \frac{\hbar c}{\lambda} = \frac{197.327 \text{ MeV fm}}{2.0 \text{ fm}} = 98.66 \text{ MeV}
\]

Thus, a 2.0 fm range implies a mediator mass of approximately **98.7 MeV**.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{range\_fm} &= 1.413 \\
\mathrm{nonreduced\_fm} &= 8.88 \\
\mathrm{mass\_for\_2fm\_mev} &= 98.7
\end{aligned}
\]