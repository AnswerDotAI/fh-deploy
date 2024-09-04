from fasthtml import fastapp as fh

app, rt = fh.fast_app()


@rt("/")
def get():
    return fh.Titled("FastHTML", fh.P("FastHTML on Fly.io!"))


if __name__ == "__main__":
    fh.serve(port=8080)
