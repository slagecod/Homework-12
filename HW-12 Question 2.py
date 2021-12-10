# Assignment: Homework 12 Question 2
# Date: 12/9/21
# Author: Spencer Lage
# Description: This program will take a Database file and do several different commands
import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

pd.options.display.max_columns = 10
a = pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])
b = pd.read_sql('SELECT * FROM titles', connection)
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
c = pd.read_sql('SELECT first, last FROM authors', connection)
d = pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)
e = pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id'])
f = pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id'])
g = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
h = pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last, first""", connection, index_col=['id'])
i = pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""", connection, index_col=['id'])
j = pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY 
                title""", connection)
k = pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER 
                BY last, first""", connection).head()

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")

l = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])

cursor = cursor.execute("""UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'""")
m = cursor.rowcount

n = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])

cursor = cursor.execute('DELETE FROM authors WHERE id=6')

o = cursor.rowcount

p = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])

q = pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3)

r = pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection)

s = pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY 
                title""", connection)

# print commands
print(a)
print()
print(b)
print()
print(df.head())
print()
print(c)
print()
print(d)
print()
print(e)
print()
print(f)
print()
print(g)
print()
print(h)
print()
print(i)
print()
print(j)
print()
print(k)
print()
print(l)
print()
print(m)
print()
print(n)
print()
print(o)
print()
print(p)
print()
print(q)
print()
print(r)
print()
print(s)
print()
