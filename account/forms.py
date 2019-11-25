from django import forms
from . models import profile
from django.contrib.auth.models import User
from betterforms.multiform import MultiForm
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):

    class Meta:
        model=profile
        fields=('studentnum','groupname','major','name')
        labels={
            'studentnum':('학번'),
            'groupname':('소속 동아리'),
            'major':('소속 동아리 분과'),
            'name':('이름'),
        }

class UserCreationMultiForm(MultiForm):
    labels={'username':('아이디')}
    form_classes={
        'user':UserCreationForm,
        'signup':ProfileForm,

    }
