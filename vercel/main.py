from fasthtml.fastapp import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML", P("FastHTML on Vercel!"))

serve()
