# Code from here: https://github.com/arihanv/fasthtml-modal/blob/main/deploy.py
from modal import App, Image, asgi_app
from app import fasthtml_app

app = App(name="fasthtml-app")

image = Image.debian_slim(python_version="3.11").pip_install(
    "python-fasthtml"
)

@app.function(image=image)
@asgi_app()
def get():
    return fasthtml_app