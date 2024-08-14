# Deploying a fastHTML Web App on a DigitalOcean Droplet

This guide details the process of setting up a $4/month Ubuntu Virtual Machine (Droplet) on DigitalOcean to host a fastHTML web application. It leverages the DigitalOcean API to streamline the creation and configuration of SSH keys and the Droplet.

### References
- [How to Create a Droplet](https://docs.digitalocean.com/products/droplets/how-to/create/)
- [How to Create a Personal Access Token](https://docs.digitalocean.com/reference/api/create-personal-access-token/)
- [How To Install Python 3 and Set Up a Programming Environment on an Ubuntu 20.04 Server](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server)
- [Cómo subir una app con FastAPI a DigitalOcean](https://www.youtube.com/watch?v=ZZNZbnTbodI)
- [DEPLOY a DJANGO app with SQLite database on DIGITALOCEAN (Ubuntu 22.04) -- NO DOCKER](https://www.youtube.com/watch?v=pUG-uNzWAf4)


### Setup
Run the commands below on your local machine.

```commandline
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd fh-deploy/droplet
pip install -r requirements.txt
```

### Run the app locally
```commandline
uvicorn main:app --reload
```

### Deploying to DigitalOcean

#### Setting Up DigitalOcean

1. Create a DigitalOcean [account](https://www.digitalocean.com/)
2. Create a new Personal Access Token [here](https://cloud.digitalocean.com/account/api/tokens)
3. Create a `DIGITALOCEAN_TOKEN` environment variable (e.g. run `export DIGITALOCEAN_TOKEN=YOUR_API_TOKEN`).

#### Create an SSH key

[API Docs](https://docs.digitalocean.com/reference/api/api-reference/#operation/sshKeys_create)

1. Create a public key.
2. When asked, save it to `/home/{user}/.ssh/{public_key_filename}`.
3. Store it as an environment variable `PUBLIC_KEY`.

```commandline
ssh-keygen
(...)
export PUBLIC_KEY=$(cat /home/{user}/.ssh/{public_key_filename}.pub)
```
4. Generate the SSH key using the API endpoint and passing the public key.

```curl
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  -d '{"name":"fastHTML SSH Public Key","public_key":"'"$PUBLIC_KEY"'"}' \
  "https://api.digitalocean.com/v2/account/keys" 
```

5. After the API call, copy the returned SSH key ID and store it as an environment variable (e.g. run `export SSH_KEY_ID=YOUR_SSH_KEY_ID`).


#### Creating a new Droplet

[API Docs](https://docs.digitalocean.com/reference/api/api-reference/#operation/droplets_create)

1. While the DigitalOcean interface offers Droplet creation, this guide demonstrates the process using the API.

The $4/month Droplet will have the following specifications:

- name: `fastHTML-Droplet`
- region: `nyc1`
- size: `s-1vcpu-512mb-10gb` (1 CPU, 512 MB, 10 GB SSD Disk)
- OS: `Ubuntu 22.04 (LTS) x64`

```curl
$ curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  -d '{"name":"fastHTML-Droplet","region":"nyc1","size":"s-1vcpu-512mb-10gb","image":"ubuntu-22-04-x64","ssh_keys":['"$SSH_KEY_ID"']}' \
  "https://api.digitalocean.com/v2/droplets"
```
Go to [droplets](https://cloud.digitalocean.com/droplets) and see the that was just created:

![](01_droplet.PNG)

2. Save the IP address as an environment variable `export IP_ADDRESS=<DROPLET_IP_ADDRESS>`

3. Before attempting to SSH into the Droplet, ensure the security of your public SSH key file by setting its permissions appropriately. 
   
```commandline
chmod 600 /home/{user}/.ssh/{public_key_filename}.pub
ssh -i /home/{user}/.ssh/{public_key_filename} root@$IP_ADDRESS
```
4. If everything has been configured correctly, you should be able to connect successfully.

![](02_droplet.PNG)

#### Configuring the Droplet as a web server

1. After the SSH connection is established, configure the remote server.

These commands prepare your Ubuntu system for Python development and web application deployment by updating packages, installing necessary tools and libraries, and setting up a web server (Nginx).

```commandline
sudo apt-get update
sudo apt update
sudo apt -y upgrade
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-setuptools python3-venv
sudo apt install nginx
```

If asked, reboot the server with `sudo reboot`


2. Clone the repository

```commandline
mkdir project
cd project
python3 -m venv env
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd fh-deploy/droplet
pip install -r requirements.txt
```


















### Deploying to DigitalOcean's Droplet

- create a Railway [account](https://railway.app/) and signup to the Hobby plan. 
- install the Railway [CLI](https://docs.railway.app/guides/cli#installing-the-cli).
- run `railway login` to log in to your Railway account.
- run `fh_railway_deploy YOUR_APP_NAME`.

⚠️ Your app's entry point must be located in a `main.py` file for this to work.

### Supplementary Info.
`fh_railway_deploy` runs the following commands behind the scenes for you:

```bash
railway init -n <app-name>
railway up -c
railway domain
railway link ...
railway volume add -m /app/data
```

It handles automatically linking your current app to a railway project, setting up all the environment variables such as the port to listen on and setting up a `requirements.txt` if you haven't one already.

### Customizing your Domain Name

Railway automatically assigns your website a unique domain name such as `quickdraw-production.up.railway.app`. However, if you want to use your own that you've purchased through services like [GoDaddy](https://www.godaddy.com/) or [Squarespace Domains](https://domains.squarespace.com/) and have users be able to navigate to your site using that domain, you'll need to configure it both in your domain registration service and in Railway. Railway has put together a nice tutorial for setting it up [here](https://docs.railway.app/guides/public-networking#custom-domains).

Make sure to notice the difference between setting up a regular domain and a subdomain. Regular domains don't have any prefixes before the main site name such as `example.com` and is setup differently from a subdomain which might look like `subdomain.example.com`. Make sure to follow your domain registration service's documentation on how to set these types up.