from json import load

f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\book.json")

data=load(f)

#for books in data:
   
  #  print(books)
#

#all_titles=[books.get("title")for books in data]

#print(all_titles)

#books with  pages<250

#ipage_filter=[book.get("title")for book in data if book.get("pages")<250]

#print(page_filter)

#print all genres

#all_genres=[books.get("genre")for books in data]

#print(set(all_genres))
#genre_count={genre:all_genres.count(genre)for genre in all_genres}

#print(genre_count)

# print costly books

#costly_books=max(data,key=lambda d:d.get("price"))

#print(costly_books)

#author with more than one book

all_author=[books.get("author")for books in data]

print(all_author)


author_count={author:all_author.count(author) for author in all_author}

print((k for k,v in author_count.items()if v>1))