from fasthtml.common import *

fasthtml_app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML", P("FastHTML on Modal!"))

serve(app='fasthtml_app')
