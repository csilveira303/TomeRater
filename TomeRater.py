import operator


class User(object):
    def __init__(self, name, email):
        """
        Constructs an instance of User

        :param name: name of the user
        :param email: email address of the user
        """
        self.name = name    # string
        self.email = email  # string
        self.books = {}     # dictionary of books read by user where key is book, value is its rating

    def get_email(self):
        """
        Gets a user's email address

        :return: email address of user
        """
        return self.email

    def get_books_read(self):
        """
        Returns number of books read by user

        :return: number of books read by user
        """
        return len(self.books)

    def change_email(self, address):
        """
        Changes a user's email address

        :param address: new email address for user
        :return: success message upon change
        """
        self.email = address
        print("Email has been updated to {email} for user {user}".format(email=self.email, user=self.name))

    def __repr__(self):
        """
        String representation of user
        :return: string representation of user
        """
        return "User: {user}, email: {email}, books read: {read}".format(email=self.email, user=self.name, read=len(self.books))

    def __eq__(self, other_user):
        """
        Compares to other user for equality

        :param other_user: user to compare
        :return: True if equal, False if not equal
        """
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.email)

    def read_book(self, book, rating="None"):
        """
        Adds book to user's list of books read. Can take a rating for book.
        Defaults to "None" if no rating provided

        :param book: title of book
        :param rating: user rating of book from 0 - 4, defaults to "None"
        :return: none
        """
        self.books[book] = rating

    def get_average_rating(self):
        """
        Gets the user's average rating for books read

        :return: average rating for books read
        """
        total = 0
        count = 0
        for book in self.books:
            if self.books[book] == "None":
                pass
            else:
                #print("Book: {book}, rating: {rating}".format(book=book, rating=self.books[book]))
                total += self.books[book]   # rating of the book, add to total
                count += 1                 # counter
        if count == 0:
            return 0
        else:
            return total / count


class Book(object):
    def __init__(self, title, isbn):
        """
        Creates an instance of Book

        :param title: title of book
        :param isbn: ISBN of book
        """
        self.title = title    # string
        self.isbn = isbn      # number
        self.ratings = []

    def __eq__(self, other):
        """
        Compares to other book for equality

        :param other: other book to compare
        :return: True if books  are equal, False if not equal
        """
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

    def __hash__(self):

        return hash((self.title, self.isbn))

    def get_title(self):
        """
        Get book title

        :return: title of book
        """
        return self.title

    def get_isbn(self):
        """
        Get book ISBN

        :return: ISBN of book
        """
        return self.isbn

    def set_isbn(self, isbn):
        """
        Set book ISBN

        :param isbn: ISBN of book
        :return: Success message
        """
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
            total += rating   # rating of the book, add to total
            count += 1        # counter
        if count == 0:
            return 0
        else:
            return total / count

    def add_rating(self, rating):
        """
        Add book to user. If book is added to user without providing a rating, it defaults to the string "None"

        :param rating: rating of book from 0 - 4, defaults to "None" if not provided
        :return: none
        """
        # "None" needs to be handled as a special case since the comparison for ratings is an int between 0 and 4
        if rating == "None":
            pass
        elif 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating")


class Fiction(Book):
    def __init__(self, title, author, isbn):
        """
        Creates an instance of a fiction book

        :param title: title of book
        :param author: author of book
        :param isbn: ISBN of book
        """
        super().__init__(title, isbn)
        self.author = author    # string

    def get_author(self):
        """
        Gets book author
        :return: author of book
        """
        return self.author

    def __repr__(self):
        """
        String representation of fiction book

        :return: string representation of fiction book
        """
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        """
         Creates an instance of a non-fiction book

        :param title: title of book
        :param subject: subject of book
        :param level: level/difficulty of book
        :param isbn: ISBN of book
        """
        super().__init__(title, isbn)
        self.subject = subject  # string like "Geology"
        self.level = level      # string like "advanced"

    def get_subject(self):
        """
        Gets subject of book

        :return: subject of book
        """
        return self.subject

    def get_level(self):
        """
        Gets level/difficulty of book

        :return: level of book
        """
        return self.level

    def __repr__(self):
        """
        String representation of non-fiction book

        :return: string representation of non-fiction book
        """
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        """
        Creates a Book
        :param title: title of book
        :param isbn: ISBN of book
        :return: instance of Book
        """
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        """
        Creates a novel, or fiction book

        :param title: title of book
        :param author: author of book
        :param isbn: ISBN of book
        :return: instance of Fiction book
        """
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        """
        Creates a non-fiction book

        :param title: title of book
        :param subject: subject of book
        :param level: level/difficulty of book
        :param isbn: ISBN of book
        :return: instance of Non_Fiction book
        """
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating="None"):
        """
        Adds a book to a user

        :param book: title of book
        :param email: email address of user
        :param rating: user rating of book, defaults to "None" if not provided
        :return: none
        """
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
        """
        Adds a user

        :param name: name of user
        :param email: email address of user
        :param user_books: list of books user had read, defaults to empty if not provided
        :return: none
        """
        self.users[email] = User(name, email)
        for book in user_books:
            self.add_book_to_user(book, email)

    def print_catalog(self):
        """
        Prints a catalog of books

        :return: none
        """
        print("Book Catalog:")
        for key in self.books:
            print("Title: {title}, Times read: {read}".format(title=key, read=self.books[key]))

    def print_users(self):
        """
        Prints a list of users

        :return:
        """
        print("List of users:")
        for key in self.users:
            print(self.users[key])

    def highest_rated_book(self):
        """
        Returns the book from catalog with the highest user rating

        :return: Book with highest user rating
        """
        highest_book = ''
        highest_rating = 0
        for book in self.books:
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_rating = rating
                highest_book = book
        return highest_book

    def most_positive_user(self):
        """
        Returns user with the highest rating

        :return: User with highest rating
        """
        highest_user = ''
        highest_rating = 0

        for user in self.users:
            print(self.users[user].get_average_rating())
            rating = self.users[user].get_average_rating()
            if rating > highest_rating:
                highest_rating = rating
                highest_user = user
        return highest_user

    def most_read_book(self):
        """
        Returns the book that is read by the most users

        :return: Book that is read by the most users
        """
        most_read = 0
        title = ''
        for book in self.books:
            if self.books[book] > most_read:
                title = book
                most_read = self.books[book]
        return title

    def get_n_most_read_books(self, n):
        """
        Returns 'n' number of books sorted by most read in descending order
        :param n: number of books to return
        :return: a list with 'n' number of books sorted by most read
        """
        # create list
        n_books = []
        # sort the book catalog by most reads
        sorted_books = sorted(self.books.items(), key=operator.itemgetter(1), reverse=True)
        # grab 'n' books from the sorted list
        for i in range(n):
            n_books.append(sorted_books[i])
        return n_books

    def get_n_most_prolific_readers(self, n):
        """
        Returns 'n' number of users with the most books read, sorted in descending order

        :param n: number of users to return
        :return: 'n' number of users with most books read
        """
        # create dictionary
        temp_users = {}
        # extract users and number of books read
        for user in self.users:
            temp_users[user] = self.users[user].get_books_read()

        # sort users by most books read and take the first n elements
        n_users = dict(sorted(temp_users.items(), key=operator.itemgetter(1), reverse=True)[:n])

        return n_users
