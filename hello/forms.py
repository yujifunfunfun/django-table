from django import forms
from . import models
from .models import Kimetsu

class KimetsuForm(forms.Form):
    name = forms.CharField(max_length=10, label='名前')
    CHOICE = {
      ('男','男'),
      ('女','女'),
    }
    gender = forms.ChoiceField(label='性別',widget=forms.RadioSelect,choices=CHOICE,initial=0)
    features = forms.CharField(max_length=100, label='特徴')
    def save(self):
        data = self.cleaned_data
        post = Kimetsu(name=data['name'], gender=data['gender'], features=data['features'])
        post.save()
