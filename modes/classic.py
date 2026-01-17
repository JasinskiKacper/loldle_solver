import pandas as pd
from solver.utils import load_champions
from main import clear_terminal
from solver.logic import filtering


class Classic:
    def __init__(self):
        self.champions = load_champions('data/champions.json')
        
    def start(self) -> None:
        champion = self.guess()
        
        answers = self.correct_wrong()

        filtered = filtering(self.champions, champion, answers)
        
        
        self.possibilities(filtered)

        self.correct()

    def guess(self) -> str:
        champion_name = str(input('Enter your champion: '))
        return champion_name
            
    def correct_wrong(self) -> str:
        answers = str(input('Enter your answers: '))
        return answers
    
    def possibilities(self, filtered: pd.DataFrame) -> None:
        print('Your posibility guesses:\n')
        print(filtered.index.to_list())
        
    def correct(self) -> None:
        end = str(input('Are you done?\n'))
        if end == 'No':
            self.start()
        elif end == 'Yes':
            print('We did it!')