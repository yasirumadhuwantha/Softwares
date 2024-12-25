import customtkinter as ctk


class CharacterSpaceCounterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Character and Space Counter")
        self.geometry("500x300")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Title Label
        self.title_label = ctk.CTkLabel(
            self,
            text="Character and Space Counter",
            font=("Arial", 20, "bold")
        )
        self.title_label.pack(pady=10)

        # Input Field
        self.input_label = ctk.CTkLabel(
            self,
            text="Word / Sentence",
            font=("Arial", 14)
        )
        self.input_label.pack(pady=5)

        self.input_field = ctk.CTkEntry(
            self,
            placeholder_text="Enter your word or sentence...",
            width=400
        )
        self.input_field.pack(pady=5)

        # Submit Button
        self.calculate_button = ctk.CTkButton(
            self,
            text="Proceed",
            command=self.calculate_counts
        )
        self.calculate_button.pack(pady=10)

        # Result Display
        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 14),
            wraplength=450,
            justify="left"
        )
        self.result_label.pack(pady=10)

    def calculate_counts(self):
        # Read user input
        word = self.input_field.get()

        # Initialize counters
        characters = 0
        spaces = 0

        # Count characters and spaces
        for i in word:
            if i != " ":
                characters += 1
            if i == " ":
                spaces += 1

        # Display results
        result_text = f"Characters = {characters}\nSpaces = {spaces}"
        self.result_label.configure(text=result_text, text_color="white")


# Run the application
if __name__ == "__main__":
    app = CharacterSpaceCounterApp()
    app.mainloop()
