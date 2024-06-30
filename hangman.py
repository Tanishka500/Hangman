import tkinter as tk
from tkinter import messagebox
import random

# Dictionary of words and their corresponding hints
words_with_hints = {
    'python': 'A popular programming language.',
    'hangman': 'The name of this game.',
    'programming': 'What you are doing now.',
    'developer': 'A person who writes code.',
    'software': 'What developers create.',
    'algorithm': 'A step-by-step procedure for calculations.',
    'database': 'A structured collection of data.',
    'internet': 'A global network connecting millions of computers.',
    'keyboard': 'A device used to input text.',
    'monitor': 'A device used to display visual output.',
    'computer': 'An electronic device for storing and processing data.',
    'network': 'A group of interconnected computers.',
    'debugging': 'The process of finding and fixing errors in code.',
    'compiler': 'A program that converts code into executable files.',
    'interpreter': 'A program that executes code line by line.',
    'function': 'A block of code that performs a specific task.',
    'variable': 'A storage location identified by a name.',
    'syntax': 'The rules that define the structure of a programming language.',
    'loop': 'A control flow statement for repeating a block of code.',
    'array': 'A data structure that stores a collection of elements.',
    'class': 'A blueprint for creating objects.',
    'object': 'An instance of a class.',
    'inheritance': 'A mechanism for creating a new class from an existing class.',
    'polymorphism': 'The ability to process objects differently based on their data type.',
    'encapsulation': 'The bundling of data and methods into a single unit.',
    'abstraction': 'The concept of hiding complex implementation details.',
    'constructor': 'A special method used to initialize objects.',
    'destructor': 'A method called when an object is destroyed.',
    'file': 'A container for storing data.',
    'directory': 'A folder for organizing files.',
    'path': 'The location of a file or directory.',
    'exception': 'An error that occurs during program execution.',
    'module': 'A file containing Python code.',
    'package': 'A collection of Python modules.',
    'library': 'A collection of pre-written code that can be used in programs.',
    'framework': 'A platform for developing software applications.',
    'API': 'A set of functions and protocols for building software.',
    'server': 'A computer that provides data to other computers.',
    'client': 'A computer that requests data from a server.',
    'protocol': 'A set of rules for data communication.',
    'HTTP': 'The protocol used for transferring web pages.',
    'HTTPS': 'The secure version of HTTP.',
    'FTP': 'A protocol for transferring files.',
    'SSH': 'A protocol for secure remote login.',
    'IP': 'The protocol for addressing and routing packets of data.',
    'TCP': 'A protocol for reliable data transmission.',
    'UDP': 'A protocol for fast, unreliable data transmission.',
    'DNS': 'A system for translating domain names to IP addresses.',
    'HTML': 'The markup language for creating web pages.',
    'CSS': 'The language for describing the style of web pages.',
    'JavaScript': 'A programming language for creating interactive web pages.',
}

# ASCII art for the hangman stages
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.configure(bg='#D2B48C')  # Light brown background
        self.word, self.hint = random.choice(list(words_with_hints.items()))
        self.guessed_letters = set()
        self.remaining_attempts = 6

        self.word_display = tk.StringVar()
        self.update_word_display()

        self.create_widgets()

    def create_widgets(self):
        # Word display
        tk.Label(self.root, textvariable=self.word_display, font=('Helvetica', 18, 'bold'), bg='#D2B48C', fg='black').pack(pady=20)

        # Hint display
        self.hint_label = tk.Label(self.root, text=f"Hint: {self.hint}", font=('Helvetica', 14, 'bold'), bg='#D2B48C', fg='black')
        self.hint_label.pack(pady=10)

        # Entry for guessing letters
        self.entry = tk.Entry(self.root, font=('Helvetica', 16), bg='#FFFDD0', fg='black')
        self.entry.pack(pady=20)

        # Guess button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.guess_letter, font=('Helvetica', 14, 'bold'), bg='black', fg='white')
        self.guess_button.pack(pady=10)

        # Remaining attempts label
        self.remaining_attempts_label = tk.Label(self.root, text=f"Remaining Attempts: {self.remaining_attempts}", font=('Helvetica', 14, 'bold'), bg='#D2B48C', fg='black')
        self.remaining_attempts_label.pack(pady=10)

        # Guessed letters label
        self.guessed_letters_label = tk.Label(self.root, text="Guessed Letters: ", font=('Helvetica', 14, 'bold'), bg='#D2B48C', fg='black')
        self.guessed_letters_label.pack(pady=10)

        # Canvas for hangman drawing
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg='#D2B48C', highlightthickness=0)
        self.canvas.pack(pady=20)
        self.draw_hangman()

    def update_word_display(self):
        display = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        self.word_display.set(display)

    def draw_hangman(self):
        self.canvas.delete("all")
        hangman_stage = hangman_art[6 - self.remaining_attempts]
        self.canvas.create_text(100, 100, text=hangman_stage, font=('Courier', 12, 'bold'), fill='black', justify='center')

    def guess_letter(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single alphabetic character.")
            return

        if guess in self.guessed_letters:
            messagebox.showwarning("Already Guessed", "You have already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            self.update_word_display()
            if all(letter in self.guessed_letters for letter in self.word):
                messagebox.showinfo("Congratulations", "You guessed the word!")
                self.reset_game()
        else:
            self.remaining_attempts -= 1
            self.remaining_attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
            self.guessed_letters_label.config(text=f"Guessed Letters: {', '.join(self.guessed_letters)}")
            self.draw_hangman()
            if self.remaining_attempts == 0:
                messagebox.showinfo("Game Over", f"You ran out of attempts! The word was: {self.word}")
                self.reset_game()

    def reset_game(self):
        self.word, self.hint = random.choice(list(words_with_hints.items()))
        self.guessed_letters.clear()
        self.remaining_attempts = 6
        self.update_word_display()
        self.hint_label.config(text=f"Hint: {self.hint}")
        self.remaining_attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
        self.guessed_letters_label.config(text="Guessed Letters: ")
        self.draw_hangman()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
