from classes import Author, BookItem, BookStore
from pydantic import ValidationError 

def main():
    try:
        author_info1 = Author(name = "John Doe", author_id = "JODO-1234")
        author_info2 = Author(name = "Alana Grey", author_id = "ALGR-1234")

        book_item1 = BookItem(name="The Sky is Blue", author=author_info1, year_published = 2023)
        book_item2 = BookItem(name="What to eat today?", author=author_info2, year_published = 2020)
    
        book_store = BookStore(bookstore_name="Whitcoulls", book_shelf=[book_item1, book_item2])
              
    except ValidationError as ve: 
        print("The Author's information/Book information has to be valid.")
    except: #Catch other error that I may not consider
        print("Another Error")
    else: 
        bookstore = book_store.__dict__
        print(bookstore)
    #finally: #Whatever errors happen, the code will still print the final.
        #print("Finally")
    
if __name__=="__main__":
    main()

