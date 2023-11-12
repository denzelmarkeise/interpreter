import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        # Input and output text variables
        self.input_text_var = tk.StringVar()
        self.output_text_var = tk.StringVar()

        # Language selection variables
        self.source_language_var = tk.StringVar()
        self.target_language_var = tk.StringVar()

        # Set the font size for widgets
        self.font_size = 12

        # Create and pack widgets
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", self.font_size))

        # Entry widget for input text
        input_label = ttk.Label(self.root, text="Enter Text:", font=("Arial bold", self.font_size))
        input_entry = ttk.Entry(self.root, textvariable=self.input_text_var, width=30, font=("Arial bold", self.font_size))
        input_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        input_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Language selection
        source_language_label = ttk.Label(self.root, text="Source Language:", font=("Arial bold", self.font_size))
        source_language_entry = ttk.Entry(self.root, textvariable=self.source_language_var, width=5, font=("Arial", self.font_size))
        source_language_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        source_language_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        target_language_label = ttk.Label(self.root, text="Target Language:", font=("Arial bold", self.font_size))
        target_language_entry = ttk.Entry(self.root, textvariable=self.target_language_var, width=5, font=("Arial", self.font_size))
        target_language_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        target_language_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Button to trigger translation
        translate_button = ttk.Button(self.root, text="Translate", command=self.translate_text, style="TButton")
        translate_button.grid(row=3, column=1, pady=10)

        # Output text label
        output_label = ttk.Label(self.root, text="Translated Text:", font=("Arial bold", self.font_size))
        output_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        # Output text display
        output_text = ttk.Label(self.root, textvariable=self.output_text_var, wraplength=300, font=("Arial", self.font_size))
        output_text.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    def translate_text(self):
        input_text = self.input_text_var.get()
        target_language = self.target_language_var.get().lower()

        if input_text and target_language:
            translator = Translator()
            translation = translator.translate(input_text, dest=target_language)
            self.output_text_var.set(translation.text)
        else:
            self.output_text_var.set("Please enter text and target language.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")  # Set the window size to 1000x1000 pixels
    app = LanguageTranslatorApp(root)
    root.mainloop()
