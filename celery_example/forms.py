from django import forms


class ReminderForm(forms.Form):
    email = forms.EmailField()
    reminding_text = forms.CharField(max_length=200, widget=forms.Textarea)
    reminding_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

