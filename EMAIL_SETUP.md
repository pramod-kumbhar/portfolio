# Portfolio Contact Form SMTP Email Setup

The contact form sends email through Gmail SMTP when credentials are available in environment variables.

Secrets are not stored in code.

## Local PowerShell Setup

```powershell
$env:EMAIL_HOST="smtp.gmail.com"
$env:EMAIL_PORT="587"
$env:EMAIL_USE_TLS="True"
$env:EMAIL_HOST_USER="your-gmail-address@gmail.com"
$env:EMAIL_HOST_PASSWORD="your-16-character-gmail-app-password"
$env:CONTACT_RECEIVER_EMAIL="your-gmail-address@gmail.com"
$env:DEFAULT_FROM_EMAIL="your-gmail-address@gmail.com"
python manage.py runserver 127.0.0.1:8000
```

Without `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`, Django uses the console email backend locally. The contact form will submit, but the email will print in the terminal instead of being delivered.

## Gmail Requirement

Gmail SMTP does not work with your normal Gmail password. You must enable 2-Step Verification and create an App Password.
