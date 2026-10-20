class BoundaryHorizonSystem:
    def __init__(self, outside_boundary: float, inside_boundary: float):
        if inside_boundary > outside_boundary:
            raise ValueError("Inside boundary cannot exceed outside boundary.")
        self.omega_out = float(outside_boundary)
        self.omega_in = float(inside_boundary)

    def compute_horizon(self) -> float:
        return self.omega_out - self.omega_in

    def apply_translation(self, k: float) -> float:
        return (self.omega_out + k) - (self.omega_in + k)
