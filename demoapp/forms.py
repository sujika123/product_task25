from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, userlogin, Product


class DateInput(forms.DateInput):
    input_type = "date"

class Loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput,label='password')
    password2 = forms.CharField(widget = forms.PasswordInput,label='confirm password')
    class Meta:
        model = Login
        fields = ('username','password1','password2')

GENDER_CHOICES = (
    ('Female','Female'),
    ('Male','Male')
)

class Userloginform(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)
    class Meta:
        model = userlogin
        fields = ('name','age','gender','address','phone','image')

class productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('Product_name','Product_description','Product_quantity','Product_price')

