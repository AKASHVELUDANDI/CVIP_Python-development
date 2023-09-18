import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.words = ["Conscientious", "Exaggeration", "Entrepreneur", "Mississippi", "Bureaucracy", "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
        self.current_word = ""
        self.time_start = 0

        self.label = tk.Label(root, text="Type the word below:")
        self.label.pack()

        self.word_label = tk.Label(root, text="", font=("Helvetica", 36))
        self.word_label.pack()

        self.entry = tk.Entry(root)
        self.entry.bind("<Return>", self.check_word)
        self.entry.pack()

        self.result_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.result_label.pack()

        self.new_word()

    def new_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.time_start = time.time()

    def check_word(self, event):
        typed_word = self.entry.get()
        if typed_word == self.current_word:
            time_elapsed = time.time() - self.time_start
            words_per_minute = len(typed_word) / (time_elapsed / 60)
            self.result_label.config(text=f"Typing speed: {int(words_per_minute)} WPM")
            self.new_word()
        else:
            self.result_label.config(text="Incorrect. Try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()