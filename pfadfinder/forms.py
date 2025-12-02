from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    betreff = forms.CharField(max_length=200) # Subject
    notiz = forms.CharField(widget=forms.Textarea) # Note/Message