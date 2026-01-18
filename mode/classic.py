import pandas as pd
from solver.utils import load_champions, clear_terminal
from solver.logic import filtering


class Classic:
    def __init__(self):
        self.champions = load_champions('data/champions.json')
        
    def start(self) -> None:
        filtered = self.champions
        clear_terminal()

        while filtered.shape[0] > 1:

            champion = self.guess()
            answers = self.correct_wrong()

            clear_terminal()

            filtered = filtering(filtered, champion, answers)
            if filtered.shape[0] > 1:
                self.possibilities(filtered)
            elif filtered.empty:
                print("No champions left something went wrong.")
                break

        self.final_champ(filtered)

    def guess(self) -> str:
        champion_name = str(input('Enter your champion: '))
        return champion_name
            
    def correct_wrong(self) -> str:
        answers = str(input('Enter your answers: '))
        return answers
    
    def possibilities(self, filtered: pd.DataFrame) -> None:
        print('Your posibility guesses:\n\n')
        for champ in filtered.index.to_list():
            print(champ)
        print('\n')

    def correct(self) -> str:
        end = str(input('Did you guessed it?\n'))
        return end
    
    def final_champ(self, filtered: pd.DataFrame) -> None:
        champ = filtered.index[0]
        print("\n====================")
        print("🎉 CHAMPION FOUND 🎉")
        print(f"The answer is: {champ}")
        print("====================\n")
            