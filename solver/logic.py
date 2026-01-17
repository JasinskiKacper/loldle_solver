from main import classic
import pandas as pd
from typing import Literal
# Classic algorithm
def gender_check(data: pd.DataFrame, champion: str, answer: Literal['g', 'r']) -> pd.DataFrame:
    gender = data.loc[champion]['Gender']
    if answer == 'g':
        data = data[data['Gender'] == gender] 
    elif answer == 'r':
        data = data[data['Gender'] != gender]
    
    return data

def position_check(data: pd.DataFrame, champion: str, answer: Literal['g', 'r', 'o']) -> pd.DataFrame:
    position = data.loc[champion]['Position']
    if answer == 'g':
        data = data[data['Position'].apply(lambda x: position == x)]
    elif answer == 'r':
        if len(position) == 1:
            data = data[data['Position'].apply(lambda x: position != x)]
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

def species_check(data: pd.DataFrame, champion: str, answer: Literal['g', 'r']) -> pd.DataFrame:
    species = data.loc[champion]['Species']
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
            data = data[data['Species'].apply(lambda x: species in x)]
        if type(species) == list:
            data = data[data['Species'].apply(
                lambda x: any(spec in x for spec in species))]  
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
    if not isinstance(answers, str) or not len(answers) == 7:
        return None
    
    data = gender_check(data, champion, answers[0])
    data = position_check(data, champion, answers[1])          
    
        #if i == 2: # Species
            #species = data.loc[champion]['Species']
            #if answers[i] == 'g':
                #data = data[data['Species'] == species]
            #elif answers[i] == 'r':
            #    data = data[data['Species'] != species]

        #if i == 3: # Resource
            #resource = data.loc[champion]['Resource']
            #if answers[i] == 'g':
                #data = data[data['Resource'] == resource]
            #elif answers[i] == 'r':
            #    data = data[data['Resource'] != resource]

        #if i == 4: # Range type
            #range_type = data.loc[champion]['Range_type']
            #if answers[i] == 'g':
                #data = data[data['Range_type'] == range_type]
            #elif answers[i] == 'r':
            #    data = data[data['Range_type'] != range_type]

        #if i == 5: # Region
            #region = data.loc[champion]['Region']
            #if answers[i] == 'g':
                #data = data[data['Region'] == region]
            #elif answers[i] == 'r':
            #    data = data[data['Region'] != region]

        #if i == 6: # Year
            #year = data.loc[champion]['Release_year']
            #if answers[i] == 'g':
                #data = data[data['Release_year'] == year]
            #elif answers[i] == '-':
            #    data = data[data['Release_year'] < year]
            #elif answers[i] == '+':
            #    data = data[data['Release_year'] > year]
                


    return data
    pass