from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Type Your Message'}))
