# Nicholas Smith / Lab 15 #1 / Graphing Fermat's Spiral
# 26 April 2025

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def fermat_spiral(a: float, theta: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate the coordinates of Fermat's spiral.

    Args:
        a (float): Scaling factor for the spiral.
        theta (np.ndarray): Array of theta values.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Cartesian coordinates (x, y) of the spiral.
    """

    r = a * np.sqrt(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def input_values() -> Tuple[float, np.ndarray]:
    """
    Input values for the spiral.

    Returns:
        Tuple[float, np.ndarray]: Scaling factor and range of theta values.
    """

    a = input("Enter the scaling factor (a): ")
    theta = np.linspace(0, 10 * np.pi, 500)  # Range of theta values
    return float(a), theta

def plot_fermat_spiral(a: float, theta: np.ndarray) -> None:
    """
    Plot Fermat's spiral.

    Args:
        a (float): Scaling factor for the spiral.
        theta (np.ndarray): Array of theta values.
    """

    x, y = fermat_spiral(a, theta)
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Fermat's Spiral", color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Fermat's Spiral: $r = a \\sqrt{\\theta}$")
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def main() -> None:
    """Main function to run the program."""
    
    try:
        a, theta = input_values()
    except ValueError:
        print("Invalid input. Please enter a valid number for 'a'.")
        return

    plot_fermat_spiral(a, theta)

main()

