"""Compatibility wrapper around the canonical BoundaryHorizonSystem implementation."""

try:
    from .boundary_horizon_framework import BoundaryHorizonSystem
except ImportError:  # pragma: no cover
    from boundary_horizon_framework import BoundaryHorizonSystem

__all__ = ["BoundaryHorizonSystem"]
