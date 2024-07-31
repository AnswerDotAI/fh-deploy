### Setup
Run the commands below on your local machine.
```commandline
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd vercel
pip install -r requirements.txt
```

### Run the app locally
```commandline
python main.py
```
### Deploying to Vercel
Create a Vercel [account](https://vercel.com/) and then run the commands below on your local machine.

```commandline
npm install -g vercel
vercel login
vercel --prod
```

If you would prefer to deploy to Vercel using a git integration, see this guide for more [info](https://vercel.com/docs/deployments/git).