import bookdb

books = bookdb.BookDB()
titles = books.titles()
assert len(titles) > 1
#print titles
messages = ""
for title in titles:
    x = title["title"]
    print x
    
    #messages = ('%s<br>\n' % str(title)) + messages # insert at head
    
            
print messages
    
