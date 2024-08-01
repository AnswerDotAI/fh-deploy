### Setup
Run the commands below on your local machine.
```commandline
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd railway
pip install -r requirements.txt
```

### Run the app locally
```commandline
python main.py
```
### Deploying to Railway
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