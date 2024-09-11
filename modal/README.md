### Setup
Run the commands below on your local machine.
```bash
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd modal
pip install -r requirements.txt
```

### Run the app locally
```bash
python app.py
```

### Deploying to Modal

First, install the [Modal](https://modal.com/) client:

```bash
pip install modal
```

Then, you need to obtain a token from Modal. Run the following command:

```bash
modal setup
```

Once that is set, you can setup the Modal app by running:

```bash
modal deploy deploy.py
```