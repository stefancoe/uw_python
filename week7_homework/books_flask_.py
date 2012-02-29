"""
Minimal Flask + forms demo

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_flask.html
"""

from flask import Flask, request
import bookdb
# no need for template here - just a constant string
form_page = """<head>
<title>Echo request</title>
</head>
<body>
<form method="GET" action="echo_flask.py">
Message: <input type="text" name="message" size="40">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""

message_template2 = """
<html>
<head>
<title>Echo response</title>
</head>
<body>
%s
</body>
</html>
"""

# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines

# View functions generate HTTP responses including HTML pages and headers

@app.route('/echo_flask.html')
def form():
    books = bookdb.BookDB()
    titles = books.titles()
        #assert len(titles) > 1
        #print titles
    messages = ""
    for title in titles:
        x = title["title"]
        link = '<a href= ' + '"/' + x + '"' + '>%s</a><br>'
        messages = (link %x) + messages
        #messages = ('<a href=%s>%s</a><br>' %x) + messages # insert at head
        
        page = message_template2 % messages
    return  page  # li
@app.route('/echo_flask.py')
def message_page():
    # Flask Quickstart suggests request.form should work, but here it is empty
    # Flask converts return string to HTML page
    return 'Message: %s' % request.args['message']

@app.route('/<bookTitle>')
def book_info(bookTitle):
    books = bookdb.BookDB()
    titles = books.titles()
    messages = ""
    for title in titles:
        x = title["title"]
        if x == bookTitle:
            y = title["id"]
            
            messages = books.title_info(y)
            page = message_template2 % messages
        else:
            messages = "not found"
            page = message_template2 % messages
    return page 
     

# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    app.run()

