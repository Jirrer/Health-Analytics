import pytest
from unittest.mock import patch

from src.CalculateData import (
    GiniCoeffient,
    calculateLorenzePlots,
    calculateGiniCoeffient,
    getLorenzeArea,
)
# def test_GiniCoeffient():
#     assert GiniCoeffient(2009) == -1
#     assert GiniCoeffient(2026) == None
    
def test_calculateLorenzePlots():
    pass

def test_calculateGiniCoeffient():
    validGini = [(0, 0), (0.5, 0.25), (1, 1)]
    assert calculateGiniCoeffient(validGini) == 0.25

    invalidGini = [(0, 0), (0.5, 0.75), (1, 1)]
    with pytest.raises(ValueError, match="Gini Coeffient must be between 0-0.5"):
        calculateGiniCoeffient(invalidGini)

def test_getLorenzeArea():
    validPlots = [(0, 0), (0.5, 0.75), (1, 1)]
    assert getLorenzeArea(validPlots) == 0.625

    notEnoughPlots = [(0.0, 0.0)]
    with pytest.raises(ValueError, match="Not enough plots provided"):
        getLorenzeArea(notEnoughPlots)

    outOfBounds = [(0, 0), (0.5, 1.5), (1, 2)]
    with pytest.raises(ValueError, match="Lorenz Curve must be between 0-1"):
        getLorenzeArea(outOfBounds)

    notSorted = [(1, 1), (0.5, 0.5), (0.25, 0.3), (1, 1)]
    with pytest.raises(ValueError, match="Plots are not sorted"):
        getLorenzeArea(notSorted)