import random
import os


class HangmanGameV2:
    def __init__(self):
        print("Starting now")
        self.setup_game()

    
    def setup_game(self):
        self.cheat = True
        words_list:list = ["Game", "Train", "Against"]
        self.the_word:str = random.choice(words_list)

        self.game()
    
    
    def game(self):
        guesses = []

        for word_ch in self.the_word:
            guesses.append("_")

        print("Try pick your word")
        
        the_chances:int = 10

        while True:
            guesses_list_change = str(guesses).replace("[", "").replace("]", "").replace(",", "").replace(" ", "").replace("'", "").replace("'", "")
            os.system("cls" if os.name == "nt" else "clear")
            
            if guesses_list_change == self.the_word:
                print("Finished now")
                break
            
            if self.cheat == True:
                print(self.the_word)

            print(guesses_list_change)

            if the_chances == 0:
                print("You lose")
                break
            
            user_inp = input("What is your guess?? ")
        
            if len(user_inp) != 1:
                print("You can only use one letter no more")
                continue
            
            if user_inp in self.the_word.lower():
                the_index = 0
                for a in self.the_word.lower():
                    if a == user_inp:
                        guesses[the_index] = self.the_word[the_index]
                    the_index+=1
            else:
                the_chances-=1
                print(f"Incorrect, you have {the_chances} left! Be very wise")




if __name__ == "__main__":
    HangmanGameV2()
