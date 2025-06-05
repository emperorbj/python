# def getMessage(param,reply):
#     return f"""This is a response {reply} from this question {param}"""


# productList = []

# def addProduct(product):
#     productList.append(product)
#     print('product added')

# def getProduct():
#     return productList

# addProduct({"name": "Apple Laptop", "price": 2000})
# addProduct({"name": "Samsung Monitor", "price": 300})


# print(getProduct()[0].get("name"))
# print(getProduct()[0].get("price"))



# def get_discount_customers(array):
#     discount_level = 500
#     for customer in array:
#         try:
#             total_spent = sum(purchase["price"] for purchase in customer["purchases"])
#             if total_spent >= discount_level:
#                 print(f"""{customer["name"]} your qualified for a discount """)
#         except (ValueError,TypeError) as e:
#             print(f""" Error trying to run this {customer["name"]} due to {e}  """)



# customers = [
#     {"name": "Alice Johnson", "purchases": [{"item": "Laptop", "price": 999.99}, {"item": "Mouse", "price": 29.99}]},
#     {"name": "Bob Smith", "purchases": [{"item": "Headphones", "price": 89.0}, {"item": "Keyboard", "price": 59.99}, {"item": "Monitor", "price": 199.99}]},
#     {"name": "Clara Davis", "purchases": [{"item": "Phone", "price": 499.99}]},
#     {"name": "David Lee", "purchases": [{"item": "Tablet", "price": 299.99}, {"item": "Charger", "price": 19.99}]}
#         ]

# get_discount_customers(customers)






# import json

# class Book:
#     def __init__(self,title,author,isbn):
#         try:
#             self.title = title
#             self.author = author
#             self.isbn = isbn
#             self.is_available = True
#         except (ValueError,TypeError,AttributeError) as e:
#             return f"error due to {e}"
    
#     def book_available(self):
#         try:
#             if self.is_available:
#                 self.is_available = False
#                 return f"{self.title} is taken by you"
#             else:
#                 return f"{self.title} is available in the library"
#         except (ValueError,TypeError,AttributeError) as e:
#             return f"error due to {e}"
        
#     def return_book(self):
#         try:
#             if not self.is_available:
#                 self.is_available = True
#                 return f"{self.title} has been returned to the library"
#             else:
#                 return f"{self.title} is not yet in the library"
#         except (ValueError,TypeError,AttributeError) as e:
#             return f"error due to {e}"
    
#     def get_info(self):
#         try:
#             status = "Available" if self.is_available else "Unavailable"
#             return f"{self.title} with ISBN:{self.isbn} \n and Author:{self.author} is {status}"
#         except (ValueError,TypeError,AttributeError) as e:
#             return f"error due to {e}"
#     def to_dict(self):
#         return {
#             "book_name": self.title,
#             "author": self.author,
#             "ISBN":self.isbn
#         }
    
# def save_library(library,filename="new.txt"):
#         with open(filename,'w') as file:
#             json.dump([book.to_dict() for book in library],file,indent=4)
#         print("books added to file")
    
# library = [
#     Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"),
#     Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789"),
#     Book("1984", "George Orwell", "978-0451524935")
# ]

# for book in library:
#     try:
#         print(book.book_available())
#         print(book.get_info())
#         print(book.return_book())
#     except Exception as e:
#         print (f"error due to {e}")
    
# save_library(library)

file = open('new.txt','r')
email = file.read()
for items in email:
    print(items)

