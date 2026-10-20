# Relativity Mapping: Boundary-Horizon Framework
**Authors:** `{Jeremey James Grice Rosa}` $\land$ `{Christopher Thomas Ronio}`  
**Framework Version:** 1.0.0  

---

## 1. Overview

Integrating Einstein’s theory of relativity with the **Boundary-Horizon Framework** provides a powerful mathematical lens for understanding how physical spacetime intervals, event horizons, and cosmological limits emerge as finite deltas relative to an infinite background. 

---

## 2. Special Relativity: The Light Cone as a Bounded Velocity Horizon

### Core Concept
In Special Relativity, the speed of light in a vacuum ($c$) acts as an absolute invariant speed limit, bounding all causal interactions. 

### Framework Mapping
*   **$\Omega_{out}$ (Outside Boundary):** The absolute asymptotic speed limit of the universe ($c$).
*   **$\Omega_{in}$ (Inside Boundary):** The sub-luminal velocity ($v$) of a massive reference frame or observer ($0 \le v < c$).
*   **$\mathcal{H}$ (Horizon):** The differential kinematic capacity or available velocity delta remaining before reaching the speed-of-light boundary:
    $$\mathcal{H}_v = c - v$$
*   **$N$ (Finite Number / Lorentz Factor Scaling):** The resulting finite metric scaling factor that dictates time dilation and length contraction properties.

### Mathematical Formulation
Expressing the temporal dilation factor ($\gamma$) through the boundary-horizon lens:

$$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$$

Substituting the inner boundary interaction where $v = c - \mathcal{H}_v$:
$$\gamma = \frac{1}{\sqrt{1 - \frac{(c - \mathcal{H}_v)^2}{c^2}}}$$

As the horizon delta $\mathcal{H}_v \to 0$ (velocity approaches the speed of light), the finite relativistic scaling factor $N$ approaches infinity, demonstrating how local finite systems scale dynamically as they press against the outer invariant boundary ($\Omega_{out} = c$).

---

## 3. General Relativity: Gravitational and Cosmological Horizons

### Core Concept
General Relativity describes gravity not as a force, but as the curvature of spacetime induced by mass-energy. Spacetime is bounded by local event horizons (black holes) and global cosmological horizons (de Sitter space).

### Framework Mapping
*   **$\Omega_{out}$ (Outside Boundary):** The global cosmological horizon or spatial asymptotic infinity ($\infty$) of the universe.
*   **$\Omega_{in}$ (Inside Boundary):** The local gravitational boundary, such as the Schwarzschild radius ($r_s$) of a mass:
    $$r_s = \frac{2GM}{c^2}$$
*   **$\mathcal{H}$ (Horizon):** The observable, localized metric proper distance available to an external observer:
    $$\mathcal{H}_{metric} = \Omega_{out} - r_s = N$$

### Singularity Resolution
Under Theorem 2 of the framework (Singularity Avoidance via Resolution Limits):
$$\lim_{r_s \to \Omega_{out}} (\Omega_{out} - r_s) = 0$$

When a local mass boundary expands to encompass the total outer system boundary, the horizon collapses cleanly to $0$, avoiding indeterminate anomalies and treating the gravitational boundary as a controlled differential scale rather than a mathematical break in the fabric of space.
