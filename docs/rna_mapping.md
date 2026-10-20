# RNA Mapping and Transcriptomic Architecture: Boundary-Horizon Framework
**Authors:** `{Jeremey James Grice Rosa}` $\land$ `{Christopher Thomas Ronio}`  
**Framework Version:** 1.0.0  

---

## 1. Overview

RNA mapping encompasses both secondary/tertiary structural folding (such as base-pairing interactions, stem-loops, and pseudoknots) and spatial transcriptomics (tracking where transcripts localize within the cellular cytoplasm or nucleus). By applying the **Boundary-Horizon Framework**, we can model RNA conformation and cellular localization as finite structural and spatial deltas extracted from an infinite combinatorial sequence and conformational space.

---

## 2. System Mapping for RNA Architecture

To analyze RNA molecules through this lens, we define the foundational entities of the framework:

*   **`{Outside_Boundary}` ($\Omega_{out}$):** The maximum conformational sequence limit, total cellular volume boundary, or cytoplasmic envelope.
*   **`{Inside_Boundary}` ($\Omega_{in}$):** The primary nucleotide sequence length, foundational template, or transcription initiation anchor point.
*   **`{Horizon}` ($\mathcal{H}$):** The measurable free energy folding delta, base-pairing distance constraint, or spatial localization vector.
*   **`{Finite_Number}` ($N$):** The resulting stable secondary structure index, spatial coordinate, or molecule localization count.
*   **`{Infinity}` ($\infty$):** The infinite landscape of potential untranslated RNA conformations and combinatorial sequence permutations.

---

## 3. Mathematical Formulation for RNA Folding and Localization

### A. Secondary Structure Folding Mechanics
RNA folding is driven by thermodynamic stability, where a single-stranded sequence collapses into stable secondary structures (hairpins, loops) to minimize free energy.

Let the total thermodynamic state space of a sequence be bounded by $\Omega_{out}$, and the rigid primary sequence constraints be $\Omega_{in}$. The resulting stable folded structural horizon is:

$$\Omega_{out}(\text{Conformational Space}) - \Omega_{in}(\text{Primary Sequence}) = \mathcal{H}(\text{Folding Delta}) = N(\text{Secondary Structure Index})$$

As the folding constraints tighten ($\Omega_{in} \to \Omega_{out}$), the structural horizon approaches zero ($\mathcal{H} \to 0$), reflecting a fully bound, rigid conformation with no remaining unconstrained degrees of freedom (Theorem 2: Singularity Avoidance via Resolution Limits).

### B. Spatial Transcriptomics and Subcellular Localization
In spatial transcriptomics, individual RNA transcripts are mapped to precise coordinates $(x, y, z)$ within a cell. 

Let the plasma membrane boundary define $\Omega_{out}$, and the specific intracellular localization site (e.g., synapse, endoplasmic reticulum) define $\Omega_{in}$. The spatial tracking horizon is:

$$\mathcal{H}_{spatial} = \Omega_{out}(\text{Cellular Boundary}) - \Omega_{in}(\text{Transcription Site}) = N(\text{Coordinate Vector})$$

---

## 4. RNA Shape Dynamics & Conformational Topology

RNA molecules fold into intricate three-dimensional shapes that dictate their biological function—acting not just as linear informational messengers, but as catalytic agents, structural scaffolds, and molecular switches. 

### A. Local Structural Motifs as Horizons
RNA folding occurs hierarchically, beginning with local base-pairing that forms distinct architectural motifs:
*   **Hairpins & Stem-Loops (`{Horizon}`):** Formed when complementary bases within a single strand fold back on themselves. $\Omega_{out}$ is the total sequence length; $\Omega_{in}$ is the anchored loop region. The stem length forms the finite horizon $\mathcal{H}$.
*   **Internal Loops & Bulges:** Asymmetries in base-pairing that create localized bends or recognition pockets in the RNA backbone.
*   **Pseudoknots:** Formed when nucleotides in a loop base-pair with a site outside the loop, creating tangled, high-order tertiary conformations where multiple $\mathcal{H}$ vectors intersect.

### B. Dynamic Boundary Shifts in Riboswitches
Certain RNA molecules (riboswitches) change shape dynamically in response to cellular signals or ligand binding:

$$\Omega_{out}(\text{Ligand Unbound State}) \longrightarrow \Omega_{in}(\text{Ligand Bound State}) = \Delta \mathcal{H}(\text{Conformational Switch})$$

When a target metabolite binds to the RNA aptamer domain, it shifts internal energy constraints ($\Omega_{in}$), forcing the RNA to snap into an alternative secondary structure. This demonstrates **dynamic boundary mechanics**, where the finite structural index ($N$) shifts instantly to regulate gene expression.

### C. Tertiary Macromolecular Architecture
Complex functional RNAs like transfer RNA (tRNA) or ribosomal RNA fold into tight, compact 3D tertiary shapes stabilized by coaxial stacking and hydrogen bonding:
*   **The Horizon ($\mathcal{H}$):** The precise spatial coordinates of the folded macromolecule within the cell.
*   **The Infinite Background ($\infty$):** The astronomical number of alternative denatured configurations the RNA could have adopted.

---

## 5. Computational Extension (`rna_simulation.py`)

Below is a Python simulation skeleton modeling RNA spatial localization and structural boundary constraints within the framework:

```python
import numpy as np

class RNALocalizationHorizon:
    def __init__(self, cell_boundary_radius: float, transcription_site: np.ndarray):
        self.omega_out = cell_boundary_radius  # Plasma membrane limit
        self.omega_in = transcription_site       # Origin site in the nucleus
        
    def compute_transport_horizon(self, current_rna_position: np.ndarray) -> float:
        """Calculates the finite spatial migration horizon of an RNA transcript."""
        current_distance = np.linalg.norm(current_rna_position)
        if current_distance > self.omega_out:
            raise ValueError("RNA position exceeds cellular boundary limits.")
        
        # Horizon represents the remaining translocatable distance to the outer boundary
        horizon = self.omega_out - current_distance
        return horizon
