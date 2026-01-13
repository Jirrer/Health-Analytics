import pytest
from unittest.mock import patch

from src.Methods import (
    getCurrentYear,
    balanceList,
    showLorenze,
    pushCalculations,
    prepareCountyName,
    getCensusCountyIncome,
    makeSingleQuery,
    makeManyQuery,
    groupByCounty,
    getHtmlPage,
)

def test_getCurrentYear():
    assert type(getCurrentYear()) == int