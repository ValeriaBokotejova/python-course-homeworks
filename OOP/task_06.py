class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        return f"{self.title} by {self.author} (Published: {self.year_published})"

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book)
