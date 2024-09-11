## What is this?

[Modal](https://modal.com) is a serverless computing platform for Python.

This folder demonstrates a simple pattern for developing a FastHTML app locally and deploying it to Modal,
including tips for debugging the deployed app.
Thanks to the power of open standards like ASGI, the integration between the two is seamless!

The code in `app.py` is carefully documented to help you re-use this template for serving your own apps.


## Setup

Set up a Python environment and then run the commands below on your local machine.

```bash
git clone https://github.com/AnswerDotAI/fh-deploy.git  # clone the repo
cd modal  # enter this directory
pip install -r requirements-dev.txt  # install the development dependencies
```

## Develop the app locally

FastHTML includes a local development server with automatic fast reloads for quick iteration.

Run it with

```bash
python app.py
```

and navigate to the URL shown in the terminal, which should begin with `localhost` or `127.0.0.1`.

Changes to the code will be reflected in the browser after you save the file.

This is great for working in a tight loop on core functionality.

You can stop the server with Ctrl-C.

## Develop the app on Modal

Modal can also run a web server in development mode.

If you haven't used Modal on the machine before, you'll need to obtain a token.

You can get one (and create an account if needed), by running

```bash
modal setup
```

and following the instructions on the screen and in your browser.

Once that's set up, you can run the development server with

```bash
modal serve app.py
```

and navigate to the URL in the terminal, which should end in `-dev.modal.run`.

Changes to the code (or requirements!) will trigger a new development deployment,
which should finish in seconds. This server can also be stopped with Ctrl-C.

This is useful for debugging issues that appear only in the production environment,
like issues with accessing secrets or issues with GPU acceleration.

You can also spin up a temporary shell to inspect the production environment:

```bash
modal shell app.py
cd root  # enter the root directory, where `app.py` is located
```

## Deploy the app on Modal

Deployment works much the same way, but creates a permanent server.

Deploy this server with

```bash
modal deploy app.py
```

and navigate to the URL that appears in the terminal, which should end in `.modal.run`.
It will be the same URL as your development server, but without the `-dev`.

Instead of shutting down when you close the terminal, it will continue to run
until you explicitly stop the app in the [Modal dashboard](https://modal.com/apps)
or via the [command line](https://modal.com/docs/reference/cli/app).

Unlike deployment to a traditional cloud server, this doesn't allocate a machine running your server.
Instead, your server is dynamically run on demand in Modal's infrastructure.
This can reduce costs for apps with highly variable traffic and enables easy scaling up and down of instances.

The catch is that there will be a second of extra latency when a user interacts with an app with no running instances.
You can read more about that [here](https://modal.com/docs/guide/cold-start).

Modal includes $30/month in free credits,
which is more than enough to host this application indefinitely.
Pricing information is [here](https://modal.com/pricing).
