# Portfolio Contact Form Email Setup

The contact form sends email through Resend using Django Anymail. Secrets are read from environment variables and are not stored in the codebase.

## Required Environment Variables

```powershell
$env:RESEND_API_KEY="your-resend-api-key"
$env:CONTACT_RECEIVER_EMAIL="kumbharpramod834@gmail.com"
python manage.py runserver 127.0.0.1:8000
```

Optional:

```powershell
$env:DEFAULT_FROM_EMAIL="Pramod Portfolio <onboarding@resend.dev>"
```

For production, set the same variables in Vercel Project Settings.

## Important

For a professional production setup, verify your own domain in Resend and change `DEFAULT_FROM_EMAIL` to an address on that domain, for example:

```powershell
$env:DEFAULT_FROM_EMAIL="Pramod Portfolio <contact@yourdomain.com>"
```

If `RESEND_API_KEY` is not set, Django uses the console email backend locally. The form still submits, but the email prints in the terminal instead of being sent.
