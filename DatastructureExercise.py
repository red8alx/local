#Exercise 1: Create a list to store names of your favorite fruits. Write code to access the second element and print it.
"""myFruits = ["Apple","Orange", "Banana", "Mango"]
print(f"The second element of the list is: {myFruits[1]}")
#Exercise 2: Define a dictionary to store information about your favorite book, including title, author, and genre. Use the method to retrieve the genre.
myFavBook = {
    "title" : "C++ Explained",
    "author" : "Rediet A.",
    "genre" : "Technology"
    }
bookGenre = myFavBook.get("genre")
print(f"The Book genre is: {bookGenre}")
myFavBook.update({'page_size' : '345'})
print(f"Page size of {myFavBook.get('title')} is {myFavBook.get('page_size')}")
#Exercise 3: Write a program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.
"""
import random
n = 5 #number of random numbers to be generated
my_set = set()
for i in range(n):
    random_number = random.randint(1,10)
    print(f"Number generated: {random_number}")
    my_set.add(random_number)
print(f"The numbers in the set are: {my_set}")
