from django import forms

class PostingForm(forms.Form):
    content = forms.CharField(widget=forms.TextInputm, label="content")
    place= forms.CharField(widget=forms.TextInputm, label="place")
    destination=
    due =
    cost=
    reward=
    comment=

    username = forms.CharField(widget=forms.TextInput, label="Username")
    email = forms.EmailField(widget=forms.TextInput, label="Email_address")
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="password(again)")