# Boundary–Horizon–Finitude (BHF) Framework

Authors: Christopher Thomas Ronio and Jeremy James Grice-Rosa

Status: Proposed mathematical framework  
Version: 0.1.0

A mathematical framework for exploring informational boundaries, finite representation, distinguishability, and infinity.

## Overview

The Boundary–Horizon–Finitude (BHF) Framework is a conceptual formalism for modeling systems through the relationship between an outer boundary and an inner boundary. It emphasizes the observable residual structure that remains after subtracting the internal constrained domain from the maximal domain available to a system.

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

## Motivation

Many paradoxes and apparent singularities arise when a system is analyzed without distinguishing between:

1. the broader ambient domain in which it is embedded, and
2. the internal operational domain that actually constrains its local behavior.

The BHF Framework proposes that finite observable structure can be represented by explicitly separating these domains and measuring the residual difference between them.

## Core Concept

Let:

- `Ω_out` = outer boundary, the maximal admissible or ambient extent
- `Ω_in` = inner boundary, the effective or locally constrained extent

Then the boundary horizon is defined as:

```math
\mathcal{H} = \Omega_{out} - \Omega_{in}
```

The framework studies cases where:

- the horizon is finite and interpretable,
- the system remains bounded and well-defined,
- boundary collapse occurs when `Ω_in -> Ω_out`, giving `H -> 0`,
- the difference between interior and exterior constraints carries important structural meaning.

## Repository Structure

```text
Boundary-Horizon-Finite-Framework/
├── README.md                           # Project overview and usage
├── LICENSE                             # Repository license
├── boundary_horizon_framework.md       # Main theoretical manuscript
├── docs/                               # Supplemental documents and applications
│   ├── boundary-horizon-mathematical-framework.md
│   ├── mathematical_proofs.md
│   ├── protein_folding_structural_proteomics.md
│   ├── dna_3d_mapping_chromatin_architecture.md
│   ├── rna_mapping.md
│   ├── relativity_mapping.md
│   └── set_theory_paradoxes_solutions.md
├── src/                                # Python examples and simulations
│   ├── boundary-horizon-framework.py
│   ├── simulation.py
│   └── protein_folding.py
└── .gitignore
```

## Installation

This repository is Python-based and can be used directly from a local checkout.

```bash
git clone https://github.com/yaoming-dynasty/Boundary-Horizon-Finite-Framework.git
cd Boundary-Horizon-Finite-Framework
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or .venv\Scripts\activate  # Windows
```

No additional dependencies are required for the core examples, though some files may optionally use `numpy`.

## Quick Start

The core idea can be demonstrated directly with the Python implementation in `src/`.

```python
from src.boundary_horizon_framework import BoundaryHorizonSystem

system = BoundaryHorizonSystem(outside_boundary=10.0, inside_boundary=4.0)
print(system.compute_horizon())
# Output: 6.0
```

If the Python file is named with a hyphen (`boundary-horizon-framework.py`), use a module import pattern appropriate for your environment or copy the class into a working script.

## Example Usage

```python
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
```

This reflects the framework's key property of translation invariance:

```math
(\Omega_{out} + k) - (\Omega_{in} + k) = \Omega_{out} - \Omega_{in}
```

## Scope and Intended Use

This repository is not presented as a complete verified formal system or peer-reviewed theory. Rather, it is a proposed conceptual and mathematical architecture for:

- reasoning about finite residual structure,
- interpreting paradoxes through boundary separation,
- modeling bounded systems and approximation processes,
- creating a common language for finite representation across disciplines.

The framework is intended to be read as a boundary-centric interpretive model, not as a replacement for established mathematical foundations.

## Applications Included in This Repository

The documentation explores several areas where the framework may be useful, including:

- logic and paradox analysis
- set-theoretic boundary constraints
- mathematical proofs and formal reductions
- physics and relativity-inspired mappings
- DNA/RNA structural and chromatin architecture analysis
- protein folding and structural proteomics

## Related Documents

The most important documents in the repo are:

- `boundary_horizon_framework.md` — the core manuscript
- `docs/boundary-horizon-mathematical-framework.md` — supporting mathematical framing
- `docs/mathematical_proofs.md` — proof-oriented notes
- `docs/set_theory_paradoxes_solutions.md` — paradox classification and resolution examples

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome. Suggestions, corrections, and additional application notes are encouraged. If you are extending the framework, please preserve the conceptual distinction between:

- local constrained domains,
- outer ambient domains,
- residual finite horizons.

## References

The repository references ideas from:

- Russell, B. (1901)
- Tarski, A. (1936)
- Barwise & Etchemendy
- Zeno of Elea
- Hofstadter

## Summary

This repository presents a research-oriented framework for understanding finite observable structure as a function of the boundary between a system's local constraints and the broader domain that contains it. The framework is intentionally simple in form but broad in conceptual scope.

If you are exploring finite systems, paradox resolution, or bounded approximation, this project is best viewed as a conceptual toolkit and mathematical essay rather than a conventional software library.
