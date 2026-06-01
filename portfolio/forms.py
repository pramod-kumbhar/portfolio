from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Your name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"}),
    )
    subject = forms.CharField(
        max_length=140,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Project or partnership"}),
    )
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Write your message"}),
    )
