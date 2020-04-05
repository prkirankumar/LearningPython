class BankAccount:
    def __init__(self,first_name,last_name,initial_balance):
        self.first_name=first_name
        self.last_name=last_name
        self.available_balance=initial_balance
        
    @property # getter
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property # getter
    def balance(self):
        return self.balance
    
    @balance.setter
    def balance(self, value):  # don't use same instance variable name, it will go throw RecursionError
        if not isinstance(value, int):
            raise TypeError('The value should be integer')
        elif value < 0:
            raise ValueError('Negative amount is not allowed')
        self.available_balance = value


account_1=BankAccount('fname','lname',10000)
print(f'First Name : {account_1.first_name}')
print(f'Last Name : {account_1.last_name}')
#print(f'Full Name : {account_1.full_name()}')
print(f'Full Name : {account_1.full_name}')
# though it is method we have added @property decorator, because of this we are calling as property
account_1.last_name="lname_updated"
print(f'updated Last Name : {account_1.last_name}')
print(f'updated Full Name : {account_1.full_name}')

#account_1.full_name="fullname_updated"  # AttributeError

account_2=BankAccount("kiran","kumar",20000)
print(f'Account Balance : {account_2.available_balance}')


"""
Create a Library class with following interface:

- constructor, which will create an instance of Library class. If no arguments are give, an empty collection of books
should be created. If list of books are given as a parameter to the method, each book from the list should be added
to the collection of books.

- an attribute number_of_books should return current number of books in the collection

- add_book(book) method should add a book to the collection if the book does not exist in the collection of books

- borrow_book(book) method should remove a book from the collection if the book is in the collection of books

- show_books() method should print to the console all books, which are in the collection of books
"""

class Library:
    def __init__(self,collection=None):
        self.book_collection=[]

        if collection:
            for book in collection:
                self.add_book(book)

    @property
    def number_of_books(self):
        return len(self.book_collection)

    def add_book(self,book):
        if book not in self.book_collection:
            self.book_collection.append(book)
            print(f'Book {book} removed from collection')
    
    def borrow_book(self,book):
        if book in self.book_collection:
            self.book_collection.remove(book)
            print(f'Book {book} removed from collection')

    def show_books(self):
        if self.book_collection:
            print('Book Collection')
            for book in self.book_collection:
                print(book)
            else:
                print('Book collection is empty')

collection_1 = Library()
collection_1.show_books()
collection_1.add_book('C')
collection_1.add_book('C++')
collection_1.show_books()

print('\n\n')

collection_2 = Library(['C#', 'Java', 'Python'])
collection_2.show_books()
collection_2.add_book('Ruby')
collection_2.borrow_book('C#')
collection_2.borrow_book('PHP')
collection_2.add_book('Python')
collection_2.show_books()

print(f'Number of books in collection_2: {collection_2.number_of_books}')