"""Backward-compatible alias for the canonical BoundaryHorizonSystem."""

try:
    from .boundary_horizon_framework import BoundaryHorizonSystem
except ImportError:  # pragma: no cover
    from boundary_horizon_framework import BoundaryHorizonSystem

__all__ = ["BoundaryHorizonSystem"]
