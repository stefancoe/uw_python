"""
Minimal Flask + forms demo

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_flask.html
"""

from flask import Flask, request
import bookdb

# no need for template here - just a constant string
titles_template = """<head>

<title>Echo request</title>
</head>
<body>
<form method="GET" action="echo_flask.py">
Message %s
<input type="submit" value="Submit">
</form>
</body>
</html>
"""
titles_template2 = """
<html>
<head>
<title>Echo response</title>
</head>
<body>
Message %s
</body>
</html>
"""



# Global varible


# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines

# View functions generate HTTP responses including HTML pages and headers

@app.route('/test.html')
def form():
    books = bookdb.BookDB()
    titles = str(books.titles())
    #assert len(titles) > 1
    #print titles
    messages = ""
    for title in titles:
        x = str(title["title"])

        messages = ('%s<br>\n' % x) + messages # insert at head
    page = titles_template % messages

    
    return  page  # list of strings - must return iterable, not just a string


    #return form_page

@app.route('/echo_flask.py')
def message_page():
    # Flask Quickstart suggests request.form should work, but here it is empty
    # Flask converts return string to HTML page
    return 'Message: %s' % request.args['message']

# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    app.run()

