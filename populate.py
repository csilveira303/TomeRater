from TomeRater import *

Tome_Rater = TomeRater()

# Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)
novel4 = Tome_Rater.create_novel("The Hobbit", "J.R.R. Tolkien", 10002001)
novel5 = Tome_Rater.create_novel("The Fellowship of the Ring", "J.R.R. Tolkien", 10002002)
novel6 = Tome_Rater.create_novel("The Two Towers", "J.R.R. Tolkien", 10002003)
novel7 = Tome_Rater.create_novel("The Return of the King", "J.R.R. Tolkien", 10002004)

# Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
Tome_Rater.add_user("Alice Test", "alice@test.com")
Tome_Rater.add_user("Bob Test", "bob@test.com")
Tome_Rater.add_user("Carly Test", "carly@test.com")

# Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

# Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel5, "alan@turing.com", 2)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

Tome_Rater.add_book_to_user(novel3, "alice@test.com", 3)
Tome_Rater.add_book_to_user(novel4, "alice@test.com", 4)
Tome_Rater.add_book_to_user(novel5, "alice@test.com", 2)
Tome_Rater.add_book_to_user(novel6, "alice@test.com", 4)
Tome_Rater.add_book_to_user(novel7, "alice@test.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alice@test.com", 1)
Tome_Rater.add_book_to_user(nonfiction1, "alice@test.com", 0)

Tome_Rater.add_book_to_user(novel5, "bob@test.com", 3)
Tome_Rater.add_book_to_user(novel6, "bob@test.com", 4)
Tome_Rater.add_book_to_user(novel7, "bob@test.com", 3)

Tome_Rater.add_book_to_user(nonfiction1, "carly@test.com", 2)

# Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

# Final requirements
print("3 most prolific readers:")
print(Tome_Rater.get_n_most_prolific_readers(3))
print("3 most read books:")
print(Tome_Rater.get_n_most_read_books(3))
