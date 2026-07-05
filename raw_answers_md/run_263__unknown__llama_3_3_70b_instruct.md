## Step 1: Derive the PBC spectrum $E(k)$
To derive the PBC spectrum, we consider the Hamiltonian $H$ with periodic boundary conditions. The eigenstates can be written as $\psi_j = e^{ikj}$, where $k$ is the wavevector. Substituting this into the Hamiltonian, we get $E(k) = t_R e^{ik} + t_L e^{-ik}$.

## Step 2: Describe the curve traced by $E(k)$ in the complex energy plane
Using Euler's formula, $E(k) = t_R (\cos k + i \sin k) + t_L (\cos k - i \sin k) = (t_R + t_L) \cos k + i (t_R - t_L) \sin k$. This represents an ellipse in the complex energy plane with semi-axes $t_R + t_L$ and $t_R - t_L$.

## Step 3: Write the characteristic equation for $\beta$ at energy $E$
For open-boundary conditions, we use the ansatz $\psi_j = \beta^j$. Substituting into the Hamiltonian, we get $E \beta^j = t_R \beta^{j+1} + t_L \beta^{j-1}$. Simplifying, we obtain the characteristic equation $E = t_R \beta + \frac{t_L}{\beta}$.

## Step 4: Give the product of the roots of the characteristic equation
Rearranging the characteristic equation, we get $E \beta = t_R \beta^2 + t_L$. Multiplying through by $\beta$, we obtain $E \beta^2 = t_R \beta^3 + t_L \beta$. Rearranging again, $t_R \beta^3 - E \beta^2 + t_L \beta = 0$. Factoring out $\beta$, we have $\beta (t_R \beta^2 - E \beta + t_L) = 0$. The product of the roots of the quadratic equation $t_R \beta^2 - E \beta + t_L = 0$ is $\frac{t_L}{t_R}$.

## Step 5: Derive the GBZ radius $|\beta|$ in closed form
The GBZ radius $|\beta|$ is the common modulus of the two solutions of the characteristic equation. From the quadratic equation $t_R \beta^2 - E \beta + t_L = 0$, using the quadratic formula, $\beta = \frac{E \pm \sqrt{E^2 - 4 t_R t_L}}{2 t_R}$. For the GBZ radius, we consider the case where $E = 0$, giving $\beta = \pm \sqrt{\frac{t_L}{t_R}}$. Thus, $|\beta| = \sqrt{\frac{t_L}{t_R}}$.

## Step 6: Evaluate the GBZ radius $|\beta|$
Given $t_R = 1.4$ and $t_L = 0.6$, $|\beta| = \sqrt{\frac{0.6}{1.4}} = \sqrt{\frac{3}{7}}$.

## Step 7: Determine if the OBC spectrum is real or complex
The OBC spectrum can be complex due to the non-Hermitian nature of the Hamiltonian.

## Step 8: Find the maximum $|E|$ of the OBC spectrum in the large-$N$ limit
The maximum $|E|$ occurs when $\beta$ is at its maximum or minimum value on the GBZ. This corresponds to $E = t_R \beta + \frac{t_L}{\beta}$, with $\beta = \sqrt{\frac{t_L}{t_R}}$ or $\beta = -\sqrt{\frac{t_L}{t_R}}$. Substituting, $E = t_R \sqrt{\frac{t_L}{t_R}} + \frac{t_L}{\sqrt{\frac{t_L}{t_R}}} = \sqrt{t_R t_L} + \sqrt{t_R t_L} = 2 \sqrt{t_R t_L}$.

## Step 9: Evaluate the maximum $|E|$ of the OBC spectrum
Given $t_R = 1.4$ and $t_L = 0.6$, $|E|_{max} = 2 \sqrt{1.4 \cdot 0.6} = 2 \sqrt{0.84}$.

## Step 10: Determine if a skin effect occurs
A skin effect occurs when the OBC spectrum differs from the PBC prediction, with eigenstates localized at a boundary. This happens when $t_R \neq t_L$.

## Step 11: Determine the conditions for the skin effect to occur
The skin effect occurs when $t_R \neq t_L$, which is the case here since $t_R = 1.4$ and $t_L = 0.6$.

## Step 12: Determine the edge at which the eigenstates are localized
Given the convention that $t_R$ is the amplitude for hopping to the right and $t_L$ to the left, and since $t_R > t_L$, the eigenstates are localized at the right edge.

The final answer is: 
\[
\begin{aligned}
\mathrm{pbc\_real\_semiaxis} &= 2 \\
\mathrm{pbc\_imag\_semiaxis} &= 0.8 \\
\mathrm{beta\_GBZ} &= \sqrt{\frac{3}{7}} \\
\mathrm{obc\_E\_max} &= 2 \sqrt{0.84}
\end{aligned}
\]