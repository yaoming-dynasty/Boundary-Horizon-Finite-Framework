import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def render_dna_model_3d(coordinates: np.ndarray, output_filename: str = "dna_model_1280x640.png"):
    """
    Renders a 3D DNA spatial conformation and saves it at 1280x640 resolution.
    """
    # Set figure size to match 1280x640 ratio (12.8 inches by 6.4 inches at 100 DPI)
    fig = plt.figure(figsize=(12.8, 6.4), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract x, y, z coordinates of the DNA backbone / chromatin loop
    x, y, z = coordinates[:, 0], coordinates[:, 1], coordinates[:, 2]
    
    # Plot the DNA chain
    ax.plot(x, y, z, color='royalblue', linewidth=2, label='Chromatin Backbone ($\mathcal{H}$)')
    ax.scatter(x, y, z, color='crimson', s=20, label='Nucleotide Nodes ($N$)')
    
    ax.set_title("Boundary-Horizon Framework: 3D DNA Chromatin Folding", fontsize=14, fontweight='bold')
    ax.set_xlabel("X Boundary Axis")
    ax.set_ylabel("Y Boundary Axis")
    ax.set_zlabel("Z Boundary Axis")
    ax.legend()
    
    # Save with exact pixel dimensions (1280 x 640)
    plt.savefig(output_filename, dpi=100, bbox_inches='tight')
    plt.close()
    print(f"3D DNA model successfully rendered and saved as {output_filename} (1280x640).")

if __name__ == "__main__":
    # Generate mock 3D helical coordinates for testing
    t = np.linspace(0, 4 * np.pi, 100)
    mock_coords = np.stack([np.cos(t), np.sin(t), t], axis=-1)
    render_dna_model_3d(mock_coords)
