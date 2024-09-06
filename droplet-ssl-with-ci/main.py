from fasthtml.common import *

app,rt = fast_app()
db = database('data/yourdatabase.db')

@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

@rt("/healthcheck")
def get(): return JSONResponse({"status": "ok"})

serve()
