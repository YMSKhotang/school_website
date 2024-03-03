# forms.py
from django import forms
from blog.models import Comment,Contact

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone_number', 'message']
        
    widgets = {
        'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        'phone_number': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
        'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Your Message'}),
    }



