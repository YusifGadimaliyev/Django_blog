from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailInput()
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('passwords do not match')
        return password2


class UserProfileForm(forms.ModelForm):
    men = "K"
    women = "Q"
    choice = "gender"
    genders = (
        (men, "Kişi"),
        (women, "Qadın"),
        (choice, "gender")
    )

    gender = forms.CharField(widget=forms.Select(choices=genders), required=False)
    bio = forms.CharField(widget=forms.Textarea, max_length=100, label="Your bio", required=False)
    birth_date = forms.DateField(widget=forms.SelectDateWidget, label="Your Birth Date", required=False)
    phone_num = forms.CharField(max_length=15, label="Your phone number", required=False)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'gender', 'bio', 'birth_date', 'phone_num']
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class': 'form-control'}


class UserProfileEdit(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'bio', 'birth_date', 'phone_num']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('You entered username or password incorrectly !')
        return super(LoginForm, self).clean()

