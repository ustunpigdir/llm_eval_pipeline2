## Step 1: State the GR perihelion advance per orbit in closed form
The first-order general-relativistic perihelion advance per orbit is given by the formula:

$$\Delta\phi = \frac{6\pi GM_\odot}{c^2 a(1-e^2)}$$

where $GM_\odot$ is the gravitational constant times the mass of the Sun, $a$ is the semi-major axis of the orbit, $e$ is the eccentricity of the orbit, and $c$ is the speed of light.

## Step 2: Evaluate the GR perihelion advance per orbit in arcseconds
We need to plug in the given values into the formula:

$$\Delta\phi = \frac{6\pi \times 1.32712 \times 10^{20} \, \mathrm{m}^3/\mathrm{s}^2}{(3 \times 10^8 \, \mathrm{m}/\mathrm{s})^2 \times 5.7909 \times 10^{10} \, \mathrm{m} \times (1-0.2056^2)}$$

First, calculate the denominator:

$$(3 \times 10^8 \, \mathrm{m}/\mathrm{s})^2 \times 5.7909 \times 10^{10} \, \mathrm{m} \times (1-0.2056^2) = 8.8704 \times 10^{20} \, \mathrm{m}^2/\mathrm{s}^2$$

Now, plug this value into the formula:

$$\Delta\phi = \frac{6\pi \times 1.32712 \times 10^{20} \, \mathrm{m}^3/\mathrm{s}^2}{8.8704 \times 10^{20} \, \mathrm{m}^2/\mathrm{s}^2} = 0.0468$$

Since we want the result in arcseconds, we need to convert the result from radians to arcseconds. There are $1/(2\pi)$ radians in an arcsecond, so:

$$\Delta\phi = 0.0468 \times \frac{1}{2\pi} \, \mathrm{rad} \times \frac{3600 \, \mathrm{s}}{1 \, \mathrm{h}} \times \frac{24 \, \mathrm{h}}{1 \, \mathrm{d}} \times \frac{1 \, \mathrm{d}}{87.969 \, \mathrm{d}} \times \frac{3600 \, \mathrm{s}}{1 \, \mathrm{h}} \times \frac{1 \, \mathrm{h}}{60 \, \mathrm{min}} \times \frac{1 \, \mathrm{min}}{60 \, \mathrm{s}} \times \frac{1 \, \mathrm{rad}}{206265 \, \mathrm{arcsec}} = 42.98 \, \mathrm{arcsec}$$

## Step 3: Convert the GR perihelion advance per orbit to arcseconds per century
To convert the result to arcseconds per century, we need to multiply by the number of orbits per century:

$$\mathrm{orbits\_per\_century} = \frac{1 \, \mathrm{century}}{87.969 \, \mathrm{d}} \times \frac{1 \, \mathrm{d}}{1 \, \mathrm{orbit}} = 11.37$$

Now, multiply the result by the number of orbits per century:

$$\mathrm{advance\_arcsec\_century} = 42.98 \, \mathrm{arcsec/orbit} \times 11.37 \, \mathrm{orbits/century} = 488.3 \, \mathrm{arcsec/century}$$

## Step 4: Explain the remainder of the observed precession
The observed precession is about 574 arcseconds per century, and the general-relativistic perihelion advance is about 488 arcseconds per century. The remainder is due to other effects, such as the oblateness of the Sun and the effects of the other planets in the solar system.

## Step 5: State the final answer
The final answer is:

$$
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 42.98 \\
\mathrm{advance\_arcsec\_century} &= 488.3 \\
\mathrm{orbits\_per\_century} &= 11.37
\end{aligned}
$$

FINAL ANSWER
\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 42.98 \\
\mathrm{advance\_arcsec\_century} &= 488.3 \\
\mathrm{orbits\_per\_century} &= 11.37
\end{aligned}
\]