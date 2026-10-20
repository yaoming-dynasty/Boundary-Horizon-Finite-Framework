"""
Refraction Simulation Module - Boundary-Horizon Framework
Authors: Jeremey James Grice Rosa & Christopher Thomas Ronio
Framework Version: 1.0.0
Domain Code: 888.2026.RR.REFR.PY
"""

import numpy as np

class RefractionHorizon:
    def __init__(self, n1: float, n2: float):
        """
        Initialize the Refraction Horizon interface.
        
        Parameters:
        -----------
        n1 : float
            Refractive index of the origin medium (Omega_out domain).
        n2 : float
            Refractive index of the boundary medium (Omega_in domain).
        """
        if n1 <= 0 or n2 <= 0:
            raise ValueError("Refractive indices must be strictly positive.")
        self.n1 = n1
        self.n2 = n2
        self.eta = n1 / n2  # Relative phase velocity constraint ratio
        self.critical_angle_rad = np.arcsin(n2 / n1) if n1 > n2 else None

    def compute_refracted_vector(self, incident_vector: np.ndarray, normal_vector: np.ndarray = np.array([0.0, 0.0, 1.0])) -> dict:
        """
        Computes the refracted ray vector, transmission angle, and phase velocity delta.
        
        Parameters:
        -----------
        incident_vector : np.ndarray
            Incoming ray direction vector (unnormalized or normalized).
        normal_vector : np.ndarray
            Surface normal vector pointing into the origin medium (n1). Default is [0, 0, 1].
            
        Returns:
        --------
        dict
            Contains refracted_vector, angle_incidence, angle_refraction, is_total_internal_reflection, and horizon_delta.
        """
        # Normalize vectors
        i_unit = incident_vector / np.linalg.norm(incident_vector)
        n_unit = normal_vector / np.linalg.norm(normal_vector)

        # Angle of incidence (cos theta_1)
        cos_theta1 = np.clip(np.dot(-i_unit, n_unit), -1.0, 1.0)
        theta1 = np.arccos(cos_theta1)

        # Evaluate Total Internal Reflection condition under Snell's Horizon
        sin2_theta2 = (self.eta ** 2) * (1.0 - cos_theta1 ** 2)

        if sin2_theta2 > 1.0:
            # Total Internal Reflection: Horizon saturates, refraction collapses
            return {
                "refracted_vector": None,
                "angle_incidence_deg": np.degrees(theta1),
                "angle_refraction_deg": None,
                "is_total_internal_reflection": True,
                "horizon_delta": 0.0,
                "description": "Total Internal Reflection: Evanescent wave limit reached."
            }

        cos_theta2 = np.sqrt(1.0 - sin2_theta2)
        theta2 = np.arccos(cos_theta2)

        # Refracted direction vector via vector Snell's Law
        refracted_dir = self.eta * i_unit + (self.eta * cos_theta1 - cos_theta2) * n_unit
        refracted_dir = refracted_dir / np.linalg.norm(refracted_dir)

        # Compute finite structural horizon delta (phase velocity shift: v1 - v2)
        v1 = 1.0 / self.n1
        v2 = 1.0 / self.n2
        horizon_delta = v1 - v2

        return {
            "refracted_vector": refracted_dir,
            "angle_incidence_deg": np.degrees(theta1),
            "angle_refraction_deg": np.degrees(theta2),
            "is_total_internal_reflection": False,
            "horizon_delta": horizon_delta,
            "description": "Refraction successful: Energy transmitted across medium boundary."
        }

if __name__ == "__main__":
    print("=== Refraction Horizon Simulation ===")
    
    # Example 1: Air (n1 = 1.0) to Glass (n2 = 1.5)
    sim_glass = RefractionHorizon(n1=1.0, n2=1.5)
    incident_ray = np.array([1.0, 0.0, -1.0])  # 45-degree angle
    result = sim_glass.compute_refracted_vector(incident_ray)
    print("\nCase 1: Air -> Glass (n1=1.0, n2=1.5)")
    print(f"Incident Angle: {result['angle_incidence_deg']:.2f}°")
    print(f"Refracted Angle: {result['angle_refraction_deg']:.2f}°")
    print(f"Refracted Vector: {result['refracted_vector']}")
    print(f"Horizon Delta (Velocity Shift): {result['horizon_delta']:.4f}")

    # Example 2: Water (n1 = 1.333) to Air (n2 = 1.0) with TIR test
    sim_water = RefractionHorizon(n1=1.333, n2=1.0)
    steep_ray = np.array([2.0, 0.0, -1.0])  # ~63.4-degree angle (exceeds critical angle ~48.6°)
    result_tir = sim_water.compute_refracted_vector(steep_ray)
    print("\nCase 2: Water -> Air (n1=1.333, n2=1.0) - High Angle")
    print(f"Incident Angle: {result_tir['angle_incidence_deg']:.2f}°")
    print(f"Total Internal Reflection: {result_tir['is_total_internal_reflection']}")
    print(f"Description: {result_tir['description']}")
