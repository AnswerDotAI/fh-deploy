### Setup

Run the commands below on your local machine.

```commandline
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd heroku 
pip install -r requirements.txt
```

### Run the app locally

```commandline
python main.py
```
### Deploying to Heroku
Create a Heroku [account](https://signup.heroku.com/), install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and then run the commands below on your local machine:

```commandline
heroku login
heroku create <app-name>
git subtree push --prefix heroku heroku main
```

> [!NOTE]
> `git subtree` is only used to deploy the `heroku` subfolder, on projects where your FastHTML is the main app you can just use `git push heroku main`

For more information on how to deploy Python applications to Heroku refer to the [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python) docs.
