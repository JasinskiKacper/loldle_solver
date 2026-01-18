import pandas as pd
from typing import Literal


# Classic algorithm
def gender_check(data: pd.DataFrame, gender: str, answer: Literal['g', 'r', 'o']) -> pd.DataFrame:
    '''Filter champions based on gender'''
    
    if answer == 'g':
        data = data[data['Gender'] == gender] 
    elif answer == 'r':
        data = data[data['Gender'] != gender]
    
    return data

def position_check(data: pd.DataFrame, position: list, answer: Literal['g', 'r', 'o']) -> pd.DataFrame:
    '''Filter champions based on position'''
    if answer == 'g':
        data = data[data['Position'].apply(lambda x: position == x)]
    elif answer == 'r':
        if len(position) == 1:
            data = data[data['Position'].apply(lambda x: position[0] not in x)]
        elif len(position) != 1:
            for i in range(len(position)):
                data = data[data['Position'].apply(
                    lambda x: position[i] not in x)]
    elif answer == 'o':
        if len(position) == 1:
            data = data[data['Position'].apply(lambda x: len(x) > 1)]
            data = data[data['Position'].apply(
                lambda x: any(pos in x for pos in position))]
        if len(position) != 1:
            data = data[data['Position'].apply(
                lambda x: any(pos in x for pos in position))]
    return data

def species_check(data: pd.DataFrame, species: str|list, answer: Literal['g', 'r', 'o']) -> pd.DataFrame:
    '''Filter champions based on specie'''
    if answer == 'g':
        data = data[data['Species'].apply(lambda x: species == x)]
    elif answer == 'r':
        if type(species) == str:
            data = data[data['Species'].apply(lambda x: species not in x)]
        if type(species) == list:
            for i in range(len(species)):
                data = data[data['Species'].apply(
                    lambda x: species[i] not in x)]
    elif answer == 'o':
        if type(species) == str:
            data = data[data['Species'].apply(
                lambda x: any(species in spec for spec in x))]
        if type(species) == list:
            data = data[data['Species'].apply(
                lambda x: any(spec in x for spec in species))]  
    return data

def resource_check(data: pd.DataFrame, resource: str, answer: Literal['g', 'r', 'o']) -> pd.DataFrame:
    '''Filter champions based on resource'''
    if answer == 'g':
        if type(resource) == str:
            data = data[data['Resource'] == resource]
    elif answer == 'r':
        data = data[data['Resource'] != resource]

    return data

def range_check(data: pd.DataFrame, range_type: str|list, answer: Literal['g', 'r', 'o']) -> pd.DataFrame:
    '''Filter champions based on range type'''
    if answer == 'g':
        data = data[data['Range_type'] == range_type]
    elif answer == 'r':
        data = data[data['Range_type'].apply(lambda x: type(x) == str)]
        data = data[data['Range_type'] != range_type]
    elif answer == 'o':
        if type(range_type) == str:
            data = data[data['Range_type'].apply(lambda x: type(x) == list)]

    return data

def region_check(data: pd.DataFrame, region: list, answer: Literal['g', 'r', 'o']) -> pd.DataFrame:
    '''Filter champions based on region'''
    if answer == 'g':
        if len(region) == 1:
            data = data[data['Regions'].apply(
                lambda x: all(region[0] == x[i] for i in range(len(x))))]
        elif len(region) != 1:
            data = data[data['Regions'].apply(
                lambda x: len(x) == len(region))]
            data = data[data['Regions'].apply(
                lambda x: all(reg in x for reg in data))]
    if answer == 'r':
        if len(region) == 1:
            data = data[data['Regions'].apply(lambda x: region[0] not in x)]
        elif len(region) != 1:
            data = data[data['Regions'].apply(
                lambda x: all(reg not in x for reg in region))]
    elif answer == 'o':
        if len(region) == 1:
            data = data[data['Regions'].apply(lambda x: len(x) > 1)]
            data = data[data['Regions'].apply(lambda x: region[0] in x)]
        elif len(region) != 1:
            data = data[data['Regions'].apply(
                lambda x: any(reg in x for reg in region) and x != region)]
    
    return data

def year_check(data: pd.DataFrame, year: int, answer: Literal['g', '+', '-']) -> pd.DataFrame:
    '''Filter champions based on year realesed'''
    if answer == 'g':
        data = data[data['Release_year'] == year]
    if answer == '+':
        data = data[data['Release_year'] > year]
    if answer == '-':
        data = data[data['Release_year'] < year]

    return data

def filtering(data: pd.DataFrame, champion: str, answers: str) -> pd.DataFrame | None:
    '''
    filtering champions based on the answers

    Args:
        data (pd.DataFrame): DataFrame containing champions' data.
        champion (str): The champion that was guessed.
        answers (str): String representing the player's answers for each category
                        ('g' = correct, 'r' = wrong, 'o' = partial).

    Returns:
        pd.DataFrame: DataFrame of champions that match the given answers.
    '''
    if not isinstance(data, pd.DataFrame) or not isinstance(champion, str):
        return None
    if not isinstance(answers, str):
        return None
    if len(answers) != 7:
        raise ValueError('answers must have exactly 7 characters')

    gender = data.loc[champion]['Gender']
    position = data.loc[champion]['Position']
    specie = data.loc[champion]['Species']
    resource = data.loc[champion]['Resource']
    range_type = data.loc[champion]['Range_type']
    region = data.loc[champion]['Regions']
    year = data.loc[champion]['Release_year']

    data = gender_check(data, gender, answers[0])
    data = position_check(data, position, answers[1])
    data = species_check(data, specie, answers[2])
    data = resource_check(data, resource, answers[3])
    data = range_check(data, range_type, answers[4])
    data = region_check(data, region, answers[5])
    data = year_check(data, year, answers[6])
    
    return data
    pass