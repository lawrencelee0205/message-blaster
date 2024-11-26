from django import forms

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=15)

class VerificationCodeForm(forms.Form):
    code = forms.CharField(label='Verification Code', max_length=6)

class MessageForm(forms.Form):
    message = forms.CharField(label='Message', max_length=100)