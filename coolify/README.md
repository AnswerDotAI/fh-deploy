### Step 1 - Setup Coolify
- Setup Coolify on your server by following the [documentation](https://coolify.io/docs/installation), and open Coolify's UI.


### Step 2 - Make a Github App to be used as your source
- Click "Sources" in the left menu
- Click "Add Source", name your app, and click continue.
- Click "Register Now" on the Register a GitHub App screen
- Sign into Github, give your app a name, and click "Create Github App". You will then be redirected back to your Coolify instance.
- Click "Install Repositories on Github", and select your FastHTML app repo and click "Install".
- Once redirected back to Coolify, click Save on your Github app.


### Step 3 - Deploy your Github App
- In your Coolify project, click New, and then select "Private Repository (with GitHub App)"
- Select the app you made in step 2.
- Click "Load Repository"
- Ensure your build pack is set as "Nixpacks" and click continue.
- On the Configuration screen, on the General tab, under Network, and "Ports Exposes" ensure you list the ports your application uses separated by commas.
- Remember to click Save at the top of the General tab when updating your ports.
- Add any environment variables to the Environment Variables tab, remember to click Save.
- Click Deploy
- Once the deployment is finished, click Links, and click the link to your shiny new FastHTML app!