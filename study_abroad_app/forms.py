from django import forms
from .models import CounsellorMessage, CounsellingPopup, ContactMessage

class CounsellorMessageForm(forms.ModelForm):
    class Meta:
        model = CounsellorMessage
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'city', 'state', 'target_country', 'target_intake', 'message'
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'required': True}),
            'city': forms.TextInput(attrs={'placeholder': 'City', 'required': True}),
            
            # Use a class for Choices.js
            'state': forms.Select(attrs={'required': True, 'class': 'choices-select'}),
            'target_country': forms.Select(attrs={'required': True, 'class': 'choices-select'}),
            'target_intake': forms.Select(attrs={'required': True, 'class': 'choices-select'}),
            
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 4}),
        }

class CounsellingPopupForm(forms.ModelForm):
    class Meta:
        model = CounsellingPopup
        fields = ['name', 'email', 'phone', 'message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone','subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control', 'required': True}),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Your Phone',
                'class': 'form-control',
                'required': True,
                'pattern': '[0-9]{10}',
                'title': 'Enter 10 digit phone number'
            }),
            'subject':forms.TextInput(attrs={'placeholder': 'Your Subject', 'class': 'form-control', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 4, 'required': True}),
        }
