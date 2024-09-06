# Run FastHTML on your Digital Ocean droplet

> If you don't need SSL and extra bells and whistles or do not want to use Docker, check out [this guide](https://github.com/AnswerDotAI/fh-deploy/tree/main/droplet)


What's included:

- SQLite database
- SSL using [SWAG](https://github.com/linuxserver/docker-swag)
- CI using GH actions

# Getting started

## Droplet + SSL

Let's get a droplet up and get SSL to work

- create [a droplet](https://cloud.digitalocean.com/droplets?i=102a02)
- create or use your existing [container registry](https://cloud.digitalocean.com/registry)
- point your domain/subdomain to your droplet IP (using `A Record`)
- ssh into your droplet and [install docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- stay in your droplet and configure swag; replace `YOUR_DOMAIN_HERE` with your domain (e.g. `fasthtml.com`)

```bash
touch docker-compose.yml
echo "services:
  swag:
    image: lscr.io/linuxserver/swag:latest
    container_name: swag
    cap_add:
      - NET_ADMIN
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - URL=YOUR_DOMAIN_HERE
      - VALIDATION=http
    volumes:
      - /etc/config/swag:/config
    ports:
      - 443:443
      - 80:80
    restart: unless-stopped
" > docker-compose.yml

docker compose up
```
- navigate to your domain (e.g. https://fasthtml.com) and make sure you see SWAG welcome message `Welcome to your SWAG instance`
- stop the container (Ctrl+C)
- clean up

```bash
rm docker-compose.yml
docker rm swag
```

## Github 

Configure GH actions to build and deploy the app to your droplet. Start by generating SSH key-pair to access server from GH CI server

```bash
ssh-keygen -f ./id_rsa -t rsa -b 4096 -C "YOUR EMAIL HERE"
```

Grab the public key 

```bash
cat ./id_rsa.pub
```

SSH into your droplet and add it to `~/.ssh/authorized_keys`

```bash
echo "YOUR_PUBLIC_KEY" >> ~/.ssh/authorized_keys
```

Head to `Settings > Secrets and variables > Actions` for your GH repository and set the following secrets


| Input Parameter    | Description            |
|--------------------|------------------------|
| SSHKEY             | SSH private key that you generated above using ssh-keygen (`id_rsa`)        |
| PASSPHRASE         | Passphrase used when running ssh-keygen |
| HOST_IP            | IP address of your droplet |
| HOST_URL           | Your app URL (e.g. `fasthtml.com` )   |
| HEALTH_CHECK_URL   | e.g. `https://fasthtml.com/healthcheck`|
| SERVER_APP_DIRECTORY | smth like `/opt/your_app_name`      |
| DOCKER_REGISTRY     |  URL of your docker registry on Digital ocean (smth like `registry.digitalocean.com/YOUR_REGISTRY_NAME`) |
| DOCKER_IMAGE        | name for you application's docker image |
| DIGITALOCEAN_ACCESS_TOKEN | Digital ocean access token - needs at least `registry` and `image` scopes, get it [here](https://cloud.digitalocean.com/account/api/tokens) looks smth like `dop_v1_XXXXXXXX`|
| PRODUCTION_DOT_ENV | `.env` style file content for your application specific env vars (can start with `FOO=bar` for now) |

## Credits

- [SWAG](https://github.com/linuxserver/docker-swag)
- [Full CI/CD with Docker + GitHub Actions + DigitalOcean (Droplets + Container Registry)](https://faun.pub/full-ci-cd-with-docker-github-actions-digitalocean-droplets-container-registry-db2938db8246)
