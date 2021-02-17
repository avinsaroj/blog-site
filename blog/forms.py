from django import forms
from .models import Contact,comment,Post,auther

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
class  ContactForm(forms.ModelForm):
    class Meta:
        model =  Contact
        fields = ['name','email','subject','message']
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))   
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}),
    )    
class Signup(UserCreationForm):
   
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label= 'Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email','username':'User Name'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})
                 ,'email':forms.EmailInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'})}

class  CommentForm(forms.ModelForm):
    class Meta:
        model =  comment
        fields = ['comment']
        widgets={'comment':forms.TextInput(attrs={'class':'form-control'})}
class  PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']  
        widgets={'title':forms.TextInput(attrs={'class':'form-control'})
                 ,'desc':forms.TextInput(attrs={'class':'form-control'})
                 }   
class autherform(forms.ModelForm):
    class Meta:
        model = auther
        fields = ['about','profession','image'] 
        widgets={'about':forms.TextInput(attrs={'class':'form-control'})
                 ,'profession':forms.TextInput(attrs={'class':'form-control'})
                 }          
class autherforms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})
                 ,'email':forms.EmailInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'})}          