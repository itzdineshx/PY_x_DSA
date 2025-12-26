# Dunder or magic methods -automatically called by program 
# Allow us to define or customize the behaviour of objects

"""
Python Build-in Dunder methods:
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__',
 '__divmod__', '__doc__', '__eq__','__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '_...
"""

class Book:
    def __init__(self, title, author, page_num):
        self.title = title
        self.author = author
        self.page_num = page_num

    # Dunder or magic methods
    def __str__(self): # str dunder method
        return f"{self.title} by {self.author}"

    def __eq__(self, value): # equal dunder method
        return self.title == value.title and self.author == value.author

book1 = Book("The Habbit", "Tolkein", 310)
book2 = Book("Harry Potter", "Rowling", 224)

print(book1) # str dunder method
print(book1 == book2) # equal dunder method