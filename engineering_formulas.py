"""Engineering calculations for ENSC 201 PA4. Author: Noah Gaido."""

import math


def calculate_force(mass, acceleration):
    """Return force in N for mass in kg and acceleration in m/s^2."""
    return mass * acceleration


def calculate_density(mass, volume):
    """Return density in kg/m^3 for mass in kg and nonzero volume in m^3."""
    # The original formula gave 0.2 for mass 10 and volume 2.
    # Density is mass / volume, so the correct result is 5.
    return mass / volume


def calculate_power(current, voltage):
    """Return electrical power in W for current in A and voltage in V."""
    return current * voltage


def calculate_kinetic_energy(mass, velocity):
    """Return kinetic energy in J for mass in kg and velocity in m/s."""
    # The original formula gave 10 for mass 5 and velocity 4.
    # Velocity needs to be squared, which gives 40 J.
    return 0.5 * mass * velocity ** 2


def calculate_circle_area(radius):
    """Return circle area in m^2 for radius in m."""
    return math.pi * radius ** 2


def celsius_to_fahrenheit(celsius):
    """Return temperature in Fahrenheit for temperature in Celsius."""
    return (9 / 5) * celsius + 32


def main():
    """Provide a place for optional manual testing."""
    pass


if __name__ == "__main__":
    main()
