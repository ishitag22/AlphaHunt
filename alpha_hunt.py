# import random

# words_list=['hello','paris','toast','friends','manchester']
# word=random.choice(words_list)
# word_len=len(word)
# masked_word=[]

# for i in range(0,word_len):
#     masked_word+='*'
# chances=word_len

# print('word is',masked_word, 'its length is',word_len)
# incorrect=''
# wrong= False
# while chances>0 and not wrong:
#     print('You have',chances,'attempts left')
#     guess=input('Enter a char(lowercase):')

#     for i in range(0,word_len):
#         if guess==word[i]:
#             masked_word[i]=guess
#             print('correct..')
#             print('word is',masked_word)
#             if not '*' in masked_word:
#                 print('Congratulations! you got the word')
#                 wrong=True
         
#     if guess not in word and guess not  in incorrect:
#         chances=chances-1
#         incorrect+=guess
#         print('Previous guess:',incorrect)
#         print('try again..')
#         print('word is',masked_word)
# if not wrong:
#     print('You Lost!')
#     print('The correct word is ',word)
    


import random
import tkinter as tk
from tkinter import messagebox

# List of words
words_list = [
    'hello', 'paris', 'toast', 'friends', 'manchester', 'python', 'developer', 
    'sunshine', 'adventure', 'program', 'flutter', 'javascript', 'keyboard', 
    'mountain', 'universe', 'galaxy', 'earth', 'ocean', 'forest', 'eclipse'
]

class WordGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Guessing Game")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Initialize game variables
        self.reset_game_variables()

        # Create UI components
        self.create_widgets()

    def reset_game_variables(self):
        self.word = random.choice(words_list)
        self.word_len = len(self.word)
        self.masked_word = ['*'] * self.word_len
        self.chances = self.word_len
        self.incorrect = set()
        self.game_over = False

    def create_widgets(self):
        # Masked word label
        self.word_label = tk.Label(self.master, text="Word: " + ''.join(self.masked_word), font=("Helvetica", 16))
        self.word_label.pack(pady=20)

        # Chances label
        self.chances_label = tk.Label(self.master, text=f"Chances Left: {self.chances}", font=("Helvetica", 12))
        self.chances_label.pack()

        # Incorrect guesses label
        self.incorrect_label = tk.Label(self.master, text="Incorrect Guesses: None", font=("Helvetica", 12))
        self.incorrect_label.pack(pady=10)

        # Entry for user's guess
        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind("<Return>", self.submit_guess)  # Allow pressing Enter to submit

        # Submit button
        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.submit_guess, font=("Helvetica", 12))
        self.submit_button.pack(pady=5)

        # Reset button (initially hidden)
        self.reset_button = tk.Button(self.master, text="Play Again", command=self.reset_game, font=("Helvetica", 12))
        # self.reset_button.pack(pady=5)  # We'll pack it when needed

    def submit_guess(self, event=None):
        if self.game_over:
            messagebox.showinfo("Game Over", "The game is over. Please reset to play again.")
            return

        guess = self.guess_entry.get().lower().strip()
        self.guess_entry.delete(0, tk.END)  # Clear entry field

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single lowercase alphabetic character.")
            return

        if guess in self.masked_word or guess in self.incorrect:
            messagebox.showinfo("Already Guessed", f"You have already guessed '{guess}'. Try another letter.")
            return

        if guess in self.word:
            for idx, char in enumerate(self.word):
                if char == guess:
                    self.masked_word[idx] = guess
            self.word_label.config(text="Word: " + ''.join(self.masked_word))
            self.update_chances_label()

            if '*' not in self.masked_word:
                self.game_over = True
                messagebox.showinfo("Congratulations!", f"You guessed the word '{self.word}' correctly!")
                self.show_reset_button()
        else:
            if guess not in self.incorrect:
                self.chances -= 1
                self.incorrect.add(guess)
                self.update_chances_label()
                self.update_incorrect_label()
                if self.chances == 0:
                    self.game_over = True
                    messagebox.showinfo("Game Over", f"You lost! The correct word was '{self.word}'.")
                    self.show_reset_button()

    def update_chances_label(self):
        self.chances_label.config(text=f"Chances Left: {self.chances}")

    def update_incorrect_label(self):
        incorrect_guesses = ', '.join(sorted(self.incorrect)) if self.incorrect else 'None'
        self.incorrect_label.config(text=f"Incorrect Guesses: {incorrect_guesses}")

    def show_reset_button(self):
        self.reset_button.pack(pady=10)

    def reset_game(self):
        self.reset_game_variables()
        self.word_label.config(text="Word: " + ''.join(self.masked_word))
        self.update_chances_label()
        self.update_incorrect_label()
        self.reset_button.pack_forget()
        self.game_over = False

# Create the main window
root = tk.Tk()
game = WordGuessingGame(root)
root.mainloop()
