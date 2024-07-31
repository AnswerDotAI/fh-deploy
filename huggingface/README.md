### Setup
Run the commands below on your local machine.
```commandline
git clone https://github.com/AnswerDotAI/fh-deploy.git
cd huggingface
pip install -r requirements.txt
```

### Run the app locally
```commandline
python main.py
```
### Deploying to HuggingFace
1. Create a Huggingface [account](https://huggingface.co/).
2. Go to your account settings and create an access token with write access. Keep this token safe and don't share it.
3. Create a `HF_TOKEN` environment variable (e.g. run `export HF_TOKEN=YOUR_API_TOKEN`).
4. HuggingFace Spaces are [configured](https://huggingface.co/docs/hub/spaces-config-reference#spaces-configuration-reference) using a YAML block at the top of the app's README.md. To configure the HuggingFace Space for your app, add the YAML below to the top of **THIS** README.md file.
```yaml
---
title: FastHTML on HuggingFace!
emoji: 🤗
colorFrom: indigo
colorTo: green
sdk: docker
pinned: false
---
```

5. Run `fh_hf_deploy NAME_OF_YOUR_APP`

Note: 
- By default, your app will be public. To create a private app use `--private true` when running `fh_hf_deploy`.
- For more information on how your app is being deployed on HuggingFace visit the fasthtml-hf [repo](https://github.com/AnswerDotAI/fasthtml-hf)