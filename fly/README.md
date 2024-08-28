### Setup

Run the commands below on your local machine.

```commandline
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd fly
pip install -r requirements.txt
```

### Run the app locally

```commandline
python main.py
```

### Deploying to Fly.io

1. Create a Fly.io [account](https://fly.io/)
2. install the [CLI](https://fly.io/docs/flyctl/install/)
3. run the command `fly launch`
4. answer "n" when asked: `Do you want to tweak these settings before proceeding? (y/N)`

Once your app is deployed, the CLI will display the endpoint.
