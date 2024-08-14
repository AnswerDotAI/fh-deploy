from fasthtml.fastapp import fast_app, Titled, P

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML", P("FastHTML on a Digital Ocean's Droplet!"))

#serve()
