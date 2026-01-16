from main import classic
import pandas as pd

# Classic algorithm
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
    
    
    for i in range(len(answers)):
        if i == 0: # Gender
            gender = data.loc[champion]['Gender']
            if answers[i] == 'g':
                data = data[data['Gender'] == gender] 
            elif answers[i] == 'r':
                data = data[data['Gender'] != gender] 
                
        if i == 1: # Position
            position = data.loc[champion]['Position']
            if answers[i] == 'g':
                data = data[data['Position'] == position]
            elif answers[i] == 'r':
                data = data[data['Position'] != position]

        if i == 2: # Species
            species = data.loc[champion]['Species']
            if answers[i] == 'g':
                data = data[data['Species'] == species]
            elif answers[i] == 'r':
                data = data[data['Species'] != species]

        if i == 3: # Resource
            resource = data.loc[champion]['Resource']
            if answers[i] == 'g':
                data = data[data['Resource'] == resource]
            elif answers[i] == 'r':
                data = data[data['Resource'] != resource]

        if i == 4: # Range type
            range_type = data.loc[champion]['Range_type']
            if answers[i] == 'g':
                data = data[data['Range_type'] == range_type]
            elif answers[i] == 'r':
                data = data[data['Range_type'] != range_type]

        if i == 5: # Region
            region = data.loc[champion]['Region']
            if answers[i] == 'g':
                data = data[data['Region'] == region]
            elif answers[i] == 'r':
                data = data[data['Region'] != region]

        if i == 6: # Year
            year = data.loc[champion]['Release_year']
            if answers[i] == 'g':
                data = data[data['Release_year'] == year]
            elif answers[i] == '-':
                data = data[data['Release_year'] < year]
            elif answers[i] == '+':
                data = data[data['Release_year'] > year]
                


    return data
    pass