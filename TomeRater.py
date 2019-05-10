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
            # TODO: fix this method, need to figure out how books are stored and accessed in the dictionary, add rating to book object?
            total += self.books[book]   # rating of the book, add to total
            count += 1                  # counter
        return total / count
            
class Book(object):
    def __init__(self, title, isbn):
        self.title = title    # string
        self.isbn = isbn      # number
        self.ratings = []

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The ISBN for this book has been changed to {isbn}.".format(isbn=self.isbn))

    def get_average_rating(self):
        """
        Calculates the average rating of a book by adding all ratings and dividing by the number of ratings

        :return: average rating
        """
        total = 0
        count = 0
        for rating in self.ratings:
            # TODO: test this method
            total += rating   # rating of the book, add to total
            count += 1                  # counter
        return total / count

    def add_rating(self, rating):
        """
        Adds a rating to a book
        :param rating:
        :return:
        """
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating")




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


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating="None"):
        if email in self.users:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            # check if book exists in catalog
            if book in self.books:
                # increase value by one since it was read by a new user
                self.books[book] += 1
            else:
                # if not, add book to catalog with value of one since it was read one time
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=[]):
        self.users[email] = User(name, email)
        for book in user_books:
            self.add_book_to_user(book, email)

