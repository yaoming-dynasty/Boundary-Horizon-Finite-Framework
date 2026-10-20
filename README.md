# Boundary–Horizon–Finitude (BHF) Framework

Authors: Christopher Thomas Ronio and Jeremy James Grice-Rosa

Status: Proposed mathematical framework
Version: 0.1.0

A mathematical framework for exploring informational boundaries, finite representation, distinguishability, and infinity.

## Overview

The Boundary–Horizon–Finitude (BHF) Framework is a conceptual formalism for modeling systems through the relationship between an outer boundary and an inner boundary. It emphasizes the observable residual between constrained local behavior and the broader ambient domain.

At the center of the framework is the boundary-horizon operator:

```math
\mathcal{B}(\Omega_{out}, \Omega_{in}) = \Omega_{out} - \Omega_{in}
```

This quantity is interpreted as the finite horizon or residual differential between the broader domain and the locally constrained domain. The framework is intended for reasoning about:

- finite representability
- bounded recursion
- paradox resolution
- distinguishability and structure in finite systems
- approximation of unbounded or asymptotic behavior

## Quick Start

The canonical implementation lives in `src/boundary_horizon_framework.py`.

```python
from src.boundary_horizon_framework import BoundaryHorizonSystem

system = BoundaryHorizonSystem(outside_boundary=10.0, inside_boundary=4.0)
print(system.compute_horizon())
# Output: 6.0
```

The class also supports boundary translation invariance and relative scaling:

```python
system = BoundaryHorizonSystem(outside_boundary=10.0, inside_boundary=4.0)
print(system.apply_translation(2.0))
print(system.scale_relative_to_infinity(2.0))
```

## Repository Structure

```text
Boundary-Horizon-Finite-Framework/
├── README.md                           # Project overview and usage
├── LICENSE                             # Repository license
├── boundary_horizon_framework.md       # Main theoretical manuscript
├── docs/                               # Supplemental documents and applications
├── src/                                # Python examples and simulations
│   ├── __init__.py
│   ├── boundary_horizon_framework.py   # Canonical model implementation
│   ├── boundary-horizon-framework.py   # Backward compatibility wrapper
│   ├── simulation.py                  # Compatibility wrapper
│   └── dynamic_horizon_simulation.py
└── .gitignore
```
