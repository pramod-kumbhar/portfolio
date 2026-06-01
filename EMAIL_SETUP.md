# Portfolio Contact Form Email Setup

The contact form is ready to send email through SMTP. It reads credentials from environment variables so passwords are not saved in the project.

## Gmail Setup

1. Turn on 2-Step Verification for the Gmail account.
2. Create a Gmail App Password.
3. Start Django with these environment variables:

```powershell
$env:EMAIL_HOST_USER="kumbharpramod834@gmail.com"
$env:EMAIL_HOST_PASSWORD="your-16-character-app-password"
$env:CONTACT_RECEIVER_EMAIL="kumbharpramod834@gmail.com"
python manage.py runserver 127.0.0.1:8000
```

Optional values:

```powershell
$env:EMAIL_HOST="smtp.gmail.com"
$env:EMAIL_PORT="587"
$env:EMAIL_USE_TLS="True"
$env:DEFAULT_FROM_EMAIL="kumbharpramod834@gmail.com"
```

Without `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`, Django uses the console email backend for local testing. The form still works, but messages print in the terminal instead of being delivered.
