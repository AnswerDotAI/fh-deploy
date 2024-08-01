# fh-deploy

This repo contains deployment guides for the platforms listed below.

| Platform                               | Deployment Guide                                                         |
|----------------------------------------|--------------------------------------------------------------------------|
| [HuggingFace](https://huggingface.co/) | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/huggingface)  |
| [Railway](https://railway.app/)        | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/railway)      |
| [Replit](https://replit.com/)          | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/replit)       |
| [Vercel](https://vercel.com/)          | [guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/vercel)       |

If you would like to add a guide for another platform feel free to fork this repo and submit a PR.

### Platform Agnostic Deployment
- [Uvicorn](https://www.uvicorn.org/) is the server used to run FastHTML apps. For general info on uvicorn deployments see this [guide](https://www.uvicorn.org/deployment/). 
- The Apache HTTP Server doesn't support ASGI deployments, which includes FastHTML. We suggest running [uvicorn behind nginx](https://www.uvicorn.org/deployment/#running-behind-nginx) instead.