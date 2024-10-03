import random
import tkinter as tk
from tkinter import messagebox

words_list = [
    'hello', 'paris', 'toast', 'friends', 'manchester', 'python', 'developer', 
    'sunshine', 'adventure', 'program', 'flutter', 'javascript', 'keyboard', 
    'mountain', 'universe', 'galaxy', 'earth', 'ocean', 'forest', 'eclipse'
]

class WordGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Alpha Hunt")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.reset_game_variables()
        self.create_widgets()

    def reset_game_variables(self):
        self.word = random.choice(words_list)
        self.word_len = len(self.word)
        self.masked_word = ['*'] * self.word_len
        self.chances = self.word_len
        self.incorrect = set()
        self.game_over = False

    def create_widgets(self):
        self.word_label = tk.Label(self.master, text="Word: " + ''.join(self.masked_word), font=("Helvetica", 16))
        self.word_label.pack(pady=20)

        self.chances_label = tk.Label(self.master, text=f"Chances Left: {self.chances}", font=("Helvetica", 12))
        self.chances_label.pack()

        self.incorrect_label = tk.Label(self.master, text="Incorrect Guesses: None", font=("Helvetica", 12))
        self.incorrect_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind("<Return>", self.submit_guess)  # Allow pressing Enter to submit

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.submit_guess, font=("Helvetica", 12))
        self.submit_button.pack(pady=5)

        self.reset_button = tk.Button(self.master, text="Play Again", command=self.reset_game, font=("Helvetica", 12))

    def submit_guess(self, event=None):
        if self.game_over:
            messagebox.showinfo("Game Over", "The game is over. Please reset to play again.")
            return

        guess = self.guess_entry.get().lower().strip()
        self.guess_entry.delete(0, tk.END)

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

root = tk.Tk()
game = WordGuessingGame(root)
root.mainloop()
