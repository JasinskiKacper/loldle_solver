import pandas as pd
import pytest

from solver.logic import *

@pytest.fixture
def test_df():
    return pd.DataFrame({
        "Gender": ["Male", "Female", "Male"],
        "Position": [["Top"], ["Top", "Jungle"], ["Mid"]],
        "Species": ["Human", ["Yordle", "Human"], "Undead"],
        "Resource": ["Mana", "Energy", "Mana"],
        "Range_type": ["Melee", "Ranged", ["Melee", "Ranged"]],
        "Regions": [["Noxus"], ["Demacia", "Noxus"], ["Shadow Isles"]],
        "Release_year": [2015, 2018, 2021]
    }, index=["A", "B", "C"])

def test_gender_check_g(test_df):
    result = gender_check(test_df, gender='Male', answer='g')
    assert list(result.index) == ['A', 'C']

def test_gender_check_r(test_df):
    result = gender_check(test_df, gender='Male', answer='r')
    assert list(result.index) == ['B']

def test_position_check_g(test_df):
    result = position_check(test_df, position=['Top'], answer='g')
    assert list(result.index) == ['A']

def test_position_check_r(test_df):
    result = position_check(test_df, position=['Top'], answer='r')
    assert list(result.index) == ['C']

def test_position_check_o(test_df):
    result = position_check(test_df, position=['Top'], answer='o')
    assert list(result.index) == ['B']

def test_specie_check_g(test_df):
    result = species_check(test_df, species='Human', answer='g')
    assert list(result.index) == ['A']

def test_specie_check_r(test_df):
    result = species_check(test_df, species='Human', answer='r')
    assert list(result.index) == ['C']

def test_specie_check_o(test_df):
    result = species_check(test_df, species='Human', answer='o')
    assert list(result.index) == ['B'] 

def test_resource_check_g(test_df):
    result = resource_check(test_df, resource='Mana', answer='g')
    assert list(result.index) == ['A', 'C']

def test_resource_check_r(test_df):
    result = resource_check(test_df, resource='Mana', answer='r')
    assert list(result.index) == ['B']

def test_range_check_g(test_df):
    result = range_check(test_df, range_type='Melee', answer='g')
    assert list(result.index) == ['A']

def test_range_check_r(test_df):
    result = range_check(test_df, range_type='Melee', answer='r')
    assert list(result.index) == ['B']

def test_range_check_o(test_df):
    result = range_check(test_df, range_type='Melee', answer='o')
    assert list(result.index) == ['C']

def test_region_check_g(test_df):
    result = region_check(test_df, region=["Noxus"], answer='g')
    assert list(result.index) == ['A']

def test_region_check_r(test_df):
    result = region_check(test_df, region=["Noxus"], answer='r')
    assert list(result.index) == ['C']

def test_region_check_o(test_df):
    result = region_check(test_df, region=["Noxus"], answer='o')
    assert list(result.index) == ['B']

def test_region_check_o2(test_df):
    result = region_check(test_df, region=["Demacia", "Noxus"], answer='o')
    assert list(result.index) == ['A']

def test_year_check_g(test_df):
    result = year_check(test_df, year=2015, answer='+')
    assert list(result.index) == ['B', 'C']

def test_year_check_r(test_df):
    result = year_check(test_df, year=2015, answer='g')
    assert list(result.index) == ['A']

def test_year_check_o(test_df):
    result = year_check(test_df, year=2018, answer='-')
    assert list(result.index) == ['A']