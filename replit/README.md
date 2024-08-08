# Building and deploying on Replit

<div align="center">
   <img src="https://github.com/user-attachments/assets/c838618a-992c-4d9a-84ae-cbb9b7d37a4e" width="15%"/>
</div>


Replit is a cloud-based development and deployment platform that allows you to build and deploy in a single, integrated environment.
It comes with tools like [secrets management](https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables) and [AI assisted coding](https://docs.replit.com/programming-ide/ai-code-completion), and has good Python, JS, HTML, and CSS support for FastHTML apps. Replit also has cloud services like [object storage](https://docs.replit.com/storage/replit-database), [embedded Postgres](https://docs.replit.com/hosting/databases/postgresql-database), and [key-value databases](https://docs.replit.com/hosting/databases/replit-database).

<div align="center">
   <img src="https://github.com/user-attachments/assets/562c06ad-8407-4d4a-b91e-c94e06471e11" width="75%"/>
</div>

## Setup

To get started on Replit, follow these steps:

1. Create a Replit [account](https://replit.com/),
2. Fork this Replit [template](https://replit.com/@jh151/FastHTML?v=1), which contains the same code in this folder.
3. To run the app click `Run` in the nav bar.

A web view pane will open up with your application. Edit the code in the editor to see changes in real time.

**An important note:** because Replit is a cloud-based editor, the [development URL](https://docs.replit.com/additional-resources/add-a-made-with-replit-badge-to-your-webview#what-is-the-webview) is accessible from any device (while your Repl is running). That means you can test your app out on desktop and mobile simultaneously.

<div align="center">
   <img src="https://github.com/user-attachments/assets/85141ad6-aec9-4d75-ab2a-47cb25a4ca22" width="75%"/>
</div>

## Deployment

Deployment on Replit can be done in a few steps:

1. Click `Deploy` in the top navigation bar of your Repl.
2. Choose a deployment type:
   - For frontend apps, select "Autoscale" deployments. These automatically scale based on traffic.
   - For services requiring continuous execution (e.g., backends, APIs, bots), choose "Reserved VM" deployments.
3. Select a custom subdomain for your app or use the auto-generated one.
4. Configure your deployment settings, including environment variables if needed.
5. Review and confirm your deployment configuration.

Important notes:
- You'll need to add a payment method to deploy your app.
- Additional options can be configured in the `.replit` file present in your project, note that you may have to reveal hidden files if you can't see it. For more information on configuring the `.replit` file, refer to the [docs](https://docs.replit.com/programming-ide/configuring-repl).
- For detailed instructions and advanced configuration options, refer to the [official Replit deployment documentation](https://docs.replit.com/hosting/deployments/about-deployments).

For a sample Replit app that makes use of the key-value database, go [here](https://replit.com/@matt/FastHTML-guestbook?v=1#README.md) or check out the live version [here](https://guestbook.mattpalmer.io) and follow the same instructions.

### Custom Domains

Replit automatically assigns your website a unique domain name such as `your-app-name-your-username.replit.app`. However, if you want to use your own domain that you've purchased through services like [CloudFlare](https://www.cloudflare.com/) or [Name-cheap](https://www.namecheap.com/), you can configure it in your Replit deployment settings. Here's how:

1. Go to your Repl's "Deployment" tab.
2. Click on "Configure custom domain".
3. Enter your custom domain name and follow the instructions to set up DNS records with your domain provider.

Make sure to notice the difference between setting up a root domain and a subdomain. Root domains don't have any prefixes before the main site name (e.g., `example.com`), while subdomains do (e.g., `subdomain.example.com`). The setup process might differ slightly for each. Always refer to your domain registrar's documentation for specific instructions on how to set up DNS records for your custom domain.

For more detailed information on setting up custom domains in Replit, you can refer to their official documentation [here](https://docs.replit.com/hosting/deployments/custom-domains).
