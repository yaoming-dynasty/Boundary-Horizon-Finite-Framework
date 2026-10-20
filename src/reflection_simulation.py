import numpy as np

class ReflectionHorizon:
    def __init__(self, surface_impedance: float):
        self.omega_in_constraint = surface_impedance  # Boundary resistance/reflectivity index
        
    def compute_reflected_horizon(self, incident_vector: np.ndarray) -> np.ndarray:
        """Calculates the reflected vector and phase delta across a boundary interface."""
        amplitude = np.linalg.norm(incident_vector)
        if amplitude == 0:
            return np.zeros_like(incident_vector)
            
        # Standard specular reflection simulation along a normalized boundary normal
        normal = np.array([0.0, 0.0, 1.0]) # Assuming z-axis interface boundary
        reflected_vector = incident_vector - 2.0 * np.dot(incident_vector, normal) * normal
        
        # Scale by boundary constraint efficiency (reflectivity coefficient)
        reflected_horizon = reflected_vector * (self.omega_in_constraint / (1.0 + self.omega_in_constraint))
        return reflected_horizon
