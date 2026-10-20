# Refraction & Medium-Transition Mechanics via the Boundary-Horizon Framework

> **Document Class:** Applied Theoretical Framework & Wave Dynamics
>
> **Authors:** `{Jeremey James Grice Rosa}` $\land$ `{Christopher Thomas Ronio}`
>
> **Framework Version:** 1.0.0
>
> **Certification Index:** `888.2026.RR.REFR`

## 1. Executive Summary

Refraction—traditionally described as the bending of a wave as it passes from one medium to another due to a change in speed—is recontextualized under the **Boundary-Horizon Framework** as a **boundary-mediated phase velocity transformation and trajectory delta**.

While reflection occurs when energy is rejected by an impermeable boundary constraint, **refraction represents boundary transmission across an impedance gradient**. The finite observable trajectory change ($N$) emerges from the differential constraint imposed by the dielectric or refractive properties ($\Omega_{in}$) of the local medium relative to the broader wave domain ($\Omega_{out}$).

$$
\Omega_{out}(\text{Incident Wave Domain}) - \Omega_{in}(\text{Medium Index Constraint}) = \mathcal{H}(\text{Refracted Trajectory Delta}) = N(\text{Index: 888.2026.RR.REFR})
$$

## 2. System Mapping for Refraction Dynamics

The wave and dielectric parameters of refraction map directly to the core framework entities:

* **`{Outside_Boundary}` (**$\Omega_{out}$**):** The incident wave domain, phase velocity in the initial medium ($v_1$), or broader unconstrained signal trajectory.

* **`{Inside_Boundary}` (**$\Omega_{in}$**):** The localized boundary constraint defined by the refractive index ($n_2$) or dielectric permittivity ($\epsilon_2$) of the target medium.

* **`{Horizon}` (**$\mathcal{H}$**):** The angular deviation delta ($\Delta\theta$), phase velocity shift, or phase front bending across the interface boundary.

* **`{Finite_Number}` (**$N$**):** The observable angle of refraction ($\theta_2$), wavelength compression factor ($\lambda_2$), or focused beam path.

* **`{Infinity}` (**$\infty$**):** Unbounded, straight-line wave propagation through a perfectly homogenous, isotropic void.

## 3. Mathematical Formalism & Snell's Law Integration

Applying the framework's meta-principle—*finite observable structure as a function of the boundary between a system's local constraints and the broader domain containing it*:

$$
\Omega_{out}(\text{Incident Waveform}) - \Omega_{in}(\text{Medium Boundary Constraint}) = \mathcal{H}(\text{Refracted Trajectory}) = N
$$

### 3.1 Snell's Law as a Horizon Equilibrium

Snell's Law ($\frac{\sin \theta_1}{\sin \theta_2} = \frac{n_2}{n_1} = \frac{v_1}{v_2}$) maps directly into the framework as the conservation of phase continuity across the boundary interface:

$$
\mathcal{H}_{refr} = \Omega_{out}(v_1 \sin \theta_1) - \Omega_{in}(v_2 \sin \theta_2) = 0 \quad \text{(At Horizon Equilibrium)}
$$

Solving for the finite observable refracted angle $\theta_2$:

$$
\theta_2 = \arcsin\left( \frac{\Omega_{out}(n_1)}{\Omega_{in}(n_2)} \cdot \sin(\theta_1) \right)
$$

### 3.2 Total Internal Reflection as Boundary Saturation ($\mathcal{H} \to \text{Max}$)

When the incident angle exceeds the critical angle ($\theta_1 > \theta_c$), the local medium constraint ($\Omega_{in}$) can no longer support phase transmission across the boundary interface. The horizon delta reaches its boundary capacity ($\mathcal{H} \to \text{Max}$), collapsing the transmitted refracted wave and converting 100% of the signal energy into the reflected domain ($\mathcal{H}_{refl}$, Index: `888.2026.RR.REFL`).

## 4. Algorithmic Implementation (`src/refraction_simulation.py`)

Below is a Python implementation modeling wave trajectory bending and phase velocity adjustment across medium boundaries:

```python
import numpy as np

class RefractionHorizonModel:
    """Models wave refraction, phase velocity shifts, and medium boundary interactions."""
    
    def __init__(self, n1: float, n2: float):
        self.omega_out_medium = float(n1)  # Refractive index of initial medium (\Omega_{out})
        self.omega_in_medium = float(n2)   # Refractive index of target medium (\Omega_{in})
        
    def compute_refracted_horizon(self, incident_angle_deg: float) -> dict:
        """Calculates the refracted trajectory angle and horizon phase delta."""
        theta1 = np.radians(incident_angle_deg)
        
        # Calculate sine of refracted angle using Snell's horizon relation
        sin_theta2 = (self.omega_out_medium / self.omega_in_medium) * np.sin(theta1)
        
        # Check for Total Internal Reflection (Boundary Saturation)
        if np.abs(sin_theta2) > 1.0:
            return {
                "status": "Total Internal Reflection (Boundary Saturation)",
                "refracted_angle_deg": None,
                "horizon_delta": "Collapsed to Reflected Projection (888.2026.RR.REFL)"
            }
            
        theta2 = np.arcsin(sin_theta2)
        horizon_delta_rad = theta1 - theta2
        
        return {
            "status": "Transmitted & Refracted",
            "refracted_angle_deg": float(np.degrees(theta2)),
            "horizon_delta_deg": float(np.degrees(horizon_delta_rad)),
            "certification_index": "888.2026.RR.REFR"
        }
```

## 5. Algorithmic Certification

$$
\Omega_{out} (\text{Incident Waveform}) - \Omega_{in} (\text{Refractive Medium Boundary}) = \mathcal{H} (\text{Refracted Trajectory}) = N (\text{Index: 888.2026.RR.REFR})
$$

$$
\text{Certification Status: Validated Relative to } \infty
$$