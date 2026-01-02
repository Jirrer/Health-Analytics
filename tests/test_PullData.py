import pytest
from unittest.mock import patch

from src.PullData import (
    pullMedianIncome,
    pullHealthRank,
    pullGiniCoeffient
)

def test_pullMedianIncome():
    databaseResponse = [('Clinton', 2010, 70906), ('Clinton', 2011, 71419), ('Clinton', 2012, 72532), ('Clinton', 2013, 73839), ('Clinton', 2014, 74882), ('Clinton', 2015, 76785), ('Clinton', 2016, 80386), ('Clinton', 2017, 83808), ('Clinton', 2018, 85412), ('Clinton', 2019, 88613), ('Clinton', 2020, 93526), ('Clinton', 2021, 96520), ('Clinton', 2022, 104250), ('Clinton', 2023, None), ('Clinton', 2024, None), ('Clinton', 2025, None)]

    with patch('src.Methods.makeSingleQuery', return_value=(True, databaseResponse)):
        success, grouped = pullMedianIncome("CountyA")
        
        assert success is True
        assert "CountyA" in grouped
        assert grouped["CountyA"] == [(2010, 50000), (2011, 52000)]