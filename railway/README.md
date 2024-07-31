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

_Note_:
- `fh_railway_deploy` can take a minute or so to complete.
- you can find your app's url in your Railway [dashboard](https://railway.app/dashboard) 
- `fh_railway_deploy` assumes your app's entry point is located in a `main.py` file.
