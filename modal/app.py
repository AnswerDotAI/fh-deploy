from pathlib import Path

import fasthtml.common as fh
import modal

# create the fasthtml_app object and its rt decorator
fasthtml_app, rt = fh.fast_app()


# define the app first, e.g. adding routes
# FastHTML uses decorators to add routes:
@rt("/")
def get():
    return fh.Titled("FastHTML", fh.P("FastHTML on️ Modal!"))


if __name__ == "__main__":  # if invoked with `python`, run locally
    fh.serve(app="fasthtml-app")
else:  # create a modal app, which can be imported in another file or used with modal commands as in README
    app = modal.App(name="fasthtml-app")

    # modal uses decorators to define infrastructure and deployments
    @app.function(  # here's where you can attach GPUs, define concurrency limits, etc.
        image=modal.Image.debian_slim().pip_install_from_requirements(  # see https://modal.com/docs/guide/custom-container for more ways to install dependencies
            Path(__file__).parent / "requirements.txt"
        ),
        allow_concurrent_inputs=1000,  # async functions can handle multiple inputs
    )
    @modal.asgi_app()  # add this decorator to a function that returns your fastHTML app to make it deployable on Modal
    def serve():
        return fasthtml_app
