"""
Dynamic Horizon Simulation Module - Boundary-Horizon Framework
Authors: Jeremey James Grice Rosa & Christopher Thomas Ronio
Framework Version: 1.0.0
Domain Code: 888.2026.RR.DYN.PY
"""

import numpy as np

class DynamicHorizonSimulation:
    def __init__(self, omega_out_initial: float, omega_in_rate: float, steps: int = 50):
        """
        Initializes a dynamic boundary-horizon simulation where constraints evolve over time.
        
        Parameters:
        -----------
        omega_out_initial : float
            Initial capacity of the outer unbounded domain.
        omega_in_rate : float
            Rate at which local boundary constraints expand or contract.
        steps : int
            Number of temporal simulation steps.
        """
        self.omega_out_initial = omega_out_initial
        self.omega_in_rate = omega_in_rate
        self.steps = steps

    def run_simulation(self) -> dict:
        """
        Runs the time-evolution loop of the boundary-horizon equation:
        H(t) = Omega_out(t) - Omega_in(t) = N(t)
        """
        time_steps = np.linspace(0, 10, self.steps)
        omega_out_vals = self.omega_out_initial * np.ones_like(time_steps)
        
        # Omega_in evolves dynamically (e.g., oscillating constraint boundary)
        omega_in_vals = self.omega_in_profile(time_steps)
        
        # Core equation evaluation across time
        horizon_deltas = omega_out_vals - omega_in_vals
        observable_states = np.maximum(0, horizon_deltas)  # Ensure non-negative observable bits/structure

        return {
            "time": time_steps,
            "omega_out": omega_out_vals,
            "omega_in": omega_in_vals,
            "horizon_delta": horizon_deltas,
            "observable_state_N": observable_states
        }

    def omega_in_profile(self, t: np.ndarray) -> np.ndarray:
        # Dynamic oscillatory local constraint boundary model
        return 50.0 + 30.0 * np.sin(0.5 * t) * np.exp(0.1 * t)

if __name__ == "__main__":
    print("=== Dynamic Horizon Simulation Execution ===")
    sim = DynamicHorizonSimulation(omega_out_initial=200.0, omega_in_rate=0.1, steps=10)
    results = sim.run_simulation()
    
    print("\nStep | Omega_Out | Omega_In (Constraint) | Horizon Delta (H) | Observable State (N)")
    print("-" * 75)
    for i in range(len(results["time"])):
        t = results["time"][i]
        out_val = results["omega_out"][i]
        in_val = results["omega_in"][i]
        h_val = results["horizon_delta"][i]
        n_val = results["observable_state_N"][i]
        print(f"{t:4.1f} | {out_val:9.2f} | {in_val:21.2f} | {h_val:17.2f} | {n_val:20.2f}")
