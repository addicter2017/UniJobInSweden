from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
    email = forms.CharField(label='邮箱',max_length=256,widget=forms.EmailInput)
