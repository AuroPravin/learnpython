class books:
    def __init__(self,title,author):
        self.title=title
        self.author=author

#functionality of library mentioned here
class library:
    def __init__(self):
        self.books=[]

    #add book to library
    def addbook(self,books):
        self.books.append(books)

    #Display the available book
    def displaybook(self):
        print("Available books in the library")
        for books in self.books:
            print(f"{books.title} by {books.author}")

#Here the object for the class library is created  
lib=library()

#display the available options
while True:
    print("\n 1. Add book")
    print("\n 2. Display all Book")
    print("\n 3. Exit")
    choice=input("Enter ur choice :")


    if choice == "1":
        title=input("Enter the title of book :")
        author=input("Enter the author of a book :")
        Book=books(title,author)
        lib.addbook(Book)
        print("Book Added")
    elif choice=="2":
        lib.displaybook()
    elif choice=="3":
        print("Exiting...")
        break
    else:
        print("Invalid input")