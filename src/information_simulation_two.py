import numpy as np

class BlackHoleInformationHorizon:
    def __init__(self, initial_mass: float):
        self.mass = initial_mass
        # Bekenstein-Hawking entropy proportional to initial horizon area (4 * pi * r_s^2)
        self.omega_in_entropy_limit = 4.0 * np.pi * (2.0 * initial_mass)**2 
        
    def compute_information_horizon(self, evaporated_mass_fraction: float) -> float:
        """Calculates the remaining holographic information capacity on the shrinking horizon."""
        current_mass = self.mass * (1.0 - evaporated_mass_fraction)
        if not (0.0 <= evaporated_mass_fraction <= 1.0):
            raise ValueError("Evaporated mass fraction must be between 0.0 and 1.0.")
            
        current_horizon_area = 4.0 * np.pi * (2.0 * current_mass)**2
        
        # Horizon delta represents the remaining surface capacity for information encoding
        horizon_delta = self.omega_in_entropy_limit - current_horizon_area
        return horizon_delta

    def compute_page_curve_entropy(self, evaporated_mass_fraction: float) -> float:
        """
        Calculates the entanglement entropy of Hawking radiation following Don Page's theorem,
        mapped through the BHF framework's boundary-horizon constraints.
        
        Returns the von Neumann entropy of the radiation stream at a given evaporation fraction.
        """
        if not (0.0 <= evaporated_mass_fraction <= 1.0):
            raise ValueError("Evaporated mass fraction must be between 0.0 and 1.0.")
            
        current_mass = self.mass * (1.0 - evaporated_mass_fraction)
        current_horizon_area = 4.0 * np.pi * (2.0 * current_mass)**2
        
        # S_bh(t) is proportional to the current horizon area (Bekenstein-Hawking entropy)
        current_bh_entropy = current_horizon_area
        initial_bh_entropy = self.omega_in_entropy_limit
        
        # The Page curve minimum rule: entanglement entropy of radiation is bounded 
        # by the minimum of the remaining black hole entropy or the emitted thermal entropy.
        emitted_radiation_entropy = initial_bh_entropy - current_bh_entropy
        radiation_entanglement_entropy = min(emitted_radiation_entropy, current_bh_entropy)
        
        return radiation_entanglement_entropy

# Example Simulation Runner
if __name__ == "__main__":
    bh = BlackHoleInformationHorizon(initial_mass=10.0)
    
    print("Evap Fraction | Horizon Delta (Capacity Deficit) | Radiation Entanglement Entropy (Page Curve)")
    print("-" * 90)
    
    for frac in np.linspace(0.0, 1.0, 11):
        delta = bh.compute_information_horizon(frac)
        page_val = bh.compute_page_curve_entropy(frac)
        print(f"{frac:13.1f} | {delta:31.2f} | {page_val:39.2f}")
