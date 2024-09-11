# fh-deploy

This repo contains deployment guides for the platforms listed below. Each guide contains a "hello world" style project which you'll setup on your local device before deploying it on the platform.

| Platform                                 | Deployment Guide                                                         |
|------------------------------------------|--------------------------------------------------------------------------|
| [HuggingFace](https://huggingface.co/)   | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/huggingface)  |
| [Railway](https://railway.app/)          | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/railway)      |
| [Replit](https://replit.com/)            | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/replit)       |
| [Vercel](https://vercel.com/)            | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/vercel)       |
| [Heroku](https://heroku.com/)            | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/heroku)       |
| [Droplet](https://www.digitalocean.com/products/droplets)   | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/droplet) [Docker + SSL guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/droplet-ssl-with-ci)     |
| [Fly.io](https://fly.io/)              | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/fly)         |
| [Coolify](https://coolify.io/)         | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/coolify)     |
| [Modal](https://modal.com/)         | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/modal)     |

If you would like to add a guide for another platform feel free to fork this repo and submit a PR.

### Platform Agnostic Deployment

- [Uvicorn](https://www.uvicorn.org/) is the server used to run FastHTML apps. For general info on uvicorn deployments see this [guide](https://www.uvicorn.org/deployment/).
- The Apache HTTP Server doesn't support ASGI deployments, which includes FastHTML. We suggest running [uvicorn behind nginx](https://www.uvicorn.org/deployment/#running-behind-nginx) or [Caddy](https://caddyserver.com/) instead.
