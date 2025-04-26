import numpy as np
import matplotlib.pyplot as plt

def fermat_spiral(a, theta):
    """Calculate the coordinates of Fermat's spiral."""
    r = a * np.sqrt(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def input_values():
    """Input values for the spiral."""
    a = input("Enter the scaling factor (a): ")
    theta = input("Enter the range of theta (e.g., 0 to 10*pi): ")
    theta = np.linspace(0, 10 * np.pi, 500)  # Range of theta values
    return a, theta

def plot_fermat_spiral(a, theta):
    """Plot Fermat's spiral."""
    x, y = fermat_spiral(a, theta)
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Fermat's Spiral")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Fermat's Spiral: $r = a \\sqrt{\\theta}$")
    plt.legend()
    plt.axis('equal')  # Ensure the aspect ratio is equal
    plt.grid()
    plt.show()

def main():
    """Main function to run the program."""
    try:
        a, theta = input_values()
        a = float(a)
    except ValueError:
        print("Invalid input. Please enter a valid number for 'a'.")
        return

    plot_fermat_spiral(a, theta)

main()

