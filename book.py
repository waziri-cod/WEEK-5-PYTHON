# Base class
class PhilosophicalBook:
    """Base class for philosophical books."""
    def __init__(self, title, philosopher, pages, theme):
        self.title = title
        self.philosopher = philosopher
        self.pages = pages
        self.theme = theme
        self.current_page = 1

    def read(self, pages_to_read):
        if self.current_page + pages_to_read <= self.pages:
            self.current_page += pages_to_read
            return f"Reading {pages_to_read} pages of '{self.title}'... now on page {self.current_page}."
        else:
            self.current_page = self.pages
            return f"You have completed '{self.title}' by {self.philosopher}, exploring the theme of {self.theme}."

    def bookmark(self):
        return f"Bookmark placed at page {self.current_page} in '{self.title}'."

    def info(self):
        return f"'{self.title}' by {self.philosopher} | {self.pages} pages | Theme: {self.theme}"


# Child class 1
class Ebook(PhilosophicalBook):
    def __init__(self, title, philosopher, pages, theme, file_size):
        super().__init__(title, philosopher, pages, theme)
        self.file_size = file_size  # in MB

    # Overriding read() method
    def read(self, pages_to_read):
        result = super().read(pages_to_read)
        return result + f" (Digital edition, file size: {self.file_size}MB)."


# Child class 2
class AudioPhilosophyBook(PhilosophicalBook):
    def __init__(self, title, philosopher, pages, theme, duration):
        super().__init__(title, philosopher, pages, theme)
        self.duration = duration  # in hours

    # Overriding read() method
    def read(self, pages_to_read):
        return f"Listening to '{self.title}' by {self.philosopher}, about {self.theme}. Total duration: {self.duration} hours."


# Example usage
if __name__ == "__main__":
    book1 = PhilosophicalBook("Critique of Pure Reason", "Immanuel Kant", 800, "Epistemology")
    ebook1 = Ebook("Being and Time", "Martin Heidegger", 600, "Existentialism", 12)
    audio1 = AudioPhilosophyBook("Republic", "Plato", 400, "Justice and Politics", 20)

    # Print information and interactions
    print(book1.info())
    print(book1.read(50))
    print(book1.bookmark())

    print("\n--- Ebook ---")
    print(ebook1.info())
    print(ebook1.read(150))
    print(ebook1.bookmark())

    print("\n--- Audio Philosophy Book ---")
    print(audio1.info())
    print(audio1.read(50))  # Polymorphic behavior here
