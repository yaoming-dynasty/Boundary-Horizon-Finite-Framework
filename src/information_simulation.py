import numpy as np

class BlackHoleInformationHorizon:
    def __init__(self, initial_mass: float):
        self.mass = initial_mass
        # Bekenstein-Hawking entropy proportional to horizon area (4 * pi * r_s^2)
        self.omega_in_entropy_limit = 4.0 * np.pi * (2.0 * initial_mass)**2 
        
    def compute_information_horizon(self, evaporated_mass_fraction: float) -> float:
        """Calculates the remaining holographic information capacity on the shrinking horizon."""
        current_mass = self.mass * (1.0 - evaporated_mass_fraction)
        if current_mass < 0:
            raise ValueError("Evaporated mass fraction cannot exceed 100%.")
            
        current_horizon_area = 4.0 * np.pi * (2.0 * current_mass)**2
        
        # Horizon delta represents the remaining surface capacity for information encoding
        horizon_delta = self.omega_in_entropy_limit - current_horizon_area
        return horizon_delta
