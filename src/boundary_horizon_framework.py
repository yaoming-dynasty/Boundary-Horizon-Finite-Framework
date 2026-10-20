"""Canonical implementation of the Boundary–Horizon–Finitude model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BoundaryHorizonSystem:
    """Representation of the finite residual between outer and inner boundaries."""

    outside_boundary: float
    inside_boundary: float

    def __post_init__(self) -> None:
        self.omega_out = float(self.outside_boundary)
        self.omega_in = float(self.inside_boundary)

        if self.omega_in > self.omega_out:
            raise ValueError("Inside boundary cannot exceed outside boundary.")

    def compute_horizon(self) -> float:
        """Calculates the finite horizon N from differential boundaries."""
        return self.omega_out - self.omega_in

    def apply_translation(self, k: float) -> float:
        """Translation invariance of the residual boundary horizon."""
        return (self.omega_out + k) - (self.omega_in + k)

    def scale_relative_to_infinity(self, infinity_scale: float) -> float:
        """Evaluate the proportional weight of N relative to background infinity."""
        horizon = self.compute_horizon()
        if infinity_scale == 0:
            return float("inf")
        return horizon / infinity_scale


__all__ = ["BoundaryHorizonSystem"]
