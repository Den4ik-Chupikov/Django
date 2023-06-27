from django import forms

class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length = 100)
    age = forms.IntegerField(label='My age')
    
class LoginForm(forms.Form):
    user_name = forms.CharField(label = "User name", max_length = 30)
    password = forms.CharField(label = "Password", max_length = 20)
    email = forms.EmailField(label ="Email", max_length = 30)

