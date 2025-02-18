#question one
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def get_genre(self):
        print(f"The genre of '{self.title}' is {self.genre}.")

# Initialize a book object with unique values
harry_potter = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", 309)
harry_potter.read()
harry_potter.get_genre()

#question two
class Animal:
    def move(self):
        pass

class Car(Animal):
    def move(self):
        print("Driving")

class Plane(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")


car = Car()
plane = Plane()
fish = Fish()

animals = [car, plane, fish]
for animal in animals:
    animal.move()

