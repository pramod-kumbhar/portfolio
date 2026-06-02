# Portfolio Contact Form Email Setup

The contact form sends email through Resend, a modern email service API. It reads the API key from environment variables so credentials are not saved in the project.

## Resend Setup

1. Create a free account at [https://resend.com](https://resend.com)
2. Verify your domain or use the provided Resend domain (onboarding@resend.dev)
3. Get your API key from the Resend dashboard
4. Start Django with the environment variable:

```powershell
$env:RESEND_API_KEY="re_your_api_key_here"
$env:CONTACT_RECEIVER_EMAIL="your-email@example.com"
python manage.py runserver 127.0.0.1:8000
```

### Optional Configuration

```powershell
$env:DEFAULT_FROM_EMAIL="noreply@yourdomain.com"
```

If you own a domain, configure it in Resend to send from your custom domain instead of onboarding@resend.dev.

## Testing Locally

To test locally without Resend API key, set `RESEND_API_KEY` to empty or use a mock. The form validation will work, but email sending will fail gracefully with an error message.

## Environment Variables Reference

- `RESEND_API_KEY` - Your Resend API key (required for sending emails)
- `CONTACT_RECEIVER_EMAIL` - Email address to receive contact form submissions (defaults to portfolio owner email)
- `DEFAULT_FROM_EMAIL` - Email address to send from (defaults to onboarding@resend.dev)

