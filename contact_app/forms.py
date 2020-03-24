from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'email',
            'message',
        ]
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': ' Your email address'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'rows': 5,
                    'placeholder': ' Your message'
                }
            ),
        }
