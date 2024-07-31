from fasthtml_hf import setup_hf_backup
from fasthtml.fastapp import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML", P("FastHTML on HuggingFace 🤗!"))

setup_hf_backup(app)
serve()
