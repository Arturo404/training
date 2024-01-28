from flask import Flask, request


books = []
authors = {}
id_cnt = 0

app = Flask(__name__)

@app.post("/addBooks")
def addBooks():
    global id_cnt

    data = request.json
    newBooks = data["newBooks"]

    for book in newBooks:
        bookTitle = book["bookTitle"]
        authorName = book["AuthorName"]

        already_exist = False

        for existing_book in books:
            if bookTitle == existing_book[1]:
                already_exist = True

        if(not already_exist):
            books.append((id_cnt, bookTitle, authorName))
            
            if authorName in authors:
                authors[authorName].append(id_cnt)
            else:
                authors[authorName] = [id_cnt]
            
            id_cnt += 1

    return [books, authors]



@app.get("/searchBookByAuthor/<authorName>")
def searchBookByAuthor(authorName):
    if authorName in authors:
        return [book[1] for book in books if book[0] in authors[authorName]]
    else:
        return []



@app.get("/searchAuthorByBook/<bookName>")
def searchAuthorByBook(bookName):
    for book in books:
        if book[1] == bookName:
            return book[2]
    
    return "BOOK NOT EXIST"
        


def bookIdToTitle(id):
    for book in books:
        if book[0] == id:
            return book[1]


@app.get("/library")
def library():
    library = {}
    for i, (authorName, bookIds) in enumerate(authors.items()):
        author_books = []
        for bookId in bookIds:
            bookTitle = bookIdToTitle(bookId)
            book = {"bookID": str(bookId), "bookTitle": bookTitle}
            author_books.append(book)
        
        library[authorName] = author_books
    
    output_dict = {"library": library}

    return output_dict

@app.post("/reset")
def reset():
    global books
    global authors
    global id_cnt

    books = []
    authors = {}
    id_cnt = 0
    
    return [books, authors]

if __name__ == "__main__":
    app.run()
