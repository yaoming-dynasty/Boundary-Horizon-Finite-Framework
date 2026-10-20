class BoundaryHorizonSystem:
    def __init__(self, outside_boundary: float, inside_boundary: float):
        self.omega_out = outside_boundary
        self.omega_in = inside_boundary

    def compute_horizon(self) -> float:
        """Calculates the finite horizon N from differential boundaries."""
        if self.omega_in > self.omega_out:
            raise ValueError("Inside boundary cannot exceed outside boundary.")
        return self.omega_out - self.omega_in

    def scale_relative_to_infinity(self, infinity_scale: float) -> float:
        """Evaluates the proportional weight of N relative to background infinity."""
        horizon = self.compute_horizon()
        if infinity_scale == 0:
            return float('inf')
        return horizon / infinity_scale
