"""Unit tests for PA4 engineering formulas.

An assert checks whether a condition is true. If the calculated answer
matches the expected answer, it passes. Otherwise, pytest reports a
failure. np.isclose allows for small floating-point differences.
"""

import numpy as np

from engineering_formulas import (
    calculate_force,
    calculate_density,
    calculate_power,
    calculate_kinetic_energy,
    calculate_circle_area,
    celsius_to_fahrenheit,
)


def test_calculate_force():
    """Check ordinary force, zero mass, and decimal inputs."""
    assert calculate_force(10, 2) == 20
    assert calculate_force(0, 100) == 0
    assert np.isclose(calculate_force(2.5, 1.2), 3.0)


def test_calculate_density():
    """Check ordinary density, zero mass, and decimal inputs."""
    assert calculate_density(10, 2) == 5
    assert calculate_density(0, 4) == 0
    assert np.isclose(calculate_density(7.5, 2.5), 3.0)


def test_calculate_power():
    """Check ordinary power, zero current, and decimal inputs."""
    # The original test expected 15, but power is current * voltage.
    # 3 * 12 = 36, so the expected answer needed to change.
    assert calculate_power(3, 12) == 36
    assert calculate_power(0, 12) == 0
    assert np.isclose(calculate_power(0.25, 4.8), 1.2)


def test_calculate_kinetic_energy():
    """Check ordinary energy, no motion, and negative decimal velocity."""
    assert calculate_kinetic_energy(5, 4) == 40
    assert calculate_kinetic_energy(5, 0) == 0
    assert np.isclose(calculate_kinetic_energy(2.5, -2.0), 5.0)


def test_calculate_circle_area():
    """Check a unit circle, zero radius, and decimal radius."""
    assert np.isclose(calculate_circle_area(1), 3.141592653589793)
    assert np.isclose(calculate_circle_area(0), 0.0)
    assert np.isclose(calculate_circle_area(0.5), 0.7853981633974483)


def test_celsius_to_fahrenheit():
    """Check freezing, boiling, and a negative decimal temperature."""
    assert np.isclose(celsius_to_fahrenheit(0), 32.0)
    assert np.isclose(celsius_to_fahrenheit(100), 212.0)
    assert np.isclose(celsius_to_fahrenheit(-12.5), 9.5)
