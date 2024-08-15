from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML", P("FastHTML on a Digital Ocean's Droplet!"))

#serve()
