# Assignment: Homework 12 Question 3
# Date: 12/9/21
# Author: Spencer Lage
# Description: This program will take a Database file and do several different commands

import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

# Question A

a = pd.read_sql("""SELECT last FROM authors ORDER BY last DESC""", connection)
print()
print(a)
print()

# Question B

b = pd.read_sql("""SELECT * FROM titles ORDER BY title ASC """, connection)
print()
print(b)
print()

# Question C

c = pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER 
                BY last, first""", connection).head()
print()
print(c)
print()

# Question D

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Spencer', 'Lage')""")
d = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])

print()
print(d)
print()

# Question E

cursor1 = connection.cursor()
cursor1 = cursor1.execute("""INSERT INTO titles (title) VALUES ('cod')""")
e = pd.read_sql('SELECT id, titles last FROM titles', connection, index_col=['title'])

print()
print(e)
print()
