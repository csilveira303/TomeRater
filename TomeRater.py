class User(object):
    def __init__(self, name, email):
        self.name = name    # string
        self.email = email  # string
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email has been updated to {email} for user {user}".format(email=self.email, user=self.name))

    def __repr__(self):
        return "User: {user}, email: {email}, books read: {read}".format(email=self.email, user=self.name, read=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating="None"):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        count = 0
        for book in self.books:
            
class Book(object):
    def __init__(self, title, isbn):
        self.title = title    # string
        self.isbn = isbn      # number
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The ISBN for this book has been changed to {isbn}.".format(isbn=self.isbn))

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating")

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author    # string

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject  # string like "Geology"
        self.level = level      # string like "advanced"

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

