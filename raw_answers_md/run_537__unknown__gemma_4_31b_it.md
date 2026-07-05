### Reasoning

**1. Compute the Lorentz factor $\gamma$**
The Lorentz factor is defined as $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$.
Given $v = 0.8c$:
\[ \gamma = \frac{1}{\sqrt{1 - (0.8)^2}} = \frac{1}{\sqrt{1 - 0.64}} = \frac{1}{\sqrt{0.36}} = \frac{1}{0.6} = \frac{10}{6} = \frac{5}{3} \approx 1.667 \]

**2. Lab-frame separation of the rockets**
The problem states that both rockets follow "identical acceleration programs" and their velocities are equal at every lab-frame instant.
Let $x_1(t)$ be the position of the trailing rocket and $x_2(t)$ be the position of the leading rocket in the lab frame.
At $t=0$, $x_2(0) - x_1(0) = L_0 = 100$ m.
Since $v_1(t) = v_2(t)$ for all $t$, the distance between them in the lab frame is:
\[ \Delta x_{lab}(t) = x_2(t) - x_1(t) = \int (v_2(t) - v_1(t)) dt + (x_2(0) - x_1(0)) = 0 + L_0 \]
Thus, the lab-frame separation remains $100$ m.

**3. Proper separation in the rockets' final rest frame**
The "proper separation" is the distance measured in the frame moving with the rockets (the co-moving frame).
According to the length contraction formula, a length $L_{proper}$ in the rest frame appears as $L_{lab} = L_{proper}/\gamma$ in a frame moving at velocity $v$.
Here, the lab-frame separation $L_{lab} = 100$ m is the contracted version of the proper separation $L_{proper}$ between the two worldlines.
\[ L_{proper} = \gamma \cdot L_{lab} = \frac{5}{3} \cdot 100 \text{ m} = \frac{500}{3} \text{ m} \approx 166.67 \text{ m} \]

**4. Does the string break?**
The string has a rest length of $L_{string} = 100$ m.
The proper separation between the rockets (the distance they are "trying" to maintain in their own frame) is $166.67$ m.
Since the distance between the endpoints of the string in the string's own rest frame (which is the rockets' final rest frame) is $166.67$ m, but the string can only stretch to $100$ m without breaking, the string will break.
Physical reason: To maintain a constant distance in the lab frame, the leading rocket must accelerate "harder" in its own instantaneous rest frame than the trailing rocket. This increases the proper distance between them.

**5. Analysis of the student's argument**
The student argues that the separation $L_0$ length-contracts to $L_0/\gamma$.
The error is a confusion between the **coordinate separation of two worldlines** and the **length of a physical object**.
Length contraction applies to a physical object (like the string) measured by an observer in motion relative to it.
The $100$ m separation in the lab frame is not the "rest length" of a physical object; it is the distance between two independently programmed trajectories. To find the distance in the rockets' frame, one must apply the inverse Lorentz transformation (or the length contraction formula in reverse), which increases the distance. The string is a physical object; its rest length is $100$ m, but the distance it is stretched across is $166.67$ m.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{gamma\_factor} &= 1.66666666667 \\
\mathrm{lab\_separation\_m} &= 100 \\
\mathrm{proper\_separation\_m} &= 166.666666667
\end{aligned}
\]